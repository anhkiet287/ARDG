from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# SciencePlots style setup
# ============================================================================

# Run once if not installed:
# !pip install -q SciencePlots

try:
    import scienceplots  # noqa: F401
    # Use "no-latex" in Colab to avoid LaTeX dependency errors.
    # If your runtime has LaTeX installed, you can remove "no-latex".
    plt.style.use(["science", "no-latex"])
except Exception:
    pass

plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.titlesize": 13,
})

BASE = Path(__file__).resolve().parent
RAW_PATH = BASE / "ablation_raw_runs.csv"
OUT_DIR = BASE / "report" / "figures" / "ablations"
OUT_DIR.mkdir(parents=True, exist_ok=True)

raw = pd.read_csv(RAW_PATH)

def summarize_for_plot(experiment, order=None):
    df = raw[raw["experiment"] == experiment].copy()
    df["setting_value"] = df["setting_value"].astype(str)
    rows = []
    for setting, g in df.groupby("setting_value", sort=False):
        vals = g["mean8_pct"].astype(float)
        rows.append({
            "setting": setting,
            "n": len(vals),
            "mean": vals.mean(),
            "std": vals.std(ddof=1) if len(vals) > 1 else 0.0,
            "min": vals.min(),
            "max": vals.max(),
        })
    s = pd.DataFrame(rows)
    if order is not None:
        order_str = [str(x) for x in order]
        s["order"] = s["setting"].map({v: i for i, v in enumerate(order_str)})
        s = s.sort_values("order").drop(columns=["order"])
    return s.reset_index(drop=True)

def tight_ylim(min_val, max_val, pad=0.08):
    span = max_val - min_val
    if span <= 0:
        span = 0.2
    lo = min_val - max(pad, span * 0.25)
    hi = max_val + max(pad, span * 0.25)
    return lo, hi

def plot_mean8_minmax(summary, title, xlabel, output_name, x_formatter=None):
    x = np.arange(len(summary))
    y = summary["mean"].to_numpy()
    ymin = summary["min"].to_numpy()
    ymax = summary["max"].to_numpy()
    yerr = np.vstack([y - ymin, ymax - y])

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.errorbar(x, y, yerr=yerr, fmt="o-", capsize=4, linewidth=1.6, markersize=5)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Mean(8) robust accuracy (%)")
    ax.set_xticks(x)

    if x_formatter is None:
        labels = summary["setting"].astype(str).tolist()
    else:
        labels = [x_formatter(v) for v in summary["setting"].astype(str).tolist()]
    ax.set_xticklabels(labels)

    lo, hi = tight_ylim(float(ymin.min()), float(ymax.max()), pad=0.05)
    ax.set_ylim(lo, hi)
    ax.grid(True, alpha=0.35)

    for i, row in summary.iterrows():
        label = f"mean {row['mean']:.2f}\nmin {row['min']:.2f}, max {row['max']:.2f}\nn={int(row['n'])}"
        y_text = row["max"] + (hi - lo) * 0.035
        ax.annotate(label, (i, row["mean"]), xytext=(i, y_text),
                    textcoords="data", ha="center", va="bottom", fontsize=8)

    fig.tight_layout()
    fig.savefig(OUT_DIR / output_name, bbox_inches="tight")
    plt.close(fig)

cluster_summary = summarize_for_plot("cluster_count", order=["2", "4", "6", "10"])
anchor_summary = summarize_for_plot("anchor_strength", order=["0.20", "0.35", "0.50"])
recluster_summary = summarize_for_plot("recluster_frequency", order=["1", "2"])

plot_mean8_minmax(
    cluster_summary,
    "Cluster-count ablation: Mean(8) with min--max range",
    "Number of clusters K",
    "ablation_num_clusters.png",
    x_formatter=lambda v: f"K={v}",
)
plot_mean8_minmax(
    anchor_summary,
    "Anchor-strength ablation: Mean(8) with min--max range",
    "Anchor strength $\\lambda_{\\mathrm{DRO}}$",
    "ablation_anchor_strength.png",
    x_formatter=lambda v: f"$\\lambda$={float(v):.2f}",
)
plot_mean8_minmax(
    recluster_summary,
    "Recluster-frequency ablation: Mean(8) with min--max range",
    "Cluster-refresh interval",
    "ablation_recluster_frequency.png",
    x_formatter=lambda v: f"{v} epoch" + ("" if v == "1" else "s"),
)

print(f"Saved figures to {OUT_DIR}")

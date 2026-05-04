"""Regenerate Chapter 6 ablation figures from CSV summaries.

Expected input files in the same directory as this script by default:
- ablation_summary.csv
- wrn2810_architecture_check.csv

Outputs are written to ./ablation_figures by default.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
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
except Exception as exc:
    print(f"[WARN] SciencePlots is unavailable ({exc}). Using Matplotlib default style.")

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


METRIC_SPECS = [
    ("mean8_pct", "Mean(8)"),
    ("worst8_pct", "Worst(8)"),
    ("autoattack_linf_pct", r"AutoAttack-$\ell_\infty$"),
]


def _format_axis(ax: plt.Axes, title: str, xlabel: str) -> None:
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Robust accuracy (%)")
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(frameon=True)


def plot_ablation(summary: pd.DataFrame, experiment: str, xlabel: str, title: str, out_path: Path) -> None:
    data = summary[summary["experiment"] == experiment].copy()
    if data.empty:
        raise ValueError(f"No rows found for experiment={experiment!r}")
    data["setting_numeric"] = pd.to_numeric(data["setting_value"], errors="coerce")
    data = data.sort_values("setting_numeric")

    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    for metric, label in METRIC_SPECS:
        ax.errorbar(
            data["setting_numeric"],
            data[f"{metric}_mean"],
            yerr=data[f"{metric}_std"],
            marker="o",
            linewidth=1.5,
            capsize=3,
            label=label,
        )

    ax.set_xticks(data["setting_numeric"])
    ax.set_xticklabels(data["setting_value"].astype(str))
    _format_axis(ax, title=title, xlabel=xlabel)
    fig.tight_layout()
    fig.savefig(out_path.with_suffix(".png"), bbox_inches="tight")
    fig.savefig(out_path.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)


def plot_wrn_check(wrn: pd.DataFrame, out_path: Path) -> None:
    if wrn.empty:
        raise ValueError("WRN architecture check CSV is empty")

    metrics = [
        ("mean8_pct", "Mean(8)"),
        ("worst8_pct", "Worst(8)"),
        ("autoattack_linf_pct", r"AutoAttack-$\ell_\infty$"),
    ]
    methods = wrn["method"].tolist()
    x = list(range(len(methods)))
    width = 0.24

    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    for idx, (metric, label) in enumerate(metrics):
        offset = (idx - 1) * width
        values = wrn[metric].astype(float).tolist()
        bars = ax.bar([v + offset for v in x], values, width=width, label=label)
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.25,
                f"{value:.1f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_ylim(0, max(wrn[[m for m, _ in metrics]].max()) + 8)
    _format_axis(ax, title="Supplementary WRN-28-10 Architecture Check", xlabel="Method")
    fig.tight_layout()
    fig.savefig(out_path.with_suffix(".png"), bbox_inches="tight")
    fig.savefig(out_path.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate ablation figures from CSV files.")
    parser.add_argument("--input-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir or input_dir / "ablation_figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = pd.read_csv(input_dir / "ablation_summary.csv")
    wrn = pd.read_csv(input_dir / "wrn2810_architecture_check.csv")

    plot_ablation(
        summary,
        experiment="cluster_count",
        xlabel="Number of clusters K",
        title="Sensitivity to Number of Clusters",
        out_path=output_dir / "ablation_num_clusters",
    )
    plot_ablation(
        summary,
        experiment="anchor_strength",
        xlabel=r"Anchor strength $\lambda_{\mathrm{DRO}}$",
        title="Sensitivity to Anchor Strength",
        out_path=output_dir / "ablation_anchor_strength",
    )
    plot_ablation(
        summary,
        experiment="recluster_frequency",
        xlabel="Cluster refresh interval (epochs)",
        title="Sensitivity to Cluster Refresh Schedule",
        out_path=output_dir / "ablation_recluster_frequency",
    )
    plot_wrn_check(wrn, output_dir / "wrn2810_architecture_check")

    print(f"Saved figures to: {output_dir}")


if __name__ == "__main__":
    main()

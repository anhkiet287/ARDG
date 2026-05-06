"""Regenerate the Appendix C WRN-28-10 architecture-check figure.

This uses only the standard library plus the report's XeLaTeX/TikZ toolchain so
the figure can be refreshed on machines without matplotlib.
"""

from __future__ import annotations

import csv
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT / "data/ablation/wrn2810_architecture_check.csv"
OUT_PDF = ROOT / "report/figures/ablations/wrn2810_architecture_check.pdf"

METHODS = ["Multi-AT", "AttackDRO++"]
METRICS = [
    ("Mean(8)", "mean8_pct"),
    ("Worst(8)", "worst8_pct"),
    (r"AutoAttack\\$\ell_\infty$", "autoattack_linf_pct"),
]
COLORS = {
    "Multi-AT": "multiat",
    "AttackDRO++": "attackdropp",
}


def load_rows() -> dict[str, dict[str, float]]:
    with INPUT_CSV.open(newline="", encoding="utf-8") as f:
        rows = {}
        for row in csv.DictReader(f):
            rows[row["method"]] = {key: float(value) for _label, key in METRICS for value in [row[key]]}
    missing = [method for method in METHODS if method not in rows]
    if missing:
        raise ValueError(f"Missing methods in {INPUT_CSV}: {missing}")
    return rows


def write_figure(rows: dict[str, dict[str, float]]) -> None:
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    bar_w = 0.28
    method_gap = 0.52
    group_gap = 2.2
    y_scale = 0.075
    y_max = 80.0
    height = y_max * y_scale
    width = (len(METRICS) - 1) * group_gap + 1.1

    lines = [
        r"\documentclass[tikz,border=6pt]{standalone}",
        r"\usepackage{xcolor}",
        r"\usepackage{amsmath}",
        r"\begin{document}",
        r"\begin{tikzpicture}[x=1cm,y=1cm]",
        r"\definecolor{multiat}{RGB}{66,133,244}",
        r"\definecolor{attackdropp}{RGB}{15,157,88}",
        rf"\node[font=\large] at ({width / 2:.3f},{height + 0.82:.3f}) {{WRN-28-10 architecture check}};",
        rf"\draw[->] (-0.45,0) -- ({width + 0.45:.3f},0);",
        rf"\draw[->] (-0.45,0) -- (-0.45,{height + 0.35:.3f});",
        rf"\node[rotate=90,font=\footnotesize] at (-0.95,{height / 2:.3f}) {{Robust accuracy (\%)}};",
    ]

    for tick in [0, 20, 40, 60, 80]:
        y = tick * y_scale
        lines.append(rf"\draw[gray!35] (-0.45,{y:.3f}) -- ({width + 0.25:.3f},{y:.3f});")
        lines.append(rf"\node[anchor=east,font=\scriptsize] at (-0.52,{y:.3f}) {{{tick}}};")

    for i, (metric_label, key) in enumerate(METRICS):
        center = i * group_gap + 0.35
        for method_idx, method in enumerate(METHODS):
            x0 = center + (method_idx - 0.5) * method_gap
            x1 = x0 + bar_w
            value = rows[method][key]
            y = value * y_scale
            color = COLORS[method]
            lines.append(rf"\filldraw[fill={color}!75,draw={color}] ({x0:.3f},0) rectangle ({x1:.3f},{y:.3f});")
            value_offset = 0.06 if method_idx == 0 else 0.34
            lines.append(rf"\node[anchor=south,font=\tiny] at ({(x0 + x1) / 2:.3f},{y + value_offset:.3f}) {{{value:.2f}}};")
        lines.append(rf"\node[align=center,font=\footnotesize] at ({center + bar_w / 2:.3f},-0.50) {{{metric_label}}};")

    legend_x = width - 1.4
    legend_y = height + 0.3
    lines.extend(
        [
            rf"\filldraw[fill=multiat!75,draw=multiat] ({legend_x:.3f},{legend_y:.3f}) rectangle ({legend_x + 0.22:.3f},{legend_y + 0.16:.3f});",
            rf"\node[anchor=west,font=\scriptsize] at ({legend_x + 0.28:.3f},{legend_y + 0.08:.3f}) {{Multi-AT}};",
            rf"\filldraw[fill=attackdropp!75,draw=attackdropp] ({legend_x + 1.28:.3f},{legend_y:.3f}) rectangle ({legend_x + 1.50:.3f},{legend_y + 0.16:.3f});",
            rf"\node[anchor=west,font=\scriptsize] at ({legend_x + 1.56:.3f},{legend_y + 0.08:.3f}) {{AttackDRO++}};",
            r"\end{tikzpicture}",
            r"\end{document}",
        ]
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        tex_path = tmp_path / "wrn2810_architecture_check.tex"
        tex_path.write_text("\n".join(lines), encoding="utf-8")
        subprocess.run(
            [
                "xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={tmp}",
                str(tex_path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        OUT_PDF.write_bytes((tmp_path / "wrn2810_architecture_check.pdf").read_bytes())

    gs = shutil.which("gs")
    if gs:
        with tempfile.TemporaryDirectory() as tmp:
            normalized = Path(tmp) / OUT_PDF.name
            subprocess.run(
                [
                    gs,
                    "-dSAFER",
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-sDEVICE=pdfwrite",
                    "-dCompatibilityLevel=1.5",
                    "-dPDFSETTINGS=/prepress",
                    f"-sOutputFile={normalized}",
                    str(OUT_PDF),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            OUT_PDF.write_bytes(normalized.read_bytes())


def main() -> None:
    write_figure(load_rows())


if __name__ == "__main__":
    main()

"""Regenerate mentor-visible graybox heatmaps used in Chapter 6.

The local report build already depends on XeLaTeX/TikZ, so this script avoids
extra plotting dependencies. It reads the graybox transfer CSV, writes compact
standalone TikZ heatmaps, and compiles them to PDF.
"""

from __future__ import annotations

import csv
import math
import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSFER_CSV = ROOT / "data/graybox/transfer_per_class_attack.csv"
OUT_DIR = ROOT / "report/figures/graybox"

GRAYBOX_METHODS = [
    "single_at_pgd_linf",
    "single_at_ddn_l2",
    "multi_attack_pgd_linf_ddn_l2_mb",
    "attackdro_pp_anchor035_gradfp_online_k4",
]

METHOD_DISPLAY_NAMES = {
    "single_at_pgd_linf": "PGD-AT",
    "single_at_ddn_l2": "DDN-AT",
    "multi_attack_pgd_linf_ddn_l2_mb": "Multi-AT",
    "attackdro_pp_anchor035_gradfp_online_k4": "AttackDRO++",
}

GAP_FILES = {
    "single_at_ddn_l2": "whitebox_graybox_gap_DDNAT.pdf",
    "single_at_pgd_linf": "whitebox_graybox_gap_PGDAT.pdf",
    "multi_attack_pgd_linf_ddn_l2_mb": "whitebox_graybox_gap_MultiAT.pdf",
    "attackdro_pp_anchor035_gradfp_online_k4": "whitebox_graybox_gap_AttackDROpp.pdf",
}

DELTA_FIGURES = [
    (
        "attackdro_pp_anchor035_gradfp_online_k4",
        "multi_attack_pgd_linf_ddn_l2_mb",
        "graybox_delta_per_class_attack_AttackDRO++_vs_uniform.pdf",
        "AttackDRO++ minus Multi-AT",
    ),
    (
        "attackdro_pp_anchor035_gradfp_online_k4",
        "single_at_pgd_linf",
        "graybox_delta_per_class_attack_AttackDRO++_vs_singlePGD.pdf",
        "AttackDRO++ minus PGD-AT",
    ),
    (
        "attackdro_pp_anchor035_gradfp_online_k4",
        "single_at_ddn_l2",
        "graybox_delta_per_class_attack_AttackDRO++_vs_singleDDN.pdf",
        "AttackDRO++ minus DDN-AT",
    ),
]

ATTACK_ORDER = [
    "pgd20_ce",
    "ddn_l2",
    "fgsm_rs",
    "tpgd",
    "mifgsm",
    "pgd_l2",
    "deepfool_l2",
    "cw_l2",
]

ATTACK_LABELS = {
    "pgd20_ce": r"PGD-$\ell_\infty$",
    "ddn_l2": r"DDN-$\ell_2$",
    "fgsm_rs": "FGSM-RS",
    "tpgd": "TPGD",
    "mifgsm": "MI-FGSM",
    "pgd_l2": r"PGD-$\ell_2$",
    "deepfool_l2": r"DeepFool-$\ell_2$",
    "cw_l2": r"CW-$\ell_2$",
}

CLASS_ORDER = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def tex_escape(text: str) -> str:
    return text.replace("_", r"\_").replace("%", r"\%")


def rgb_for_value(value: float, vmax: float) -> tuple[int, int, int]:
    # Simple red-yellow-green scale: negative is red, zero is pale yellow, positive is green.
    t = max(-1.0, min(1.0, value / vmax if vmax else 0.0))
    if t < 0:
        a = t + 1.0
        r0, g0, b0 = (180, 0, 38)
        r1, g1, b1 = (255, 245, 150)
    else:
        a = t
        r0, g0, b0 = (255, 245, 150)
        r1, g1, b1 = (0, 120, 70)
    r = round(r0 + a * (r1 - r0))
    g = round(g0 + a * (g1 - g0))
    b = round(b0 + a * (b1 - b0))
    return r, g, b


def load_rows() -> list[dict[str, str]]:
    with TRANSFER_CSV.open(newline="") as f:
        return list(csv.DictReader(f))


def grouped_mean(rows: list[dict[str, str]], method: str, graybox_only: bool) -> dict[tuple[str, str], float]:
    buckets: dict[tuple[str, str], list[float]] = defaultdict(list)
    for row in rows:
        if row["target_method"] != method:
            continue
        if graybox_only and row["surrogate_method"] == row["target_method"]:
            continue
        key = (row["class_name"], row["attack"])
        buckets[key].append(float(row["acc"]))
    return {key: sum(values) / len(values) for key, values in buckets.items()}


def whitebox_mean(rows: list[dict[str, str]], method: str) -> dict[tuple[str, str], float]:
    buckets: dict[tuple[str, str], list[float]] = defaultdict(list)
    for row in rows:
        if row["target_method"] != method:
            continue
        if row["surrogate_method"] != row["target_method"]:
            continue
        if row["surrogate_seed"] != row["target_seed"]:
            continue
        key = (row["class_name"], row["attack"])
        buckets[key].append(float(row["acc"]))
    return {key: sum(values) / len(values) for key, values in buckets.items()}


def matrix_from(values: dict[tuple[str, str], float]) -> list[list[float]]:
    return [[values[(cls, attack)] for attack in ATTACK_ORDER] for cls in CLASS_ORDER]


def write_tikz_heatmap(title: str, matrix: list[list[float]], out_pdf: Path) -> None:
    vmax = max(1.0, max(abs(v) for row in matrix for v in row if math.isfinite(v)))
    cell_w = 1.35
    cell_h = 0.62
    cols = len(ATTACK_ORDER)
    rows = len(CLASS_ORDER)
    width = cols * cell_w
    height = rows * cell_h
    bar_x = width + 0.65
    bar_h = height
    bar_w = 0.28

    lines = [
        r"\documentclass[tikz,border=4pt]{standalone}",
        r"\usepackage{xcolor}",
        r"\usepackage{amsmath}",
        r"\begin{document}",
        r"\begin{tikzpicture}[x=1cm,y=1cm]",
        rf"\node[font=\large] at ({width / 2:.3f},{height + 0.72:.3f}) {{{title}}};",
    ]

    color_idx = 0
    for i, cls in enumerate(CLASS_ORDER):
        y = (rows - 1 - i) * cell_h
        lines.append(rf"\node[anchor=east,font=\footnotesize] at (-0.12,{y + cell_h / 2:.3f}) {{{tex_escape(cls)}}};")
        for j, _attack in enumerate(ATTACK_ORDER):
            x = j * cell_w
            value = matrix[i][j]
            r, g, b = rgb_for_value(value, vmax)
            cname = f"cell{color_idx}"
            color_idx += 1
            lines.append(rf"\definecolor{{{cname}}}{{RGB}}{{{r},{g},{b}}}")
            lines.append(rf"\filldraw[fill={cname},draw={cname}] ({x:.3f},{y:.3f}) rectangle ({x + cell_w:.3f},{y + cell_h:.3f});")
            lines.append(rf"\node[font=\scriptsize] at ({x + cell_w / 2:.3f},{y + cell_h / 2:.3f}) {{{value:.1f}}};")

    for j, attack in enumerate(ATTACK_ORDER):
        x = j * cell_w + cell_w / 2
        lines.append(rf"\node[anchor=east,rotate=45,font=\footnotesize] at ({x:.3f},-0.22) {{{ATTACK_LABELS[attack]}}};")

    segments = 40
    for k in range(segments):
        low = -vmax + (2 * vmax * k / segments)
        high = -vmax + (2 * vmax * (k + 1) / segments)
        value = (low + high) / 2
        r, g, b = rgb_for_value(value, vmax)
        cname = f"bar{k}"
        y0 = bar_h * k / segments
        y1 = bar_h * (k + 1) / segments
        lines.append(rf"\definecolor{{{cname}}}{{RGB}}{{{r},{g},{b}}}")
        lines.append(rf"\filldraw[fill={cname},draw={cname}] ({bar_x:.3f},{y0:.3f}) rectangle ({bar_x + bar_w:.3f},{y1:.3f});")

    lines.extend(
        [
            rf"\draw ({bar_x:.3f},0) rectangle ({bar_x + bar_w:.3f},{bar_h:.3f});",
            rf"\node[anchor=west,font=\scriptsize] at ({bar_x + bar_w + 0.08:.3f},{bar_h:.3f}) {{{vmax:.1f}}};",
            rf"\node[anchor=west,font=\scriptsize] at ({bar_x + bar_w + 0.08:.3f},{bar_h / 2:.3f}) {{0.0}};",
            rf"\node[anchor=west,font=\scriptsize] at ({bar_x + bar_w + 0.08:.3f},0) {{-{vmax:.1f}}};",
            r"\end{tikzpicture}",
            r"\end{document}",
        ]
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        tex_path = tmp_path / f"{out_pdf.stem}.tex"
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
        out_pdf.write_bytes((tmp_path / f"{out_pdf.stem}.pdf").read_bytes())

    gs = shutil.which("gs")
    if gs:
        with tempfile.TemporaryDirectory() as tmp:
            normalized = Path(tmp) / out_pdf.name
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
                    str(out_pdf),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            out_pdf.write_bytes(normalized.read_bytes())


def main() -> None:
    rows = load_rows()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    gray_cells = {method: grouped_mean(rows, method, graybox_only=True) for method in GRAYBOX_METHODS}

    for method, filename in GAP_FILES.items():
        white = whitebox_mean(rows, method)
        gap = {
            key: 100.0 * (gray_cells[method][key] - white[key])
            for key in gray_cells[method]
            if key in white
        }
        write_tikz_heatmap(
            f"graybox - whitebox gap: {METHOD_DISPLAY_NAMES[method]}",
            matrix_from(gap),
            OUT_DIR / filename,
        )

    for method_a, method_b, filename, title in DELTA_FIGURES:
        delta = {
            key: 100.0 * (gray_cells[method_a][key] - gray_cells[method_b][key])
            for key in gray_cells[method_a]
            if key in gray_cells[method_b]
        }
        write_tikz_heatmap(title, matrix_from(delta), OUT_DIR / filename)


if __name__ == "__main__":
    main()

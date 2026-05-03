# 04_figure_table_registry.md

Purpose:
A single source of truth for all figures and tables used or planned in the report.

Scope:
This registry reflects the current 7-chapter LaTeX report structure compiled from `report/main.tex`. It inventories numbered figures and tables in active chapter files, records unused files under `report/figures/`, and compares current assets against `docs/01_outline.md`. No LaTeX source files were edited while creating this registry.

## 1. Figure/table style rules

- LaTeX figure paths should use `figures/...` when compiling from `report/main.tex`.
- Markdown previews under `docs/` should use `../report/figures/...`.
- Chapter 6 main figures usually use `width=0.95\linewidth`.
- Figure fonts are generated at size 12, so avoid shrinking below `0.82\linewidth` unless the figure remains readable.
- Captions must be self-contained: define the metric, averaging condition, sample/seed condition, and comparison direction when needed.
- Captions should not start with "The figure shows..." or "This table presents...".
- Result tables should use `booktabs`.
- Bold the best value per metric column only when appropriate, and mention the bolding rule in the caption.
- Avoid metric/internal shorthand in figure or table titles unless the metric has already been defined. `Mean(8)`, `Worst(8)`, and `AutoAttack-512` are acceptable after definition; code-style forms such as `PGD20-CE` should be mapped to report-facing attack names.
- Preserve existing labels unless they are broken, duplicated, misleading, or against the style rules.

Status values used below: `active`, `inactive`, `missing file`, `unused`, `needs caption polish`, `needs width check`, `planned`, `appendix candidate`.

## 2. Figure inventory

| Figure label | File | Image path | Exists? | Width | Caption summary | Referenced? | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| `fig:ablation_dashboard` | `report/chapters/chapter6/3_ablation.tex` | `figures/anchor_strength_ablation` | yes | `\linewidth` | Anchor-strength ablation dashboard for AttackDRO++. | yes | active, needs caption polish | Caption uses `M(8)`; prefer `Mean(8)` after metric definition. Extensionless path resolves to `anchor_strength_ablation.png`. |
| `fig:whitebox_radar_per_attack_accuracy` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_radar_per_attack_accuracy_n5.png` | yes | `0.78\linewidth` | Whitebox per-attack robust accuracy profile averaged over five seeds. | no | active, unused, needs width check | Width is below the `0.82\linewidth` guidance for size-12 plot fonts. |
| `fig:whitebox_abs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_PGDAT_n5.png` | yes | `\linewidth` | Whitebox per-class/per-attack robust accuracy for PGD-AT. | no | active, unused | Caption includes metric unit `(\%)`. |
| `fig:whitebox_abs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_DDNAT_n5.png` | yes | `\linewidth` | Whitebox per-class/per-attack robust accuracy for DDN-AT. | no | active, unused | Caption includes metric unit `(\%)`. |
| `fig:whitebox_abs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_MultiAT_n5.png` | yes | `\linewidth` | Whitebox per-class/per-attack robust accuracy for Multi-AT. | no | active, unused | Caption includes metric unit `(\%)`. |
| `fig:whitebox_abs_attackdropp` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_AttackDROpp_n5.png` | yes | `\linewidth` | Whitebox per-class/per-attack robust accuracy for AttackDRO++ (Ours). | no | active, unused | Caption includes metric unit `(\%)`. |
| `fig:whitebox_delta_vs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_delta_per_class_attack_AttackDROpp_vs_MultiAT_n5.png` | yes | `\linewidth` | AttackDRO++ minus Multi-AT by class and attack, averaged over five seeds. | no | active, unused | Delta direction and unit are clear. |
| `fig:whitebox_delta_vs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_delta_per_class_attack_AttackDROpp_vs_PGDAT_n5.png` | yes | `\linewidth` | AttackDRO++ minus PGD-AT by class and attack. | no | active, unused, needs caption polish | Caption contains "The figure shows..." in a later sentence; avoid that construction when polishing. |
| `fig:whitebox_delta_vs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_delta_per_class_attack_AttackDROpp_vs_DDNAT_n5.png` | yes | `\linewidth` | AttackDRO++ minus DDN-AT by class and attack. | no | active, unused | Caption explains the main positive cells qualitatively. |
| `fig:whitebox_radar_delta_vs_baselines` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_radar_attackdropp_delta_vs_baselines_n5.png` | yes | `\linewidth` | Attack-wise whitebox delta of AttackDRO++ relative to baselines. | no | active, unused, needs caption polish | Caption is terse and should state unit and averaging condition. |
| `fig:whitebox_bottomk_lift` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_bottomk_lift_bar_n5.png` | yes | `0.64\linewidth` | Bottom-`K` whitebox class-attack lift of AttackDRO++ over each baseline. | no | active, unused, needs width check, needs caption polish | Width is below guidance; `Bottom-K` should be defined before use or expanded. |
| `fig:graybox_transfer_matrix` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_transfer_matrix_4method_aggregate_science_clean.png` | yes | `0.78\linewidth` | Method-level graybox transfer matrix over eight attacks and five seeds. | yes | active, needs width check | Width is below size-12 plot guidance but the caption is self-contained. |
| `fig:graybox_transfer_linf` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/transfer_matrix_4method_pgd20_ce_science_clean.png`; `figures/graybox/transfer_matrix_4method_fgsm_rs_science_clean.png`; `figures/graybox/transfer_matrix_4method_tpgd_science_clean.png`; `figures/graybox/transfer_matrix_4method_mifgsm_science_clean.png` | yes | `\linewidth` each subfigure | Per-attack graybox transfer matrices for `\ell_\infty` attacks. | yes | active | Source filename uses `pgd20_ce`, but caption/subcaption use report-facing PGD-`\ell_\infty`. |
| `fig:graybox_transfer_l2` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/transfer_matrix_4method_pgd_l2_science_clean.png`; `figures/graybox/transfer_matrix_4method_ddn_l2_science_clean.png`; `figures/graybox/transfer_matrix_4method_deepfool_l2_science_clean.png`; `figures/graybox/transfer_matrix_4method_cw_l2_science_clean.png` | yes | `\linewidth` each subfigure | Per-attack graybox transfer matrices for `\ell_2` attacks. | yes | active | Caption states metric unit. |
| `fig:graybox_gap_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_DDNAT.png` | yes | `\linewidth` | Whitebox-graybox gap heatmap for DDN-AT. | yes | active, needs caption polish | Referenced as first figure in a range; caption should define sign, unit, and averaging. |
| `fig:graybox_gap_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_PGDAT.png` | yes | `\linewidth` | Whitebox-graybox gap heatmap for PGD-AT. | no | active, unused, needs caption polish | Middle item in figure range, but not directly referenced. |
| `fig:graybox_gap_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_MultiAT.png` | yes | `\linewidth` | Whitebox-graybox gap heatmap for Multi-AT. | no | active, unused, needs caption polish | Middle item in figure range, but not directly referenced. |
| `fig:graybox_gap_attackdropp` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_AttackDROpp.png` | yes | `\linewidth` | Whitebox-graybox gap heatmap for AttackDRO++ (Ours). | yes | active, needs caption polish | Referenced as last figure in a range; caption should define sign, unit, and averaging. |
| `fig:graybox_delta_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_delta_per_class_attack_AttackDRO++_vs_uniform.png` | yes | `\linewidth` | AttackDRO++ minus Multi-AT graybox robust accuracy by class and attack. | yes | active | Caption states green/red direction. |
| `fig:graybox_delta_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_delta_per_class_attack_AttackDRO++_vs_singlePGD.png` | yes | `\linewidth` | AttackDRO++ minus PGD-AT graybox robust accuracy by class and attack. | no | active, unused | Middle item in figure range, but not directly referenced. |
| `fig:graybox_delta_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_delta_per_class_attack_AttackDRO++_vs_singleDDN.png` | yes | `\linewidth` | AttackDRO++ minus DDN-AT graybox robust accuracy by class and attack. | yes | active | Caption states green/red direction. |
| `fig:method_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/method_decomposition_three_panel_science.png` | yes | `\linewidth` | Decomposes AttackDRO++ improvement into multi-attack and Cluster-DRO effects. | no | active, unused | Useful synthesis figure but currently not cited. |

Notes:
- `report/outsider/cover-page.tex` and `report/outsider/frontmatter.tex` include `figures/Logo_BK.png`; this is a frontmatter logo, not a numbered report figure.
- All active `\includegraphics` paths found in active chapter files resolve under `report/figures/`.

## 3. Table inventory

| Table label | File | Caption summary | Environment | Uses booktabs? | Referenced? | Status | Notes |
|---|---|---|---|---|---|---|---|
| `tab:hparams` | `report/chapters/chapter4/7-complete_pipeline.tex` | Default hyperparameters for AttackDRO++ in main experiments. | `table + tabularx` | yes | yes | active | Chapter 4 method defaults; outline later also expects Chapter 5 hyperparameter tables. |
| `tab:training_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Training attack configuration. | `table + tabular` | yes | yes | active, needs caption polish | Caption is terse; active equivalent of planned `tab:ch5_training_attacks`. |
| `tab:evaluation_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Validation and test attacks used for `Mean(8)`. | `table + tabular` | yes | yes | active, needs caption polish | Active partial equivalent of planned attack/config table. |
| `tab:autoattack_config` | `report/chapters/chapter5/3-attack_suite.tex` | AutoAttack configuration. | `table + tabular` | yes | no | active, unused, needs caption polish | Active equivalent of planned `tab:ch5_autoattack_config`; should be cited if kept. |
| `tab:training_config` | `report/chapters/chapter5/4-configuration.tex` | General training configuration for the main experiments. | `table + tabularx` | yes | yes | active | Active equivalent of planned `tab:ch5_training_config`. |
| `tab:method_training_summary` | `report/chapters/chapter5/4-configuration.tex` | Summary of compared training methods. | `table + tabularx` | yes | yes | active, needs caption polish | Active equivalent of planned `tab:ch5_compared_methods`; caption starts with generic "Summary of". |
| `tab:main_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Default hyperparameters for AttackDRO++ (Ours). | `table + tabularx` | yes | no | active, unused | Active equivalent of planned `tab:ch5_attackdro_defaults`; source attack row contains code-style `PGD-20_{\mathrm{CE}}` mapping. |
| `tab:ablation_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Hyperparameters varied in ablation studies. | `table + tabularx` | yes | yes | active | Active equivalent of planned `tab:ch5_ablation_factors`. |
| `tab:statistical-reporting-format` | `report/chapters/chapter5/6-metrics.tex` | Statistical reporting format. | `table + tabularx` | yes | yes | active, needs caption polish | Label uses hyphens; caption is terse. Active equivalent of planned `tab:ch5_reporting_format`. |
| `tab:evaluation_metrics_summary` | `report/chapters/chapter5/6-metrics.tex` | Summary of evaluation metrics. | `table + tabularx` | yes | no | active, unused, needs caption polish | Active equivalent of planned `tab:ch5_eval_metrics`; should be cited if kept. |
| `tab:graybox_transfer_regimes` | `report/chapters/chapter5/8-graybox_protocol.tex` | Transfer regimes in the graybox evaluation protocol. | `table + tabularx` | yes | yes | active | Active equivalent of planned `tab:ch5_graybox_transfer_regimes`. |
| `tab:agg-results` | `report/chapters/chapter6/1_main_results.tex` | Aggregate robust accuracy on CIFAR-10, mean +/- std across 20 seeds, AutoAttack separate. | `table + tabular` | yes | yes | active | Main Chapter 6 aggregate table; active equivalent of planned `tab:ch6_main_aggregate`. Label uses hyphen. |
| `tab:effect_size_summary` | `report/chapters/chapter6/1_main_results.tex` | Effect-size summary comparing AttackDRO++ (Ours) with each baseline. | `table + tabular` | yes | yes | active | Caption states delta direction and paired effect size. |
| `tab:paired_aggregate_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Paired aggregate robustness comparison between AttackDRO++ (Ours) and each baseline. | `table + tabular` | yes | yes | active | Active equivalent of planned paired aggregate table. |
| `tab:corrected_paired_tests` | `report/chapters/chapter6/1_main_results.tex` | Multiple-comparison-corrected paired significance tests. | `table + resizebox + tabular` | yes | yes | active, needs width check | Dense result table; resizebox may reduce readability. |
| `tab:per_attack_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Per-attack robust accuracy for all four methods over 20 seeds. | `table + tabular` | yes | yes | active, needs width check | Dense table with many columns and a vertical rule; likely overfull/readability risk. |
| `tab:worst_autoattack_sanity` | `report/chapters/chapter6/1_main_results.tex` | `Worst(8)` and 512-sample AutoAttack sanity results across 20 seeds. | `table + tabular` | yes | yes | active | Caption explains bolding and the non-AutoAttack row. |
| `tab:autoattack_fulltest` | `report/chapters/chapter6/1_main_results.tex` | Full-test AutoAttack-`\ell_\infty` results on a representative seed. | `table + tabular` | yes | yes | active | Caption states delta direction against Multi-AT. |
| `tab:variance-reduction` | `report/chapters/chapter6/1_main_results.tex` | Variance reduction across 20 training seeds. | `table + tabular` | yes | yes | active | Label uses hyphen; caption defines ratio direction. |
| `tab:whitebox_per_cell_summary` | `report/chapters/chapter6/4_whitebox.tex` | Per-class/per-attack whitebox comparison with cell counts out of 80. | `table + tabular` | yes | yes | active | Active equivalent of planned `tab:ch6_whitebox_class_summary`. |
| `tab:graybox_whitebox_sanity` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox sanity check from the graybox pipeline subset. | `table + tabular` | yes | no | active, unused | Should be cited or moved to appendix if retained. |
| `tab:paired-graybox-two-panel` | `report/chapters/chapter6/2_graybox_results.tex` | Paired graybox comparisons for off-diagonal transfer conditions. | `table + tabular` | yes | yes | active | Active equivalent of planned `tab:ch6_graybox_method_pair_tests`; label uses hyphens. |
| `tab:graybox_per_attack` | `report/chapters/chapter6/2_graybox_results.tex` | Per-attack symmetric graybox comparison between AttackDRO++ and Multi-AT. | `table + tabular` | yes | no | active, unused | Should be cited if it remains in main flow. |
| `tab:graybox_attack_family` | `report/chapters/chapter6/2_graybox_results.tex` | Cross-method graybox accuracy by attack family. | `table + tabular` | yes | yes | active | Caption states off-diagonal averaging. |
| `tab:graybox_gap` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox-graybox gap by target method on five seeds. | `table + tabular` | yes | no | active, unused | Should be cited if gap discussion remains. |
| `tab:graybox_per_cell` | `report/chapters/chapter6/2_graybox_results.tex` | Per-class/per-attack graybox tests comparing AttackDRO++ target against baseline target. | `table + tabular` | yes | no | active, unused | Dense but caption states delta direction. |
| `tab:graybox_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | AttackDRO++ gain decomposition in percentage points. | `table + tabular` | yes | no | active, unused, needs caption polish | Uses shortened `DRO++` column naming; should map clearly to AttackDRO++ if retained. |
| `tab:ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Number-of-clusters ablation for AttackDRO++. | `table + tabular` | yes | yes | active, needs caption polish | Caption uses `M(8)` and table contains placeholder-style `--` values. |
| `tab:cluster_refresh_schedule_ablation` | `report/chapters/chapter6/3_ablation.tex` | Cluster-refresh schedule ablation for AttackDRO++ with Anchor35, GradFP, and `K=4`. | `table + resizebox + tabular` | yes | yes | active, needs width check, needs caption polish | Dense table; caption uses shorthand variants that should be mapped or defined. |

## 4. Planned figures and tables from outline

### Planned figures not found

| Planned figure | Intended section | Expected label | Status | Notes |
|---|---|---|---|---|
| Motivating attack illustration | Chapter 1.1 | TBD | planned | Optional figure suggested by outline; no active matching figure found. |
| Method pipeline figure | Chapter 4 | `fig:ch4_method_pipeline` or TBD | planned | Outline expects a methodology/pipeline visual; no active matching figure found. |
| Per-attack profile | Chapter 6.1 | `fig:ch6_per_attack_profile` | planned | Active related asset exists as `fig:whitebox_radar_per_attack_accuracy`; root file `figures/plot_attack_profile.png` is unused. |
| Forest plot of paired differences | Chapter 6.1 | `fig:ch6_forest_plot` | planned | Root file `figures/plot_pairwise_diff_forest.png` is unused and likely intended for this. |
| Whitebox delta vs Multi-AT | Chapter 6.2 | `fig:ch6_whitebox_delta_vs_uniform` | planned | Active equivalent exists as `fig:whitebox_delta_vs_multiat`, but expected label is not present. |
| Whitebox delta vs PGD-AT | Chapter 6.2 | `fig:ch6_whitebox_delta_vs_pgd` | planned | Active equivalent exists as `fig:whitebox_delta_vs_pgdat`, but expected label is not present. |
| Whitebox delta vs DDN-AT | Chapter 6.2 | `fig:ch6_whitebox_delta_vs_ddn` | planned | Active equivalent exists as `fig:whitebox_delta_vs_ddnat`, but expected label is not present. |
| Whitebox radar/profile | Chapter 6.2 | `fig:ch6_whitebox_radar` | planned | Active equivalent exists as `fig:whitebox_radar_per_attack_accuracy`. |
| Selected graybox transfer matrix | Chapter 6.3 | `fig:ch6_transfer_matrix_selected` | planned | Active richer set exists as `fig:graybox_transfer_matrix`, `fig:graybox_transfer_linf`, and `fig:graybox_transfer_l2`. |
| Graybox delta vs Multi-AT | Chapter 6.3 | `fig:ch6_graybox_delta_vs_uniform` | planned | Active equivalent exists as `fig:graybox_delta_multiat`. |
| Graybox delta vs PGD-AT | Chapter 6.3 | `fig:ch6_graybox_delta_vs_pgd` | planned | Active equivalent exists as `fig:graybox_delta_pgdat`. |
| Graybox delta vs DDN-AT | Chapter 6.3 | `fig:ch6_graybox_delta_vs_ddn` | planned | Active equivalent exists as `fig:graybox_delta_ddnat`. |
| Whitebox-graybox gap visualization | Chapter 6.3 | `fig:ch6_whitebox_graybox_gap` | planned | Active gap heatmaps exist as `fig:graybox_gap_ddnat` through `fig:graybox_gap_attackdropp`; expected label is not present. |

### Planned tables not found

| Planned table | Intended section | Expected label | Status | Notes |
|---|---|---|---|---|
| Stage 1 recap table | Chapter 1.2 | TBD | planned | Outline mentions a Stage 1 recap; no active matching table found. |
| Training attacks | Chapter 5.3 | `tab:ch5_training_attacks` | planned | Active equivalent exists as `tab:training_attacks`. |
| Attack/configuration source of truth | Chapter 5.3 | `tab:ch5_attack_configurations` | planned | Active partial equivalents are `tab:evaluation_attacks` and `tab:autoattack_config`; full source-of-truth table still appears missing. |
| AutoAttack configuration | Chapter 5.3 | `tab:ch5_autoattack_config` | planned | Active equivalent exists as `tab:autoattack_config`. |
| Training configuration | Chapter 5.4 | `tab:ch5_training_config` | planned | Active equivalent exists as `tab:training_config`. |
| Compared methods | Chapter 5.4 | `tab:ch5_compared_methods` | planned | Active equivalent exists as `tab:method_training_summary`. |
| AttackDRO++ defaults | Chapter 5.5 | `tab:ch5_attackdro_defaults` | planned | Active equivalents exist as `tab:main_hyperparams` and Chapter 4 `tab:hparams`. |
| Ablation factors | Chapter 5.5 | `tab:ch5_ablation_factors` | planned | Active equivalent exists as `tab:ablation_hyperparams`. |
| Statistical reporting format | Chapter 5.6 | `tab:ch5_reporting_format` | planned | Active equivalent exists as `tab:statistical-reporting-format`. |
| Evaluation metrics | Chapter 5.7 | `tab:ch5_eval_metrics` | planned | Active equivalent exists as `tab:evaluation_metrics_summary`. |
| Graybox transfer regimes | Chapter 5.8 | `tab:ch5_graybox_transfer_regimes` | planned | Active equivalent exists as `tab:graybox_transfer_regimes`. |
| Tools and platforms | Chapter 5.9 | `tab:ch5_tools_platforms` | planned | Not found; Chapter 5.9 remains a missing section/table item in prior registries. |
| Experimental setup recap | Chapter 5 summary | `tab:ch5_setup_summary` | planned | Not found; style rules call for a special recap-table summary if Chapter 5 summary is present. |
| Main aggregate results | Chapter 6.1 | `tab:ch6_main_aggregate` | planned | Active equivalent exists as `tab:agg-results`. |
| Paired aggregate results | Chapter 6.1 | `tab:ch6_paired_aggregate` | planned | Active equivalents exist as `tab:paired_aggregate_all_baselines` and `tab:corrected_paired_tests`. |
| Whitebox class summary | Chapter 6.2 | `tab:ch6_whitebox_class_summary` | planned | Active equivalent exists as `tab:whitebox_per_cell_summary`. |
| Graybox method-pair tests | Chapter 6.3 | `tab:ch6_graybox_method_pair_tests` | planned | Active equivalent exists as `tab:paired-graybox-two-panel`. |
| Cluster-count ablation | Chapter 6.4 | `tab:ch6_ablation_clusters` | planned | Active equivalent exists as `tab:ablation_num_clusters`. |
| Anchor-strength ablation | Chapter 6.4 | `tab:ch6_ablation_anchor` | planned | No active table found; active figure `fig:ablation_dashboard` covers anchor strength. |
| Re-clustering schedule ablation | Chapter 6.4 | `tab:ch6_ablation_recluster` | planned | Active equivalent exists as `tab:cluster_refresh_schedule_ablation`. |
| Research-question answer table | Chapter 7 | `tab:ch7_rq_answers` or TBD | planned | Not found; Chapter 7 is still an empty shell. |

## 5. Figure files not used in LaTeX

Active numbered figure files are listed in Section 2. The table below lists files under `report/figures/` that are not used by active numbered LaTeX figures, plus the non-numbered frontmatter logo.

| Image file | Used in LaTeX? | Possible section | Notes |
|---|---|---|---|
| `report/figures/Logo_BK.png` | yes | Frontmatter | Used by `report/outsider/cover-page.tex` and `report/outsider/frontmatter.tex`; not a numbered report figure. |
| `report/figures/graybox/graybox_delta_per_class_attack_AttackDROpp_vs_DDNAT.png` | no | Chapter 6.3 or appendix | Older/alternate graybox delta naming; active current file uses `AttackDRO++_vs_singleDDN.png`. |
| `report/figures/graybox/graybox_delta_per_class_attack_AttackDROpp_vs_MultiAT.png` | no | Chapter 6.3 or appendix | Older/alternate graybox delta naming; active current file uses `AttackDRO++_vs_uniform.png`. |
| `report/figures/graybox/graybox_delta_per_class_attack_AttackDROpp_vs_PGDAT.png` | no | Chapter 6.3 or appendix | Older/alternate graybox delta naming; active current file uses `AttackDRO++_vs_singlePGD.png`. |
| `report/figures/graybox/graybox_delta_per_class_attack_MultiAT_vs_DDNAT.png` | no | Appendix candidate | Baseline-vs-baseline graybox delta; not in current outline. |
| `report/figures/graybox/graybox_delta_per_class_attack_MultiAT_vs_PGDAT.png` | no | Appendix candidate | Baseline-vs-baseline graybox delta; not in current outline. |
| `report/figures/graybox/graybox_delta_per_class_attack_uniform_vs_singleDDN.png` | no | Appendix candidate | Alternate baseline naming; no active include. |
| `report/figures/graybox/graybox_delta_per_class_attack_uniform_vs_singlePGD.png` | no | Appendix candidate | Alternate baseline naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_AttackDROpp.png` | no | Appendix candidate | Older graybox absolute heatmap naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_DDNAT.png` | no | Appendix candidate | Older graybox absolute heatmap naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_MultiAT.png` | no | Appendix candidate | Older graybox absolute heatmap naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_PGDAT.png` | no | Appendix candidate | Older graybox absolute heatmap naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_singleDDN.png` | no | Appendix candidate | Alternate single-attack naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_singlePGD.png` | no | Appendix candidate | Alternate single-attack naming; no active include. |
| `report/figures/graybox/graybox_per_class_attack_uniform.png` | no | Appendix candidate | Alternate Multi-AT naming; no active include. |
| `report/figures/graybox/graybox_transfer_matrix_4method.pdf` | no | Chapter 6.3 or appendix | PDF version not used; active include uses cleaned PNG. |
| `report/figures/graybox/method_decomposition.png` | no | Chapter 6.3 or appendix | Older decomposition file; active include uses `method_decomposition_three_panel_science.png`. |
| `report/figures/graybox/transfer_matrix_4method_cw_l2.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_ddn_l2.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_deepfool_l2.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_fgsm_rs.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_mifgsm.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_pgd_l2.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_pgd20_ce.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/transfer_matrix_4method_tpgd.png` | no | Chapter 6.3 or appendix | Older/non-clean transfer matrix; active include uses `_science_clean.png`. |
| `report/figures/graybox/whitebox_graybox_gap_singleDDN.png` | no | Chapter 6.3 or appendix | Alternate naming; active include uses `whitebox_graybox_gap_DDNAT.png`. |
| `report/figures/graybox/whitebox_graybox_gap_singlePGD.png` | no | Chapter 6.3 or appendix | Alternate naming; active include uses `whitebox_graybox_gap_PGDAT.png`. |
| `report/figures/graybox/whitebox_graybox_gap_uniform.png` | no | Chapter 6.3 or appendix | Alternate naming; active include uses `whitebox_graybox_gap_MultiAT.png`. |
| `report/figures/plot_aggregate_boxplots.png` | no | Chapter 6.1 or appendix | Could support aggregate distribution/stability narrative. |
| `report/figures/plot_attack_profile.png` | no | Chapter 6.1 | Likely candidate for planned per-attack profile figure. |
| `report/figures/plot_diff_heatmap.png` | no | Chapter 6.1 or appendix | Could support paired difference visualization. |
| `report/figures/plot_pairwise_diff_forest.png` | no | Chapter 6.1 | Likely candidate for planned forest plot. |
| `report/figures/plot_seen_heldout.png` | no | Chapter 6.1 or appendix | Could support seen/held-out or robustness split discussion if the prose defines it. |
| `report/figures/whitebox/whitebox_per_class_attack_AttackDRO++.png` | no | Chapter 6.2 or appendix | Older absolute whitebox heatmap; active include uses `_AttackDROpp_n5.png`. |
| `report/figures/whitebox/whitebox_per_class_attack_DDN_AT.png` | no | Chapter 6.2 or appendix | Older absolute whitebox heatmap; active include uses `_DDNAT_n5.png`. |
| `report/figures/whitebox/whitebox_per_class_attack_MultiAT.png` | no | Chapter 6.2 or appendix | Older absolute whitebox heatmap; active include uses `_MultiAT_n5.png`. |
| `report/figures/whitebox/whitebox_per_class_attack_PGD_AT.png` | no | Chapter 6.2 or appendix | Older absolute whitebox heatmap; active include uses `_PGDAT_n5.png`. |

## 6. Caption and naming audit

| Issue | Asset | File | Current text / problem | Suggested action |
|---|---|---|---|---|
| Figure width below guidance | `fig:whitebox_radar_per_attack_accuracy` | `report/chapters/chapter6/4_whitebox.tex` | Uses `width=0.78\linewidth`. | Increase toward `0.95\linewidth` if layout permits. |
| Figure width below guidance | `fig:graybox_transfer_matrix` | `report/chapters/chapter6/2_graybox_results.tex` | Uses `width=0.78\linewidth`. | Increase toward `0.95\linewidth` or verify readability in PDF. |
| Figure width below guidance | `fig:whitebox_bottomk_lift` | `report/chapters/chapter6/4_whitebox.tex` | Uses `width=0.64\linewidth`. | Increase width or move to appendix if visually secondary. |
| Caption contains discouraged wording | `fig:whitebox_delta_vs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | Caption includes "The figure shows..." in a later sentence. | Rephrase during caption-polish patch. |
| Terse caption, missing conditions | `fig:whitebox_radar_delta_vs_baselines` | `report/chapters/chapter6/4_whitebox.tex` | Caption does not state unit or averaging condition. | Add percentage-point unit and seed/attack averaging condition. |
| Terse captions, missing sign convention | `fig:graybox_gap_ddnat` to `fig:graybox_gap_attackdropp` | `report/chapters/chapter6/2_graybox_results.tex` | Captions say only "Whitebox--graybox gap heatmap for ...". | Define gap sign, unit, seed count, and attack averaging condition. |
| Metric shorthand in caption | `fig:ablation_dashboard` | `report/chapters/chapter6/3_ablation.tex` | Uses `M(8)` instead of report-facing `Mean(8)`. | Replace with `Mean(8)` after confirming all related text uses same metric definition. |
| Metric shorthand in caption | `tab:ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Caption defines `M(8)`; notation registry prefers `Mean(8)`. | Use `Mean(8)` in formal caption/table context. |
| Variant shorthand in caption | `tab:cluster_refresh_schedule_ablation` | `report/chapters/chapter6/3_ablation.tex` | Caption uses `Anchor35`, `GradFP`, and `K=4` without expanded mapping. | Define or map the variant shorthand before the table or in caption. |
| Code-style attack name in table body | `tab:main_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Source attack row contains `PGD-20_{\mathrm{CE}}`. | Map to PGD-`\ell_\infty` with 20 steps and cross-entropy loss in Chapter 5 attack configuration. |
| Generic caption opening | `tab:method_training_summary` | `report/chapters/chapter5/4-configuration.tex` | Caption starts "Summary of compared training methods." | Make caption more specific when polishing. |
| Generic caption opening | `tab:evaluation_metrics_summary` | `report/chapters/chapter5/6-metrics.tex` | Caption starts "Summary of evaluation metrics." | Make caption self-contained and cite if kept. |
| Terse caption | `tab:training_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Caption is "Training attack configuration." | Include training scope and where the attack is used. |
| Terse caption | `tab:autoattack_config` | `report/chapters/chapter5/3-attack_suite.tex` | Caption is "AutoAttack configuration." | Include that this is the 512-sample sanity/full-test AutoAttack-`\ell_\infty` setup as appropriate. |
| Dense table risk | `tab:corrected_paired_tests` | `report/chapters/chapter6/1_main_results.tex` | Uses `\resizebox{\textwidth}{!}{...}`. | Check PDF readability; split or move details to appendix if cramped. |
| Dense table risk | `tab:cluster_refresh_schedule_ablation` | `report/chapters/chapter6/3_ablation.tex` | Uses `\resizebox{\textwidth}{!}{...}`. | Check PDF readability; split or move details to appendix if cramped. |
| Dense table risk | `tab:per_attack_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Many columns and a vertical rule. | Check overfull boxes and consider a smaller main table plus appendix detail. |
| Label style drift | `tab:agg-results`, `tab:variance-reduction`, `tab:paired-graybox-two-panel`, `tab:statistical-reporting-format` | Chapter 5 and Chapter 6 files | Labels use hyphens while style guidance prefers stable type-prefixed labels. | Preserve for now; rename only in a coordinated label-cleanup patch. |
| Active asset not referenced | Many Chapter 6 figures and tables | `report/chapters/chapter6/*.tex` | Several active figures/tables are not referenced in running text. | Add references or move secondary assets to appendix in a later prose/structure patch. |
| Planned labels differ from active labels | Chapter 5 and Chapter 6 tables/figures | Multiple files | Outline labels such as `tab:ch6_main_aggregate` do not match active labels such as `tab:agg-results`. | Decide whether to preserve compiled references or run a label-alignment patch later. |
| Chapter 7 planned table missing | `tab:ch7_rq_answers` or TBD | `report/chapters/chapter7.tex` | Chapter 7 is still an empty shell. | Add after Chapter 7 prose plan is approved. |

## 7. Recommended cleanup later

### Safe automatic cleanup

- Add text references to active but unreferenced figures/tables that already appear in the main flow, without changing results.
- Normalize caption metric shorthand from `M(8)` to `Mean(8)` where the metric has already been defined.
- Expand terse captions with seed count, averaging condition, unit, and comparison direction.
- Increase main Chapter 6 figure widths below `0.82\linewidth` where layout permits.
- Map formal table/body occurrences of `PGD-20_{\mathrm{CE}}` to PGD-`\ell_\infty` with 20 steps and cross-entropy loss in the Chapter 5 attack-configuration context.

### Needs user confirmation

- Whether to align active labels to outline labels such as `tab:ch6_main_aggregate` and `fig:ch6_whitebox_delta_vs_uniform`, since current references compile.
- Whether to keep all Chapter 6 heatmaps in the main text or move some to an appendix.
- Whether unused root figures (`plot_attack_profile.png`, `plot_pairwise_diff_forest.png`, etc.) should be inserted, archived, or ignored.
- Whether Chapter 5.9 should add the planned tools/platforms table `tab:ch5_tools_platforms`.
- Whether Chapter 7 should include a compact RQ answer table.

### Postpone

- Renaming image files to report-facing names; this is unnecessary for compilation and could create path churn.
- Rebuilding figures to adjust embedded fonts or color scales unless PDF readability is poor.
- Moving old alternate graybox/whitebox figure files until the final appendix plan is settled.
- Creating `docs/02_writing_templates.md` or `docs/07_task_assignment.md`; both are intentionally out of scope for this task.

## 8. Maintenance rule

Whenever a figure/table is added, removed, renamed, moved, or relabeled, update `docs/04_figure_table_registry.md` in the same writing session.

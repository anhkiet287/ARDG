# 04_figure_table_registry.md

Purpose:
A source of truth for active figures and tables in the DATN report.

Scope:
This registry reflects the active LaTeX report compiled from `report/main.tex`.
It follows the standardized labels in `docs/03_label_registry.md`; old
pre-standardization labels are not listed as active requirements.

## 1. Style rules

- LaTeX image paths are relative to `report/` and should use `figures/...`.
- Markdown previews under `docs/` should use `../report/figures/...`.
- Captions must be self-contained and should state units, averaging conditions,
  and comparison direction when relevant.
- Result tables use `booktabs` and `\bestval{...}` for best-value highlighting.
- If bold values are used, the caption must state whether bold indicates the
  best method or best setting.
- `Mean(8)` and `Worst(8)` are allowed in captions and tables after definition,
  but not in section or subsection headings.
- W&B exports are tracking telemetry in Appendix B, not Chapter 5 result
  evidence.
- WRN-28-10 evidence is supplementary architecture evidence in Appendix C, not
  part of the main paired claims.

Status values: `active`, `final`, `appendix`, `unused`, `referenced`,
`supplementary`, `not numbered`.

## 2. Active figure inventory

| Label | File | Image path | Status | Notes |
|---|---|---|---|---|
| `fig:app_wandb_core_metrics` | `report/appendices.tex` | `figures/wandb/wb_train_loss.png`; `figures/wandb/wb_train_acc.png`; `figures/wandb/wb_val_clean_acc.png`; `figures/wandb/wb_pgd_linf_acc.png`; `figures/wandb/wb_ddn_l2_acc.png`; `figures/wandb/media_images_media_q_trajectory_15650_2752bccd0ffdd754ab89.png` | active, appendix | Appendix B W&B tracking telemetry; not result evidence. |
| `fig:ch6_ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | `figures/ablations/ablation_num_clusters.png` | active, final | Mean(8) sensitivity across cluster counts with min--max range. |
| `fig:ch6_ablation_anchor_strength` | `report/chapters/chapter6/3_ablation.tex` | `figures/ablations/ablation_anchor_strength.png` | active, final | Mean(8) sensitivity across anchor strengths with min--max range. |
| `fig:ch6_ablation_recluster_frequency` | `report/chapters/chapter6/3_ablation.tex` | `figures/ablations/ablation_recluster_frequency.png` | active, final | Mean(8) sensitivity across cluster-refresh intervals with min--max range. |
| `fig:ch6_whitebox_radar_per_attack_accuracy` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_radar_per_attack_accuracy_n5.png` | active | Whitebox per-attack radar profile. |
| `fig:ch6_whitebox_abs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_PGDAT_n5.png` | active | Absolute whitebox class-attack heatmap for PGD-AT. |
| `fig:ch6_whitebox_abs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_DDNAT_n5.png` | active | Absolute whitebox class-attack heatmap for DDN-AT. |
| `fig:ch6_whitebox_abs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_MultiAT_n5.png` | active | Absolute whitebox class-attack heatmap for Multi-AT. |
| `fig:ch6_whitebox_abs_attackdropp` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_per_class_attack_AttackDROpp_n5.png` | active | Absolute whitebox class-attack heatmap for AttackDRO++ (Ours). |
| `fig:ch6_whitebox_delta_vs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_delta_per_class_attack_AttackDROpp_vs_MultiAT_n5.png` | active | Whitebox delta heatmap against Multi-AT. |
| `fig:ch6_whitebox_delta_vs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_delta_per_class_attack_AttackDROpp_vs_PGDAT_n5.png` | active | Whitebox delta heatmap against PGD-AT. |
| `fig:ch6_whitebox_delta_vs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_delta_per_class_attack_AttackDROpp_vs_DDNAT_n5.png` | active | Whitebox delta heatmap against DDN-AT. |
| `fig:ch6_whitebox_radar_delta_vs_baselines` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_radar_attackdropp_delta_vs_baselines_n5.png` | active | Attack-wise whitebox delta against baselines. |
| `fig:ch6_whitebox_bottomk_lift` | `report/chapters/chapter6/4_whitebox.tex` | `figures/whitebox/whitebox_bottomk_lift_bar_n5.png` | active | Weakest-cell lift figure. |
| `fig:ch6_graybox_transfer_matrix` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_transfer_matrix_4method_aggregate_science_clean.png` | active, referenced | Method-level graybox transfer matrix. |
| `fig:ch6_graybox_transfer_linf` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/transfer_matrix_4method_pgd20_ce_science_clean.png`; `figures/graybox/transfer_matrix_4method_fgsm_rs_science_clean.png`; `figures/graybox/transfer_matrix_4method_tpgd_science_clean.png`; `figures/graybox/transfer_matrix_4method_mifgsm_science_clean.png` | active, referenced | Graybox transfer matrices for the `\ell_\infty` attack family. |
| `fig:ch6_graybox_transfer_l2` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/transfer_matrix_4method_pgd_l2_science_clean.png`; `figures/graybox/transfer_matrix_4method_ddn_l2_science_clean.png`; `figures/graybox/transfer_matrix_4method_deepfool_l2_science_clean.png`; `figures/graybox/transfer_matrix_4method_cw_l2_science_clean.png` | active, referenced | Graybox transfer matrices for the `\ell_2` attack family. |
| `fig:ch6_graybox_gap_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_DDNAT.png` | active, referenced | Whitebox-graybox gap heatmap for DDN-AT. |
| `fig:ch6_graybox_gap_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_PGDAT.png` | active | Whitebox-graybox gap heatmap for PGD-AT. |
| `fig:ch6_graybox_gap_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_MultiAT.png` | active | Whitebox-graybox gap heatmap for Multi-AT. |
| `fig:ch6_graybox_gap_attackdropp` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/whitebox_graybox_gap_AttackDROpp.png` | active, referenced | Whitebox-graybox gap heatmap for AttackDRO++ (Ours). |
| `fig:ch6_graybox_delta_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_delta_per_class_attack_AttackDRO++_vs_uniform.png` | active, referenced | Graybox delta heatmap against Multi-AT. |
| `fig:ch6_graybox_delta_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_delta_per_class_attack_AttackDRO++_vs_singlePGD.png` | active | Graybox delta heatmap against PGD-AT. |
| `fig:ch6_graybox_delta_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/graybox_delta_per_class_attack_AttackDRO++_vs_singleDDN.png` | active, referenced | Graybox delta heatmap against DDN-AT. |
| `fig:ch6_method_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | `figures/graybox/method_decomposition_three_panel_science.png` | active | Graybox method contribution decomposition figure. |
| `fig:app_wrn2810_architecture_check` | `report/appendices.tex` | `figures/ablations/wrn2810_architecture_check.png` | active, appendix, supplementary | Appendix C WRN-28-10 single-run architecture check. |

Frontmatter logo files such as `figures/Logo_BK.png` are not numbered report
figures and are not included in the active figure inventory.

## 3. Active table inventory

| Label | File | Status | Notes |
|---|---|---|---|
| `tab:ch4_hparams` | `report/chapters/chapter4/7-complete_pipeline.tex` | active, referenced | Default AttackDRO++ hyperparameters in the methodology chapter. |
| `tab:ch5_training_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | active, referenced | Source attack configuration used during training. |
| `tab:ch5_evaluation_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | active, referenced | Evaluation attacks used for Mean(8). |
| `tab:ch5_autoattack_config` | `report/chapters/chapter5/3-attack_suite.tex` | active | AutoAttack-$\ell_\infty$ configuration. |
| `tab:ch5_training_config` | `report/chapters/chapter5/4-configuration.tex` | active, referenced | Main training configuration. |
| `tab:ch5_method_training_summary` | `report/chapters/chapter5/4-configuration.tex` | active, referenced | Compared training methods. |
| `tab:ch5_main_hyperparams` | `report/chapters/chapter5/5-choices.tex` | active | Main AttackDRO++ hyperparameters. |
| `tab:ch5_ablation_hyperparams` | `report/chapters/chapter5/5-choices.tex` | active, referenced | Ablation hyperparameters. |
| `tab:ch5_statistical_reporting_format` | `report/chapters/chapter5/6-protocol.tex` | active, referenced | Statistical reporting format. |
| `tab:ch5_evaluation_metrics_summary` | `report/chapters/chapter5/7-eval_metrics.tex` | active | Evaluation metric definitions. |
| `tab:ch5_graybox_transfer_regimes` | `report/chapters/chapter5/8-graybox_transfer.tex` | active, referenced | Graybox transfer regimes. |
| `tab:ch5_tools_platforms` | `report/chapters/chapter5/9-tools_tracking.tex` | active, referenced | Chapter 5.9 tools and platforms table. |
| `tab:ch5_setup_summary` | `report/chapters/chapter5/9-tools_tracking.tex` | active, referenced | Chapter 5 setup recap table. |
| `tab:ch6_aggregate_results` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Main aggregate robustness table. |
| `tab:ch6_effect_size_summary` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Effect-size summary. |
| `tab:ch6_paired_aggregate_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Paired aggregate comparisons. |
| `tab:ch6_corrected_paired_tests` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Multiple-comparison-corrected paired tests. |
| `tab:ch6_per_attack_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Per-attack robust accuracy. |
| `tab:ch6_worst_autoattack_sanity` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Worst(8) and AutoAttack sanity results. |
| `tab:ch6_autoattack_fulltest` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Full-test AutoAttack results. |
| `tab:ch6_variance_reduction` | `report/chapters/chapter6/1_main_results.tex` | active, final, referenced | Seed-to-seed variance reduction. |
| `tab:ch6_whitebox_per_cell_summary` | `report/chapters/chapter6/4_whitebox.tex` | active, final, referenced | Whitebox per-cell summary. |
| `tab:ch6_graybox_whitebox_sanity` | `report/chapters/chapter6/2_graybox_results.tex` | active, final | Whitebox sanity check for graybox pipeline. |
| `tab:ch6_paired_graybox_two_panel` | `report/chapters/chapter6/2_graybox_results.tex` | active, final, referenced | Paired graybox comparisons. |
| `tab:ch6_graybox_per_attack` | `report/chapters/chapter6/2_graybox_results.tex` | active, final | Per-attack graybox comparison. |
| `tab:ch6_graybox_attack_family` | `report/chapters/chapter6/2_graybox_results.tex` | active, final, referenced | Graybox accuracy by attack family. |
| `tab:ch6_graybox_gap` | `report/chapters/chapter6/2_graybox_results.tex` | active, final | Whitebox-graybox gap by target method. |
| `tab:ch6_graybox_per_cell` | `report/chapters/chapter6/2_graybox_results.tex` | active, final | Graybox per-cell tests. |
| `tab:ch6_graybox_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | active, final | AttackDRO++ gain decomposition. |
| `tab:ch6_ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | active, final, referenced | Number-of-clusters ablation. |
| `tab:ch6_ablation_anchor_strength` | `report/chapters/chapter6/3_ablation.tex` | active, final, referenced | Anchor-strength ablation. |
| `tab:ch6_cluster_refresh_schedule_ablation` | `report/chapters/chapter6/3_ablation.tex` | active, final, referenced | Cluster-refresh schedule ablation. |
| `tab:ch7_rq_answers` | `report/chapters/chapter7.tex` | active | Summary answers to research questions. |
| `tab:app_wrn2810_architecture_check` | `report/appendices.tex` | active, appendix, supplementary | Appendix C WRN-28-10 single-run architecture check. |

## 4. Stale label cleanup status

Old pre-standardization figure and table labels have been removed from the
active inventory. Use only the standardized labels listed in Sections 2 and 3
for new prose, captions, and cross-references.

## 5. Unused or alternate figure files

Several files under `report/figures/` are older or alternate exports that are
not included in active numbered figures. They may remain in the repository as
raw assets, but they are not planned report requirements unless a future patch
explicitly adds them. Examples include older graybox transfer PNG/PDF exports,
root-level exploratory plots such as `plot_attack_profile.png`, and older
whitebox heatmaps without the current `_n5` naming.

## 6. Maintenance rule

Whenever a figure or table is added, removed, moved, relabeled, or converted
between main text and appendix, update this file together with
`docs/03_label_registry.md`.

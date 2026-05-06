# 03_label_registry.md

Purpose:
A single source of truth for all LaTeX labels and references in the report.

Scope: this registry reflects the current active 7-chapter flow compiled from `report/main.tex`. Archived files are listed only when they contain labels that should not be reused.

## 1. Label naming rules

Source: `docs/06_style_rules.md`.

- `chap:` labels point to chapters and use readable underscore names, e.g. `chap:experimental_setup`.
- `sec:` labels point only to `\section` headings and use `sec:ch<chapter>_<section_name>`.
- `subsec:` labels point to `\subsection` headings and use `subsec:ch<chapter>_<subsection_name>`.
- `fig:` labels point to figures and use `fig:ch<chapter>_<figure_name>`.
- `tab:` labels point to tables and use `tab:ch<chapter>_<table_name>`.
- `alg:` labels point to algorithms and use `alg:ch<chapter>_<algorithm_name>`.
- `eq:` labels point to equations and use `eq:<equation_name>`.
- `app:` labels point to appendices.

Additional rules:

- Only label equations that are referenced later.
- Do not add labels just because an equation is displayed.
- Prefer preserving existing labels unless they are broken, duplicated, misleading, or against style.
- Use underscores only in active labels; avoid hyphenated labels.
- Whenever a label is added, removed, or renamed in LaTeX, update `docs/03_label_registry.md` in the same writing session.

Status values:

- `active`: label is in the current compiled flow.
- `referenced`: at least one active reference points to the label.
- `unused`: no active reference points to the label.
- `inactive`: label exists in an archived file or disabled block that is not part of the compiled flow.

## 2. Label inventory

### Chapter labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `chap:introduction` | `report/chapters/chapter1.tex` | Chapter 1: Introduction | active, referenced | Referenced from Chapter 7 RQ answer section. |
| `chap:background` | `report/chapters/chapter2.tex` | Chapter 2: Background | active, unused | Prefix ok. |
| `chap:related_work` | `report/chapters/chapter3.tex` | Chapter 3: Related Work | active, unused | Standardized chapter label. |
| `chap:methodology` | `report/chapters/chapter4.tex` | Chapter 4: Proposed Methodology | active, referenced | Referenced from Chapter 6 ablation interpretation. |
| `chap:experimental_setup` | `report/chapters/chapter5.tex` | Chapter 5: Experimental Setup | active, referenced | Referenced from Chapters 4 and 6. |
| `chap:results_analysis` | `report/chapters/chapter6.tex` | Chapter 6: Results and Analysis | active, referenced | Standardized chapter label. |
| `chap:conclusion` | `report/chapters/chapter7.tex` | Chapter 7: Conclusion and Future Work | active, referenced | Referenced from Chapter 6 closing synthesis. |
| `chap:analysis` | `report/chapters/chapter7_old_analysis_discussion.tex` | Archived old Chapter 7: Analysis and Discussion | inactive | Do not rename unless archive is reactivated. |

### Section labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `sec:ch4_problem_formulation` | `report/chapters/chapter4/1-problem_formulation.tex` | Multi-Attack Training as a Domain Problem | active, referenced | Standardized section label. |
| `sec:ch4_multi_attack_erm` | `report/chapters/chapter4/2-multi_attack.tex` | Uniform Multi-Attack ERM Baseline | active, referenced | Standardized section label. |
| `sec:ch4_attackdro` | `report/chapters/chapter4/3-attackDRO.tex` | AttackDRO: Group DRO Over Attack Identities | active, referenced | Standardized section label. |
| `sec:ch4_attackdropp` | `report/chapters/chapter4/4-attackDRO++.tex` | AttackDRO++: Group DRO Over Discovered Clusters | active, referenced | Standardized section label. |
| `sec:ch4_gradfp` | `report/chapters/chapter4/5-clustering_feature.tex` | Augmented Clustering with Gradient Fingerprints | active, referenced | Duplicate old clustering label removed. |
| `sec:ch4_anchor_objective` | `report/chapters/chapter4/6-anchor_objective.tex` | Uniform-Anchored Training Objective | active, referenced | Renamed from `sec:anchor`. |
| `sec:ch4_complete_pipeline` | `report/chapters/chapter4/7-complete_pipeline.tex` | Complete Training Framework | active, unused | Renamed from `sec:pipeline`. |
| `sec:ch5_hyperparameters` | `report/chapters/chapter5/5-choices.tex` | Hyperparameter Choices and Ablation Factors | active, unused | Renamed from `sec:hyperparameters`. |
| `sec:ch5_statistical_protocol` | `report/chapters/chapter5/6-protocol.tex` | Statistical Significance Protocol | active, unused | Renamed from `sec:statistical-significance-protocol`. |
| `sec:ch5_evaluation_metrics` | `report/chapters/chapter5/7-eval_metrics.tex` | Evaluation Metrics and Robustness Definitions | active, referenced | Renamed from `sec:evaluation_metrics`. |
| `sec:ch5_graybox_protocol` | `report/chapters/chapter5/8-graybox_transfer.tex` | Graybox Transfer Protocol | active, referenced | Renamed from `sec:graybox-design`. |
| `sec:ch5_tools_platforms` | `report/chapters/chapter5/9-tools_tracking.tex` | Tools, Platforms, and Experiment Tracking | active, unused | New Chapter 5.9 section label. |
| `sec:ch6_whitebox` | `report/chapters/chapter6/1_main_results.tex` | Whitebox Robustness Under Direct Attacks | active, referenced | Chapter-aware section label. |
| `sec:ch6_whitebox_class_attack` | `report/chapters/chapter6/4_whitebox.tex` | Class-wise Whitebox Robustness Across Attacks | active, referenced | Referenced from Chapter 7 RQ answer section. |
| `sec:ch6_graybox` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox Robustness Across Surrogate Models | active, referenced | Referenced from Chapter 7 RQ answer section. |
| `sec:ch6_ablation` | `report/chapters/chapter6/3_ablation.tex` | Sensitivity to Key Hyperparameters | active, referenced | Referenced from Chapter 7 RQ answer section. |

### Subsection labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `subsec:ch5_evaluation_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Evaluation Attacks | active, unused | Renamed from `sec:evaluation_attacks`. |
| `subsec:ch6_aggregate_comparison` | `report/chapters/chapter6/1_main_results.tex` | Aggregate Comparison Across Methods | active, unused | No active prose reference after Chapter 7 RQ table removal. |
| `subsec:ch6_per_attack_accuracy` | `report/chapters/chapter6/1_main_results.tex` | Per-Attack Accuracy: Where Do Methods Diverge? | active, referenced | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_hardest_evaluation_cases` | `report/chapters/chapter6/1_main_results.tex` | Robustness Under the Hardest Evaluation Cases | active, referenced | Approved replacement for the old metric-heavy 6.1.3 title. |
| `subsec:ch6_training_stability` | `report/chapters/chapter6/1_main_results.tex` | Training Stability: How Predictable Is the Outcome? | active, unused | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_class_level_gains` | `report/chapters/chapter6/4_whitebox.tex` | Class-Level Gains and Persistent Difficulties | active, unused | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_tail_class_robustness` | `report/chapters/chapter6/4_whitebox.tex` | Tail-Class Robustness: Do the Weakest Cells Improve? | active, unused | Old Bottom-K heading folded into prose. |
| `subsec:ch6_graybox_transfer_structure` | `report/chapters/chapter6/2_graybox_results.tex` | Cross-Method Transfer Structure | active, unused | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_paired_graybox_comparisons` | `report/chapters/chapter6/2_graybox_results.tex` | Paired Graybox Comparisons: Does the Whitebox Advantage Carry Over? | active, referenced | Granular graybox comparisons folded under this subsection. |
| `subsec:ch6_class_level_transfer_patterns` | `report/chapters/chapter6/2_graybox_results.tex` | Class-Level Transfer Patterns | active, unused | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Number of Clusters: How Many Groups Are Needed? | active, referenced | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_ablation_anchor_strength` | `report/chapters/chapter6/3_ablation.tex` | Anchor Strength: Finding a Stable Trade-off | active, unused | Aligned with `docs/01_outline.md`. |
| `subsec:ch6_ablation_recluster_frequency` | `report/chapters/chapter6/3_ablation.tex` | Recluster Frequency: How Often Should Groups Update? | active, unused | Renamed from cluster-refresh schedule to match outline. |

### Figure labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `fig:app_wandb_core_metrics` | `report/appendices.tex` | W&B core logging metrics and Q-trajectory dashboard exports | active, unused | Moved from Chapter 5 to Appendix B as tracking telemetry. |
| `fig:ch6_ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Number-of-clusters ablation figure | active, unused | Specific Chapter 6 ablation figure. |
| `fig:ch6_ablation_anchor_strength` | `report/chapters/chapter6/3_ablation.tex` | Anchor-strength ablation figure | active, unused | Specific Chapter 6 ablation figure. |
| `fig:ch6_ablation_recluster_frequency` | `report/chapters/chapter6/3_ablation.tex` | Cluster-refresh interval ablation figure | active, unused | Specific Chapter 6 ablation figure. |
| `fig:ch6_whitebox_radar_per_attack_accuracy` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox per-attack radar | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_abs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for PGD-AT | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_abs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for DDN-AT | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_abs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for Multi-AT | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_abs_attackdropp` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for AttackDRO++ | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_delta_vs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox delta heatmap vs Multi-AT | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_delta_vs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox delta heatmap vs PGD-AT | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_delta_vs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox delta heatmap vs DDN-AT | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_radar_delta_vs_baselines` | `report/chapters/chapter6/4_whitebox.tex` | Attack-wise whitebox delta vs baselines | active, unused | Chapter-aware rename. |
| `fig:ch6_whitebox_bottomk_lift` | `report/chapters/chapter6/4_whitebox.tex` | Bottom-K whitebox class-attack lift | active, unused | Chapter-aware rename. |
| `fig:ch6_graybox_transfer_matrix` | `report/chapters/chapter6/2_graybox_results.tex` | Method-level graybox transfer matrix | active, referenced | Chapter-aware rename. |
| `fig:ch6_graybox_transfer_linf` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox transfer matrices for linf attack family | active, referenced | Chapter-aware rename. |
| `fig:ch6_graybox_transfer_l2` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox transfer matrices for l2 attack family | active, referenced | Chapter-aware rename. |
| `fig:ch6_graybox_gap_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox-minus-whitebox gap heatmap for DDN-AT | active, referenced | Start of figure range. |
| `fig:ch6_graybox_gap_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox-minus-whitebox gap heatmap for PGD-AT | active, unused | Middle of figure range. |
| `fig:ch6_graybox_gap_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox-minus-whitebox gap heatmap for Multi-AT | active, unused | Middle of figure range. |
| `fig:ch6_graybox_gap_attackdropp` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox-minus-whitebox gap heatmap for AttackDRO++ | active, referenced | End of figure range. |
| `fig:ch6_graybox_delta_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox delta heatmap vs Multi-AT | active, referenced | Start of figure range. |
| `fig:ch6_graybox_delta_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox delta heatmap vs PGD-AT | active, unused | Middle of figure range. |
| `fig:ch6_graybox_delta_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox delta heatmap vs DDN-AT | active, referenced | End of figure range. |
| `fig:ch6_method_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | Visual decomposition of AttackDRO++ improvement | active, unused | Chapter-aware rename. |
| `fig:app_wrn2810_architecture_check` | `report/appendices.tex` | Supplementary WRN-28-10 architecture check figure | active, unused | Appendix C figure label. |

### Table labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `tab:ch4_hparams` | `report/chapters/chapter4/7-complete_pipeline.tex` | Default hyperparameters for AttackDRO++ | active, referenced | Renamed from `tab:hparams`. |
| `tab:ch5_resnet18_layer_summary` | `report/chapters/chapter5/2-architectures.tex` | CIFAR-10 ResNet-18 instantiated layer summary | active, referenced | Architecture table generated from the CIFAR-adapted ResNet-18 used in training. |
| `tab:ch5_training_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Training attack configuration | active, referenced | Chapter-aware rename. |
| `tab:ch5_evaluation_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Validation and test attacks for Mean(8) | active, referenced | Chapter-aware rename. |
| `tab:ch5_autoattack_config` | `report/chapters/chapter5/3-attack_suite.tex` | AutoAttack configuration | active, unused | Chapter-aware rename. |
| `tab:ch5_training_config` | `report/chapters/chapter5/4-configuration.tex` | General training configuration | active, referenced | Chapter-aware rename. |
| `tab:ch5_method_training_summary` | `report/chapters/chapter5/4-configuration.tex` | Compared training methods | active, referenced | Chapter-aware rename. |
| `tab:ch5_main_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Main AttackDRO++ hyperparameters | active, unused | Chapter-aware rename. |
| `tab:ch5_ablation_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Hyperparameters varied in ablations | active, referenced | Chapter-aware rename. |
| `tab:ch5_statistical_reporting_format` | `report/chapters/chapter5/6-protocol.tex` | Statistical reporting format | active, referenced | Renamed from hyphenated label. |
| `tab:ch5_evaluation_metrics_summary` | `report/chapters/chapter5/7-eval_metrics.tex` | Evaluation metrics summary | active, unused | Chapter-aware rename. |
| `tab:ch5_graybox_transfer_regimes` | `report/chapters/chapter5/8-graybox_transfer.tex` | Graybox transfer regimes | active, referenced | Chapter-aware rename. |
| `tab:ch5_tools_platforms` | `report/chapters/chapter5/9-tools_tracking.tex` | Tools and platforms used in experiments | active, referenced | New Chapter 5.9 table label. |
| `tab:ch5_setup_summary` | `report/chapters/chapter5/9-tools_tracking.tex` | Experimental setup recap | active, referenced | New Chapter 5.9 table label. |
| `tab:ch6_aggregate_results` | `report/chapters/chapter6/1_main_results.tex` | Aggregate robust accuracy | active, referenced | Standardized table label. |
| `tab:ch6_effect_size_summary` | `report/chapters/chapter6/1_main_results.tex` | Effect-size summary | active, referenced | Chapter-aware rename. |
| `tab:ch6_paired_aggregate_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Paired aggregate robustness comparisons | active, referenced | Chapter-aware rename. |
| `tab:ch6_corrected_paired_tests` | `report/chapters/chapter6/1_main_results.tex` | Multiple-comparison-corrected paired tests | active, referenced | Chapter-aware rename. |
| `tab:ch6_per_attack_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Per-attack robust accuracy | active, referenced | Chapter-aware rename. |
| `tab:ch6_worst_autoattack_sanity` | `report/chapters/chapter6/1_main_results.tex` | Worst(8) and AutoAttack sanity results | active, referenced | Chapter-aware rename. |
| `tab:ch6_autoattack_fulltest` | `report/chapters/chapter6/1_main_results.tex` | Full-test AutoAttack results | active, referenced | Chapter-aware rename. |
| `tab:ch6_variance_reduction` | `report/chapters/chapter6/1_main_results.tex` | Variance reduction across seeds | active, referenced | Renamed from hyphenated label. |
| `tab:ch6_whitebox_per_cell_summary` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox per-cell comparison | active, referenced | Chapter-aware rename. |
| `tab:ch6_graybox_whitebox_sanity` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox pipeline whitebox sanity check | active, unused | Chapter-aware rename. |
| `tab:ch6_paired_graybox_two_panel` | `report/chapters/chapter6/2_graybox_results.tex` | Paired graybox comparisons | active, referenced | Renamed from hyphenated label. |
| `tab:ch6_graybox_per_attack` | `report/chapters/chapter6/2_graybox_results.tex` | Per-attack symmetric graybox comparison | active, unused | Chapter-aware rename. |
| `tab:ch6_graybox_attack_family` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox accuracy by attack family | active, referenced | Chapter-aware rename. |
| `tab:ch6_graybox_gap` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox-graybox gap by target method | active, unused | Chapter-aware rename. |
| `tab:ch6_graybox_per_cell` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox per-cell tests | active, unused | Chapter-aware rename. |
| `tab:ch6_graybox_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | AttackDRO++ gain decomposition | active, unused | Chapter-aware rename. |
| `tab:ch6_ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Number-of-clusters ablation | active, referenced | Chapter-aware rename. |
| `tab:ch6_ablation_anchor_strength` | `report/chapters/chapter6/3_ablation.tex` | Anchor-strength ablation | active, referenced | Added for active Chapter 6 ablation table. |
| `tab:ch6_cluster_refresh_schedule_ablation` | `report/chapters/chapter6/3_ablation.tex` | Cluster-refresh schedule ablation | active, referenced | Chapter-aware rename. |
| `tab:ch7_rq_answers` | `report/chapters/chapter7.tex` | Removed research-question answer table | removed, deprecated | Section 7.2 now answers the research questions in prose paragraphs. |
| `tab:app_wrn2810_architecture_check` | `report/appendices.tex` | Supplementary WRN-28-10 architecture check | active, unused | Appendix C table label. |

### Algorithm labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `alg:ch4_attackdropp` | `report/chapters/chapter4/7-complete_pipeline.tex` | AttackDRO++ with Gradient Fingerprints and Uniform Anchor | active, referenced | Renamed from `alg:attackdropp`. |

### Equation labels

| Label | File | Points to | Referenced? | Notes |
|---|---|---|---|---|
| `eq:avg_risk` | `report/chapters/chapter4/1-problem_formulation.tex` | Average multi-attack risk | yes | Referenced by `\eqref`. |
| `eq:erm_loss` | `report/chapters/chapter4/2-multi_attack.tex` | Uniform Multi-Attack ERM loss | yes | Referenced by `\eqref`. |
| `eq:eg` | `report/chapters/chapter4/3-attackDRO.tex` | Exponentiated-gradient style update | no | Candidate for removal later if not referenced. |
| `eq:attackdro_floor` | `report/chapters/chapter4/3-attackDRO.tex` | AttackDRO floor / stabilizer equation | no | Candidate for removal later if not referenced. |
| `eq:cluster_loss` | `report/chapters/chapter4/4-attackDRO++.tex` | Cluster loss definition | no | Candidate for removal later if not referenced. |
| `eq:cluster_dro_loss` | `report/chapters/chapter4/4-attackDRO++.tex` | Cluster-DRO loss definition | no | Candidate for removal later if not referenced. |
| `eq:final_loss` | `report/chapters/chapter4/6-anchor_objective.tex` | Final anchored objective | yes | Referenced by `\eqref`. |
| `eq:floor` | `report/chapters/chapter4/6-anchor_objective.tex` | Uniform-anchor floor equation | no | Candidate for removal later if not referenced. |
| `eq:attack_acc` | `report/chapters/chapter5/7-eval_metrics.tex` | Attack-specific robust accuracy | no | Candidate for removal later if not referenced. |
| `eq:mean8` | `report/chapters/chapter5/7-eval_metrics.tex` | Mean(8) metric | no | Candidate for removal later if not referenced. |
| `eq:worst8` | `report/chapters/chapter5/7-eval_metrics.tex` | Worst(8) metric | no | Candidate for removal later if not referenced. |
| `eq:graybox_acc` | `report/chapters/chapter5/7-eval_metrics.tex` | Graybox accuracy metric | no | Candidate for removal later if not referenced. |
| `eq:attack_class_acc` | `report/chapters/chapter5/7-eval_metrics.tex` | Attack-class accuracy metric | no | Candidate for removal later if not referenced. |

### Appendix labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `app:algorithms` | `report/appendices/algorithms.tex` | Appendix A: Algorithms and Pseudocode | active, referenced | Referenced from Chapter 2 attack algorithms section. |
| `app:logs` | `report/appendices.tex` | Appendix B: Experimental Logs and Configurations | active, referenced | Referenced from Chapter 5.9 after moving the W&B tracking figure. |
| `app:extras` | `report/appendices.tex` | Appendix C: Additional Tables and Visualizations | active, referenced | Referenced from Chapter 6.4 supplementary architecture note. |
| `app:compute` | `report/appendices.tex` | Appendix D: Compute Resources and Environment Notes | active, unused | Prefix ok. |

### Other / unknown labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| None | - | - | - | No active unknown-label category remains. |

## 3. Reference audit

Active reference commands found: `\ref` and `\eqref`. No active uses were found for `\autoref`, `\cref`, `\Cref`, `\nameref`, or `\pageref`.

| Reference | Type | File | Target exists? | Notes |
|---|---|---|---|---|
| `chap:results_analysis` | `\ref` | `report/chapters/chapter5/9-tools_tracking.tex`; `report/chapters/chapter7.tex` | yes | Chapter 5.9 transition and Chapter 7 RQ answer section. |
| `chap:conclusion` | `\ref` | `report/chapters/chapter6/6_summary.tex` | yes | Chapter 6 transition to conclusion. |
| `chap:introduction` | `\ref` | `report/chapters/chapter7.tex` | yes | Chapter 7 maps answers back to the research questions. |
| `alg:ch4_attackdropp` | `\ref` | `report/chapters/chapter4/7-complete_pipeline.tex` | yes | Algorithm reference. |
| `eq:avg_risk` | `\eqref` | `report/chapters/chapter4/1-problem_formulation.tex` | yes | Equation reference. |
| `eq:erm_loss` | `\eqref` | `report/chapters/chapter4/2-multi_attack.tex` | yes | Equation reference. |
| `eq:final_loss` | `\eqref` | `report/chapters/chapter4/6-anchor_objective.tex` | yes | Equation reference. |
| `sec:ch4_problem_formulation` | `\ref` | `report/chapters/chapter4.tex` | yes | Chapter 4 overview. |
| `sec:ch4_multi_attack_erm` | `\ref` | `report/chapters/chapter4.tex` | yes | Chapter 4 overview. |
| `sec:ch4_attackdro` | `\ref` | `report/chapters/chapter4.tex` | yes | Chapter 4 overview. |
| `sec:ch4_attackdropp` | `\ref` | `report/chapters/chapter4.tex` | yes | Chapter 4 overview. |
| `sec:ch4_gradfp` | `\ref` | `report/chapters/chapter4.tex` | yes | Chapter 4 overview. |
| `sec:ch4_anchor_objective` | `\ref` | `report/chapters/chapter4.tex` | yes | Chapter 4 overview. |
| `sec:ch5_evaluation_metrics` | `\ref` | `report/chapters/chapter5/3-attack_suite.tex`; `report/chapters/chapter6/2_graybox_results.tex` | yes | Metric definitions. |
| `sec:ch5_graybox_protocol` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Graybox protocol reference. |
| `sec:ch6_whitebox` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex`; `report/chapters/chapter6/4_whitebox.tex`; `report/chapters/chapter7.tex` | yes | Whitebox result reference. |
| `sec:ch6_whitebox_class_attack` | `\ref` | `report/chapters/chapter7.tex` | yes | Chapter 7 RQ answer section. |
| `sec:ch6_graybox` | `\ref` | `report/chapters/chapter7.tex` | yes | Chapter 7 RQ answer section. |
| `sec:ch6_ablation` | `\ref` | `report/chapters/chapter7.tex` | yes | Chapter 7 RQ answer section. |
| `chap:experimental_setup` | `\ref` | `report/chapters/chapter4/summary.tex`; `report/chapters/chapter6/3_ablation.tex`; `report/chapters/chapter7.tex` | yes | Setup chapter references. |
| `chap:methodology` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Method chapter reference. |
| `app:logs` | `\ref` | `report/chapters/chapter5/9-tools_tracking.tex` | yes | Appendix B tracking export reference. |
| `app:algorithms` | `\ref` | `report/chapters/chapter2/2-at-deep-dive.tex` | yes | Appendix A attack and training pseudocode reference. |
| `app:extras` | `\ref` | `report/chapters/chapter6/3_ablation.tex`; `report/chapters/chapter7.tex` | yes | Appendix C supplementary architecture reference. |
| `subsec:ch6_per_attack_accuracy` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex`; `report/chapters/chapter7.tex` | yes | Per-attack whitebox subsection reference. |
| `subsec:ch6_hardest_evaluation_cases` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Hardest-evaluation subsection reference. |
| `subsec:ch6_paired_graybox_comparisons` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Graybox comparison subsection reference. |
| `tab:ch4_hparams` | `\ref` | `report/chapters/chapter4/7-complete_pipeline.tex` | yes | Table reference. |
| `tab:ch5_resnet18_layer_summary` | `\ref` | `report/chapters/chapter5/2-architectures.tex` | yes | Model architecture table reference. |
| `tab:ch5_training_attacks` | `\ref` | `report/chapters/chapter5/3-attack_suite.tex` | yes | Table reference. |
| `tab:ch5_evaluation_attacks` | `\ref` | `report/chapters/chapter5/3-attack_suite.tex` | yes | Table reference. |
| `tab:ch5_training_config` | `\ref` | `report/chapters/chapter5/4-configuration.tex` | yes | Table reference. |
| `tab:ch5_method_training_summary` | `\ref` | `report/chapters/chapter5/4-configuration.tex` | yes | Table reference. |
| `tab:ch5_ablation_hyperparams` | `\ref` | `report/chapters/chapter5/5-choices.tex` | yes | Table reference. |
| `tab:ch5_statistical_reporting_format` | `\ref` | `report/chapters/chapter5/6-protocol.tex` | yes | Table reference. |
| `tab:ch5_graybox_transfer_regimes` | `\ref` | `report/chapters/chapter5/8-graybox_transfer.tex` | yes | Table reference. |
| `tab:ch5_tools_platforms` | `\ref` | `report/chapters/chapter5/9-tools_tracking.tex` | yes | New Chapter 5.9 table reference. |
| `tab:ch5_setup_summary` | `\ref` | `report/chapters/chapter5/9-tools_tracking.tex` | yes | New Chapter 5.9 table reference. |
| `tab:ch6_aggregate_results` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Table reference. |
| `tab:ch6_effect_size_summary` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_paired_aggregate_all_baselines` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_corrected_paired_tests` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_per_attack_all_baselines` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_worst_autoattack_sanity` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_autoattack_fulltest` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_variance_reduction` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:ch6_whitebox_per_cell_summary` | `\ref` | `report/chapters/chapter6/4_whitebox.tex` | yes | Table reference. |
| `tab:ch6_paired_graybox_two_panel` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Table reference. |
| `tab:ch6_graybox_attack_family` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Table reference. |
| `tab:ch6_ablation_num_clusters` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Table reference. |
| `tab:ch6_ablation_anchor_strength` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Table reference. |
| `tab:ch6_cluster_refresh_schedule_ablation` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Table reference. |
| `fig:ch6_graybox_transfer_matrix` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Figure reference. |
| `fig:ch6_graybox_transfer_linf` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Figure reference. |
| `fig:ch6_graybox_transfer_l2` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Figure reference. |
| `fig:ch6_graybox_gap_ddnat` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Start of heatmap range. |
| `fig:ch6_graybox_gap_attackdropp` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | End of heatmap range. |
| `fig:ch6_graybox_delta_multiat` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Start of heatmap range. |
| `fig:ch6_graybox_delta_ddnat` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | End of heatmap range. |

Audit findings:

- Undefined references in active source audit: none.
- Duplicate labels in active source audit: none.
- Active references to archived files or inactive sections: none.
- Active labels with `sec:` attached to a subsection: none.
- Active hyphenated labels: none.
- Inactive labels noted but not renamed: `chap:analysis` in archived old Chapter 7.
- Equation labels that are never referenced: `eq:attack_acc`, `eq:attack_class_acc`, `eq:attackdro_floor`, `eq:cluster_dro_loss`, `eq:cluster_loss`, `eq:eg`, `eq:floor`, `eq:graybox_acc`, `eq:mean8`, `eq:worst8`.
- Several active figure and table labels are unused because the objects are shown in sequence but not directly referenced in prose.

## 4. Recommended cleanup later

### Safe automatic cleanup

- Add direct references to important main-text figures currently unused, especially Chapter 6 whitebox heatmaps and radar figures.
- Remove labels from equations that remain unreferenced after the next prose pass.
- Keep `docs/03_label_registry.md` synchronized whenever labels are added or renamed.

### Needs user confirmation

- Whether to add labels to Chapter 1, Chapter 2, and Chapter 3 sections after those chapters are rewritten.
- Whether unused figure/table labels should remain for future prose references or be removed later.

### Postpone

- Do not rename labels inside archived `report/chapters/chapter7_old_analysis_discussion.tex` unless that file is reactivated.
- Do not remove unreferenced equation labels until the final writing pass confirms they are unnecessary.
- Do not relabel disabled Chapter 6 summary material unless the block is reactivated.

## 5. Registry maintenance rule

Whenever a label is added, removed, or renamed in LaTeX, update `docs/03_label_registry.md` in the same writing session.

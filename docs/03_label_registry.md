# 03_label_registry.md

Purpose:
A single source of truth for all LaTeX labels and references in the report.

Scope: this registry was built from the current compiled 7-chapter flow in `report/main.tex`, plus inactive/archived report `.tex` files where labels were found. Commented labels/references are not counted. Labels inside `\iffalse...\fi` are marked inactive.

## 1. Label naming rules

Source: `docs/06_style_rules.md`.

- `chap:` labels point to chapters, e.g. `chap:introduction`, `chap:background`, `chap:related_work`, `chap:methodology`, `chap:experimental_setup`, `chap:results_analysis`, `chap:conclusion`.
- `sec:` labels point to sections. Prefer chapter-aware names for major sections, e.g. `sec:ch6_whitebox`.
- `subsec:` labels point to subsections, e.g. `subsec:ch6_per_attack_results`.
- `fig:` labels point to figures, e.g. `fig:ch6_whitebox_radar`.
- `tab:` labels point to tables, e.g. `tab:ch6_main_results`.
- `alg:` labels point to algorithms and include the chapter where the algorithm is defined, e.g. `alg:ch4_attackdropp`.
- `eq:` labels point to equations. Equations normally do not need a chapter prefix unless two equations could be confused.
- `app:` labels point to appendices. Current source uses `app:pseudocode`, `app:logs`, `app:extras`, and `app:compute`.

Additional rules:

- Only label equations that are referenced later.
- Do not add labels just because an equation is displayed.
- Prefer preserving existing labels unless they are broken, duplicated, misleading, or against style.
- Whenever a label is added, removed, or renamed in LaTeX, update `docs/03_label_registry.md` in the same writing session.

Status values:

- `active`: label is in the current compiled flow.
- `referenced`: at least one active reference points to the label.
- `unused`: no active reference points to the label.
- `inactive`: label exists in a file or block that is not part of the current compiled flow.
- `style drift`: label works but does not follow the preferred style convention.
- `prefix mismatch`: label prefix does not match the actual LaTeX object type.

## 2. Label inventory

### Chapter labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `chap:introduction` | `report/chapters/chapter1.tex` | Chapter 1: Introduction | active, unused | Prefix ok. |
| `chap:background` | `report/chapters/chapter2.tex` | Chapter 2: Background | active, unused | Prefix ok. |
| `chap:related-work` | `report/chapters/chapter3.tex` | Chapter 3: Related Work | active, unused, style drift | Style examples prefer underscores: `chap:related_work`. |
| `chap:proposed_methodology` | `report/chapters/chapter4.tex` | Chapter 4: Proposed Methodology | active, unused, style drift | Style example prefers `chap:methodology`. |
| `chap:results` | `report/chapters/chapter6.tex` | Chapter 6: Results and Analysis | active, unused, style drift | Style example prefers `chap:results_analysis`. |
| `chap:conclusion` | `report/chapters/chapter7.tex` | Chapter 7: Conclusion and Future Work | active, unused | Prefix ok. |
| `chap:analysis` | `report/chapters/chapter7_old_analysis_discussion.tex` | Archived old Chapter 7: Analysis and Discussion | inactive | Archived file is not included by `report/main.tex`. |

Notes:

- Chapter 5 currently has no chapter label. Style examples suggest `chap:experimental_setup`.

### Section labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `sec:formulation` | `report/chapters/chapter4/1-problem_formulation.tex` | Multi-Attack Training as a Domain Problem | active, referenced | Prefix ok. |
| `sec:erm` | `report/chapters/chapter4/2-multi_attack.tex` | Uniform Multi-Attack ERM | active, referenced | Prefix ok. |
| `sec:attackdro` | `report/chapters/chapter4/3-attackDRO.tex` | AttackDRO: Group DRO Over Attack Identities | active, referenced | Prefix ok. |
| `sec:attackdropp` | `report/chapters/chapter4/4-attackDRO++.tex` | AttackDRO++: Group DRO Over Discovered Clusters | active, referenced | Prefix ok. |
| `sec:augmented-clustering-features` | `report/chapters/chapter4/5-clustering_feature.tex` | Augmented Clustering with Gradient Fingerprints | active, unused, style drift | Hyphenated label; `sec:gradfp` is the referenced alias. |
| `sec:gradfp` | `report/chapters/chapter4/5-clustering_feature.tex` | Augmented Clustering with Gradient Fingerprints | active, referenced | Added as working target for Chapter 4 overview. |
| `sec:anchor` | `report/chapters/chapter4/6-anchor_objective.tex` | Uniform-Anchored Training Objective | active, referenced | Prefix ok. |
| `sec:pipeline` | `report/chapters/chapter4/7-complete_pipeline.tex` | Complete Training Framework | active, unused | Prefix ok. |
| `sec:ch4summary` | `report/chapters/chapter4/summary.tex` | Chapter Summary | active, unused | Section should later become closing prose per style rules. |
| `sec:graybox-design` | `report/chapters/chapter5/8-graybox_transfer.tex` | Graybox Transfer Protocol | active, referenced, style drift | Hyphenated label. |
| `sec:evaluation_metrics` | `report/chapters/chapter5/7-eval_metrics.tex` | Evaluation Metrics and Robustness Definitions | active, referenced | Prefix ok. |
| `sec:statistical-significance-protocol` | `report/chapters/chapter5/6-protocol.tex` | Statistical Significance Protocol | active, unused, style drift | Hyphenated label. |
| `sec:hyperparameters` | `report/chapters/chapter5/5-choices.tex` | Hyperparameter Choices and Ablation Factors | active, unused | Prefix ok. |
| `sec:main_results` | `report/chapters/chapter6/1_main_results.tex` | Whitebox Robustness Under Direct Attacks | active, referenced | Prefix ok; target outline name would likely be `sec:ch6_whitebox`. |
| `sec:whitebox_class_attack` | `report/chapters/chapter6/4_whitebox.tex` | Class-wise Whitebox Robustness Across Attacks | active, unused | Prefix ok. |
| `sec:graybox_transfer_results` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox Robustness Across Surrogate Models | active, unused | Prefix ok. |

### Subsection labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `sec:evaluation_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Evaluation Attacks | active, unused, prefix mismatch | Actual object is a subsection; preferred prefix is `subsec:`. |
| `sec:aggregate_robustness` | `report/chapters/chapter6/1_main_results.tex` | Aggregate Robustness | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:per_attack_breakdown` | `report/chapters/chapter6/1_main_results.tex` | Per-Attack Robustness Breakdown | active, referenced, prefix mismatch | Actual object is a subsection. |
| `sec:worst_case_behavior` | `report/chapters/chapter6/1_main_results.tex` | Worst-Case Behavior: Worst(8) and AutoAttack | active, referenced, prefix mismatch | Actual object is a subsection. |
| `sec:variance_reduction` | `report/chapters/chapter6/1_main_results.tex` | Variance Reduction and Training Stability | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:whitebox_per_class` | `report/chapters/chapter6/4_whitebox.tex` | Per-Class Whitebox Robustness Pattern | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:whitebox_attack_class_delta` | `report/chapters/chapter6/4_whitebox.tex` | Per-Class Whitebox Robustness Pattern | active, unused, prefix mismatch | Label is not attached directly to a heading; likely intended for a local discussion block. |
| `sec:whitebox_attack_family_interpretation` | `report/chapters/chapter6/4_whitebox.tex` | Attack-Family Interpretation | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:whitebox_bottomk` | `report/chapters/chapter6/4_whitebox.tex` | Bottom-\(K\) Whitebox Tail Robustness | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_panel` | `report/chapters/chapter6/2_graybox_results.tex` | Seed Selection and Whitebox Sanity Check | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_matrix` | `report/chapters/chapter6/2_graybox_results.tex` | Cross-Method Transfer Matrix | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_headline` | `report/chapters/chapter6/2_graybox_results.tex` | AttackDRO++ vs. Multi-AT | active, referenced, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_per_attack` | `report/chapters/chapter6/2_graybox_results.tex` | Per-Attack Analysis | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_gap` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox--Graybox Gap and Specialist Inflation | active, referenced, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_per_cell` | `report/chapters/chapter6/2_graybox_results.tex` | Per-(Class-Attack) Analysis | active, unused, prefix mismatch | Actual object is a subsection. |
| `sec:graybox_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | Method Contribution Decomposition | active, unused, prefix mismatch | Actual object is a subsection. |
| `subsec:ablation_anchor_strength` | `report/chapters/chapter6/3_ablation.tex` | Anchor Strength | active, unused | Prefix ok. |
| `subsec:ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Number of Clusters | active, unused | Prefix ok. |
| `subsec:ablation_cluster_refresh` | `report/chapters/chapter6/3_ablation.tex` | Cluster-Refresh Schedule | active, unused | Prefix ok. |

### Figure labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `fig:ablation_dashboard` | `report/chapters/chapter6/3_ablation.tex` | Ablation dashboard for AttackDRO++ | active, referenced | Prefix ok. |
| `fig:whitebox_radar_per_attack_accuracy` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox per-attack radar | active, unused | Main-text figure but not directly referenced. |
| `fig:whitebox_abs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for PGD-AT | active, unused | Prefix ok. |
| `fig:whitebox_abs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for DDN-AT | active, unused | Prefix ok. |
| `fig:whitebox_abs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for Multi-AT | active, unused | Prefix ok. |
| `fig:whitebox_abs_attackdropp` | `report/chapters/chapter6/4_whitebox.tex` | Absolute whitebox class-attack heatmap for AttackDRO++ | active, unused | Prefix ok. |
| `fig:whitebox_delta_vs_multiat` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox delta heatmap vs Multi-AT | active, unused | Prefix ok. |
| `fig:whitebox_delta_vs_pgdat` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox delta heatmap vs PGD-AT | active, unused | Prefix ok. |
| `fig:whitebox_delta_vs_ddnat` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox delta heatmap vs DDN-AT | active, unused | Prefix ok. |
| `fig:whitebox_radar_delta_vs_baselines` | `report/chapters/chapter6/4_whitebox.tex` | Attack-wise whitebox delta vs baselines | active, unused | Prefix ok. |
| `fig:whitebox_bottomk_lift` | `report/chapters/chapter6/4_whitebox.tex` | Bottom-K whitebox class-attack lift | active, unused | Prefix ok. |
| `fig:graybox_transfer_matrix` | `report/chapters/chapter6/2_graybox_results.tex` | Method-level graybox transfer matrix | active, referenced | Prefix ok. |
| `fig:graybox_transfer_linf` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox transfer matrices for linf attack family | active, referenced | Prefix ok. |
| `fig:graybox_transfer_l2` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox transfer matrices for l2 attack family | active, referenced | Prefix ok. |
| `fig:graybox_gap_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox--graybox gap heatmap for DDN-AT | active, referenced | Start of figure range. |
| `fig:graybox_gap_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox--graybox gap heatmap for PGD-AT | active, unused | Middle of range `fig:graybox_gap_ddnat`--`fig:graybox_gap_attackdropp`; not directly referenced. |
| `fig:graybox_gap_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox--graybox gap heatmap for Multi-AT | active, unused | Middle of range; not directly referenced. |
| `fig:graybox_gap_attackdropp` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox--graybox gap heatmap for AttackDRO++ | active, referenced | End of figure range. |
| `fig:graybox_delta_multiat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox delta heatmap vs Multi-AT | active, referenced | Start of figure range. |
| `fig:graybox_delta_pgdat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox delta heatmap vs PGD-AT | active, unused | Middle of range `fig:graybox_delta_multiat`--`fig:graybox_delta_ddnat`; not directly referenced. |
| `fig:graybox_delta_ddnat` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox delta heatmap vs DDN-AT | active, referenced | End of figure range. |
| `fig:method_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | Visual decomposition of AttackDRO++ improvement | active, unused | Prefix ok. |

### Table labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `tab:hparams` | `report/chapters/chapter4/7-complete_pipeline.tex` | Default hyperparameters for AttackDRO++ | active, referenced | Prefix ok. |
| `tab:training_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Training attack configuration | active, referenced | Prefix ok. |
| `tab:evaluation_attacks` | `report/chapters/chapter5/3-attack_suite.tex` | Validation and test attacks for Mean(8) | active, referenced | Prefix ok. |
| `tab:autoattack_config` | `report/chapters/chapter5/3-attack_suite.tex` | AutoAttack configuration | active, unused | Prefix ok. |
| `tab:training_config` | `report/chapters/chapter5/4-configuration.tex` | General training configuration | active, referenced | Prefix ok. |
| `tab:method_training_summary` | `report/chapters/chapter5/4-configuration.tex` | Compared training methods | active, referenced | Prefix ok. |
| `tab:main_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Main AttackDRO++ hyperparameters | active, unused | Prefix ok. |
| `tab:ablation_hyperparams` | `report/chapters/chapter5/5-choices.tex` | Hyperparameters varied in ablations | active, referenced | Prefix ok. |
| `tab:statistical-reporting-format` | `report/chapters/chapter5/6-protocol.tex` | Statistical reporting format | active, referenced, style drift | Hyphenated label. |
| `tab:evaluation_metrics_summary` | `report/chapters/chapter5/7-eval_metrics.tex` | Evaluation metrics summary | active, unused | Prefix ok. |
| `tab:graybox_transfer_regimes` | `report/chapters/chapter5/8-graybox_transfer.tex` | Graybox transfer regimes | active, referenced | Prefix ok. |
| `tab:agg-results` | `report/chapters/chapter6/1_main_results.tex` | Aggregate robust accuracy | active, referenced, style drift | Hyphenated label. |
| `tab:effect_size_summary` | `report/chapters/chapter6/1_main_results.tex` | Effect-size summary | active, referenced | Prefix ok. |
| `tab:paired_aggregate_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Paired aggregate robustness comparisons | active, referenced | Prefix ok. |
| `tab:corrected_paired_tests` | `report/chapters/chapter6/1_main_results.tex` | Multiple-comparison-corrected paired tests | active, referenced | Prefix ok. |
| `tab:per_attack_all_baselines` | `report/chapters/chapter6/1_main_results.tex` | Per-attack robust accuracy | active, referenced | Prefix ok. |
| `tab:worst_autoattack_sanity` | `report/chapters/chapter6/1_main_results.tex` | Worst(8) and AutoAttack sanity results | active, referenced | Prefix ok. |
| `tab:autoattack_fulltest` | `report/chapters/chapter6/1_main_results.tex` | Full-test AutoAttack results | active, referenced | Prefix ok. |
| `tab:variance-reduction` | `report/chapters/chapter6/1_main_results.tex` | Variance reduction across seeds | active, referenced, style drift | Hyphenated label. |
| `tab:whitebox_per_cell_summary` | `report/chapters/chapter6/4_whitebox.tex` | Whitebox per-cell comparison | active, referenced | Prefix ok. |
| `tab:graybox_whitebox_sanity` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox pipeline whitebox sanity check | active, unused | Prefix ok. |
| `tab:paired-graybox-two-panel` | `report/chapters/chapter6/2_graybox_results.tex` | Paired graybox comparisons | active, referenced, style drift | Hyphenated label. |
| `tab:graybox_per_attack` | `report/chapters/chapter6/2_graybox_results.tex` | Per-attack symmetric graybox comparison | active, unused | Prefix ok. |
| `tab:graybox_attack_family` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox accuracy by attack family | active, referenced | Prefix ok. |
| `tab:graybox_gap` | `report/chapters/chapter6/2_graybox_results.tex` | Whitebox--graybox gap by target method | active, unused | Prefix ok. |
| `tab:graybox_per_cell` | `report/chapters/chapter6/2_graybox_results.tex` | Graybox per-cell tests | active, unused | Prefix ok. |
| `tab:graybox_decomposition` | `report/chapters/chapter6/2_graybox_results.tex` | AttackDRO++ gain decomposition | active, unused | Prefix ok. |
| `tab:ablation_num_clusters` | `report/chapters/chapter6/3_ablation.tex` | Number-of-clusters ablation | active, referenced | Prefix ok. |
| `tab:cluster_refresh_schedule_ablation` | `report/chapters/chapter6/3_ablation.tex` | Cluster-refresh schedule ablation | active, referenced | Prefix ok. |

### Algorithm labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `alg:attackdropp` | `report/chapters/chapter4/7-complete_pipeline.tex` | AttackDRO++ with Gradient Fingerprints and Uniform Anchor | active, referenced, style drift | Style example prefers chapter-aware `alg:ch4_attackdropp`. |

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
| `app:pseudocode` | `report/appendices.tex` | Appendix A: Illustrative Pseudo-code and Flowcharts | active, unused | Prefix ok. |
| `app:logs` | `report/appendices.tex` | Appendix B: Experimental Logs and Configurations | active, unused | Prefix ok. |
| `app:extras` | `report/appendices.tex` | Appendix C: Additional Tables and Visualizations | active, unused | Prefix ok. |
| `app:compute` | `report/appendices.tex` | Appendix D: Compute Resources and Environment Notes | active, unused | Prefix ok. |

### Other / unknown labels

| Label | File | Points to | Status | Notes |
|---|---|---|---|---|
| `sec:graybox_section_summary` | `report/chapters/chapter6/2_graybox_results.tex` | Disabled Section Summary block | inactive | Inside `\iffalse...\fi`; not compiled. Prefix also mismatches actual object type. |

Notes:

- The commented label `% \label{sec:section_summary}` in `report/chapters/chapter6/1_main_results.tex` is ignored and not part of the active registry.
- `report/chapters/chapter6/5_diagnostics.tex` contains headings but no labels; it is not input by the active Chapter 6 flow.

## 3. Reference audit

Active reference commands found: `\ref` and `\eqref`.

No active uses were found for `\autoref`, `\cref`, `\Cref`, `\nameref`, or `\pageref`.

| Reference | Type | File | Target exists? | Notes |
|---|---|---|---|---|
| `alg:attackdropp` | `\ref` | `report/chapters/chapter4/7-complete_pipeline.tex` | yes | Algorithm reference. |
| `eq:avg_risk` | `\eqref` | `report/chapters/chapter4/1-problem_formulation.tex` | yes | Equation reference. |
| `eq:erm_loss` | `\eqref` | `report/chapters/chapter4/2-multi_attack.tex` | yes | Equation reference. |
| `eq:final_loss` | `\eqref` | `report/chapters/chapter4/6-anchor_objective.tex` | yes | Equation reference. |
| `fig:ablation_dashboard` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Referenced twice. |
| `fig:graybox_delta_multiat` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Start of graybox delta figure range. |
| `fig:graybox_delta_ddnat` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | End of graybox delta figure range. |
| `fig:graybox_gap_ddnat` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Start of gap heatmap figure range. |
| `fig:graybox_gap_attackdropp` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | End of gap heatmap figure range. |
| `fig:graybox_transfer_linf` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Figure reference. |
| `fig:graybox_transfer_l2` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Figure reference. |
| `fig:graybox_transfer_matrix` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Figure reference. |
| `sec:anchor` | `\ref` | `report/chapters/chapter4.tex` | yes | Section reference. |
| `sec:attackdro` | `\ref` | `report/chapters/chapter4.tex` | yes | Section reference. |
| `sec:attackdropp` | `\ref` | `report/chapters/chapter4.tex` | yes | Section reference. |
| `sec:erm` | `\ref` | `report/chapters/chapter4.tex` | yes | Section reference. |
| `sec:evaluation_metrics` | `\ref` | `report/chapters/chapter5/3-attack_suite.tex`; `report/chapters/chapter6/2_graybox_results.tex` | yes | Referenced from Chapter 5 and Chapter 6. |
| `sec:formulation` | `\ref` | `report/chapters/chapter4.tex` | yes | Section reference. |
| `sec:gradfp` | `\ref` | `report/chapters/chapter4.tex` | yes | Section reference. |
| `sec:graybox-design` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Referenced twice; label has style drift due hyphen. |
| `sec:graybox_gap` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Referenced twice; target is a subsection with `sec:` prefix. |
| `sec:graybox_headline` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Target is a subsection with `sec:` prefix. |
| `sec:main_results` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex`; `report/chapters/chapter6/4_whitebox.tex` | yes | Referenced four times. |
| `sec:per_attack_breakdown` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Target is a subsection with `sec:` prefix. |
| `sec:worst_case_behavior` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Referenced twice; target is a subsection with `sec:` prefix. |
| `tab:ablation_hyperparams` | `\ref` | `report/chapters/chapter5/5-choices.tex` | yes | Table reference. |
| `tab:ablation_num_clusters` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Table reference. |
| `tab:agg-results` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Table reference; hyphenated label. |
| `tab:autoattack_fulltest` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:cluster_refresh_schedule_ablation` | `\ref` | `report/chapters/chapter6/3_ablation.tex` | yes | Table reference. |
| `tab:corrected_paired_tests` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Referenced twice. |
| `tab:effect_size_summary` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |
| `tab:evaluation_attacks` | `\ref` | `report/chapters/chapter5/3-attack_suite.tex` | yes | Table reference. |
| `tab:graybox_attack_family` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Table reference. |
| `tab:graybox_transfer_regimes` | `\ref` | `report/chapters/chapter5/8-graybox_transfer.tex` | yes | Table reference. |
| `tab:hparams` | `\ref` | `report/chapters/chapter4/7-complete_pipeline.tex` | yes | Table reference. |
| `tab:method_training_summary` | `\ref` | `report/chapters/chapter5/4-configuration.tex` | yes | Table reference. |
| `tab:paired_aggregate_all_baselines` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Referenced three times. |
| `tab:paired-graybox-two-panel` | `\ref` | `report/chapters/chapter6/2_graybox_results.tex` | yes | Table reference; hyphenated label. |
| `tab:per_attack_all_baselines` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Referenced three times. |
| `tab:statistical-reporting-format` | `\ref` | `report/chapters/chapter5/6-protocol.tex` | yes | Table reference; hyphenated label. |
| `tab:training_attacks` | `\ref` | `report/chapters/chapter5/3-attack_suite.tex` | yes | Table reference. |
| `tab:training_config` | `\ref` | `report/chapters/chapter5/4-configuration.tex` | yes | Table reference. |
| `tab:variance-reduction` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference; hyphenated label. |
| `tab:whitebox_per_cell_summary` | `\ref` | `report/chapters/chapter6/4_whitebox.tex` | yes | Table reference. |
| `tab:worst_autoattack_sanity` | `\ref` | `report/chapters/chapter6/1_main_results.tex` | yes | Table reference. |

Audit findings:

- Undefined references: none in active LaTeX source.
- Duplicate labels: none in active LaTeX source.
- References to archived files or inactive sections: none in active LaTeX source.
- Inactive labels found:
  - `chap:analysis` in archived `report/chapters/chapter7_old_analysis_discussion.tex`.
  - `sec:graybox_section_summary` inside a disabled `\iffalse...\fi` block.
- Equation labels that are never referenced: `eq:attack_acc`, `eq:attack_class_acc`, `eq:attackdro_floor`, `eq:cluster_dro_loss`, `eq:cluster_loss`, `eq:eg`, `eq:floor`, `eq:graybox_acc`, `eq:mean8`, `eq:worst8`.
- Labels whose prefix does not match object type: subsection labels using `sec:` in Chapter 5 and Chapter 6; see the subsection inventory.
- Labels with style drift: labels using hyphens instead of underscores, and chapter labels that differ from examples in `docs/06_style_rules.md`.

## 4. Recommended cleanup later

### Safe automatic cleanup

- Remove labels from equations that remain unreferenced after the next prose pass.
- Add missing chapter label for Chapter 5, likely `chap:experimental_setup`, if Chapter 5 will be referenced.
- Add direct references to important main-text figures currently unused, especially Chapter 6 whitebox heatmaps and radar figures.
- Replace hyphenated label names with underscore variants only if all references are updated in the same patch.

### Needs user confirmation

- Whether to rename existing working chapter labels to match style examples:
  - `chap:related-work` -> `chap:related_work`
  - `chap:proposed_methodology` -> `chap:methodology`
  - `chap:results` -> `chap:results_analysis`
- Whether to rename subsection labels from `sec:` to `subsec:` throughout Chapter 5 and Chapter 6.
- Whether to keep both `sec:augmented-clustering-features` and `sec:gradfp`, or consolidate to one label.
- Whether to add labels to Chapter 1, Chapter 2, and Chapter 3 sections after the final outline rewrite.

### Postpone

- Do not rename labels while Chapter 2, Chapter 5.9, Chapter 6 graybox consolidation, and Chapter 7 are still structurally incomplete.
- Do not create `docs/04_figure_table_registry.md` yet.
- Do not create `docs/05_notation_registry.md` yet.
- Do not move diagnostics or extra ablations into appendices until the user decides whether they should appear in the PDF.

## 5. Registry maintenance rule

Whenever a label is added, removed, or renamed in LaTeX, update `docs/03_label_registry.md` in the same writing session.

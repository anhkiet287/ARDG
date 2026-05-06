# 00_llm_handoff.md

## Current repo state

- Repo root: `C:\Users\ADMIN\Documents\GitHub\ARDG`.
- Report entry point: `report/main.tex`.
- Current figure folder: `report/figures`.
- The report now compiles as 7 active main chapters plus appendices.
- Active chapter includes in `report/main.tex`: `chapter1`, `chapter2`, `chapter3`, `chapter4`, `chapter5`, `chapter6`, `chapter7`.
- Old `report/chapters/chapter7.tex` was archived as `report/chapters/chapter7_old_analysis_discussion.tex`.
- Old `report/chapters/chapter8.tex` was renamed to `report/chapters/chapter7.tex`.
- `report/chapters/chapter7.tex` is still only an empty `Conclusion and Future Work` shell.
- `report/chapters/chapter6/5_diagnostics.tex` still exists, but is no longer input from `report/chapters/chapter6.tex`.
- `report/chapters/chapter6/6_summary.tex` is still input but empty.
- Git currently reports `report/` as untracked in this checkout, so normal `git diff` does not show most report edits. Use `git status --short` or add/stage intentionally before relying on Git rename detection.

## Latest changes

- Fixed planning-file method naming consistency across `docs/01_outline.md` and `docs/06_style_rules.md`.
- Final names: `PGD-AT`, `DDN-AT`, `Multi-AT`, and `AttackDRO++` for formal result tables/captions.
- Created `docs/07_task_assignment.md` as the practical writing task board for the report team.
- Task board assigns Chapter 2 to ĐA, Chapter 3 to Thành, Chapters 1 and 4-7 to Kiệt, and cross-file consistency to the Team.
- The task board is based on the local LaTeX to-do comments plus the outline, style rules, and label/figure/notation registries.
- No LaTeX source files were edited for the task-assignment task, and the report was not recompiled.
- Added local to-do writing instructions in the active LaTeX source files for Chapters 1-7.
- to-do owners: `to-do[ĐA]` for Chapter 2, `to-do[Thành]` for Chapter 3, `to-do[Kiệt]` for Chapters 1 and 4-7, and `to-do[Team]` for shared table/figure/setup work.
- No prose, results, labels, section titles, numerical values, figures, or tables were changed.
- No compilation required unless desired; the patch only adds LaTeX comment lines.
- Created `docs/04_figure_table_registry.md` as the current figure/table registry for the compiled 7-chapter report.
- Registry findings: all active chapter `\includegraphics` paths resolve under `report/figures/`, but many Chapter 6 figures/tables are active yet unreferenced, several captions need metric/averaging polish, and several outline-planned labels differ from the active compiled labels.
- Registry also records unused figure assets under `report/figures/`, likely candidates for Chapter 6 planned visuals, and remaining planned tables such as `tab:ch5_tools_platforms`, `tab:ch5_setup_summary`, and a Chapter 7 RQ answer table.
- No LaTeX source files were edited for the figure/table registry task, and the report was not recompiled.
- Created `docs/05_notation_registry.md` as the current notation/acronym/method/attack/metric registry for the compiled 7-chapter report.
- Registry findings: formal method names are mostly established as `PGD-AT`, `DDN-AT`, `Multi-AT`, and `AttackDRO++`, while remaining cleanup candidates include `Multi-ATtack`, `PGD20-CE`, `M(8)`, `Uniform Multi-AT`, and `AttackDRO++ Anchor35 GradFP` in older prose/table text.
- Registry also records the current metric/equation notation, attack-name mapping, acronym gaps, planned tools/platforms for Chapter 5.9, and notation issues such as the `K` class-count versus cluster-count ambiguity.
- No LaTeX source files were edited for the notation registry task, and the report was not recompiled.
- Created `docs/03_label_registry.md` as the current label/reference registry for the compiled 7-chapter report.
- Registry findings: no active duplicate labels, no active undefined references, no active references to archived/inactive labels.
- Registry flags for later cleanup: several subsection labels use `sec:` instead of `subsec:`, several labels use hyphens instead of underscores, and multiple equation labels are currently unreferenced.
- No LaTeX source files were edited for the registry task.

## Actual LaTeX structure

Active structure after the structural patch:

```text
Chapter 1: Introduction
  1.1 Adversarial Robustness and the Cross-Attack Gap
  1.2 Diagnostic Findings and Their Limitations
  1.3 Problem Statement
  1.4 Research Questions and Hypotheses
  1.5 Contributions of This Work
  1.6 Scope and Limitations
  1.7 Report Organization

Chapter 2: Background
  2.1 Preliminaries
    2.1.1 Deep Neural Networks and Classification
    2.1.2 Adversarial examples
    2.1.3 Threat models
  2.2 Adversarial Training Deep Dive
    2.2.1 Min-max formulation
    2.2.2 PGD-AT and its limitations
    2.2.3 Multi-attack AT approaches
    2.2.4 Trade-off analysis
  2.3 Distributionally Robust Optimization
    2.3.1 Classical DRO formulation
    2.3.2 Group DRO
    2.3.3 Exponentiated gradient on simplex
    2.3.4 Regularization in overparameterized models
    2.3.5 DRO in adversarial training context
  2.4 Domain Generalization via Clustering
    2.4.1 Clustering-based domain discovery
    2.4.2 Attack-as-domains perspective
  2.5 Statistical Foundations
  2.6 Chapter Summary

Chapter 3: Related Work
  3.1 Multi-Attack Adversarial Training
  3.2 Group DRO Applied to Robustness
  3.3 Domain Generalization Meets Adversarial Robustness
  3.4 Cluster Discovery in Robust Training Pipelines
  3.5 The Remaining Gap and Motivation for This Work

Chapter 4: Proposed Methodology
  4.1 Methodology Overview
  4.2 Multi-Attack Training as a Domain Problem
    4.2.1 Setup and Notation
    4.2.2 Multi-Attack Risk and Its Limitations
  4.3 Uniform Multi-Attack ERM
  4.4 AttackDRO: Group DRO Over Attack Identities
  4.5 AttackDRO++: Group DRO Over Discovered Clusters
  4.6 Augmented Clustering with Gradient Fingerprints
  4.7 Uniform-Anchored Training Objective
  4.8 Complete Training Framework
    4.8.1 Progression from Diagnostic Motivation to the Final Method
    4.8.2 Implementation and Computational Considerations
  4.9 Chapter Summary

Chapter 5: Experimental Setup
  5.1 Dataset and Preprocessing
  5.2 Model Architecture
  5.3 Attack Suite and Configuration
    5.3.1 Training attacks
    5.3.2 Evaluation Attacks
  5.4 Training Configuration
  5.5 Hyperparameter Choices and Ablation Factors
  5.6 Statistical Significance Protocol
  5.7 Evaluation Metrics and Robustness Definitions
  5.8 Graybox Transfer Protocol

Chapter 6: Results and Analysis
  6.1 Whitebox Robustness Under Direct Attacks
    6.1.1 Aggregate Robustness
    6.1.2 Per-Attack Robustness Breakdown
    6.1.3 Worst-Case Behavior: Worst(8) and AutoAttack
    6.1.4 Variance Reduction and Training Stability
  6.2 Class-wise Whitebox Robustness Across Attacks
    6.2.1 Per-Class Whitebox Robustness Pattern
    6.2.2 Attack-Family Interpretation
    6.2.3 Bottom-\(K\) Whitebox Tail Robustness
  6.3 Graybox Robustness Across Surrogate Models
    6.3.1 Seed Selection and Whitebox Sanity Check
    6.3.2 Cross-Method Transfer Matrix
    6.3.3 AttackDRO++ vs. Multi-AT
    6.3.4 Per-Attack Analysis
    6.3.5 Whitebox--Graybox Gap and Specialist Inflation
    6.3.6 Per-(Class-Attack) Analysis
    6.3.7 Method Contribution Decomposition
  6.4 Sensitivity to Key Hyperparameters
    6.4.1 Anchor Strength
    6.4.2 Number of Clusters
    6.4.3 Cluster-Refresh Schedule

Chapter 7: Conclusion and Future Work
  Empty shell only.

Appendices
  Appendix A: Illustrative Pseudo-code and Flowcharts
  Appendix B: Experimental Logs and Configurations
  Appendix C: Additional Tables and Visualizations
  Appendix D: Compute Resources and Environment Notes
```

Notes:
- No active `\subsubsection{...}` headings were found.
- `report/chapters/chapter6/2_graybox_results.tex` still contains a `Section Summary` block, but it is wrapped in `\iffalse...\fi` and is not active.
- `report/chapters/chapter6/3_ablation.tex` still contains source headings for `q-Frozen Ablation`, `Cluster Feature Mode`, and `Sample-Level Regularizer`, but those headings are wrapped in `\iffalse...\fi` and are not active.
- `report/chapters/chapter6/5_diagnostics.tex` still contains diagnostics headings, but the file is not input from the main Chapter 6 flow.

## Comparison with docs/01_outline.md

Already aligned or improved:
- Main report now follows the seven-chapter outline.
- Chapter 1 simple title renames are applied.
- Chapter 3 simple title renames are applied.
- Chapter 4 section titles are mostly aligned with the outline, and the single-child subsection issue under `Complete Training Framework` is structurally fixed with a placeholder subsection.
- Chapter 5 title renames are applied through `5.8`.
- Chapter 6 top-level section titles are aligned with the requested outline names.
- Old Chapter 7 `Analysis and Discussion` is archived and no longer in the active flow.
- Chapter 8 conclusion shell is now the active Chapter 7 shell.
- Diagnostics are removed from the main Chapter 6 flow.
- Extra ablation headings are disabled from the main flow without deleting source text.

Still not aligned:
- Chapter 2 still needs a larger outline rewrite. It does not yet have the planned standalone `Adversarial Attack Algorithms` section.
- Chapter 5 still lacks `5.9 Tools, Platforms, and Experiment Tracking`.
- Chapter 5 still lacks the special setup recap summary table `tab:ch5_setup_summary`.
- Chapter 6 graybox content is still more granular than the outline and likely needs prose-level consolidation.
- Chapter 6 still has no closing synthesis because `report/chapters/chapter6/6_summary.tex` is empty.
- Chapter 7 is still empty and needs the planned conclusion sections.
- Appendix D remains present even though the outline only calls out A-C.

## Style-rule issues found

- Chapter 1 has no summary, which follows `docs/06_style_rules.md`.
- Active section-level summaries were removed from the main flow. The old Chapter 6 graybox section summary remains only inside `\iffalse`.
- Numbered Chapter Summary sections remain in:
  - `report/chapters/chapter2/6-summary.tex`
  - `report/chapters/chapter4/summary.tex`
- to-do comments were added beside those Chapter Summary sections:
  - `% to-do: Convert numbered Chapter Summary into closing prose according to docs/06_style_rules.md.`
- Chapter 5 special summary style is still missing.
- Formal table/caption/row-label method names were partially normalized to `Multi-AT`, `AttackDRO++`, `PGD-AT`, and `DDN-AT`.
- Long explanatory prose still contains older terms such as `PGD-AT`, `DDN-AT`, `Multi-ATtack`, and `AttackDRO++ Anchor35 GradFP`. This was left intentionally because this patch was structural/path-only and should not rewrite technical paragraphs.

## Rename/move candidates

- Chapter 2 should be reorganized against `docs/01_outline.md`, especially the attack-algorithm material.
- Chapter 2 and Chapter 4 numbered `Chapter Summary` sections should be converted into unnumbered closing prose.
- Chapter 5 should add `Tools, Platforms, and Experiment Tracking` and the setup recap summary table.
- Chapter 6 graybox subsections should be consolidated to match the outline:
  - `Cross-Method Transfer Structure`
  - `Paired Graybox Comparisons`
  - `Class-Level Transfer Patterns`
- Chapter 6 diagnostics can be moved to Appendix C later if the user wants them preserved in the PDF.
- Extra ablation source blocks can be moved to appendix or deleted later after an explicit content decision.
- Chapter 7 needs prose and the planned conclusion sections.
- The Chapter 6 heading `Bottom-\(K\) Whitebox Tail Robustness` triggers a hyperref PDF-string warning; a later polish patch can rename it to avoid math in the bookmark.

## Label/reference issues noticed

Known handoff issues fixed:
- `sec:gradfp`: added to `report/chapters/chapter4/5-clustering_feature.tex`.
- `tab:worst8`: references now point to existing table labels.
- `tab:autoattack`: no exact active `\ref{tab:autoattack}` remains; existing labels are `tab:autoattack_config` and `tab:ch6_autoattack_fulltest`.
- `fig:graybox_delta_heatmaps`: replaced with the actual graybox delta figure refs.
- `tab:ablation_anchor_strength`: replaced with `fig:ablation_dashboard` where that target was the obvious intended object.
- Duplicate `eq:floor`: less central label in `report/chapters/chapter4/3-attackDRO.tex` renamed to `eq:attackdro_floor`; `eq:floor` remains on the uniform-anchor objective.
- `subsubsec:ablation_cluster_refresh`: renamed to `subsec:ablation_cluster_refresh`.

Final compile log check:
- No remaining undefined-reference warnings.
- No remaining multiply-defined-label warnings.
- Stale physical file `report/chapters/chapter8.aux` still exists from older compiles, but final `main.aux` no longer includes `chapters/chapter8.aux`.

## Suggested next patch

Recommended next patch should be prose/content oriented, not another path patch:

1. Fill Chapter 7 with the planned conclusion sections.
2. Add Chapter 5.9 and the Chapter 5 setup recap table.
3. Convert Chapter 2 and Chapter 4 numbered summaries into closing prose.
4. Write a short Chapter 6 closing synthesis in `report/chapters/chapter6/6_summary.tex`.
5. Consolidate Chapter 6 graybox subsections to the outline shape.
6. Decide whether diagnostics and extra ablations should move to Appendix C or stay archived in source only.
7. Do a controlled prose pass for method-name normalization in remaining paragraphs.
8. Optionally rename the `Bottom-\(K\)` heading to avoid the hyperref bookmark warning.

## Questions for ChatGPT/user

- Should Chapter 7 be drafted from the current research questions only, or should it cite exact numeric results from Chapter 6?
- Should Chapter 5.9 be brief environment prose, or include a table of hardware/software/config tracking?
- Should diagnostics be moved into Appendix C in the PDF, or remain unused source only?
- Should extra ablations be moved into Appendix C, or remain unused until results are complete?
- Should remaining prose use only `AttackDRO++`, or keep `AttackDRO++` in running text after first definition?
- Should `Uniform Multi-Attack ERM` in Chapter 4 remain as a method-construction name while formal result tables use `Multi-AT`?

## Codex applied changes

Files changed:
- `docs/00_llm_handoff.md`
- `docs/01_outline.md`
- `report/main.tex`
- `report/outsider/cover-page.tex`
- `report/outsider/frontmatter.tex`
- `report/chapters/chapter1.tex`
- `report/chapters/chapter3/2_group_dro.tex`
- `report/chapters/chapter3/4_cluster.tex`
- `report/chapters/chapter3/5_gap.tex`
- `report/chapters/chapter4.tex`
- `report/chapters/chapter4/1-problem_formulation.tex`
- `report/chapters/chapter4/3-attackDRO.tex`
- `report/chapters/chapter4/4-attackDRO++.tex`
- `report/chapters/chapter4/5-clustering_feature.tex`
- `report/chapters/chapter4/6-anchor_objective.tex`
- `report/chapters/chapter4/7-complete_pipeline.tex`
- `report/chapters/chapter4/summary.tex`
- `report/chapters/chapter5/2-architectures.tex`
- `report/chapters/chapter5/3-attack_suite.tex`
- `report/chapters/chapter5/4-configuration.tex`
- `report/chapters/chapter5/5-choices.tex`
- `report/chapters/chapter5/7-eval_metrics.tex`
- `report/chapters/chapter5/8-graybox_transfer.tex`
- `report/chapters/chapter6.tex`
- `report/chapters/chapter6/1_main_results.tex`
- `report/chapters/chapter6/2_graybox_results.tex`
- `report/chapters/chapter6/3_ablation.tex`
- `report/chapters/chapter6/4_whitebox.tex`
- `report/chapters/chapter7.tex`
- `report/chapters/chapter7_old_analysis_discussion.tex`

Structural changes:
- Renamed `report/chapters/chapter7.tex` to `report/chapters/chapter7_old_analysis_discussion.tex`.
- Renamed old `report/chapters/chapter8.tex` to `report/chapters/chapter7.tex`.
- Removed `\include{chapters/chapter8}` from `report/main.tex`.
- Commented out the Chapter 6 diagnostics input.
- Disabled extra ablation headings and the graybox section summary with `\iffalse`.
- Added to-do markers beside Chapter 2 and Chapter 4 numbered summaries.

Path changes:
- Renamed `report/images` to `report/figures`.
- Updated LaTeX image paths to `figures/...`.
- Updated docs Markdown preview paths to `../report/figures/...`.
- Confirmed no stale `images/`, `report/images/`, `../images/`, or `\graphicspath` matches remain in `.tex`, `.sty`, `.cls`, `.bib`, or `.md` files.

Naming changes:
- Applied requested heading renames in Chapters 1, 3, 4, 5, and 6.
- Normalized selected formal table/caption/row labels to `Multi-AT`, `AttackDRO++`, `PGD-AT`, and `DDN-AT`.

Label/reference fixes:
- Added `sec:gradfp`.
- Repointed or removed broken refs for `tab:worst8`, `tab:autoattack`, `fig:graybox_delta_heatmaps`, and `tab:ablation_anchor_strength`.
- Renamed duplicate `eq:floor` in AttackDRO to `eq:attackdro_floor`.
- Renamed `subsubsec:ablation_cluster_refresh` to `subsec:ablation_cluster_refresh`.

## Compile result

- Command used:
  ```powershell
  cd C:\Users\ADMIN\Documents\GitHub\ARDG\report
  powershell -ExecutionPolicy Bypass -File .\build.ps1
  ```
- First sandboxed compile failed because MiKTeX needed to write setup/cache files under `C:\Users\ADMIN\AppData\Roaming\MiKTeX\2.9`.
- Re-ran the same command with approval outside the sandbox.
- Result: success.
- PDF path: `C:\Users\ADMIN\Documents\GitHub\ARDG\report\main.pdf`.
- PDF output: 90 pages.
- Warnings that still matter:
  - Overfull/underfull boxes remain in several tables/paragraphs.
  - Hyperref warning remains for math in a PDF bookmark near `report/chapters/chapter6/4_whitebox.tex`.
  - MiKTeX still reports: `So far, you have not checked for MiKTeX updates.`
- Warnings resolved:
  - No final undefined-reference warnings.
  - No final multiply-defined-label warnings.

## Remaining issues

- No unresolved labels were found in the final log.
- Chapter 2 still needs structural/prose alignment to the outline.
- Chapter 5.9 is still missing.
- Chapter 5 setup recap table is still missing.
- Chapter 6 graybox section is still too granular relative to the outline.
- Chapter 6 closing synthesis is still missing because `6_summary.tex` is empty.
- Chapter 7 is still empty.
- Prose-level method naming remains inconsistent in older paragraphs by design.
- `report/chapters/chapter8.aux` remains as a stale compile artifact, but it is not active in the final `main.aux`.

## Next message to ChatGPT

Paste this:

```text
Codex applied the safe structural/path patch. The report now compiles as 7 active chapters. Old Chapter 7 `Analysis and Discussion` was archived as `report/chapters/chapter7_old_analysis_discussion.tex`; old Chapter 8 was renamed to active `report/chapters/chapter7.tex`. `report/images` was renamed to `report/figures`, LaTeX paths now use `figures/...`, and docs preview paths now use `../report/figures/...`. Chapter 6 diagnostics and extra ablation headings were removed from the main flow without deleting source text. Known broken labels/references were fixed, including `sec:gradfp`, `tab:worst8`, `tab:autoattack`, `fig:graybox_delta_heatmaps`, `tab:ablation_anchor_strength`, duplicate `eq:floor`, and `subsubsec:ablation_cluster_refresh`.

Compile result: success using `cd C:\Users\ADMIN\Documents\GitHub\ARDG\report; powershell -ExecutionPolicy Bypass -File .\build.ps1`. Output PDF is `report/main.pdf`, 90 pages. Final log has no unresolved-reference or multiply-defined-label warnings. Remaining warnings are overfull/underfull boxes, a hyperref bookmark warning from math in a heading, and the MiKTeX update notice.

Remaining issues: Chapter 5.9 is still missing; Chapter 5 special recap table is missing; Chapter 6 closing synthesis is empty; Chapter 6 graybox section is still too granular; Chapter 7 is empty; Chapter 2 still needs outline-level prose restructuring; old method names still appear in long prose because Codex only normalized formal labels/captions/tables in this patch.

Recommended next agent: ChatGPT/user for prose decisions and drafting, then Codex to apply and compile. Next proposed patch: fill Chapter 7, add Chapter 5.9 and the Chapter 5 recap table, convert Chapter 2/4 numbered summaries to closing prose, write the Chapter 6 closing synthesis, and consolidate Chapter 6 graybox subsections to the outline shape.
```

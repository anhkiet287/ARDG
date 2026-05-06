# 07_task_assignment.md

Purpose:
Task board for writing and polishing the DATN report. This file tells each member what to write, which files to edit, what to check, and what output is expected.

## 1. Current report status

- The report compiles as 7 active chapters from `report/main.tex`.
- Chapter 7 is still empty except for `\chapter{Conclusion and Future Work}`, its label, and local to-do comments.
- Chapter 5.9, `Tools, Platforms, and Experiment Tracking`, is still missing.
- The Chapter 5 setup recap table `tab:ch5_setup_summary` is still missing.
- Chapter 6 closing synthesis in `report/chapters/chapter6/6_summary.tex` is empty except for to-do guidance.
- Chapter 2 still needs outline-level restructuring: the active files use older section names, while `docs/01_outline.md` expects a clearer 2.1-2.7 background flow.
- Chapter 6 graybox section is still too granular and should later be consolidated around the main transfer story.
- Local to-do comments now exist in the active LaTeX source files for Chapters 1-7 and are the main source for writing tasks.

## 2. Global rules for all members

- Read `docs/06_style_rules.md` before writing.
- Follow `docs/01_outline.md` for each section's purpose and target flow.
- Use method, attack, metric, dataset, model, acronym, and tool names from `docs/05_notation_registry.md`.
- Do not invent labels. Check `docs/03_label_registry.md` before adding, removing, or renaming labels.
- Do not add figures or tables without updating `docs/04_figure_table_registry.md` later in the same writing session.
- Do not change numerical results unless Kiệt confirms.
- Write directly in LaTeX source files.
- Keep summaries only at chapter level. Chapter 5 is the only chapter allowed to use `\paragraph{Summary.}` for the setup recap table.
- Avoid metric/internal notation in headings, including `Mean(8)`, `Worst(8)`, `Bottom-K`, `PGD20-CE`, and code-style names.
- Preserve existing labels unless a coordinated label-cleanup patch is planned.
- After major edits, compile from `report/` with `powershell -ExecutionPolicy Bypass -File .\build.ps1`.

## 3. Task overview table

| Owner | Chapter/Area | Main files | Priority | Status | Expected output |
|---|---|---|---|---|---|
| ĐA | Chapter 2 Background | `report/chapters/chapter2.tex`, `report/chapters/chapter2/*.tex` | High | todo | Restructured background, compact attack/DRO/statistics explanations, useful tables/optional concept figure plan. |
| Thành | Chapter 3 Related Work | `report/chapters/chapter3.tex`, `report/chapters/chapter3/*.tex` | High | todo | Related-work narrative that compares prior work and ends with a clear gap. |
| Kiệt | Chapter 1 Introduction | `report/chapters/chapter1.tex` | High | todo | Compact motivation, diagnostic bridge, RQs, contributions, scope, and report organization. |
| Kiệt | Chapter 4 Proposed Methodology | `report/chapters/chapter4.tex`, `report/chapters/chapter4/*.tex` | Medium | todo | Clear method explanation with no result claims; checked equations, algorithm, and hyperparameter table. |
| Kiệt | Chapter 5 Experimental Setup | `report/chapters/chapter5.tex`, `report/chapters/chapter5/*.tex` | High | todo | Reproducible setup chapter with missing 5.9 and setup recap table added. |
| Kiệt | Chapter 6 Results and Analysis | `report/chapters/chapter6.tex`, `report/chapters/chapter6/*.tex` | High | todo | Result interpretation, figure/table references, graybox consolidation, and closing synthesis. |
| Kiệt | Chapter 7 Conclusion and Future Work | `report/chapters/chapter7.tex` | High | todo | Complete conclusion, RQ answers, limitations, future work, optional RQ answer table. |
| Team | Cross-file consistency | `docs/*.md`, active LaTeX files, front matter if needed | High | in progress | Label, notation, figure/table, acronym, caption, and compile-warning checks. |

## 4. ĐA tasks - Chapter 2 Background

Files to edit:
- `report/chapters/chapter2.tex`
- `report/chapters/chapter2/1-preliminaries.tex`
- `report/chapters/chapter2/2-at-deep-dive.tex`
- `report/chapters/chapter2/3-dro.tex`
- `report/chapters/chapter2/4-dg-via-clustering.tex`
- `report/chapters/chapter2/5-foundations.tex`
- `report/chapters/chapter2/6-summary.tex`

Target structure from `docs/01_outline.md`:
- 2.1 Notation and Learning Setting
- 2.2 Adversarial Examples and Threat Models
- 2.3 Adversarial Attack Algorithms
- 2.4 Adversarial Training as Min-Max Optimization
- 2.5 Distributionally Robust Optimization
- 2.6 Domain Generalization and Clustering
- 2.7 Statistical Tools for Multi-Seed Evaluation

Main writing goals:
- Restructure the existing Chapter 2 files toward the target 2.1-2.7 flow.
- Explain only the theory and tools needed for Chapters 4-6.
- Keep notation consistent with `docs/05_notation_registry.md`.
- Make the attack background practical: intuition, threat model/norm, objective/update only if needed, and role in this report.
- Keep Chapter 2 readable for a DATN examiner, not a textbook chapter.

Required tables/figures to consider:
- Threat model comparison table: whitebox, graybox, blackbox; access to parameters, gradients, logits/scores, labels; role in this report.
- Attack algorithm summary table: Attack, Norm, Iterative?, Targeted?, Used for training?, Used for evaluation?, Role.
- ERM/AT/DRO/Group DRO comparison table: objective idea, group assumption, role in this report.
- Optional adversarial-example concept figure: clean image -> perturbation -> adversarial image -> changed prediction.

Important naming rules:
- `PGD-$\ell_\infty$` is an attack.
- `PGD-AT` is a training method.
- `DDN-$\ell_2$` is an attack.
- `DDN-AT` is a training method.
- Use `Multi-AT` for the uniform multi-attack training baseline.
- Do not use `PGD20-CE` repeatedly in prose; map it once to PGD-$\ell_\infty$ with 20 steps and cross-entropy where needed.

Expected output:
- Revised Chapter 2 prose aligned with the target structure.
- Compact attack descriptions for FGSM-RS, PGD-$\ell_\infty$, CW-$\ell_2$, DeepFool-$\ell_2$, DDN-$\ell_2$, MI-FGSM, TPGD, and AutoAttack-$\ell_\infty$.
- No long textbook-style derivations.
- No Chapter 6 result claims.
- Chapter-level closing prose only; avoid adding new section-level summaries.

## 5. Thành tasks - Chapter 3 Related Work

Files to edit:
- `report/chapters/chapter3.tex`
- `report/chapters/chapter3/1_multi_at.tex`
- `report/chapters/chapter3/2_group_dro.tex`
- `report/chapters/chapter3/3_dg_ar.tex`
- `report/chapters/chapter3/4_cluster.tex`
- `report/chapters/chapter3/5_gap.tex`

Writing goals:
- Make Chapter 3 compare and position prior work instead of listing papers.
- Each section should end with a limitation or gap that motivates the next section.
- The chapter should make Chapter 4 feel necessary.
- Keep method and attack names consistent with `docs/05_notation_registry.md`.
- Keep experiment/result claims out of Chapter 3 unless they are claims made by cited prior work.

Optional related-work comparison table:

| Work | Setting | Grouping assumption | Attack coverage | Limitation | Relation to this report |
|---|---|---|---|---|---|

Expected output:
- Improved related-work flow across multi-attack AT, Group DRO, domain generalization, and cluster discovery.
- Clear gap statement in Section 3.5.
- No paper-by-paper dump.
- A transition into Chapter 4 that explains why AttackDRO++ is a reasonable next step.

## 6. Kiệt tasks - Chapter 1

File to edit:
- `report/chapters/chapter1.tex`

Tasks:
- Keep the chapter compact, with a 6-8 page total target.
- Do not add a Chapter 1 summary.
- Strengthen the diagnostic-to-method bridge.
- Make research questions answerable by current Chapter 6 evidence.
- Keep contributions tied to implemented method/evaluation pieces.
- Keep scope conservative: CIFAR-10, ResNet-18 main setting, defined attack suite, repeated-seed protocol.
- Mention AutoAttack status correctly: it is separate from Mean(8) and should not be described as part of the 20-seed paired aggregate panel; use the current Chapter 5/6 evidence when stating whether it is a 512-sample sanity check, fixed random-seed full-test check, or five-seed result.
- Mention WRN-28-10 only as supplementary evidence if it is actually used and supported in the report.

Expected output:
- Compact motivation.
- Clear diagnostic bridge.
- Research questions and hypotheses that match the active evaluation.
- Conservative contributions and scope.
- Report organization that previews Chapters 2-7.

## 7. Kiệt tasks - Chapter 4

Files to edit:
- `report/chapters/chapter4.tex`
- `report/chapters/chapter4/1-problem_formulation.tex`
- `report/chapters/chapter4/2-multi_attack.tex`
- `report/chapters/chapter4/3-attackDRO.tex`
- `report/chapters/chapter4/4-attackDRO++.tex`
- `report/chapters/chapter4/5-clustering_feature.tex`
- `report/chapters/chapter4/6-anchor_objective.tex`
- `report/chapters/chapter4/7-complete_pipeline.tex`
- `report/chapters/chapter4/summary.tex`

Tasks:
- Improve methodology clarity: attacks-as-domains, Multi-AT, AttackDRO, AttackDRO++, gradient fingerprints, uniform anchor, and full pipeline.
- Do not include Chapter 6 result claims.
- Keep equations only if referenced later or essential to define the method.
- Use notation from `docs/05_notation_registry.md`; avoid ambiguity between class count and cluster count.
- Check Algorithm 1 for consistency with the surrounding method description.
- Check default hyperparameter table `tab:hparams` against Chapter 5 setup tables.
- Consider a method pipeline figure if a suitable asset is available or generated later.
- Convert numbered Chapter Summary into closing prose in a later style cleanup.

Expected output:
- Method chapter that can be understood before seeing experiments.
- Algorithm and hyperparameter table aligned with Chapter 5.
- No invented theory or guarantees.

## 8. Kiệt tasks - Chapter 5

Files to edit:
- `report/chapters/chapter5.tex`
- `report/chapters/chapter5/1-dataset_preprocessing.tex`
- `report/chapters/chapter5/2-architectures.tex`
- `report/chapters/chapter5/3-attack_suite.tex`
- `report/chapters/chapter5/4-configuration.tex`
- `report/chapters/chapter5/5-choices.tex`
- `report/chapters/chapter5/6-protocol.tex`
- `report/chapters/chapter5/7-eval_metrics.tex`
- `report/chapters/chapter5/8-graybox_transfer.tex`

Tasks:
- Add missing 5.9 Tools, Platforms, and Experiment Tracking.
- Add a tools/platforms table if useful. Candidate entries: Colab, Drive, W&B, PyTorch, torchvision, TorchAttacks, AutoAttack package, adv-lib if confirmed, scikit-learn, pandas, NumPy, matplotlib.
- Add setup recap table `tab:ch5_setup_summary` using the Chapter 5 summary style in `docs/06_style_rules.md`.
- Ensure the attack configuration table is the source of truth for attack names, norms, budgets, steps, loss/objective, role, and training/evaluation usage.
- Confirm actual tools/packages before writing them into report prose.
- Keep Chapter 5 practical and reproducible, not a software manual.
- Do not interpret results in this chapter.

Expected output:
- Reproducible setup chapter.
- Full attack/source/evaluation configuration.
- Tools/platforms section with only confirmed tools.
- Chapter 5 recap table and transition to Chapter 6.

## 9. Kiệt tasks - Chapter 6

Files to edit:
- `report/chapters/chapter6.tex`
- `report/chapters/chapter6/1_main_results.tex`
- `report/chapters/chapter6/4_whitebox.tex`
- `report/chapters/chapter6/2_graybox_results.tex`
- `report/chapters/chapter6/3_ablation.tex`
- `report/chapters/chapter6/6_summary.tex`

Tasks:
- Write Chapter 6 closing synthesis in `report/chapters/chapter6/6_summary.tex`.
- Consolidate graybox section later so the main transfer story is clear.
- Reference active figures and tables where useful, especially active but currently unreferenced assets recorded in `docs/04_figure_table_registry.md`.
- Fix heading issues with math/internal notation in a later cleanup:
  - `Worst(8)` should not appear in a heading.
  - `Bottom-\(K\)` should not appear in a heading.
- Avoid overclaiming. Tie every claim to the table/figure and seed protocol that supports it.
- Follow result -> interpretation -> limitation -> next section.
- Decide which dense/secondary graybox tables and heatmaps should remain in the main flow versus appendix.

Expected output:
- Clear whitebox aggregate, class-wise, graybox, and ablation story.
- Main figures/tables cited in nearby prose.
- Conservative interpretation of statistical support.
- Chapter 6 synthesis that prepares Chapter 7.

## 10. Kiệt tasks - Chapter 7

File to edit:
- `report/chapters/chapter7.tex`

Planned structure:
- 7.1 Summary of Contributions
- 7.2 Answers to Research Questions
- 7.3 Limitations of the Current Study
- 7.4 Directions for Future Work
- 7.5 Closing Remarks

Tasks:
- Fill the empty conclusion shell.
- Answer the research questions using Chapter 6 evidence.
- Mention limitations: dataset/model scope, attack suite, compute budget, repeated-seed limits, and graybox protocol scope.
- Add a compact RQ answer table if useful.
- Do not introduce new results.
- Tie conclusions directly to Chapter 6 evidence.
- Do not add a separate chapter summary section.

Expected output:
- Complete conclusion chapter.
- RQ answers that are specific and evidence-bounded.
- Practical future work, not speculative claims.

## 11. Team consistency tasks

- Label updates: use `docs/03_label_registry.md`; update it whenever labels are added, removed, or renamed.
- Notation consistency: use `docs/05_notation_registry.md`; update it whenever method, attack, metric, acronym, notation, dataset, model, or tool names change.
- Figure/table registry updates: use `docs/04_figure_table_registry.md`; update it whenever figures/tables are added, removed, moved, relabeled, or recaptioned.
- Acronym list cleanup: front matter should define recurring acronyms such as DRO, ERM, DDN, MI-FGSM, TPGD, SGD, CI, Std, and pp if used.
- Caption polish: make captions self-contained, avoid "The figure shows..." and "This table presents...", and define units/averaging conditions.
- Overfull/underfull table review: check dense tables and any `resizebox` tables after compilation.
- Compile after major edits and record meaningful warnings.
- Keep `docs/00_llm_handoff.md` updated after substantial changes.

## 12. Suggested work order

1. ĐA updates Chapter 2 structure and attack background.
2. Thành updates Chapter 3 gap narrative.
3. Kiệt adds Chapter 5.9 and setup recap table.
4. Kiệt writes Chapter 6 closing synthesis.
5. Kiệt drafts Chapter 7.
6. Team updates registries if labels, figures, tables, or notation changed.
7. Codex compiles and audits warnings.
8. ChatGPT/user reviews story, claims, and transitions.

## 13. Review checklist before submitting a section

- Does this section match `docs/01_outline.md`?
- Does it follow `docs/06_style_rules.md`?
- Are method, attack, metric, acronym, and tool names consistent with `docs/05_notation_registry.md`?
- Are labels registered in `docs/03_label_registry.md`?
- Are figures/tables referenced and useful?
- If a figure/table changed, was `docs/04_figure_table_registry.md` updated?
- Are claims supported by the report's evidence?
- Is there a practical transition to the next section?
- Does it avoid unnecessary section-level summaries?
- Did the report compile after major edits?

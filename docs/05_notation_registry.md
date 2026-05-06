# 05_notation_registry.md

Purpose:
A single source of truth for notation, acronyms, method names, attack names, metrics, datasets, models, hyperparameters, and tools used in the report.

Scope: built from the current 7-chapter flow in `report/main.tex`, the included chapter subfiles, `report/appendices.tex`, and the planning files `docs/01_outline.md`, `docs/03_label_registry.md`, and `docs/06_style_rules.md`. No LaTeX source files were edited while creating this registry.

## 1. Naming principles

- Use readable report-facing names in prose, titles, formal tables, and captions.
- Keep code/internal names only in configuration tables, implementation notes, file names, or reproducibility details.
- Distinguish attack names from training-method names. For example, `PGD-$\ell_\infty$` is an attack, while `PGD-AT` is a training method that uses that attack.
- Define acronyms at first use in the main text. The front-matter abbreviation list should include all recurring acronyms.
- Do not use internal metric shorthand in section or subsection titles.
- Metric shorthand such as `Mean(8)`, `Worst(8)`, and `AutoAttack-512` may be used in body text, tables, captions, or metric-definition paragraphs after proper definition.
- `Mean(8)`, `Worst(8)`, `Bottom-K`, `PGD20-CE`, and code-style names should not appear in section/subsection titles.

## 2. Method name registry

| Report name | Internal/code name | Meaning | First definition location | Use in tables/captions | Notes |
|---|---|---|---|---|---|
| `PGD-AT` | `PGD-AT`; figure filenames sometimes imply `singlePGD` | Single-attack adversarial training using PGD-$\ell_\infty$. | `report/chapters/chapter5/4-configuration.tex`, `tab:ch5_method_training_summary`; background title in `report/chapters/chapter2/2-at-deep-dive.tex`. | Use `PGD-AT`. | User explicitly requested this name instead of `Single-AT PGD-$\ell_\infty$`. |
| `DDN-AT` | `DDN-AT`; figure filenames sometimes imply `singleDDN` | Single-attack adversarial training using DDN-$\ell_2$. | `report/chapters/chapter5/4-configuration.tex`, `tab:ch5_method_training_summary`. | Use `DDN-AT`. | User explicitly requested this name instead of `Single-AT DDN-$\ell_2$`. |
| `Multi-AT` | `Multi-AT`; old prose `Multi-ATtack`; sometimes `Uniform Multi-AT`; methodology name `Uniform Multi-Attack ERM`. | Uniform multi-attack adversarial training baseline over PGD-$\ell_\infty$ and DDN-$\ell_2$ source attacks. | `report/chapters/chapter4/2-multi_attack.tex`; `report/chapters/chapter5/4-configuration.tex`, `tab:ch5_method_training_summary`. | Use `Multi-AT`. | `Uniform Multi-Attack ERM` is useful in Chapter 4 when defining the objective; formal results should use `Multi-AT`. |
| `AttackDRO` | `AttackDRO`; `Group DRO over attack identity`. | Intermediate design step using Group DRO over source attack identities. | `report/chapters/chapter4/3-attackDRO.tex`; `report/chapters/chapter5/4-configuration.tex`. | Use `AttackDRO`. | Use `Group DRO` with a space in prose; do not imply it is part of the main Chapter 6 result table unless results are present. |
| `Cluster-DRO` | `Cluster-DRO`; `cluster-level DRO`. | Intermediate cluster-level design step; Group DRO over discovered latent clusters. | `report/chapters/chapter4/4-attackDRO++.tex`; `report/chapters/chapter5/4-configuration.tex`. | Use `Cluster-DRO` or `cluster-level DRO` for the intermediate design step. | Do not use AttackDRO++ to refer to the cluster-only component; do not imply full Chapter 6 evaluation unless results are present. |
| `AttackDRO++` | `attackdro_pp_anchor035_gradfp_online_k4`; `anchor035`; `Anchor35 GradFP`. | final proposed method; uniform-anchored Cluster-DRO with gradient fingerprints. | `report/chapters/chapter4/7-complete_pipeline.tex`; `report/chapters/chapter5/4-configuration.tex`. | Use `AttackDRO++`. | `(Ours)` is optional only in crowded Chapter 6 result tables if needed, not the preferred Chapter 5 method name. |
| `q`-frozen variant | `q-Frozen`, `Q-frozen`, `uniform q`, `update q vs. uniform q`. | Ablation where adaptive `q` reweighting is disabled or kept uniform. | `report/chapters/chapter5/5-choices.tex`, `tab:ch5_ablation_hyperparams`; inactive source heading in `report/chapters/chapter6/3_ablation.tex`. | Do not use in active main-flow tables unless the ablation is restored. | Current Chapter 6 `q-Frozen Ablation` heading is inside `\iffalse`; treat as inactive source. |
| `Anchor35` / anchor variants | `Anchor35`; `anchor035`; `\lambda_{\mathrm{DRO}}=0.35`; anchor strengths `{0.20, 0.35, 0.50}`. | Uniform-anchor setting controlling the strength of the Cluster-DRO correction. | `report/chapters/chapter4/6-anchor_objective.tex`; `report/chapters/chapter5/5-choices.tex`. | In formal results use `AttackDRO++`; in ablation tables use `\lambda_{\mathrm{DRO}}`. | `Anchor35` is acceptable as a config shorthand only after it is mapped to `\lambda_{\mathrm{DRO}}=0.35`. |

Important method naming rules:

- `PGD-AT` = single-attack adversarial training using PGD-$\ell_\infty$.
- `DDN-AT` = single-attack adversarial training using DDN-$\ell_2$.
- `Multi-AT` = uniform multi-attack adversarial training baseline.
- `AttackDRO` = intermediate design step using Group DRO over fixed source attack identities.
- `Cluster-DRO` = intermediate cluster-level design step; Group DRO over discovered latent clusters.
- `AttackDRO++` = final proposed method; uniform-anchored Cluster-DRO with gradient fingerprints.
- Do not use `AttackDRO++` to refer to the cluster-only component.
- Do not make the `(Ours)` suffix part of the preferred formal method name. The suffix may be used only if a crowded result table requires disambiguation; Chapter 3 and Chapter 5 should prefer `AttackDRO++`.

## 3. Attack name registry

| Report attack name | Internal/code name | Norm | Used for training? | Used for evaluation? | Configuration source | Notes |
|---|---|---|---|---|---|---|
| `FGSM-RS` | `fgsm_rs` | $\ell_\infty$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_evaluation_attacks`; style map in `docs/06_style_rules.md`. | Held-out $\ell_\infty$ attack. |
| `PGD-$\ell_\infty$` | `pgd20_ce` | $\ell_\infty$ | Yes | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_training_attacks` and `tab:ch5_evaluation_attacks`. | `pgd20_ce` maps to PGD-$\ell_\infty$; define once that it uses 20 steps and cross-entropy loss. Do not repeatedly use `PGD20-CE` in prose. |
| `TPGD` | `tpgd` | $\ell_\infty$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_evaluation_attacks`; style map in `docs/06_style_rules.md`. | Held-out $\ell_\infty$ TRADES-style Projected Gradient Descent attack. Define acronym/form in Chapter 2 or Chapter 5 if used heavily. |
| `MI-FGSM` | `mifgsm` | $\ell_\infty$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_evaluation_attacks`; style map in `docs/06_style_rules.md`. | Use hyphenated `MI-FGSM` in report text. |
| `PGD-$\ell_2$` | `pgd_l2` | $\ell_2$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_evaluation_attacks`; style map in `docs/06_style_rules.md`. | Held-out $\ell_2$ attack. |
| `DDN-$\ell_2$` | `ddn_l2` | $\ell_2$ | Yes | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_training_attacks` and `tab:ch5_evaluation_attacks`. | Source attack for `DDN-AT`; also part of Mean(8). |
| `DeepFool-$\ell_2$` | `deepfool_l2` | $\ell_2$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_evaluation_attacks`; style map in `docs/06_style_rules.md`. | Held-out $\ell_2$ attack. |
| `CW-$\ell_2$` | `cw_l2` | $\ell_2$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_evaluation_attacks`; style map in `docs/06_style_rules.md`. | Carlini-Wagner $\ell_2$ attack. |
| `AutoAttack-$\ell_\infty$` | `autoattack_linf` | $\ell_\infty$ | No | Yes | `report/chapters/chapter5/3-attack_suite.tex`, `tab:ch5_autoattack_config`; results in `tab:ch6_worst_autoattack_sanity` and `tab:ch6_autoattack_fulltest`. | Evaluated separately from the 20-seed paired aggregate panel. It appears as a 512-sample sanity check and as a full-test random-seed panel stress test; it is not part of Mean(8). |

## 4. Metric registry

| Metric name | Symbol / shorthand | Definition | Label if defined by equation | Used in | Notes |
|---|---|---|---|---|---|
| Clean accuracy | `\mathrm{Acc}_{\mathrm{clean}}`; `Clean` | Accuracy on unperturbed test images. | None. | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 aggregate tables. | Allowed in tables/captions; use descriptive titles rather than metric-only titles. |
| Robust accuracy | `\mathrm{Acc}(A)` | Accuracy under adversarial attack `A`. | `eq:attack_acc` | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 result tables. | General metric name can appear in titles; formula label is currently unreferenced per `docs/03_label_registry.md`. |
| Per-attack robust accuracy | `\mathrm{Acc}(A)` per attack | Robust accuracy reported separately for each attack. | `eq:attack_acc` | `tab:ch6_per_attack_all_baselines`; graybox per-attack tables. | Preferred in subsection titles over code attack names. |
| Mean robust accuracy over eight attacks | `Mean(8)`; `\mathrm{Mean}(8)` | Average robust accuracy over the eight non-AutoAttack evaluation attacks. | `eq:mean8` | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 aggregate/graybox/ablation tables. | Main aggregate robustness metric. Do not use `Mean(8)` in section/subsection titles. |
| `Mean(8)` shorthand | `Mean(8)` | Shorthand for mean robust accuracy over the eight bounded non-AutoAttack attacks. | `eq:mean8` | Tables, captions, metric-definition paragraphs. | Use `Mean(8)` rather than shorter variants such as `M(8)`. |
| Worst-case robust accuracy over eight attacks | `Worst(8)`; `\mathrm{Worst}(8)` | Minimum robust accuracy over the same eight non-AutoAttack attacks. | `eq:worst8` | `report/chapters/chapter5/7-eval_metrics.tex`; `tab:ch6_worst_autoattack_sanity`; Chapter 6 tables. | Do not use `Worst(8)` in subsection titles; use a readable title and define metric in body. |
| `Worst(8)` shorthand | `Worst(8)` | Shorthand for worst robust accuracy across the eight bounded non-AutoAttack attacks. | `eq:worst8` | Tables/captions and body text after definition. | The active Chapter 6 heading uses the readable title `Robustness Under the Hardest Evaluation Cases`. |
| Held-out attack mean | held-out attack mean | Average over the six evaluation attacks not used as source attacks: FGSM-RS, TPGD, MI-FGSM, PGD-$\ell_2$, DeepFool-$\ell_2$, and CW-$\ell_2$. | None. | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 aggregate tables. | Use this readable name in visible table labels instead of attack-count suffixes. |
| Held-out $\ell_\infty$ mean | `Heldout_{\ell_\infty}`; held-out $\ell_\infty$ mean | Average over FGSM-RS, TPGD, and MI-FGSM. | None. | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 aggregate/ablation tables. | Use this readable name in visible table labels instead of attack-count suffixes. |
| Held-out $\ell_2$ mean | `Heldout_{\ell_2}`; held-out $\ell_2$ mean | Average over PGD-$\ell_2$, DeepFool-$\ell_2$, and CW-$\ell_2$. | None. | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 aggregate/ablation tables. | Use this readable name in visible table labels instead of attack-count suffixes. |
| Seen-source mean | seen-source mean | Average over the source attacks PGD-$\ell_\infty$ and DDN-$\ell_2$. | None. | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 aggregate tables. | Use this readable name in visible table labels instead of attack-count suffixes. |
| AutoAttack-$\ell_\infty$ 512-sample sanity metric | `AutoAttack`; `AutoAttack-512` if needed | Robust accuracy under AutoAttack-$\ell_\infty$ on 512 test samples for sanity checks. | None. | `report/chapters/chapter5/3-attack_suite.tex`; `report/chapters/chapter6/1_main_results.tex`. | Not included in Mean(8) and not part of the 20-seed paired aggregate panel. |
| Full-test AutoAttack-$\ell_\infty$ | `AutoAttack` | Robust accuracy under AutoAttack-$\ell_\infty$ on the full test set for a fixed random-seed panel. | None. | `tab:ch6_autoattack_fulltest`. | Report separately from Mean(8). |
| Graybox accuracy | `\mathrm{Acc}_{s \rightarrow t}(A)` | Target-model accuracy on adversarial examples generated by surrogate model `s`. | `eq:graybox_acc` | `report/chapters/chapter5/7-eval_metrics.tex`; Chapter 6 graybox section. | Equation label is currently unreferenced per `docs/03_label_registry.md`. |
| Off-diagonal graybox average | Off-diagonal average; cross-method graybox average | Average graybox accuracy excluding same-checkpoint/diagonal whitebox cells; used to summarize transfer between different methods. | None. | `report/chapters/chapter6/2_graybox_results.tex`. | Define the aggregation before using it as evidence. |
| Per-class/per-attack accuracy | `\mathrm{Acc}(A,c)` | Accuracy for attack `A` and class `c`. | `eq:attack_class_acc` | `report/chapters/chapter5/7-eval_metrics.tex`; `report/chapters/chapter6/4_whitebox.tex`; graybox per-cell section. | Also called attack-class group accuracy. |
| Effect size | `Cohen's d_z`; `d_z` | Paired effect size, `d_z = \bar{d}/s_d`. | None. | `report/chapters/chapter5/6-protocol.tex`; `tab:ch6_effect_size_summary`; paired result tables. | Define before use; do not rely on p-values alone. |
| p-value | `p`; raw/corrected `p` | Significance value from paired t-test or Wilcoxon signed-rank test. | None. | `report/chapters/chapter5/6-protocol.tex`; Chapter 6 result tables. | State whether raw or Holm-corrected p-values are used. |
| Confidence interval | `95\% CI`; bootstrap CI | Bootstrap interval over seed-level means or paired differences. | None. | `report/chapters/chapter5/6-protocol.tex`; Chapter 6 paired tables. | Add `CI` to abbreviation list if shorthand is used. |
| Standard deviation | `std`; `Std`; `\sigma` | Seed-to-seed variation or sample standard deviation. | None. | `report/chapters/chapter5/6-protocol.tex`; `tab:ch6_variance_reduction`; ablation tables. | Define whether values are across seeds, paired differences, or table rows. |
| Percentage points | `pp` | Absolute difference between percentages. | None. | Chapter 6 result interpretation. | `pp` is used frequently and should be defined at first use. |

Metric title rule:

- Allowed in titles: descriptive metric concepts such as "Aggregate Robustness", "Per-Attack Robustness", "Training Stability", and "Graybox Robustness".
- Avoid in titles: `Mean(8)`, `Worst(8)`, `Bottom-K`, `PGD20-CE`, `M(8)`, and code-style metric names.

## 5. Mathematical symbol registry

| Symbol | Meaning | First definition location | Used in | Notes |
|---|---|---|---|---|
| $x$ / $\mathbf{x}_i$ | Clean input image or sample. | `report/chapters/chapter2/1-preliminaries.tex`; vector form in `report/chapters/chapter4/1-problem_formulation.tex`. | Chapters 2, 4, 5. | Use one convention per local section; Chapter 4/5 mostly use `\mathbf{x}_i`. |
| $y$ / $y_i$ | Ground-truth class label. | `report/chapters/chapter2/1-preliminaries.tex`; `report/chapters/chapter4/1-problem_formulation.tex`. | Chapters 2, 4, 5. | Keep `y_i` for indexed samples. |
| $\delta$ | Adversarial perturbation. | `report/chapters/chapter2/1-preliminaries.tex`. | Chapter 2 threat-model definitions. | Perturbation budget is governed by $\varepsilon$. |
| $\varepsilon$ / $\epsilon$ | Perturbation budget. | `report/chapters/chapter2/1-preliminaries.tex`; concrete $\varepsilon_\infty=8/255$ in `report/chapters/chapter5/3-attack_suite.tex`. | Chapters 2 and 5. | Active source uses `\varepsilon`; prefer that spelling for consistency. |
| $f_\theta$ | Classifier parameterized by $\theta$. | `report/chapters/chapter2/1-preliminaries.tex`; restated in `report/chapters/chapter4/1-problem_formulation.tex`. | Chapters 2, 4, 5. | Graybox metrics use $f_{\theta_s}$ and $f_{\theta_t}$ for surrogate and target models. |
| $z_i$ | Logits for sample `i`. | `report/chapters/chapter4/1-problem_formulation.tex`; clarified in `report/chapters/chapter4/5-clustering_feature.tex`. | Chapter 4 methodology. | Used to compute probabilities and gradient-fingerprint terms; not concatenated directly into $\psi_i$. |
| $\theta$ | Model parameters. | `report/chapters/chapter2/1-preliminaries.tex`. | Chapters 2, 4, 5. | $\eta_\theta$ appears in Algorithm 1 input but is not otherwise defined in prose. |
| $\mathcal{D}$ | Dataset; generic supervised dataset. | `report/chapters/chapter2/1-preliminaries.tex`. | Chapter 2. | Chapter 4/5 use more specific variants. |
| $\mathcal{D}_{\mathrm{train}}$ | Training dataset. | `report/chapters/chapter4/1-problem_formulation.tex`. | Chapter 4 algorithm and problem setup. | Separate from $\mathcal{D}_{\mathrm{test}}`. |
| $\mathcal{D}_{\mathrm{test}}$ | Test dataset. | `report/chapters/chapter5/7-eval_metrics.tex`. | Chapter 5 metrics. | Defines evaluation sample set. |
| $\mathcal{D}_c$ | Test subset with class label `c`. | `report/chapters/chapter5/7-eval_metrics.tex`. | Attack-class accuracy. | Used in `eq:attack_class_acc`. |
| $\mathcal{A}$ | Generic adversarial attack operator or attack family. | `report/chapters/chapter2/1-preliminaries.tex`; Chapter 5 metrics. | Chapters 2, 5. | Use script `\mathcal{A}` for sets/operators, plain `A` for one attack when clearer. |
| $\mathcal{A}_e$ | Attack-domain generator for domain index `e`. | `report/chapters/chapter2/1-preliminaries.tex`. | Background and attacks-as-domains framing. | Chapter 4 uses source attack notation $\mathcal{A}_{\mathrm{src}}$ and `A_m`. |
| $e$ | Attack/domain index. | `report/chapters/chapter2/1-preliminaries.tex`. | Background domain-risk definition. | Chapter 4 uses `m` for source attack index and `k` for cluster index. |
| $R_e(\theta)$ | Risk associated with attack domain `e`. | `report/chapters/chapter2/1-preliminaries.tex`. | Background attack-domain framing. | Chapter 4 uses $R_m(\theta)$ for source attack `m`. |
| $R_m(\theta)$ | Empirical adversarial risk under source attack `A_m`. | `report/chapters/chapter4/1-problem_formulation.tex`. | `eq:avg_risk`. | Attack index `m=1,\ldots,M`. |
| $K$ | Number of classes in Chapter 2, but number of clusters in Chapter 4/5/6. | Classes: `report/chapters/chapter2/1-preliminaries.tex`; clusters: `report/chapters/chapter4/4-attackDRO++.tex` and `tab:ch4_hparams`. | Chapters 2, 4, 5, 6. | Potential ambiguity. Chapter 4 also uses `C` for class count; consider using `C` consistently for classes and `K` for clusters. |
| $C$ | Number of classes. | `report/chapters/chapter4/1-problem_formulation.tex`; `report/chapters/chapter5/2-architectures.tex`. | Chapters 4, 5. | Preferred class-count symbol in methodology. |
| $q$ / $\mathbf{q}$ | Group or cluster weight vector. | `report/chapters/chapter4/3-attackDRO.tex`; cluster version in `report/chapters/chapter4/4-attackDRO++.tex`. | Chapters 4, 5, 6. | Use `q_m` for attack groups and `q_k` for clusters. Cluster updates use exponentiated gradient with configured score $s_k$ and floor projection. |
| $q_k$ | Weight assigned to cluster `k`. | `report/chapters/chapter4/4-attackDRO++.tex`. | AttackDRO++ update and Cluster-DRO loss. | Updated with $q_k \leftarrow \Pi_{q_{\min}}(q_k\exp(\eta_q s_k))$ over the cluster-weight vector. |
| $q_g$ | Generic group weight. | Not found in active LaTeX source. | Planned only if prose generalizes group notation. | If introduced later, define whether `g` is attack group, cluster, or class-attack group. |
| $q_{\min}$ | Minimum weight retained by every group/cluster. | `report/chapters/chapter4/3-attackDRO.tex`; `report/chapters/chapter4/6-anchor_objective.tex`; `tab:ch4_hparams`. | Chapters 4 and 5. | Default value is `0.03`. |
| $\alpha$ | Generic step size or weighting parameter. | Not found in active LaTeX source. | None. | Do not introduce unless needed; current report uses $\eta_q$ and $\lambda_{\mathrm{DRO}}` instead. |
| $\eta_q$ | Learning rate for exponentiated-gradient update of `q`. | `report/chapters/chapter4/3-attackDRO.tex`; `tab:ch4_hparams`. | Chapters 4 and 5. | Default is `3 x 10^{-4}`. |
| $\eta_\theta$ | Model-parameter learning rate. | Algorithm input in `report/chapters/chapter4/7-complete_pipeline.tex`. | Algorithm 1. | Needs prose definition if referenced outside algorithm. |
| $\lambda_{\mathrm{DRO}}$ | Anchor strength / Cluster-DRO interpolation weight. | `report/chapters/chapter4/6-anchor_objective.tex`; `tab:ch4_hparams`. | Chapters 4, 5, 6. | Default `0.35`; maps to `Anchor35`. |
| $\lambda_{\mathrm{grad}}$ | Weight applied to gradient-fingerprint component of $\psi_i$. | `report/chapters/chapter4/5-clustering_feature.tex`; `tab:ch4_hparams`. | Chapters 4 and 5. | Default `0.1`. |
| $\lambda_{\mathrm{lbl}}$ | Weight applied to the scalar normalized label feature in $\psi_i$. | `report/chapters/chapter4/5-clustering_feature.tex`; `tab:ch4_hparams`. | Chapters 4 and 5. | Default `0.1`; the implementation appends a scalar label feature, not a one-hot label vector. |
| $\tilde{y}_i$ | Scalar normalized label feature for sample `i`. | `report/chapters/chapter4/5-clustering_feature.tex`. | AttackDRO++ clustering feature. | Included only when label information is enabled and weighted by $\lambda_{\mathrm{lbl}}$. |
| $r_i$ | Classification margin for sample `i`. | `report/chapters/chapter4/3-attackDRO.tex`. | AttackDRO difficulty scoring. | Margin drives `s_i`. |
| $s_i$ | Per-sample difficulty score. | `report/chapters/chapter4/3-attackDRO.tex`. | AttackDRO and AttackDRO++. | Defined by softplus of negative margin. |
| $s_m$ | Attack-group difficulty score for attack group `m`. | `report/chapters/chapter4/3-attackDRO.tex`. | AttackDRO update. | Average of `s_i` in attack group. |
| $s_k$ | Configured cluster reweighting score for cluster `k`. | `report/chapters/chapter4/4-attackDRO++.tex`. | AttackDRO++ update. | May be based on cluster loss, the configured difficulty score, or a hybrid of loss and difficulty score depending on the q-update metric. |
| $\tau$ | Temperature in the difficulty score. | `report/chapters/chapter4/3-attackDRO.tex`. | Difficulty score. | No default value found in active Chapter 5 hyperparameter tables. |
| $c_i$ | Cluster assignment for adversarial example `i`. | `report/chapters/chapter4/4-attackDRO++.tex`. | AttackDRO++ cluster grouping. | Takes values in `{1,\ldots,K}`. |
| $\mathcal{C}_{\mathcal{B}}$ | Set of clusters present in the current minibatch. | `report/chapters/chapter4/4-attackDRO++.tex`. | Cluster-DRO loss. | Used to renormalize cluster weights. |
| $\mathcal{F}$ | Feature bank of detached augmented features. | `report/chapters/chapter4/4-attackDRO++.tex`; `tab:ch4_hparams`. | AttackDRO++ cluster refresh. | Default size `4096`. |
| $h_i$ / $\mathbf{h}$ | Penultimate-layer representation. | `report/chapters/chapter4/1-problem_formulation.tex`; `report/chapters/chapter5/2-architectures.tex`. | Chapters 4 and 5. | Used in clustering and gradient fingerprint construction. |
| $\phi_\theta$ | Feature extractor / penultimate representation map. | `report/chapters/chapter4/1-problem_formulation.tex`; `report/chapters/chapter5/2-architectures.tex`. | Chapters 4 and 5. | Should remain distinct from classifier output `f_\theta`. |
| $G_i$ | Raw classifier-head gradient proxy / gradient fingerprint matrix. | `report/chapters/chapter4/5-clustering_feature.tex`. | Gradient fingerprint feature construction. | Dimension `C x d_h`; vectorized before projection. |
| $g_i$ | Projected gradient fingerprint vector. | `report/chapters/chapter4/5-clustering_feature.tex`. | Augmented feature $\psi_i$. | Dimension `d_{\mathrm{proj}}`; normalized and weighted by $\lambda_{\mathrm{grad}}$ before concatenation. |
| $P$ | Fixed random projection matrix. | `report/chapters/chapter4/5-clustering_feature.tex`; Algorithm 1. | Gradient fingerprint projection. | Shape `C d_h x d_{\mathrm{proj}}`. |
| $d_{\mathrm{proj}}$ | Random projection dimension for gradient fingerprint. | `report/chapters/chapter4/5-clustering_feature.tex`; `tab:ch4_hparams`. | Chapters 4 and 5. | Default `128`. |
| $d_h$ | Penultimate representation dimension. | `report/chapters/chapter4/1-problem_formulation.tex`; `report/chapters/chapter5/2-architectures.tex`. | Chapters 4 and 5. | For ResNet-18/CIFAR-10 it is `512`. |
| $\psi_i$ | Canonical augmented clustering feature. | `report/chapters/chapter4/5-clustering_feature.tex`. | AttackDRO++ clustering. | Concatenates $\operatorname{norm}(h_i)$, $\lambda_{\mathrm{lbl}}\tilde{y}_i$, and $\lambda_{\mathrm{grad}}\operatorname{norm}(g_i)$; logits are used to build probabilities and gradient fingerprints but are not a direct component. |
| $T_w$ | Warmup epochs before adaptive `q` update. | `report/chapters/chapter4/6-anchor_objective.tex`; `tab:ch4_hparams`. | Chapters 4 and 5. | Default `3` epochs. |
| $R$ | Cluster refresh interval. | `report/chapters/chapter4/4-attackDRO++.tex`; `tab:ch4_hparams`; Chapter 6 ablation. | Chapters 4, 5, 6. | Default `2` epochs; ablation compares 1 and 2 epochs. |
| $\bar{d}$ | Mean paired difference. | `report/chapters/chapter5/6-protocol.tex`. | Statistical protocol. | Used in Cohen's $d_z`. |
| $s_d$ | Sample standard deviation of paired differences. | `report/chapters/chapter5/6-protocol.tex`. | Statistical protocol. | Used in Cohen's $d_z`. |
| $\sigma$ | Standard deviation in result tables. | `report/chapters/chapter6/1_main_results.tex`, `tab:ch6_variance_reduction`. | Chapter 6. | Define whether it is over seeds or paired differences. |

## 6. Acronym registry

| Acronym | Full form | First definition location | Notes |
|---|---|---|---|
| `AT` | Adversarial Training | `report/outsider/list-of-abbreviations.tex`; used in Chapter 2/3 headings. | Ensure first main-text use expands it. |
| `PGD` | Projected Gradient Descent | `report/outsider/list-of-abbreviations.tex`; used in `report/chapters/chapter2/1-preliminaries.tex`. | Also appears in method name `PGD-AT`. |
| `DDN` | Decoupled Direction and Norm | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter2/2-at-deep-dive.tex`; `report/chapters/chapter5/3-attack_suite.tex`. | Included in the front-matter abbreviation list and used in `DDN-AT` and `DDN-$\ell_2$`. |
| `FGSM` | Fast Gradient Sign Method | `report/outsider/list-of-abbreviations.tex`; used in Chapter 2. | `FGSM-RS` is listed separately as Fast Gradient Sign Method with Random Start. |
| `FGSM-RS` | Fast Gradient Sign Method with Random Start | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter2/2-at-deep-dive.tex`; `tab:ch5_evaluation_attacks`. | Held-out $\ell_\infty$ evaluation attack. |
| `MI-FGSM` | Momentum Iterative Fast Gradient Sign Method | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter2/2-at-deep-dive.tex`; `tab:ch5_evaluation_attacks`. | Use hyphenated `MI-FGSM` in report text. |
| `TPGD` | TRADES-style Projected Gradient Descent | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter2/2-at-deep-dive.tex`; `tab:ch5_evaluation_attacks`. | Expansion follows the active Chapter 2 definition. |
| `CW` | Carlini-Wagner | `report/outsider/list-of-abbreviations.tex`; used as `CW-$\ell_2$`. | Use `Carlini--Wagner` in LaTeX. |
| `DRO` | Distributionally Robust Optimization | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter4.tex`; `report/chapters/chapter4/3-attackDRO.tex`. | Central optimization shorthand; use `Group DRO` with a space in prose. |
| `ERM` | Empirical Risk Minimization | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter4/2-multi_attack.tex`; Chapter 4 method sections. | Expanded at first Chapter 4 use as empirical risk minimization (ERM). |
| `DG` | Domain Generalization | `report/outsider/list-of-abbreviations.tex`; Chapter 2/3 headings. | Already in abbreviation list. |
| `W&B` | Weights & Biases | `report/chapters/chapter5/9-tools_tracking.tex`; Appendix B tracking figure in `report/appendices.tex`. | Used for experiment logging and run tracking. |
| `GPU` | Graphics Processing Unit | Appendix D comment in `report/appendices.tex`. | Not active prose yet; add if compute section is written. |
| `CIFAR` | Canadian Institute For Advanced Research | Used through dataset name `CIFAR-10`. | Usually the dataset name is enough; expand only if required by school style. |
| `CNN` | Convolutional Neural Network | Not found in active report source; not in current abbreviation list. | Add only if Chapter 2 architecture background uses it. |
| `DNN` | Deep Neural Network | `report/outsider/list-of-abbreviations.tex`; Chapter 2 first paragraph of subsection 2.1.1. | Already in abbreviation list. |
| `ReLU` | Rectified Linear Unit | Not found in active report source. | Add only if model architecture prose discusses activations. |
| `SGD` | Stochastic Gradient Descent | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter5/4-configuration.tex`. | Expanded in Chapter 5 training configuration prose. |
| `CI` | Confidence Interval | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter5/6-protocol.tex`. | Defined before Chapter 6 tables use `95\% CI`. |
| `Std` | Standard Deviation | Concept appears in `report/chapters/chapter5/6-protocol.tex`; result tables use standard deviation or symbols. | Not included in the front-matter list because active tables use `standard deviation` or `\sigma`, not `Std`. |
| `pp` | Percentage points | `report/outsider/list-of-abbreviations.tex`; `report/chapters/chapter5/6-protocol.tex`. | Defined before Chapter 6 result prose. |
| `AA` | AutoAttack | Not active as report shorthand. | Removed from the front-matter abbreviation list because active prose spells out AutoAttack. |
| `IRM` | Invariant Risk Minimization | Not active in report prose. | Removed from the front-matter abbreviation list. Add back only if Chapter 3 is expanded to discuss IRM. |
| `REx` | Risk Extrapolation | Not active in report prose. | Removed from the front-matter abbreviation list. Add back only if Chapter 3 is expanded to discuss REx. |

## 7. Dataset, model, and tool registry

### Datasets and models

| Name | Type | Role in report | Notes |
|---|---|---|---|
| `CIFAR-10` | Dataset | Main image-classification benchmark. | Defined in `report/chapters/chapter5/1-dataset_preprocessing.tex`; 40k train / 10k validation / 10k test in current setup prose. |
| `ResNet-18` | Model architecture | Main backbone for all active experiments. | Defined in `report/chapters/chapter5/2-architectures.tex`; adapted for CIFAR-10. |
| `WRN-28-10` | Model architecture | Supplementary architecture check in Appendix C. | Values are from a single run and are not part of the main paired claims. Do not claim broad architecture generalization from this check. |
| Higher-capacity architectures | Model family | Future extension / scaling check. | Mentioned generically in `report/chapters/chapter5/2-architectures.tex`; no active named model besides ResNet-18. |

### Tools and platforms

| Tool/platform | Role | Where to mention | Notes |
|---|---|---|---|
| Google Colab | Experiment execution platform. | Chapter 5.9 tools/platform section. | Mention only as reproducibility context. |
| Google Drive | Checkpoint/result persistence. | Chapter 5.9 tools/platform section. | Stores checkpoints, cached adversarial examples, figures, and results. |
| Weights & Biases / W&B | Experiment logging and run tracking. | Chapter 5.9 tools/platform section; Appendix B tracking exports. | Tracking telemetry only, not result evidence. |
| PyTorch | Model training framework. | Chapter 5.9 tools/platform section. | Core training and automatic differentiation framework. |
| torchvision | Dataset/model utility package. | Chapter 5.9 tools/platform section. | CIFAR-10 loading, transforms, and model utilities. |
| TorchAttacks | Attack implementation package. | Chapter 5.9 tools/platform section. | Provides most gradient-based and optimization-based attacks. |
| AutoAttack package | AutoAttack-$\ell_\infty$ evaluator. | Chapter 5.9 tools/platform section and AutoAttack configuration note. | Used for the separate AutoAttack evaluation. |
| adv-lib | DDN-$\ell_2$ implementation source. | Chapter 5.9 tools/platform section. | Used for DDN-$\ell_2$ adversarial example generation. |
| scikit-learn | K-means clustering implementation. | Chapter 5.9 tools/platform section. | Provides MiniBatch K-means for cluster discovery. |
| pandas | Analysis table processing. | Chapter 5.9 tools/platform section. | Used with NumPy to aggregate result tables. |
| NumPy | Numeric analysis. | Chapter 5.9 tools/platform section. | Used for numerical processing and aggregation. |
| matplotlib | Plot generation. | Chapter 5.9 tools/platform section. | Used with SciencePlots for report figures. |
| MiKTeX | Local LaTeX build distribution. | Handoff compile notes only, unless Appendix D includes build environment. | Mention in report only if local reproducibility environment is documented. |
| VS Code / Antigravity | Editor/IDE. | Not currently relevant to report reproducibility. | Not found in active source or outline; avoid adding unless user wants environment notes. |
| RTX 5070 Ti | Hardware. | Appendix D / compute resources only if actually used. | Not found in active source or planning files. |
| CUDA/cuDNN | GPU software stack. | Appendix D compute resources if written. | Appears only in `report/appendices.tex` comment. |
| ART | Attack/robustness library. | Appendix D comment only. | Confirm whether actually used before mentioning. |

## 8. Inconsistency audit

| Issue | Found form | Preferred form | File/location | Suggested action |
|---|---|---|---|---|
| Old multi-attack method wording. | `Multi-ATtack` | `Multi-AT` for method name; `multi-attack training` for generic prose. | Previously in Chapter 5 and Chapter 6 active prose. | Cleaned in the active Chapter 4--6 flow. |
| Missing spaces around old method wording. | `ForMulti-ATtack`, `theMulti-ATtack`, `onMulti-AT` | `For Multi-AT`, `the Multi-AT`, `on Multi-AT`, or rephrased prose. | Previously in Chapter 5 and Chapter 6 active prose. | Cleaned in the active Chapter 4--6 flow. |
| Alternate baseline name in results prose. | `Uniform Multi-AT` | `Multi-AT` in formal results; `uniform multi-attack baseline` in prose if needed. | Previously in `report/chapters/chapter6/2_graybox_results.tex`. | Cleaned in active results prose. |
| Code-style attack name in prose. | `PGD20-CE` | `PGD-$\ell_\infty$`; define once as 20-step cross-entropy PGD in Chapter 5. | Previously in `report/chapters/chapter6/4_whitebox.tex`. | Cleaned in active results prose. |
| Config-table PGD spelling. | `PGD-20$_{\mathrm{CE}}$` | `PGD-$\ell_\infty$ (20 steps, cross-entropy)` or table-specific config wording. | `report/chapters/chapter5/5-choices.tex`. | Safe cleanup if table width allows. |
| Short metric shorthand. | `M(8)` | `Mean(8)` or define `M(8)` explicitly in the same caption/table. | Previously in `report/chapters/chapter6/3_ablation.tex`. | Cleaned in active Chapter 6 ablation captions and tables. |
| Metric shorthand in heading. | `Worst-Case Behavior: Worst(8) and AutoAttack` | Readable title such as `Robustness Under the Hardest Evaluation Cases`. | Previously in `report/chapters/chapter6/1_main_results.tex`. | Cleaned in active Chapter 6 headings. |
| Math/internal shorthand in heading. | `Bottom-\(K\) Whitebox Tail Robustness` | `Tail-Class Robustness: Do the Weakest Cells Improve?` | Previously in `report/chapters/chapter6/4_whitebox.tex`. | Cleaned in active Chapter 6 headings. |
| Variant name used as formal method name. | `AttackDRO++ Anchor35 GradFP`; method name with an `(Ours)` suffix | `AttackDRO++` in formal tables/captions; map config separately. | Previously in Chapter 5 and Chapter 6 active prose. | Cleaned in report-facing prose; `(Ours)` is optional and mostly discouraged in Chapter 5. |
| DRO acronym styling. | `GroupDRO` | `Group DRO` | Previously in `report/chapters/chapter4/3-attackDRO.tex`. | Cleaned in active Chapter 4 prose. |
| Acronym list synchronized. | Front matter previously omitted recurring acronyms and retained unused `AA`, `IRM`, and `REx`. | Active abbreviation list now includes recurring report acronyms and excludes unused shorthand. | `report/outsider/list-of-abbreviations.tex`; mirrored in `report/outsider/frontmatter.tex`. | Recheck if Chapter 3 or Appendix D is expanded later. |
| Notation formatting drift. | `(x)`, `(C=10)`, `(d\_h = 512)` | `\(x\)`, `\(C=10\)`, `\(d_h=512\)`. | `report/chapters/chapter5/2-architectures.tex`. | Safe LaTeX formatting cleanup later. |
| Class/cluster symbol ambiguity. | `K` means classes in Chapter 2 but clusters in Chapter 4. | Prefer `C` for classes and `K` for clusters. | `report/chapters/chapter2/1-preliminaries.tex`; Chapter 4/5 methodology. | Needs user/author confirmation because it changes notation in foundational prose. |
| Tool/platform section now active. | Tools and tracking are summarized in Chapter 5.9, with representative W&B exports moved to Appendix B. | Chapter 5.9 plus Appendix B. | `report/chapters/chapter5/9-tools_tracking.tex`; `report/appendices.tex`. | Keep tool versions and hardware details out unless verified. |
| Inactive ablation names remain in source. | `q-Frozen Ablation`, `Cluster Feature Mode`, `Sample-Level Regularizer`. | Keep inactive or move to appendix if final. | `report/chapters/chapter6/3_ablation.tex` inside `\iffalse`. | Postpone until content decision. |

## 9. Recommended cleanup later

### Safe automatic cleanup

- Keep report-facing wording such as `Multi-AT` and `multi-attack training`; do not reintroduce `Multi-ATtack`, `ForMulti-ATtack`, or `theMulti-ATtack`.
- Keep active prose uses of the main PGD attack as `PGD-$\ell_\infty$`; do not reintroduce `PGD20-CE` outside code/configuration context.
- Keep `Mean(8)` as the active shorthand in Chapter 6 ablation captions/tables; avoid reintroducing `M(8)`.
- Keep headings free of `Worst(8)`, `Bottom-\(K\)`, and other internal metric shorthand.
- Keep `Group DRO` with a space in report-facing prose.
- Fix simple LaTeX math formatting drift in `report/chapters/chapter5/2-architectures.tex`.
- Recheck `report/outsider/list-of-abbreviations.tex` only if Chapter 2/3 or Appendix D introduces additional recurring acronyms.

### Needs user confirmation

- Preserve `Multi-AT` as the formal method name; use "uniform multi-attack baseline" only as explanatory prose.
- Prefer `AttackDRO++` over adding an `(Ours)` suffix unless disambiguating in crowded tables.
- Decide whether Chapter 2 should change class-count notation from `K` to `C` to avoid conflict with the Chapter 4 cluster count `K`.
- Confirm actual tools/platforms before adding Chapter 5.9: Colab, Drive, W&B, PyTorch, torchvision, TorchAttacks, AutoAttack package, adv-lib, scikit-learn, pandas, NumPy, matplotlib, hardware, and environment.
- If Chapter 2 later defines a different meaning for `TPGD`, update the front matter and this registry; current approved outline maps it to TRADES-style Projected Gradient Descent.

### Postpone

- Do not rename notation throughout LaTeX until Chapter 2 and Chapter 5.9 are structurally updated.
- Do not move inactive ablation names or diagnostics into appendices until the user decides whether they belong in the PDF.
- Do not create `docs/04_figure_table_registry.md`, `docs/02_writing_templates.md`, or `docs/07_task_assignment.md` until requested.
- Do not remove equation labels just because they are currently unreferenced; coordinate that with `docs/03_label_registry.md` during a label cleanup patch.

## 10. Maintenance rule

Whenever a symbol, acronym, metric, method name, attack name, or tool name is added or renamed in the report, update `docs/05_notation_registry.md` in the same writing session.

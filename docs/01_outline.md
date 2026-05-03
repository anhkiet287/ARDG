# 01_outline.md — DATN Report Outline

---

## Narrative spine

The report follows one argument across seven chapters:

```
1. Adversarial robustness is attack-dependent — a model trained against one threat
   may fail against another.
2. Treating attacks as domains enables principled group-aware training.
3. Cluster-based DRO with gradient fingerprints discovers hard groups automatically.
4. This improves average-case robustness without sacrificing worst-case.
5. The improvement transfers to graybox settings.
6. Ablations reveal which configuration choices matter.
7. Negative results bound what the method cannot do.
```

---

## Evidence panels

Each results section draws from a named evidence panel. No section mixes panels
without explicit justification.

| Panel | Description | Seeds | Primary sections |
|---|---|---|---|
| A | n=20 paired aggregate whitebox | 20 paired seeds | 6.1 |
| B | n=5 per-class × attack whitebox | 5 random seeds | 6.2 |
| C | 5-seed graybox transfer (400 pairs, 32k rows) | 5 random seeds | 6.3 |
| D | Ablations (K, anchor, recluster) | 3 seeds each | 6.4 |

---

## Target length

100–120 pages total.

---

## Chapter 1 — Introduction

**Question:** Why does this problem matter, and what does this work do?

**Owner:** Leader (Kiệt)

**Summary rule:** No chapter summary. Ends with report organization.

| Section | Purpose | Target length |
|---|---|---|
| 1.1 Motivation | Why adversarial robustness matters; cross-attack gap as the central problem | 300–400 w |
| 1.2 Recap of Stage 1: Findings and Limitations | What Stage 1 showed (diagnosis) and what it could not do (intervention) | 250–350 w |
| 1.3 Problem Statement | Formal problem: improving cross-attack robustness under multi-attack training | 150–200 w |
| 1.4 Research Questions and Hypotheses | RQs and testable hypotheses tied to Chapters 5–6 | 200–300 w |
| 1.5 Contributions | Numbered list of contributions — method, evaluation protocol, findings | 150–200 w |
| 1.6 Scope and Limitations | What this work does not cover (other datasets, architectures, certified bounds) | 100–150 w |
| 1.7 Report Organization | One paragraph per chapter describing what each chapter does | 200–300 w |

**Transition out:** Report organization paragraph serves as the bridge to Chapter 2.

---

## Chapter 2 — Background

**Question:** What theory and tools does the reader need to understand the method?

**Owner:** ĐA

**Summary rule:** Chapter summary recommended (100–200 words, prose paragraph).

| Section | Purpose | Target length |
|---|---|---|
| 2.1 Preliminaries | Notation, classification setup, DNN basics (concise recap from Stage 1) | 300–400 w |
| 2.1.1 Deep Neural Networks and Classification | Standard DNN definition and supervised learning setup | — |
| 2.1.2 Loss Functions and Optimization | Cross-entropy, SGD, standard training | — |
| 2.2 Adversarial Examples and Threat Models | Definition of adversarial examples, Lp threat models, perturbation budgets | 300–400 w |
| 2.3 Adversarial Attack Algorithms | Compact template per attack: FGSM, PGD, CW, DeepFool, DDN, MI-FGSM, TPGD, AutoAttack | 800–1200 w |
| 2.4 Adversarial Training | Min-max formulation, standard AT, multi-attack AT concept | 300–400 w |
| 2.5 Distributionally Robust Optimization | ERM vs DRO, group DRO formulation, connection to worst-group risk | 400–500 w |
| 2.6 Domain Generalization and Clustering | Domain generalization concept, K-means, connection to group discovery | 300–400 w |
| 2.7 Statistical Foundations | Paired t-test, Wilcoxon signed-rank, bootstrap CI, effect size, Holm–Bonferroni | 300–400 w |

**Notes:**

- Attack algorithms should follow a consistent compact template (defined in `02_writing_templates.md`).
- Long derivations go to appendix.
- This chapter provides vocabulary for Chapter 4; do not preview results.

**Transition out:** Chapter closing → the background equips the reader; next, Chapter 3 surveys what has been tried.

---

## Chapter 3 — Related Work

**Question:** What has been tried before, and what gap remains?

**Owner:** Thành

**Summary rule:** Chapter summary recommended (100–200 words, prose paragraph).

| Section | Purpose | Target length |
|---|---|---|
| 3.1 Multi-Attack Adversarial Training | Methods that train against more than one attack; their assumptions and limits | 400–500 w |
| 3.2 Group DRO for Robustness | DRO-based methods in robustness; how groups are defined | 400–500 w |
| 3.3 Domain Generalization Meets Adversarial Robustness | DG perspective on adversarial training; overlap and differences | 300–400 w |
| 3.4 Cluster Discovery and Representation Learning | Learned group discovery in training pipelines; latent-group methods | 300–400 w |
| 3.5 Research Gap | What no existing method does: cluster-discovered group DRO with gradient features for multi-attack AT | 200–300 w |

**Notes:**

- Each section should position prior work, not just describe it.
- Section 3.5 should make Chapter 4 feel necessary.

**Transition out:** Chapter closing → the gap identified here is addressed by the method in Chapter 4.

---

## Chapter 4 — Proposed Methodology

**Question:** What is the proposed method, and why should it work?

**Owner:** Leader (Kiệt)

**Summary rule:** Chapter summary recommended (100–200 words, prose paragraph).

| Section | Purpose | Target length |
|---|---|---|
| 4.1 Overview | Road map of the chapter: five steps from observation to full method | 200–300 w |
| 4.2 Problem Formulation | Attacks-as-domains view; multi-attack risk and its limitations | 300–400 w |
| 4.2.1 Setup and Notation | Formal notation for multi-attack setting | — |
| 4.2.2 Multi-Attack Risk and Its Limitations | Why uniform averaging over attacks is suboptimal | — |
| 4.3 Uniform Multi-Attack ERM | Baseline definition — trains on mixed attacks with equal weight | 200–300 w |
| 4.4 AttackDRO: Per-Attack Group DRO | GroupDRO over attack identities; limitations of fixed group partition | 300–400 w |
| 4.5 AttackDRO++: Cluster-Discovered Group DRO | K-means over augmented features; exponentiated-gradient q-updates | 400–500 w |
| 4.6 Augmented Clustering Features | F3 feature space: penultimate layer + label embedding + gradient fingerprint | 300–400 w |
| 4.7 Uniform-Anchored Cluster-DRO Objective | Anchor loss combines cluster-DRO with uniform ERM; stability mechanisms (q-floor, q-warmup) | 300–400 w |
| 4.8 Complete AttackDRO++ Framework | Full algorithm pseudocode, default hyperparameters, training loop | 300–400 w |
| 4.8.1 Relationship to the Stage-1 Framework | Progression: Single-AT → Uniform ERM → AttackDRO → AttackDRO++ → GradFP → Anchor | 200–300 w |
| 4.9 Chapter Summary | Synthesizes the method; states what Chapter 6 will evaluate | 100–200 w |

**Notes:**

- Algorithm 1 (AttackDRO++ pseudocode) is defined here.
- Table 4.1 (default hyperparameters) is defined here.
- No results in this chapter.
- The chapter should make the experiments in Chapter 6 feel necessary and natural.

**Transition out:** Chapter closing → the method is defined; Chapter 5 specifies how it is tested.

---

## Chapter 5 — Experimental Setup

**Question:** How was the method tested, and under what conditions?

**Owner:** Leader (Kiệt)

**Summary rule:** `\paragraph{Summary.}` with setup recap table (`tab:ch5_setup_summary`), then one transition paragraph to Chapter 6.

| Section | Purpose | Target length |
|---|---|---|
| 5.1 Dataset and Preprocessing | CIFAR-10 description, split (40k/10k/10k), normalization, augmentation | 100–150 w |
| 5.2 Model Architectures | ResNet-18 specification | 100–150 w |
| 5.3 Attack Suite for Stage 2 | Training and evaluation attacks with configuration table | 400–500 w |
| 5.3.1 Training Attacks | PGD-ℓ∞ and DDN-ℓ2 with full configuration | — |
| 5.3.2 Evaluation Attacks | Eight evaluation attacks + AutoAttack; `tab:ch5_attack_configurations` | — |
| 5.4 Training Configuration | Optimizer, LR schedule, epochs, batch size, shared across all methods | 200–300 w |
| 5.5 Hyperparameter Choices | Default config for AttackDRO++; ablation factors table (`tab:ch5_ablation_factors`) | 300–400 w |
| 5.6 Statistical Significance Protocol | Paired tests, bootstrap CI, effect size, Holm–Bonferroni; reporting format table | 400–500 w |
| 5.7 Evaluation Metrics | Mean(8), Worst(8), seen/heldout splits, AutoAttack, metric definitions | 400–500 w |
| 5.8 Graybox Transfer Protocol | 4 methods × 5 seeds = 20 checkpoints, 400 pairs, 32k-row table; transfer regimes | 400–500 w |

**Required tables:**

- `tab:ch5_training_attacks` — training attack configuration
- `tab:ch5_attack_configurations` — full evaluation attack configuration (source of truth for naming)
- `tab:ch5_autoattack_config` — AutoAttack configuration
- `tab:ch5_training_config` — general training configuration
- `tab:ch5_compared_methods` — summary of compared methods
- `tab:ch5_attackdro_defaults` — AttackDRO++ default hyperparameters
- `tab:ch5_ablation_factors` — hyperparameters varied in ablations
- `tab:ch5_reporting_format` — statistical reporting format
- `tab:ch5_eval_metrics` — summary of evaluation metrics
- `tab:ch5_graybox_transfer_regimes` — transfer regimes
- `tab:ch5_setup_summary` — setup recap table (chapter-ending)

**Notes:**

- Graybox seed selection: "five randomly selected seeds" — no rationale beyond randomness.
- This chapter is the reproducibility anchor; every claim in Chapter 6 traces back here.

**Transition out:** Setup recap table + one paragraph handing off to Chapter 6.

---

## Chapter 6 — Results and Analysis

**Question:** What did the experiments show, and what does it mean?

**Owner:** Leader (Kiệt)

**Summary rule:** Chapter closing prose paragraph (100–200 words). No standalone "Main Findings" section — the closing synthesizes key findings and hands off to Chapter 7.

**Structure logic:**

```
Whitebox aggregate (n=20) → Whitebox per-class drill-down (n=5)
→ Graybox transfer (5-seed) → Ablation studies (3 seeds each)
→ Chapter closing
```

Each section follows: result → interpretation → limitation → motivation for next section.

---

### 6.1 Main Whitebox Results

**Panel:** A (n=20 paired seeds)

**Purpose:** Present aggregate whitebox robustness, per-attack breakdown, worst-case preservation, and variance reduction. This is the primary evidence section.

| Subsection | Purpose | Target length |
|---|---|---|
| 6.1.1 Aggregate Robustness | Mean(8), seen/heldout splits, four-method comparison table | 300–400 w |
| 6.1.2 Per-Attack Robustness Profile | Per-attack accuracy across methods; which attacks drive the gap | 300–400 w |
| 6.1.3 Worst-Case Behavior | Worst(8) and AutoAttack preservation; sanity vs full-test panel | 200–300 w |
| 6.1.4 Variance Reduction and Training Stability | 2.5–3.3× variance reduction woven into interpretation; not a standalone finding | 200–300 w |

**Required tables/figures:**

- `tab:ch6_main_aggregate` — main robustness table (mean ± std, n=20)
- `tab:ch6_paired_aggregate` — paired comparisons with p-values, Δ, effect sizes
- `fig:ch6_per_attack_profile` — per-attack accuracy line/bar chart
- `fig:ch6_forest_plot` — forest plot of paired differences with CI

**Allowed claims:**

- AttackDRO++ improves Mean(8) over Uniform by +0.279 pp (p=0.008)
- Heldout ℓ2 is the strongest improvement channel (+0.405 pp)
- Worst(8) and AutoAttack are preserved (Δ ≈ 0, p > 0.96)
- Variance is 2.5–3.3× lower on average-case metrics
- Single-AT baselines are specialists, not stronger defenses

**Transition out:** Aggregate results may hide uneven per-class behavior → Section 6.2.

---

### 6.2 Per-Class and Per-Attack Whitebox Analysis

**Panel:** B (n=5 random seeds)

**Purpose:** Break down whitebox results by class × attack to identify where gains concentrate and which classes remain difficult. The worst-cell story (cat × PGD-ℓ∞ falsification) emerges here naturally.

| Subsection | Purpose | Target length |
|---|---|---|
| 6.2.1 Per-Class Robustness Patterns | Which classes improve (ship, frog) and which remain hard (cat, dog); delta heatmaps | 300–400 w |
| 6.2.2 Tail Robustness | Bottom-K class behavior; does AttackDRO++ lift the weakest cells? | 200–300 w |

**Required tables/figures:**

- `fig:ch6_whitebox_delta_vs_uniform` — delta heatmap: AttackDRO++ vs Uniform (class × attack)
- `fig:ch6_whitebox_delta_vs_pgd` — delta heatmap: AttackDRO++ vs PGD-AT
- `fig:ch6_whitebox_delta_vs_ddn` — delta heatmap: AttackDRO++ vs DDN-AT
- `fig:ch6_whitebox_radar` — radar chart per attack
- `tab:ch6_whitebox_class_summary` — summary statistics (positive cells, mean Δ, tail lift)

**Allowed claims:**

- Per-class gains are unevenly distributed
- Certain classes (ship, frog) consistently benefit; others (cat, dog) are harder
- The worst individual cell (cat × PGD-ℓ∞) does not show consistent regression across seeds
- Without sample-level regularization, cluster-DRO redistributes capacity rather than uniformly improving all cells

**Notes:**

- Explain the n=5 panel briefly: "A subset of five randomly selected seeds is used for the per-class analysis to keep computation tractable."
- The per-class granularity tradeoff story belongs here, not in a separate ablation section.

**Transition out:** Whitebox assumes full model access; next section tests whether robustness transfers when the attacker uses a surrogate.

---

### 6.3 Graybox Transfer Robustness

**Panel:** C (5-seed subset, 400 surrogate–target pairs, 32k rows)

**Purpose:** Test whether AttackDRO++ changes the structure of learned robustness under cross-model transfer, not just whitebox accuracy.

| Subsection | Purpose | Target length |
|---|---|---|
| 6.3.1 Cross-Method Transfer Matrix | 4×4 method-level transfer matrices per attack; overall transfer patterns | 300–400 w |
| 6.3.2 Paired Graybox Comparisons | AttackDRO++ vs each baseline in the graybox setting; per-cell paired tests | 300–400 w |
| 6.3.3 Per-Class Graybox Patterns | Which classes show graybox-specific behavior; where transfer gaps appear | 200–300 w |

**Required tables/figures:**

- `fig:ch6_transfer_matrix_*` — 4×4 heatmaps per attack (8 attacks = 8 figures; select representative subset for main text, rest to appendix)
- `tab:ch6_graybox_method_pair_tests` — aggregate paired t-test results across methods
- `fig:ch6_graybox_delta_vs_uniform` — per-class × attack delta heatmap (graybox)
- `fig:ch6_graybox_delta_vs_pgd` — per-class × attack delta heatmap (graybox)
- `fig:ch6_graybox_delta_vs_ddn` — per-class × attack delta heatmap (graybox)
- `fig:ch6_whitebox_graybox_gap` — whitebox vs graybox gap comparison across methods

**Allowed claims:**

- AttackDRO++ graybox transfer is at least as strong as Uniform Multi-AT
- Transfer structure differs between single-AT specialists and multi-attack methods
- The whitebox-to-graybox gap is consistent across methods (no method-specific transfer collapse)
- Per-class graybox patterns largely mirror whitebox patterns

**Notes:**

- Seed framing: "five randomly selected seeds" — no further rationale.
- Select 3–4 representative transfer matrices for main text; remaining go to appendix.
- The per-class patterns in graybox naturally absorb the granularity tradeoff story for the graybox setting.

**Transition out:** The main results and transfer analysis use the default configuration; the next section tests sensitivity to key hyperparameters.

---

### 6.4 Ablation Studies

**Panel:** D (3 seeds each)

**Purpose:** Test sensitivity to the three main configuration choices. Each ablation answers a practical question for anyone using the method.

| Subsection | Purpose | Seeds | Target length |
|---|---|---|---|
| 6.4.1 Number of Clusters | Sensitivity to K = 2, 4, 6, 10 | 3 seeds | 200–300 w |
| 6.4.2 Anchor Strength | Sensitivity to λ_DRO = 0.2, 0.35, 0.5 | 3 seeds (42, 789, 7777) | 200–300 w |
| 6.4.3 Cluster-Refresh Frequency | Every 1 epoch vs every 2 epochs | 3 seeds | 200–300 w |

**Required tables/figures:**

- `tab:ch6_ablation_clusters` — Mean(8) and Worst(8) across K values
- `tab:ch6_ablation_anchor` — Mean(8) and Worst(8) across anchor strengths
- `tab:ch6_ablation_recluster` — Mean(8) and Worst(8) across refresh schedules
- One combined ablation summary figure or table (optional, if space permits)

**Allowed claims:**

- K=4 is a reasonable default; too few or too many clusters degrade performance
- Anchor35 balances adaptivity and stability; stronger anchoring removes too much DRO signal, weaker anchoring increases instability
- Recluster frequency has a modest effect; every-2-epochs is sufficient

**Notes:**

- These ablations use 3 seeds — state this once at the section opening.
- Keep interpretation practical: "how should a practitioner configure this?"
- Do not overclaim sensitivity; these are configuration guides, not theoretical results.

**Transition out:** None — this is the last results section. The chapter closing follows.

---

### Chapter 6 closing paragraph

Synthesizes the four sections into the main takeaways. Frames what Chapter 7 will conclude. Follows the chapter-ending transition rule from `06_style_rules.md`.

Content to cover:

1. AttackDRO++ improves average-case robustness with statistical significance while preserving worst-case.
2. The improvement is distributed across attacks and transfers to graybox settings.
3. Per-class analysis reveals where gains concentrate and where limits remain.
4. Ablations confirm the default configuration is reasonable.
5. Hand off: Chapter 7 answers the research questions and discusses limitations.

Target length: 150–200 words.

---

## Chapter 7 — Conclusion and Future Work

**Question:** What was learned, what are the limits, and where does the work lead?

**Owner:** Leader (Kiệt)

**Summary rule:** No separate summary — the chapter itself is the conclusion.

| Section | Purpose | Target length |
|---|---|---|
| 7.1 Summary of Contributions | Restate contributions from Chapter 1; confirm which were supported by evidence | 200–300 w |
| 7.2 Answers to Research Questions | Map each RQ/hypothesis from Section 1.4 to specific results in Chapter 6 | 300–400 w |
| 7.3 Limitations | What this study does not cover: single dataset, single architecture, no certified bounds, cluster-DRO capacity tradeoffs | 200–300 w |
| 7.4 Future Work | Concrete directions: larger datasets, other architectures, sample-level regularization, adaptive K, certified robustness | 200–300 w |
| 7.5 Closing Remarks | Final 2–3 sentences | 50–100 w |

**Notes:**

- Do not introduce new results or new methods.
- Limitations should be honest and specific, not generic hedges.
- Future work should connect to actual gaps found in Chapter 6 (e.g., per-class capacity tradeoff suggests sample-level regularization).

---

## Appendices

| Appendix | Content | Status |
|---|---|---|
| A — Pseudocode and Flowcharts | Illustrative diagrams if needed beyond Algorithm 1 | Optional |
| B — Experimental Logs and Configurations | Full configuration dumps, seed lists, compute environment | Include |
| C — Additional Tables and Visualizations | Remaining transfer matrices, full per-class tables, q-trajectory logs | Include |

**Notes:**

- Transfer matrices not shown in main text (Section 6.3) go here.
- q-trajectory logs are appendix material only — not a main chapter section.
- Full per-class × attack tables for all seed panels can go here if main text uses summaries.

---

## Front matter

| Component | Status |
|---|---|
| Title page | Required |
| Abstract | Required (250–300 words) |
| Acknowledgments | Required |
| Table of Contents | Auto-generated |
| List of Figures | Auto-generated |
| List of Tables | Auto-generated |
| List of Abbreviations | Required if >10 acronyms (likely yes) |

---

## Cross-reference: existing report vs new outline

This table maps the old report structure to the new outline for restructuring.

| Old structure | New location | Action |
|---|---|---|
| Ch 1 (1.1–1.7) | Ch 1 (1.1–1.7) | Keep, revise if needed |
| Ch 2 (2.1–2.7) | Ch 2 (2.1–2.7) | Keep, revise if needed |
| Ch 3 (3.1–3.5) | Ch 3 (3.1–3.5) | Keep, revise if needed |
| Ch 4 (4.1–4.9) | Ch 4 (4.1–4.9) | Keep as-is |
| Ch 5 (5.1–5.8) | Ch 5 (5.1–5.8) | Keep as-is |
| Old 6.1 Overview of Results | Remove | Absorbed into 6.1 opening |
| Old 6.2 Aggregate Robustness | New 6.1.1 | Restructure |
| Old 6.3 Per-Attack Robustness Profile | New 6.1.2 | Restructure |
| Old 6.4 Statistical Evidence | New 6.1 (woven into subsections) | Merge |
| Old 6.5 Source and Held-Out Robustness | New 6.1.1 (part of aggregate) | Merge |
| Old 6.6 Key Takeaways | Remove | Replaced by chapter closing |
| Old 6.7 Main Results | New 6.1 | Restructure (was a second pass; consolidate) |
| Old 6.8 Graybox Transfer Results | New 6.3 | Restructure |
| Old 6.9 Ablation Studies | New 6.4 (trimmed to K, anchor, recluster only) | Trim and restructure |
| Old 6.10 Per-(Class × Attack) Whitebox | New 6.2 | Move earlier |
| Old 6.11 Diagnostics | Appendix C | Move to appendix |
| Old Ch 7 Analysis and Discussion | Remove | Absorbed into Chapter 6 sections |
| Old Ch 8 Conclusion | New Ch 7 | Renumber |
| Old Appendix A–C | Keep | Review content |

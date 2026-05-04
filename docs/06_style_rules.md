# 06_style_rules.md — DATN Report Style Rules

---

## Part A — Narrative and Story Rules

---

## 1. Report style

The report should be written in a **formal but story-driven** style.

The reader should be able to follow the logic:

```text
Problem → Limitation → Method → Evaluation → Finding → Interpretation → Next question
```

Avoid writing the report as a collection of disconnected technical sections. Each major section should explain why it exists and how it connects to the next part, beyond just the technical requirements of a report.

---

## 2. Chapter structure

Final report structure:

```latex
Chapter 1 — Introduction
Chapter 2 — Background
Chapter 3 — Related Work
Chapter 4 — Proposed Methodology
Chapter 5 — Experimental Setup
Chapter 6 — Results and Analysis
Chapter 7 — Conclusion and Future Work
```

The old standalone **Analysis and Discussion** chapter is removed. Analysis should appear directly after the corresponding result in Chapter 6.

Recommended logic for Chapter 6:

```text
Result → Interpretation → Limitation/Motivation from this view → Next experiment
```

---

## 3. Chapter story arcs

Each chapter answers one question and sets up the next. The table below defines the narrative role of each chapter.

| Chapter | The question it answers | What it sets up |
|---|---|---|
| 1 — Introduction | Why does this problem matter, and what does this work do? | Grounds the reader before background |
| 2 — Background | What theory and tools does the reader need to understand the method? | Vocabulary and foundations for Chapter 4 |
| 3 — Related Work | What has been tried before, and what gap remains? | Justifies the proposed method in Chapter 4 |
| 4 — Proposed Methodology | What is the proposed method, and why should it work? | The evaluation target for Chapters 5–6 |
| 5 — Experimental Setup | How was the method tested, and under what conditions? | Grounds all result claims in Chapter 6 |
| 6 — Results and Analysis | What did the experiments show, and what does it mean? | Informs the scope of conclusions in Chapter 7 |
| 7 — Conclusion | What was learned, what are the limits, and where does the work lead? | — |

Use this table when deciding where a paragraph belongs. If a paragraph does not fit the question of its chapter, it is likely misplaced.

---

## 4. Summary rule

Use summaries only at chapter level.

| Chapter | Summary rule | Reason |
|---|---|---|
| Chapter 1 | No chapter summary | It already ends with report organization. |
| Chapter 2 | Chapter summary recommended | Background is long and needs consolidation. |
| Chapter 3 | Chapter summary recommended | Helps transition from related work to research gap. |
| Chapter 4 | Chapter summary recommended | Methodology has multiple components. |
| Chapter 5 | Chapter summary with recap table | Best for reproducibility and compact setup review. |
| Chapter 6 | Chapter summary recommended | Synthesizes main findings. |
| Chapter 7 | No separate summary | The chapter itself is the conclusion. |

**Form:** Chapter summaries should be plain closing prose paragraphs — not a `\section{Chapter Summary}` or `\subsection{Summary}`. Target length: 100–200 words. End with a sentence that frames what the next chapter does.

**Exception:** Chapter 5 uses `\paragraph{Summary.}` to introduce the setup recap table. This is the only case where that command is permitted. See Rule 7 for the full Chapter 5 summary format.

Do **not** use section-level summaries such as:

```latex
\subsection{Section Summary}
```

or:

```latex
\paragraph{Summary.}
```

in any chapter other than Chapter 5. Instead, use transition paragraphs only when needed.

---

## 5. Title naming rule

Use clear, understandable titles.

Preferred style: **mixed, concise, and explanatory**.

Examples:

```latex
\section{Whitebox Robustness Under Direct Attacks}
\section{Graybox Robustness Across Surrogate Models}
\section{Anchor Ablation and Stability Analysis}
```

For subsections, a slightly more story-driven style is allowed:

```latex
\subsection{Per-Class Robustness: Which Classes Remain Difficult?}
\subsection{Anchor Strength: Finding a Stable Trade-off}
\subsection{Graybox Transfer: Does Robustness Carry Across Models?}
```

**Question-mark titles** are allowed only at the `\subsection` level. Do not use question marks in `\section` or `\chapter` titles.

Avoid titles that are too internal, uncommon, or hard to understand.

Less preferred:

```latex
\subsection{Bottom-K Whitebox Tail Robustness}
\subsection{GradFP Cluster Dynamics}
\subsection{Q-collapse Mitigation}
```

Better:

```latex
\subsection{Tail-Class Robustness: Which Classes Remain Difficult?}
\subsection{Gradient-Based Clustering: How Hard Groups Are Discovered}
\subsection{Stabilizing Group Weights During Training}
```

Use method names only when the section is specifically about that method.

---

## 6. Transition paragraph rule

### 6.1 Within-chapter transitions

A transition paragraph between sections should be practical and reader-oriented.

It should answer:

```text
1. What did the current section show?
2. What limitation remains?
3. Why is the next section needed?
```

General template:

```latex
[Current section] gives us [what we learned]. However, [what this section cannot answer]. To address this, the next section examines [next topic] using [protocol/table/figure/definition].
```

Preferred tone:

- Clear
- Practical
- Not too academic
- Not too long
- Usually 2–4 sentences

Example: whitebox to graybox

```latex
Whitebox evaluation is the most direct way to test whether a model can resist attacks generated with full access to its parameters and gradients. However, in practical deployment, attackers do not always have this level of access. They may instead craft adversarial examples using a surrogate model and transfer them to the target model. For this reason, the next section evaluates robustness under the graybox protocol defined in Section~\ref{sec:ch5_graybox_protocol}.
```

Example: aggregate results to per-class results

```latex
The aggregate results provide a compact view of overall robustness, but they can hide uneven behavior across CIFAR-10 classes. A method may improve the mean score while still leaving certain classes consistently vulnerable. The next section therefore breaks the whitebox results down by class and attack to identify where the gains are concentrated and which failure cases remain.
```

When requested, provide 2–3 transition options with different tone or emphasis while following this same rule.

### 6.2 Chapter-ending transitions

The last paragraph of each chapter should follow the same structure as a section transition but at chapter level. It should:

1. State the key takeaway from the current chapter.
2. Name what gap or question the chapter cannot resolve on its own.
3. State what the next chapter does in response.

General template:

```latex
[This chapter] established [key takeaway]. However, [what this chapter cannot resolve]. Chapter~\ref{chap:X} addresses this by [what it does].
```

Example: Chapter 3 to Chapter 4

```latex
The related work reviewed in this chapter shows that existing adversarial training methods treat all training examples uniformly, without accounting for the varying difficulty of different input groups. This uniform treatment leaves a gap: hard groups are systematically under-trained while easier groups may be over-regularized. Chapter~\ref{chap:methodology} proposes a method that directly addresses this gap by identifying hard groups dynamically during training and upweighting their contribution to the adversarial objective.
```

Example: Chapter 5 to Chapter 6

```latex
This chapter has defined the full experimental protocol, including the datasets, models, attacks, and evaluation metrics used throughout this work. All result claims in the following chapter are grounded in this setup. Chapter~\ref{chap:results_analysis} now presents and interprets the results produced under this protocol.
```

---

## Part B — LaTeX Technical Rules

---

## 7. Chapter 5 summary style

Chapter 5 should end with a practical setup recap table introduced by `\paragraph{Summary.}`. This is the one permitted use of that command in the report (see Rule 4).

Recommended structure:

```latex
\paragraph{Summary.}
```

Inside this paragraph, use a compact table such as:

```latex
\begin{table}[t]
\centering
\caption{Summary of the experimental setup used in this report.}
\label{tab:ch5_setup_summary}
\begin{tabular}{ll}
\toprule
Component & Configuration \\
\midrule
Dataset & CIFAR-10 \\
Backbone & ResNet-18 \\
Training attacks & PGD-$\ell_\infty$, DDN-$\ell_2$ \\
Evaluation attacks & FGSM-RS, PGD-$\ell_\infty$, TPGD, MIFGSM, PGD-$\ell_2$, DDN-$\ell_2$, DeepFool-$\ell_2$, CW-$\ell_2$, AutoAttack-$\ell_\infty$ \\
Main metric & Mean robust accuracy over eight attacks, excluding AutoAttack-$\ell_\infty$ \\
Seeds & Five random seeds \\
\bottomrule
\end{tabular}
\end{table}
```

After the table, add only one short paragraph to transition into Chapter 6 following the chapter-ending transition rule in Section 6.2.

---

## 8. Attack naming rule

Use consistent, readable attack names in the report.

### 8.1 PGD naming

Do **not** repeatedly write `PGD20-CE` or `pgd20_ce` in prose.

Because the main PGD-$\ell_\infty$ evaluation attack is fixed to 20 steps, define this once in the attack configuration table, then use:

```latex
PGD-$\ell_\infty$
```

throughout the report.

If a distinction is necessary in code/configuration discussion, write:

```latex
PGD-$\ell_\infty$ (20 steps, cross-entropy loss)
```

but only where needed.

### 8.2 Recommended attack names in prose

| Internal / code name | Report name |
|---|---|
| `fgsm_rs` | FGSM-RS |
| `pgd20_ce` | PGD-$\ell_\infty$ |
| `pgd_l2` | PGD-$\ell_2$ |
| `tpgd` | TPGD |
| `mifgsm` | MI-FGSM |
| `cw_l2` | CW-$\ell_2$ |
| `deepfool_l2` | DeepFool-$\ell_2$ |
| `ddn_l2` | DDN-$\ell_2$ |
| `autoattack_linf` | AutoAttack-$\ell_\infty$ |

### 8.3 Attack configuration table

Chapter 5 must include a table defining:

- Report attack name
- Internal code name
- Norm
- Threat model
- Number of steps
- Perturbation budget
- Step size
- Loss/objective
- Library/package
- Used for training or evaluation
- Notes

Suggested label:

```latex
\label{tab:ch5_attack_configurations}
```

This table is the source of truth for attack naming and configuration.

---

## 9. Equation labeling rule

Only label equations that are referenced later.

Do not label every displayed equation automatically.

Use labels only when the text will later say:

```latex
Equation~\ref{eq:groupdro_objective}
```

or:

```latex
as defined in Eq.~\ref{eq:attack_domain_risk}
```

If an equation is included only for explanation and will not be referenced again, do not add a label.

Good:

```latex
\begin{equation}
R_e(\theta) =
\mathbb{E}_{(x,y)\sim \mathcal{D}}
\left[
\ell(f_\theta(\mathcal{A}_e(x,y,f_\theta)), y)
\right].
\label{eq:attack_domain_risk}
\end{equation}
```

Bad:

```latex
\begin{equation}
x' = x + \delta.
\label{eq:x_adv_basic}
\end{equation}
```

unless the report explicitly references it later.

---

## 10. Label naming convention

Use consistent labels across the report.

### Label registry

All labels used in the report must be recorded in **`label_registry.md`**.

This file is the single source of truth for every `\label{...}` in the project. Its purpose is to prevent duplicate labels, resolve cross-reference conflicts, and give all members a searchable index of what exists before they write a new section.

**When to update:** every time a member adds or removes a label in the LaTeX source, they must update `label_registry.md` in the same commit or writing session. Do not add a label to the LaTeX file without registering it.

**Structure of `label_registry.md`:** one entry per label, grouped by type (chapters, sections, subsections, figures, tables, algorithms, equations), with a short description of what the label points to. Example entry format:

```markdown
| Label | Type | Points to | Chapter |
|---|---|---|---|
| chap:methodology | chapter | Chapter 4 — Proposed Methodology | 4 |
| sec:ch6_whitebox | section | Whitebox Robustness Under Direct Attacks | 6 |
| fig:ch6_whitebox_radar | figure | Radar chart of whitebox per-attack results | 6 |
| alg:ch4_attackdro | algorithm | AttackDRO training procedure | 4 |
| eq:groupdro_objective | equation | Group DRO objective function | 4 |
```
## 11. Method naming convention

Use these report-facing method names consistently in titles, tables, captions, and prose.

| Old / shorthand name | Final report name | Notes |
|---|---|---|
| PGD-AT | PGD-AT | Single-attack adversarial training using PGD-$\ell_\infty$. |
| DDN-AT | DDN-AT | Single-attack adversarial training using DDN-$\ell_2$. |
| Multi-AT | Multi-AT | Uniform multi-attack adversarial training baseline. |
| AttackDRO++ | AttackDRO++; AttackDRO++ (Ours) in formal result comparisons when needed | Proposed method. Use “the proposed method” when avoiding repeated method names in prose. |

Usage rules:

- Use `PGD-AT` in formal tables/captions.
- Use `DDN-AT` in formal tables/captions.
- Use `Multi-AT` as the formal baseline name.
- Use “uniform multi-attack adversarial training baseline” only as explanatory prose, not as the formal method name.
- Use `AttackDRO++` in prose after first definition.
- Use `AttackDRO++ (Ours)` in formal result tables/captions when comparison clarity is needed.
- Define these method names once in Chapter 5, preferably in `tab:ch5_compared_methods`.

### Chapters

```latex
\label{chap:introduction}
\label{chap:background}
\label{chap:related_work}
\label{chap:methodology}
\label{chap:experimental_setup}
\label{chap:results_analysis}
\label{chap:conclusion}
```

### Sections

```latex
\label{sec:ch6_whitebox}
\label{sec:ch6_graybox}
\label{sec:ch6_anchor_ablation}
```

### Subsections

```latex
\label{subsec:ch6_per_attack_results}
\label{subsec:ch6_per_class_results}
```

### Figures

```latex
\label{fig:ch6_whitebox_radar}
\label{fig:ch6_graybox_transfer_matrix}
```

### Tables

```latex
\label{tab:ch6_main_results}
\label{tab:ch6_anchor_ablation}
```

### Algorithms

Algorithm labels include the chapter of definition:

```latex
\label{alg:ch4_attackdro}
\label{alg:ch4_attackdropp}
\label{alg:ch4_gradient_fingerprint}
```

If an algorithm is referenced in a later chapter, the label still reflects the chapter where it was first defined.

### Equations

Equations use no chapter prefix by default, since they are mathematical definitions that may be referenced across chapters:

```latex
\label{eq:multi_attack_risk}
\label{eq:groupdro_objective}
```

If two equations in different chapters share a similar concept and could be confused, add the chapter of definition:

```latex
\label{eq:ch2_group_risk}
\label{eq:ch4_group_risk}
```

---

## 11. Figure and table caption style

Captions must be self-contained. The reader should understand the figure or table without reading the surrounding text.

### Required elements — figures

- What is being shown
- The metric, with units in parentheses where applicable
- Key conditions (attack names, model, dataset) if not obvious from context
- A directional note only when non-obvious (e.g., "Higher is better")

### Required elements — tables

- What the table reports
- The metric, with units
- Averaging or aggregation method if relevant (e.g., mean over five seeds)
- A note about bolding if the best value per column is highlighted

### Style rules

- End captions with a period.
- Do not begin with *"The figure shows..."* or *"This table presents..."* — describe the content directly.
- Keep to 1–3 sentences.
- Bold the best value per column in result tables and note this in the caption.

Examples:

Bad:

```latex
\caption{Whitebox results.}
```

Good:

```latex
\caption{Mean robust accuracy (\%) under seven whitebox evaluation attacks, averaged over five seeds. Higher is better. The best result per attack is bolded.}
```

Bad:

```latex
\caption{The figure shows per-class accuracy for different methods.}
```

Good:

```latex
\caption{Per-class robust accuracy (\%) under PGD-$\ell_\infty$ for CIFAR-10 classes, averaged over five seeds. Error bars show one standard deviation.}
```

---

## 12. Acronym management

- Define each acronym at first use in the main text: e.g., *adversarial training (AT)*.
- After definition, use only the short form consistently.
- Do not redefine acronyms in captions, table footnotes, figure labels, or appendices — they inherit definitions from the main text.
- If the total number of distinct acronyms exceeds ten, add an abbreviations list in the front matter.
- Method acronyms established in Chapters 2–3 (AT, PGD, FGSM, DRO, etc.) do not need to be redefined in Chapters 4–6 unless the context changes.

---

## Part C — Writing Process Rules

---

## 13. Partner writing rule

Use the appropriate template based on section type.

**Use the full template for:** any section that introduces a method, presents a result, or makes a claim.

**Use the short template for:** setup, context, or connector sections that do not introduce new claims.

### Full template

```markdown
Section:
Purpose:
Required input:
Paragraph flow:
Required equations:
Required tables/figures:
Required references:
Allowed claims:
Tone/voice:
Avoid:
Expected length:
Output format:
```

> **Allowed claims** — list only claims directly supported by the data or argument presented in this section. Any broader generalization belongs in Chapter 7. If uncertain whether a claim is allowed, ask: *Does the evidence in this section directly support this?* If not, move it to the discussion or conclusion.

> **Tone/voice** — specify the intended register for this section: e.g., *analytical and precise*, *narrative and accessible*, *concise and technical*. This field prevents tone drift across long sections or across multiple writing sessions.

**Example — full template filled in** (Chapter 6, whitebox results section):

```markdown
Section: Whitebox Robustness Under Direct Attacks (Section 6.1)
Purpose: Present and interpret the main whitebox evaluation results for all five
  models across seven attacks, and identify which methods show the strongest and
  most consistent robustness.
Required input: Table tab:ch6_main_results (mean robust accuracy per model per
  attack, five seeds); Figure fig:ch6_whitebox_radar (radar chart of per-attack
  scores).
Paragraph flow:
  1. Open with one sentence framing the whitebox setting (full model access,
     seven attacks, five seeds).
  2. Present aggregate results from tab:ch6_main_results — name the top model
     and the margin over the baseline.
  3. Break down per-attack — which attacks expose the largest gap between
     methods, and which attacks are nearly equal across all models?
  4. Interpret — what does this pattern suggest about how the method distributes
     robustness across attacks?
  5. Close with the limitation that motivates the next section: whitebox results
     do not tell us whether robustness holds against unknown attackers or
     transferred examples.
Required equations: None new — reference eq:attack_domain_risk only if the
  discussion requires it.
Required tables/figures: tab:ch6_main_results (primary), fig:ch6_whitebox_radar
  (supporting visual).
Required references: Madry et al. for the PGD baseline; Croce & Hein for
  AutoAttack-linf.
Allowed claims:
  - AttackDRO achieves higher mean robust accuracy than baseline AT under
    PGD-linf on CIFAR-10/ResNet-18.
  - The improvement is consistent across five seeds (support with std values
    from the table).
  - Do NOT claim the method is universally better or generalizes to other
    datasets or architectures — that belongs in Chapter 7.
Tone/voice: Analytical and precise. State numbers first, interpret second. Do
  not hedge on results the table directly supports.
Avoid: Repeating experimental setup already defined in Chapter 5. Claiming
  results that are not in tab:ch6_main_results. Using vague phrases like
  "our method performs well" without citing specific numbers.
Expected length: 400–500 words.
Output format: LaTeX prose only — no new \section or \subsection headers
  inside this block.
```

---

### Short template

```markdown
Section:
Goal:
What to include:
Required figure/table:
Expected length:
Output format:
```

**Example — short template filled in** (Chapter 5, dataset subsection):

```markdown
Section: Dataset — CIFAR-10 (Section 5.1)
Goal: Describe CIFAR-10 and justify why it is the appropriate benchmark for
  this evaluation.
What to include:
  - Standard statistics: 50,000 training images, 10,000 test images, 10 classes,
    32x32 RGB.
  - Why CIFAR-10 is the accepted benchmark for adversarial training research
    (cite two or three representative papers that use it).
  - The normalization values used in preprocessing.
  - One sentence noting that the class distribution is balanced, which is
    relevant to group-based analysis in Chapter 6.
Required figure/table: None. Point to tab:ch5_setup_summary for the compact
  reference.
Expected length: 100–150 words, one paragraph.
Output format: LaTeX prose.
```

All final writing should be delivered in LaTeX.

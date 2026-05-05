Below is a Chapter-2-focused research package aligned with your current report structure and naming. I use **AttackDRO++** only for the final proposed method: **uniform-anchored Cluster-DRO with gradient fingerprints**. The cluster-only variant is referred to as **Cluster-DRO**.

Your current report already fixes the Stage 2 protocol: the source attacks are **PGD-(\ell_\infty)** and **DDN-(\ell_2)**, and these are shared across Multi-AT, AttackDRO, Cluster-DRO, and AttackDRO++ so that the compared methods differ mainly in grouping/weighting rather than adversarial data generation.  The current default AttackDRO++ configuration uses (K=4), anchor strength (\lambda_{\mathrm{DRO}}=0.35), (q)-flooring, warmup, periodic clustering, and projected gradient-fingerprint features. 

---

## 1. Citation map table

| Chapter 2 subsection                             | Concept                                                                                     | Essential citations                                                     | Recommended citations                                                                           | What each citation supports                                                                                                                                                                                                                                                                     |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1.1 Deep Neural Networks and Classification    | Supervised classification, logits, softmax, ERM                                             | Standard ML notation; no attack-specific primary citation required      | Goodfellow et al. deep learning textbook can be used if your reference list already includes it | Use this subsection mainly to define (f_\theta), logits, cross-entropy, and ERM. Avoid over-citing basic definitions unless your supervisor requires textbook citations.                                                                                                                        |
| 2.1.2 Adversarial Examples                       | Existence and definition of adversarial examples                                            | `szegedy2014intriguing`, `goodfellow2015explaining`                     | `athalye2018obfuscated`                                                                         | Szegedy et al. introduced the surprising existence and transferability of imperceptible adversarial perturbations; Goodfellow et al. formalized the linearity explanation and FGSM; Athalye et al. supports evaluation pitfalls such as gradient masking. ([OpenReview][1])                     |
| 2.1.3 Threat Models                              | White-box, graybox/transfer, black-box; norm-bounded perturbation sets                      | `madry2018towards`, `szegedy2014intriguing`                             | `athalye2018obfuscated`, `croce2020reliable`                                                    | Madry et al. gives the first-order white-box adversary and robust optimization framing; Szegedy et al. supports transferability; Athalye and AutoAttack motivate strong evaluation against false robustness. ([ICLR][2])                                                                        |
| 2.2.1 Min-max formulation                        | Adversarial training as robust optimization                                                 | `madry2018towards`                                                      | `goodfellow2015explaining`                                                                      | Madry et al. is the standard citation for the adversarial training min-max objective and PGD-based approximation; Goodfellow et al. supports the earlier FGSM-based adversarial training framing. ([ICLR][2])                                                                                   |
| 2.2.2 PGD-AT and its limitations                 | PGD adversarial training, first-order adversary, robust overfitting, clean/robust trade-off | `madry2018towards`, `rice2020overfitting`, `tsipras2019robustness`      | `zhang2019trades`, `athalye2018obfuscated`                                                      | Madry supports PGD-AT; Rice et al. supports robust overfitting and early stopping; Tsipras et al. and TRADES support the accuracy–robustness trade-off; Athalye supports not trusting weak attacks. ([ICLR][2])                                                                                 |
| 2.2.3 Multi-attack AT approaches                 | Robustness under a union of attacks/threat models                                           | `tramer2019multiple`, `maini2020union`                                  | `madaan2021learning`, `laidlaw2021perceptual`                                                   | Tramèr & Boneh show single-perturbation defenses do not guarantee robustness to other perturbation models; Maini et al. introduces multi-steepest descent for union robustness; Madaan and Laidlaw are useful broader multi-attack/unseen-threat references. ([NIPS Papers][3])                 |
| 2.2.4 Trade-off analysis                         | Clean accuracy vs robust accuracy; boundary error; robust overfitting                       | `zhang2019trades`, `tsipras2019robustness`, `rice2020overfitting`       | `madry2018towards`                                                                              | TRADES decomposes robust error and motivates a principled robustness–accuracy trade-off; Tsipras et al. argues robustness can be at odds with standard accuracy; Rice et al. supports training-time overfitting in AT. ([Proceedings of Machine Learning Research][4])                          |
| 2.3.1 Classical DRO formulation                  | Worst-case risk over an uncertainty set                                                     | `namkoong2016stochastic`, `hashimoto2018fairness`                       | `duchi2021learning` if you later add a broader DRO survey                                       | Namkoong & Duchi provide stochastic optimization for (f)-divergence DRO; Hashimoto et al. connects DRO to protecting high-loss minority subpopulations without demographic labels. ([NIPS Papers][5])                                                                                           |
| 2.3.2 Group DRO                                  | Worst-group risk over known groups                                                          | `sagawa2020groupdro`                                                    | `hashimoto2018fairness`                                                                         | Sagawa et al. is the key Group DRO citation for predefined groups, stochastic updates, and worst-group generalization. ([OpenReview][6])                                                                                                                                                        |
| 2.3.3 Exponentiated gradient on simplex          | Updating group weights (q)                                                                  | `sagawa2020groupdro`, `beck2003mirror`                                  | `kivinen1997exponentiated`                                                                      | Sagawa uses group reweighting in Group DRO; Beck & Teboulle supports entropic mirror descent/simplex geometry; Kivinen & Warmuth is a classic exponentiated-gradient reference. ([OpenReview][6])                                                                                               |
| 2.3.4 Regularization in overparameterized models | Why vanilla Group DRO may fail without regularization                                       | `sagawa2020groupdro`                                                    | `rice2020overfitting`                                                                           | Sagawa et al. directly shows Group DRO can fail in overparameterized models without strong regularization/early stopping; Rice et al. provides an adversarial-training analogue through robust overfitting. ([OpenReview][6])                                                                   |
| 2.3.5 DRO in adversarial training context        | Attack identities as groups; attack-domain risks                                            | `sagawa2020groupdro`, `tramer2019multiple`, `maini2020union`            | Current report context                                                                          | Use Sagawa for group minimax, Tramèr/Maini for multiple perturbation domains, and your report for the concrete PGD-(\ell_\infty)+DDN-(\ell_2) source setting. ([OpenReview][6])                                                                                                                 |
| 2.4.1 Clustering-based domain discovery          | Hidden groups, inferred environments, cluster-discovered groups                             | `creager2021environment`, `liu2021just`                                 | `thopalli2021automated` / GroupDRO++ domain relabeling, manual verification needed              | Creager et al. supports inferring environments when labels are hidden; JTT supports robustness without group labels; Thopalli-style domain relabeling is directly relevant but should be manually verified before final submission. ([ICML 2026][7])                                            |
| 2.4.2 Attack-as-domains perspective              | Treat each attack generator as an induced domain                                            | `wang2021generalizing`, `gulrajani2021domainbed`, `tramer2019multiple`  | Current Stage 1/Stage 2 report context                                                          | Wang et al. gives the DG taxonomy; DomainBed gives cautious DG benchmarking practice; Tramèr & Boneh motivates cross-perturbation generalization; your report provides the attack-domain formalization and source/evaluation attack design. ([ResearchGate][8])                                 |
| 2.5 Statistical Foundations                      | Paired tests, Wilcoxon signed-rank, effect size, confidence intervals, multi-seed reporting | `student1908probable`, `wilcoxon1945individual`, `cohen1988statistical` | `reimers2017reporting`, `bouthillier2021accounting`, `cumming2014new`                           | Student and Wilcoxon support paired parametric/nonparametric tests; Cohen supports standardized effect sizes; Reimers and Bouthillier support reporting score distributions and variance across random seeds; Cumming supports confidence intervals and estimation framing. ([OUP Academic][9]) |

---

## 2. Technical background notes

### 2.1 Preliminaries

#### 2.1.1 Deep Neural Networks and Classification

For Chapter 2, this subsection should be concise and notation-driven. Define the classifier (f_\theta:\mathcal{X}\rightarrow\mathbb{R}^K), logits (f_\theta(x)*k), the predicted label (\hat y=\arg\max_k f*\theta(x)*k), the softmax probability (p*\theta(y=k\mid x)), and the cross-entropy loss (\ell(f_\theta(x),y)=-\log p_\theta(y\mid x)). Then define empirical risk minimization as the clean baseline objective. This gives the reader the symbols needed for adversarial inner maximization and Group DRO later.

The important transition is that standard ERM only constrains average loss on clean samples. It does not require local stability of the classifier inside a neighborhood of each input. This local-stability gap is what adversarial robustness formalizes: a classifier should preserve its prediction under semantically label-preserving perturbations (x+\delta). This leads naturally to adversarial examples and norm-bounded threat models.

#### 2.1.2 Adversarial Examples

Adversarial examples are inputs (x_{\mathrm{adv}}=x+\delta) designed to cause model error while remaining close to the original input. Szegedy et al. first demonstrated that small, often imperceptible perturbations can reliably cause misclassification and can transfer across models, while Goodfellow et al. proposed a linearity-based explanation and the FGSM construction. Use these two papers as the primary historical and technical citations for the definition, not as a broad related-work discussion. ([OpenReview][1])

In the report’s notation, the adversary searches over a feasible perturbation set (\mathcal{S}_p(\varepsilon)={\delta:|\delta|*p\le \varepsilon}), often with clipping (x+\delta\in[0,1]^d) for normalized images. Untargeted attacks seek (\arg\max_k f*\theta(x+\delta)_k\ne y), while targeted attacks seek a specified target class (y_t\ne y). The label-preservation assumption should be stated carefully: the mathematical norm constraint is a proxy for preserving semantic label, not a proof that the label is unchanged.

#### 2.1.3 Threat Models

A threat model specifies the adversary’s knowledge, objective, perturbation geometry, and budget. In a **white-box** threat model, the adversary has access to model parameters and gradients, which is the setting used by FGSM, PGD, CW, DDN, DeepFool, and AutoAttack components. Madry et al.’s first-order adversary is the standard citation for this white-box robust-optimization view. ([ICLR][2])

A **graybox** or transfer setting separates the surrogate model used to generate adversarial examples from the target model used for evaluation. This is relevant because adversarial examples can transfer across models, as already observed by Szegedy et al. ([OpenReview][1]) In your report, graybox transfer is not merely an implementation detail: it measures whether robustness learned by one method changes the structure of adversarial vulnerability across models. Your current protocol explicitly evaluates surrogate–target transfer regimes over method families and seeds. 

A **black-box** setting restricts access to gradients and may allow only scores or decisions. It is useful in a background chapter mainly to explain why reliable evaluation cannot rely only on one gradient attack. Athalye et al. showed that gradient obfuscation can create a false sense of robustness, while AutoAttack was designed as a parameter-free ensemble to reduce evaluation fragility. ([Proceedings of Machine Learning Research][10])

---

### 2.2 Adversarial Training Deep Dive

#### 2.2.1 Min-max formulation

Adversarial training replaces the clean ERM objective with a robust risk objective. For each training example, an inner maximization constructs a high-loss perturbation, and the outer minimization updates model parameters to reduce the loss on these adversarial examples. The canonical formulation is
[
\min_\theta \mathbb{E}*{(x,y)\sim P*{XY}}
\left[
\max_{\delta\in\mathcal{S}*p(\varepsilon)}
\ell(f*\theta(x+\delta),y)
\right].
]
Madry et al. frame this as robust optimization against a first-order adversary, and this is the standard citation for PGD-based adversarial training. ([ICLR][2])

In practice, the exact inner maximization is nonconvex and is approximated by attack algorithms. Therefore, the training objective depends not only on the perturbation norm and budget but also on the attack procedure used to approximate the inner maximizer. This distinction is central to your thesis: different attacks can induce different adversarial training distributions even under similar budgets, motivating the attack-as-domain formulation.

#### 2.2.2 PGD-AT and its limitations

PGD adversarial training uses iterative projected gradient ascent to approximate the inner maximization, typically under an (\ell_\infty) threat model. It is a strong and widely used baseline because multi-step PGD is a stronger adversary than single-step FGSM and was proposed by Madry et al. as a universal first-order adversary for robust training. ([ICLR][2])

However, PGD-AT is not a complete solution. It is attack- and threat-model-specific: robustness against one norm, budget, loss, or optimizer does not guarantee robustness against other perturbation models. Tramèr and Boneh directly study robustness to multiple perturbation types and show that defenses tailored to a single perturbation model can fail against others. ([NIPS Papers][3]) In your report, this supports the claim that single-attack PGD-(\ell_\infty) training can become a specialist rather than a general multi-attack defense.

PGD-AT also has training dynamics limitations. Tsipras et al. and TRADES support the idea that robustness and standard accuracy can be in tension, while Rice et al. shows robust overfitting: robust test accuracy may degrade even as robust training accuracy improves. ([ICLR][11]) This supports a background discussion of clean–robust trade-offs, checkpoint selection, and why multi-seed validation matters.

#### 2.2.3 Multi-attack AT approaches

Multi-attack adversarial training expands the source adversarial distribution beyond a single attack. A simple baseline is uniform multi-attack ERM:
[
\min_\theta \frac{1}{|\mathcal{E}*{\mathrm{src}}|}
\sum*{e\in\mathcal{E}_{\mathrm{src}}} R_e(\theta),
]
where (R_e(\theta)) is the risk induced by attack generator (\mathcal{A}*e). In your report, this is **Multi-AT**, the uniform mixed-batch baseline over PGD-(\ell*\infty) and DDN-(\ell_2). 

The broader literature supports this design choice. Tramèr and Boneh analyze adversarial training against multiple perturbations, while Maini et al. formulate robustness against a union of perturbation models and propose multi-steepest descent to optimize the worst attack in the union. ([NIPS Papers][3]) These papers should be used in Chapter 2 to define the background problem of multi-attack robustness, leaving the detailed comparison to Chapter 3.

#### 2.2.4 Trade-off analysis

The background chapter should define the trade-off problem without turning it into a survey. Robust training may reduce clean accuracy, and improved robustness to one attack can come with reduced robustness to another attack. TRADES provides a useful formal lens by decomposing robust error into natural error and boundary error, motivating objectives that explicitly balance clean and robust performance. ([Proceedings of Machine Learning Research][4])

For your thesis, the key point is not only clean-vs-robust trade-off but also **cross-attack trade-off**. Training more strongly on one attack domain can reduce risk (R_e(\theta)) while leaving another attack-domain risk (R_{e'}(\theta)) high. This motivates reporting per-attack robust accuracy, Mean(8), norm-group averages, worst-attack accuracy, and graybox transfer metrics rather than relying on a single number.

---

### 2.3 Distributionally Robust Optimization

#### 2.3.1 Classical DRO formulation

Distributionally robust optimization minimizes worst-case risk over a set of distributions near the empirical distribution:
[
\min_\theta \sup_{Q\in\mathcal{U}(P_0)}
\mathbb{E}*{(x,y)\sim Q}[\ell(f*\theta(x),y)].
]
Namkoong and Duchi provide a classical formulation and stochastic optimization procedures for (f)-divergence uncertainty sets. Hashimoto et al. apply a related DRO idea to protect minority subpopulations without demographic labels, showing why DRO is relevant when average loss can hide high-risk subgroups. ([NIPS Papers][5])

In this report, the most important background interpretation is that adversarial examples create structured subpopulations of examples with different risks. These subpopulations may be known, such as attack identities in AttackDRO, or latent, such as cluster-discovered groups in Cluster-DRO and AttackDRO++.

#### 2.3.2 Group DRO

Group DRO assumes that each example belongs to a group (g\in{1,\ldots,G}), and it minimizes the maximum group risk:
[
\min_\theta \max_{g\in{1,\ldots,G}} R_g(\theta)
===============================================

\min_\theta \max_{q\in\Delta_G}
\sum_{g=1}^G q_g R_g(\theta).
]
Sagawa et al. is the essential citation: it studies group shifts, worst-group generalization, stochastic group reweighting, and the importance of regularization for overparameterized neural networks. ([OpenReview][6])

This is the direct background for **AttackDRO**, where groups are fixed source attack identities. It also motivates Cluster-DRO, where groups are discovered rather than fixed. Chapter 2 should present the general Group DRO machinery; Chapter 4 can then specialize it to attack identities, clusters, and the anchored GradFP variant.

#### 2.3.3 Exponentiated gradient on simplex

The group weights (q\in\Delta_G) are commonly updated using an exponentiated-gradient or entropic mirror-descent step:
[
q_g^{(t+1)}
===========

\frac{
q_g^{(t)}\exp(\eta_q \widehat{R}*g^{(t)})
}{
\sum*{h=1}^G q_h^{(t)}\exp(\eta_q \widehat{R}_h^{(t)})
}.
]
This update increases mass on high-loss groups while keeping (q) on the probability simplex. Sagawa et al. provides the Group DRO algorithmic context, and Beck & Teboulle provides the broader mirror-descent background for simplex-style updates. ([OpenReview][6])

For your implementation, it is also useful to mention practical stabilizers: warmup, (q)-flooring, and resetting (q) after cluster refreshes. These are method-specific choices in the current report rather than standard Group DRO definitions, so Chapter 2 should present them as implementation stabilizers and defer the final anchored formulation to Chapter 4. 

#### 2.3.4 Regularization in overparameterized models

A crucial Sagawa et al. finding is that Group DRO alone may not improve worst-group test accuracy in overparameterized neural networks unless it is paired with sufficient regularization or early stopping. This matters for your thesis because adaptive reweighting can over-focus on noisy or unstable groups, especially when groups are dynamically discovered. ([OpenReview][6])

This background supports your anchor mechanism conceptually: a uniform multi-attack component can act as a stabilizing signal, while the DRO component corrects hard groups. The Chapter 2 wording should avoid claiming that the anchor is a known Group DRO theorem. Instead, state that prior Group DRO results motivate careful regularization and stabilization; your AttackDRO++ anchor is introduced later as a method-specific stabilization strategy.

#### 2.3.5 DRO in adversarial training context

AttackDRO can be introduced as an application of Group DRO to adversarial training: each source attack (e\in\mathcal{E}_{\mathrm{src}}) defines a risk (R_e(\theta)), and the optimizer upweights the attack with higher current loss. This is mathematically natural because multi-attack adversarial training already decomposes risk by attack generator.

However, fixed attack identities may be too coarse. Two PGD examples can differ substantially in difficulty, class, margin, or gradient geometry; similarly, DDN examples may overlap with PGD examples in representation space. This motivates Cluster-DRO and ultimately AttackDRO++, where latent groups are discovered from adversarial examples rather than equated with attack identity.

---

### 2.4 Domain Generalization via Clustering

#### 2.4.1 Clustering-based domain discovery

Domain generalization studies how to learn from source domains so that performance transfers to unseen target domains. Wang et al. provide a useful taxonomy: data manipulation, representation learning, and learning strategy; DomainBed emphasizes that DG claims require careful evaluation and model selection. ([ResearchGate][8])

For clustering-based group discovery, the most stable primary background is hidden-environment inference rather than a single clustering paper. Creager et al.’s EIIL infers environments when environment labels are not available, and JTT shows that group robustness can be improved without explicit group annotations by identifying hard examples. ([ICML 2026][7]) These works justify the general idea that group labels need not be manually provided; they can be inferred from model behavior or learned representations.

A Thopalli-style “domain relabeling” or GroupDRO++ citation appears directly relevant to cluster-discovered domains, but the exact title/author/venue metadata should be manually verified before final thesis submission because search results show inconsistent titles. ([CatalyzeX][12]) Use it as Recommended or Optional unless you verify it from the paper PDF.

#### 2.4.2 Attack-as-domains perspective

The attack-as-domains perspective maps each attack generator (\mathcal{A}*e) to an induced adversarial distribution:
[
(x,y)\sim P*{XY}
\quad\mapsto\quad
(x^{\mathrm{adv}}_e,y),\qquad
x^{\mathrm{adv}}_e=\mathcal{A}*e(x,y,f*\theta).
]
The corresponding attack-domain risk is
[
R_e(\theta)
===========

\mathbb{E}*{(x,y)\sim P*{XY}}
\left[
\ell(f_\theta(\mathcal{A}*e(x,y,f*\theta)),y)
\right].
]
This formalism lets Chapter 2 connect adversarial robustness to DG without claiming that attacks are natural domains. They are **algorithm-induced domains**: distributions produced by different optimization procedures, perturbation norms, and loss functions.

This framing is already consistent with your report: Stage 1 identifies cross-attack robustness gaps and Stage 2 studies methods that reduce those gaps by training on PGD-(\ell_\infty) and DDN-(\ell_2) while evaluating on a broader attack suite.  The background citations should support the ingredients—DG, multi-perturbation robustness, and Group DRO—while the attacks-as-domains formulation remains your report’s conceptual bridge.

---

### 2.5 Statistical Foundations

For multi-seed reporting, define each seed as a paired experimental replicate whenever the same seeds are used for two methods. For methods (A) and (B), let (a_s) and (b_s) be the metric values under seed (s), and define paired differences (d_s=a_s-b_s). A paired (t)-test evaluates whether (\mathbb{E}[d_s]=0) under approximate normality of differences, while the Wilcoxon signed-rank test is a nonparametric alternative based on signed ranks. Student’s (t)-test and Wilcoxon’s signed-rank test are the classical citations. ([OUP Academic][9])

Report p-values together with effect sizes and confidence intervals. A p-value is evidence against a null hypothesis, not the magnitude of improvement. Cohen’s (d_z=\bar d/s_d) or the raw mean improvement (\bar d) in percentage points is often more interpretable for robust accuracy. Cohen is the standard effect-size reference, and Cumming supports the estimation/CI framing. ([Open Library][13])

Do not state that five seeds are a universal “minimum standard” in adversarial training. A safer thesis statement is: **this report uses five seeds as a pragmatic minimum for paired multi-seed reporting under compute constraints**. Reimers & Gurevych and Bouthillier et al. support the broader principle that single-run results can be misleading and that reporting score distributions or variance across runs is important. ([ACL Anthology][14])

---

### 2.6 Chapter Summary

Chapter 2 should end by connecting the definitions: ERM trains on clean average risk; adversarial examples expose local instability; PGD-AT approximates robust optimization for a specific threat model; multi-attack AT expands the adversarial source distribution; Group DRO reweights high-risk groups; clustering and hidden-group inference motivate replacing fixed attack identities with discovered groups; and statistical testing provides the reporting discipline needed for multi-seed comparisons. This prepares Chapter 4 to introduce Multi-AT, AttackDRO, Cluster-DRO, and AttackDRO++ without re-explaining the background machinery.

---

## 3. Equations to include

| Equation                                       | LaTeX                                                                                                                                                                               | Where it belongs                                       | Citation support                                                                          |       |                                                                                                 |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------- |
| Supervised ERM                                 | (\displaystyle \hat R_{\mathrm{clean}}(\theta)=\frac{1}{n}\sum_{i=1}^n \ell(f_\theta(x_i),y_i),\qquad \hat\theta_{\mathrm{ERM}}\in\arg\min_\theta \hat R_{\mathrm{clean}}(\theta).) | 2.1.1                                                  | Standard supervised learning notation.                                                    |       |                                                                                                 |
| Softmax and cross-entropy                      | (\displaystyle p_\theta(y=k\mid x)=\frac{\exp(f_\theta(x)*k)}{\sum*{j=1}^K\exp(f_\theta(x)*j)},\qquad \ell(f*\theta(x),y)=-\log p_\theta(y\mid x).)                                 | 2.1.1                                                  | Standard classification notation.                                                         |       |                                                                                                 |
| Adversarial example                            | (\displaystyle x_{\mathrm{adv}}=x+\delta,\qquad \arg\max_k f_\theta(x_{\mathrm{adv}})_k\ne y.)                                                                                      | 2.1.2                                                  | Szegedy et al.; Goodfellow et al. ([OpenReview][1])                                       |       |                                                                                                 |
| Targeted adversarial example                   | (\displaystyle \arg\max_k f_\theta(x_{\mathrm{adv}})_k = y_t,\qquad y_t\ne y.)                                                                                                      | 2.1.2 or 2.1.3                                         | CW and PGD variants; use only if targeted attacks are discussed. ([IEEE TCSP][15])        |       |                                                                                                 |
| Perturbation set                               | (\displaystyle \mathcal{S}_p(\varepsilon)={\delta\in\mathbb{R}^d:|\delta|_p\le\varepsilon},\qquad x+\delta\in[0,1]^d.)                                                              | 2.1.3                                                  | Standard threat-model notation; Madry et al. for robust optimization. ([ICLR][2])         |       |                                                                                                 |
| Inner maximization                             | (\displaystyle \delta^\star(x,y;\theta)\in\arg\max_{\delta\in\mathcal{S}*p(\varepsilon)} \ell(f*\theta(x+\delta),y).)                                                               | 2.2.1                                                  | Goodfellow et al.; Madry et al. ([Google Nghiên Cứu][16])                                 |       |                                                                                                 |
| PGD-(\ell_\infty) update                       | (\displaystyle \delta^{t+1}=\Pi_{\mathcal{S}*\infty(\varepsilon)}\left(\delta^t+\alpha,\mathrm{sign}\left(\nabla_x\ell(f*\theta(x+\delta^t),y)\right)\right).)                      | 2.2.2                                                  | Madry et al. ([ICLR][2])                                                                  |       |                                                                                                 |
| PGD-(\ell_2) update                            | (\displaystyle \delta^{t+1}=\Pi_{\mathcal{S}_2(\varepsilon)}\left(\delta^t+\alpha,\frac{g^t}{|g^t|*2+\tau}\right),\quad g^t=\nabla_x\ell(f*\theta(x+\delta^t),y).)                  | 2.2.2 / attack summary                                 | Madry et al.; implementation detail can be stated as normalized-gradient PGD. ([ICLR][2]) |       |                                                                                                 |
| Adversarial training min-max                   | (\displaystyle \min_\theta \mathbb{E}*{(x,y)\sim P*{XY}}\left[\max_{\delta\in\mathcal{S}*p(\varepsilon)} \ell(f*\theta(x+\delta),y)\right].)                                        | 2.2.1                                                  | Madry et al. ([ICLR][2])                                                                  |       |                                                                                                 |
| Attack-domain risk                             | (\displaystyle R_e(\theta)=\mathbb{E}*{(x,y)\sim P*{XY}}\left[\ell(f_\theta(\mathcal{A}*e(x,y,f*\theta)),y)\right].)                                                                | 2.2.3 or 2.4.2                                         | Your report formulation; multi-attack robustness literature.  ([NIPS Papers][3])          |       |                                                                                                 |
| Uniform Multi-AT                               | (\displaystyle \min_\theta \frac{1}{                                                                                                                                                | \mathcal{E}_{\mathrm{src}}                             | }\sum_{e\in\mathcal{E}_{\mathrm{src}}} R_e(\theta).)                                      | 2.2.3 | Use to define Multi-AT background; your source attacks are PGD-(\ell_\infty) and DDN-(\ell_2).  |
| Group DRO objective                            | (\displaystyle \min_\theta \max_{q\in\Delta_G}\sum_{g=1}^G q_g R_g(\theta)=\min_\theta\max_g R_g(\theta).)                                                                          | 2.3.2                                                  | Sagawa et al. ([OpenReview][6])                                                           |       |                                                                                                 |
| Exponentiated-gradient (q) update              | (\displaystyle q_g^{t+1}=\frac{q_g^t\exp(\eta_q \widehat R_g^t)}{\sum_{h=1}^G q_h^t\exp(\eta_q \widehat R_h^t)}.)                                                                   | 2.3.3                                                  | Sagawa et al.; mirror descent. ([OpenReview][6])                                          |       |                                                                                                 |
| Optional (q)-floor projection                  | (\displaystyle q^{t+1}\leftarrow \Pi_{\Delta_G\cap{q_g\ge q_{\min}}}\left(q^{t+1}\right).)                                                                                          | 2.3.3 as practical stabilization; Chapter 4 for method | This is your implementation stabilization, not a standard theorem.                        |       |                                                                                                 |
| Paired differences                             | (\displaystyle d_s=m_{A,s}-m_{B,s},\qquad \bar d=\frac{1}{S}\sum_{s=1}^S d_s.)                                                                                                      | 2.5                                                    | Paired multi-seed comparison.                                                             |       |                                                                                                 |
| Paired (t)-statistic                           | (\displaystyle t=\frac{\bar d}{s_d/\sqrt{S}},\qquad s_d^2=\frac{1}{S-1}\sum_{s=1}^S(d_s-\bar d)^2.)                                                                                 | 2.5                                                    | Student’s (t)-test. ([OUP Academic][9])                                                   |       |                                                                                                 |
| Confidence interval for mean paired difference | (\displaystyle \bar d \pm t_{S-1,1-\alpha/2}\frac{s_d}{\sqrt{S}}.)                                                                                                                  | 2.5                                                    | Student; Cumming for estimation framing. ([OUP Academic][9])                              |       |                                                                                                 |
| Paired standardized effect size                | (\displaystyle d_z=\frac{\bar d}{s_d}.)                                                                                                                                             | 2.5                                                    | Cohen. ([Open Library][13])                                                               |       |                                                                                                 |

---

## 4. Attack summary

Current report alignment: **training attacks** are PGD-(\ell_\infty) and DDN-(\ell_2); the main evaluation suite includes FGSM-RS, PGD-(\ell_\infty), TPGD, MI-FGSM, PGD-(\ell_2), DDN-(\ell_2), DeepFool-(\ell_2), and CW-(\ell_2); AutoAttack-(\ell_\infty) is a separate stress/sanity evaluation rather than part of Mean(8).  

| Attack                   | Full name                                             | Norm / threat model                                 | Main idea                                                                                                                                                      | Used for training in this report? | Used for evaluation in this report? | Primary citation                                                           |
| ------------------------ | ----------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------: | ----------------------------------: | -------------------------------------------------------------------------- |
| FGSM-RS                  | Fast Gradient Sign Method with Random Start           | (\ell_\infty), white-box                            | Start from a random point in the (\ell_\infty) ball, then take one FGSM sign-gradient step. Useful as a fast baseline and for reducing single-step degeneracy. |                                No |                                 Yes | `goodfellow2015explaining`, `tramer2018ensemble` ([Google Nghiên Cứu][16]) |
| PGD-(\ell_\infty)        | Projected Gradient Descent under (\ell_\infty) budget | (\ell_\infty), white-box                            | Iterative gradient ascent on loss with projection back to (\mathcal{S}_\infty(\varepsilon)). Standard first-order adversary.                                   |                               Yes |                                 Yes | `madry2018towards` ([ICLR][2])                                             |
| PGD-(\ell_2)             | Projected Gradient Descent under (\ell_2) budget      | (\ell_2), white-box                                 | Iterative normalized-gradient ascent with projection to the (\ell_2) ball.                                                                                     |                                No |                                 Yes | `madry2018towards` ([ICLR][2])                                             |
| CW-(\ell_2)              | Carlini–Wagner (\ell_2) attack                        | (\ell_2), white-box optimization attack             | Optimizes a margin-style misclassification objective plus (\ell_2) distortion penalty, often with a box constraint transformation.                             |                                No |                                 Yes | `carlini2017towards` ([IEEE TCSP][15])                                     |
| DeepFool-(\ell_2)        | DeepFool                                              | (\ell_2), white-box boundary attack                 | Iteratively linearizes the classifier and moves toward the closest estimated decision boundary to find small perturbations.                                    |                                No |                                 Yes | `moosavi2016deepfool` ([CVF Open Access][17])                              |
| DDN-(\ell_2)             | Decoupled Direction and Norm                          | (\ell_2), white-box                                 | Separates direction search from perturbation-norm adjustment, dynamically shrinking or expanding the norm while following adversarial directions.              |                               Yes |                                 Yes | `rony2019decoupling` ([CVF Open Access][18])                               |
| MI-FGSM                  | Momentum Iterative Fast Gradient Sign Method          | Usually (\ell_\infty), white-box/transfer           | Accumulates normalized gradients with momentum to stabilize update directions and improve transferability.                                                     |                                No |                                 Yes | `dong2018boosting` ([CVF Open Access][19])                                 |
| TPGD                     | TRADES-style PGD / KL-PGD                             | (\ell_\infty), white-box                            | Uses PGD-style perturbation search with KL divergence between clean and adversarial predictions, as in TRADES-style robustness training/evaluation.            |                                No |                                 Yes | `zhang2019trades` ([Proceedings of Machine Learning Research][4])          |
| AutoAttack-(\ell_\infty) | AutoAttack ensemble                                   | (\ell_\infty), white-box plus score-based component | Parameter-free ensemble including strong adaptive attacks designed to reduce unreliable robustness estimates.                                                  |                                No |           Yes, separate stress test | `croce2020reliable` ([Proceedings of Machine Learning Research][20])       |

---

## 5. BibTeX entries

```bibtex
@inproceedings{szegedy2014intriguing,
  title        = {Intriguing Properties of Neural Networks},
  author       = {Szegedy, Christian and Zaremba, Wojciech and Sutskever, Ilya and Bruna, Joan and Erhan, Dumitru and Goodfellow, Ian and Fergus, Rob},
  booktitle    = {International Conference on Learning Representations},
  year         = {2014},
  url          = {https://openreview.net/forum?id=kklr_MTHMRQjG}
}

@inproceedings{goodfellow2015explaining,
  title        = {Explaining and Harnessing Adversarial Examples},
  author       = {Goodfellow, Ian J. and Shlens, Jonathon and Szegedy, Christian},
  booktitle    = {International Conference on Learning Representations},
  year         = {2015},
  url          = {https://arxiv.org/abs/1412.6572}
}

@inproceedings{tramer2018ensemble,
  title        = {Ensemble Adversarial Training: Attacks and Defenses},
  author       = {Tram{\`e}r, Florian and Kurakin, Alexey and Papernot, Nicolas and Goodfellow, Ian and Boneh, Dan and McDaniel, Patrick},
  booktitle    = {International Conference on Learning Representations},
  year         = {2018},
  url          = {https://openreview.net/forum?id=rkZvSe-RZ}
}

@inproceedings{madry2018towards,
  title        = {Towards Deep Learning Models Resistant to Adversarial Attacks},
  author       = {Madry, Aleksander and Makelov, Aleksandar and Schmidt, Ludwig and Tsipras, Dimitris and Vladu, Adrian},
  booktitle    = {International Conference on Learning Representations},
  year         = {2018},
  url          = {https://openreview.net/forum?id=rJzIBfZAb}
}

@inproceedings{carlini2017towards,
  title        = {Towards Evaluating the Robustness of Neural Networks},
  author       = {Carlini, Nicholas and Wagner, David},
  booktitle    = {2017 IEEE Symposium on Security and Privacy (SP)},
  pages        = {39--57},
  year         = {2017},
  publisher    = {IEEE},
  doi          = {10.1109/SP.2017.49}
}

@inproceedings{moosavi2016deepfool,
  title        = {DeepFool: A Simple and Accurate Method to Fool Deep Neural Networks},
  author       = {Moosavi-Dezfooli, Seyed-Mohsen and Fawzi, Alhussein and Frossard, Pascal},
  booktitle    = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages        = {2574--2582},
  year         = {2016},
  doi          = {10.1109/CVPR.2016.282}
}

@inproceedings{rony2019decoupling,
  title        = {Decoupling Direction and Norm for Efficient Gradient-Based L2 Adversarial Attacks and Defenses},
  author       = {Rony, J{\'e}r{\^o}me and Hafemann, Luiz G. and Oliveira, Luiz S. and Ayed, Ismail Ben and Sabourin, Robert and Granger, Eric},
  booktitle    = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages        = {4322--4330},
  year         = {2019},
  doi          = {10.1109/CVPR.2019.00445}
}

@inproceedings{dong2018boosting,
  title        = {Boosting Adversarial Attacks with Momentum},
  author       = {Dong, Yinpeng and Liao, Fangzhou and Pang, Tianyu and Su, Hang and Zhu, Jun and Hu, Xiaolin and Li, Jianguo},
  booktitle    = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages        = {9185--9193},
  year         = {2018}
}

@inproceedings{zhang2019trades,
  title        = {Theoretically Principled Trade-off between Robustness and Accuracy},
  author       = {Zhang, Hongyang and Yu, Yaodong and Jiao, Jiantao and Xing, Eric P. and El Ghaoui, Laurent and Jordan, Michael I.},
  booktitle    = {Proceedings of the 36th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {97},
  pages        = {7472--7482},
  year         = {2019},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v97/zhang19p.html}
}

@inproceedings{croce2020reliable,
  title        = {Reliable Evaluation of Adversarial Robustness with an Ensemble of Diverse Parameter-free Attacks},
  author       = {Croce, Francesco and Hein, Matthias},
  booktitle    = {Proceedings of the 37th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {119},
  pages        = {2206--2216},
  year         = {2020},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v119/croce20b.html}
}

@inproceedings{athalye2018obfuscated,
  title        = {Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples},
  author       = {Athalye, Anish and Carlini, Nicholas and Wagner, David},
  booktitle    = {Proceedings of the 35th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {80},
  pages        = {274--283},
  year         = {2018},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v80/athalye18a.html}
}

@inproceedings{rice2020overfitting,
  title        = {Overfitting in Adversarially Robust Deep Learning},
  author       = {Rice, Leslie and Wong, Eric and Kolter, J. Zico},
  booktitle    = {Proceedings of the 37th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {119},
  pages        = {8093--8104},
  year         = {2020},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v119/rice20a.html}
}

@inproceedings{tsipras2019robustness,
  title        = {Robustness May Be at Odds with Accuracy},
  author       = {Tsipras, Dimitris and Santurkar, Shibani and Engstrom, Logan and Turner, Alexander and Madry, Aleksander},
  booktitle    = {International Conference on Learning Representations},
  year         = {2019},
  url          = {https://openreview.net/forum?id=SyxAb30cY7}
}

@inproceedings{tramer2019multiple,
  title        = {Adversarial Training and Robustness for Multiple Perturbations},
  author       = {Tram{\`e}r, Florian and Boneh, Dan},
  booktitle    = {Advances in Neural Information Processing Systems},
  volume       = {32},
  year         = {2019},
  url          = {https://papers.nips.cc/paper/8821-adversarial-training-and-robustness-for-multiple-perturbations}
}

@inproceedings{maini2020union,
  title        = {Adversarial Robustness against the Union of Multiple Perturbation Models},
  author       = {Maini, Pratyush and Wong, Eric and Kolter, J. Zico},
  booktitle    = {Proceedings of the 37th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {119},
  pages        = {6640--6650},
  year         = {2020},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v119/maini20a.html}
}

@inproceedings{madaan2021learning,
  title        = {Learning to Generate Noise for Multi-Attack Robustness},
  author       = {Madaan, Divyam and Shin, Jinwoo and Hwang, Sung Ju},
  booktitle    = {Proceedings of the 38th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {139},
  pages        = {7279--7289},
  year         = {2021},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v139/madaan21a.html}
}

@inproceedings{laidlaw2021perceptual,
  title        = {Perceptual Adversarial Robustness: Defense Against Unseen Threat Models},
  author       = {Laidlaw, Cassidy and Singla, Sahil and Feizi, Soheil},
  booktitle    = {International Conference on Learning Representations},
  year         = {2021},
  url          = {https://openreview.net/forum?id=dFwBosAcJkN}
}

@inproceedings{namkoong2016stochastic,
  title        = {Stochastic Gradient Methods for Distributionally Robust Optimization with f-divergences},
  author       = {Namkoong, Hongseok and Duchi, John C.},
  booktitle    = {Advances in Neural Information Processing Systems},
  volume       = {29},
  pages        = {2208--2216},
  year         = {2016},
  url          = {https://papers.nips.cc/paper/2016/hash/4588e674d3f0faf985047d4c3f13ed0d-Abstract.html}
}

@inproceedings{hashimoto2018fairness,
  title        = {Fairness Without Demographics in Repeated Loss Minimization},
  author       = {Hashimoto, Tatsunori B. and Srivastava, Megha and Namkoong, Hongseok and Liang, Percy},
  booktitle    = {Proceedings of the 35th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {80},
  pages        = {1929--1938},
  year         = {2018},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v80/hashimoto18a.html}
}

@inproceedings{sagawa2020groupdro,
  title        = {Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization},
  author       = {Sagawa, Shiori and Koh, Pang Wei and Hashimoto, Tatsunori B. and Liang, Percy},
  booktitle    = {International Conference on Learning Representations},
  year         = {2020},
  url          = {https://openreview.net/forum?id=ryxGuJrFvS}
}

@article{beck2003mirror,
  title        = {Mirror Descent and Nonlinear Projected Subgradient Methods for Convex Optimization},
  author       = {Beck, Amir and Teboulle, Marc},
  journal      = {Operations Research Letters},
  volume       = {31},
  number       = {3},
  pages        = {167--175},
  year         = {2003},
  doi          = {10.1016/S0167-6377(02)00231-6}
}

@article{kivinen1997exponentiated,
  title        = {Exponentiated Gradient versus Gradient Descent for Linear Predictors},
  author       = {Kivinen, Jyrki and Warmuth, Manfred K.},
  journal      = {Information and Computation},
  volume       = {132},
  number       = {1},
  pages        = {1--63},
  year         = {1997},
  doi          = {10.1006/inco.1996.2612}
}

@inproceedings{wang2021generalizing,
  title        = {Generalizing to Unseen Domains: A Survey on Domain Generalization},
  author       = {Wang, Jindong and Lan, Cuiling and Liu, Chang and Ouyang, Yidong and Qin, Tao},
  booktitle    = {Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence},
  pages        = {4627--4635},
  year         = {2021},
  doi          = {10.24963/ijcai.2021/628}
}

@inproceedings{gulrajani2021domainbed,
  title        = {In Search of Lost Domain Generalization},
  author       = {Gulrajani, Ishaan and Lopez-Paz, David},
  booktitle    = {International Conference on Learning Representations},
  year         = {2021},
  url          = {https://openreview.net/forum?id=lQdXeXDoWtI}
}

@inproceedings{creager2021environment,
  title        = {Environment Inference for Invariant Learning},
  author       = {Creager, Elliot and Jacobsen, J{\"o}rn-Henrik and Zemel, Richard},
  booktitle    = {Proceedings of the 38th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {139},
  pages        = {2189--2200},
  year         = {2021},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v139/creager21a.html}
}

@inproceedings{liu2021just,
  title        = {Just Train Twice: Improving Group Robustness without Training Group Information},
  author       = {Liu, Evan Z. and Haghgoo, Behzad and Chen, Annie S. and Raghunathan, Aditi and Koh, Pang Wei and Sagawa, Shiori and Liang, Percy and Finn, Chelsea},
  booktitle    = {Proceedings of the 38th International Conference on Machine Learning},
  series       = {Proceedings of Machine Learning Research},
  volume       = {139},
  pages        = {6781--6792},
  year         = {2021},
  publisher    = {PMLR},
  url          = {https://proceedings.mlr.press/v139/liu21f.html}
}

@misc{thopalli2021automated,
  title        = {Automated Domain Discovery from Multiple Sources to Improve Zero-Shot Generalization},
  author       = {Thopalli, Kowshik and Katoch, Sameeksha and Turaga, Pavan and Thiagarajan, Jayaraman J.},
  year         = {2021},
  eprint       = {2112.09802},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url          = {https://arxiv.org/abs/2112.09802},
  note         = {Manually verify title, author list, and venue before final submission.}
}

@article{student1908probable,
  title        = {The Probable Error of a Mean},
  author       = {Student},
  journal      = {Biometrika},
  volume       = {6},
  number       = {1},
  pages        = {1--25},
  year         = {1908},
  doi          = {10.1093/biomet/6.1.1}
}

@article{wilcoxon1945individual,
  title        = {Individual Comparisons by Ranking Methods},
  author       = {Wilcoxon, Frank},
  journal      = {Biometrics Bulletin},
  volume       = {1},
  number       = {6},
  pages        = {80--83},
  year         = {1945},
  doi          = {10.2307/3001968}
}

@book{cohen1988statistical,
  title        = {Statistical Power Analysis for the Behavioral Sciences},
  author       = {Cohen, Jacob},
  edition      = {2},
  publisher    = {Lawrence Erlbaum Associates},
  address      = {Hillsdale, NJ},
  year         = {1988}
}

@article{cumming2014new,
  title        = {The New Statistics: Why and How},
  author       = {Cumming, Geoff},
  journal      = {Psychological Science},
  volume       = {25},
  number       = {1},
  pages        = {7--29},
  year         = {2014},
  doi          = {10.1177/0956797613504966}
}

@inproceedings{reimers2017reporting,
  title        = {Reporting Score Distributions Makes a Difference: Performance Study of LSTM-networks for Sequence Tagging},
  author       = {Reimers, Nils and Gurevych, Iryna},
  booktitle    = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  pages        = {338--348},
  year         = {2017},
  doi          = {10.18653/v1/D17-1035},
  url          = {https://aclanthology.org/D17-1035/}
}

@article{bouthillier2021accounting,
  title        = {Accounting for Variance in Machine Learning Benchmarks},
  author       = {Bouthillier, Xavier and Delaunay, Pierre and Bronzi, Mirko and Trofimov, Alexandre and Nichyporuk, Brennan and Szeto, Justin and Sepah, Nafise and Raff, Edward and Madan, Kanika and Voleti, Vikram and Ebrahimi Kahou, Samira and Michalski, Vincent and Serdyuk, Dmitriy and Arbel, Tal and Pal, Christopher and Varoquaux, Ga{\"e}l and Vincent, Pascal},
  journal      = {Proceedings of Machine Learning and Systems},
  volume       = {3},
  year         = {2021},
  url          = {https://proceedings.mlsys.org/paper/2021/hash/cfecdb276f634854f3ef915e2e980c31-Abstract.html}
}

@inproceedings{henderson2018deep,
  title        = {Deep Reinforcement Learning That Matters},
  author       = {Henderson, Peter and Islam, Riashat and Bachman, Philip and Pineau, Joelle and Precup, Doina and Meger, David},
  booktitle    = {Proceedings of the AAAI Conference on Artificial Intelligence},
  year         = {2018},
  url          = {https://ojs.aaai.org/index.php/AAAI/article/view/11694}
}
```

---

## 6. Risks and uncertainty

1. **Thopalli / GroupDRO++ citation needs manual verification.** Search results show inconsistent metadata: one title appears as *Automated Domain Discovery from Multiple Sources to Improve Zero-Shot Generalization*, while another appears as *Improving Multi-Domain Generalization through Domain Re-labeling*. The author list also varies across sources. Use it as Recommended/Optional until verified from the PDF or official proceedings. ([CatalyzeX][12])

2. **TPGD naming is ambiguous.** In some contexts, “targeted PGD” means PGD toward a target label. In TorchAttacks-style usage, `TPGD` often refers to TRADES-style PGD using KL divergence between clean and adversarial predictions. In your report, call it **TRADES-style PGD / KL-PGD** unless your code truly uses target-label PGD.

3. **FGSM-RS should cite two ideas.** FGSM itself is Goodfellow et al.; the random-start/R+FGSM idea is better supported by Tramèr et al. or fast adversarial training papers. Do not cite Goodfellow alone for FGSM-RS.

4. **“Five seeds is the minimum standard” should be softened.** A defensible statement is: five seeds are a pragmatic minimum in this report for paired comparisons under compute constraints. It is not a universal statistical guarantee, and tests with (n=5) remain low-powered.

5. **AutoAttack-512 should not be overclaimed.** Your current report notes that AutoAttack evaluated on 512 samples should be treated as a sanity/stress metric rather than the primary ranking metric. Keep Mean(8) as the main aggregate unless full AutoAttack is available for all methods/seeds. 

6. **AttackDRO++ naming must remain strict.** In Chapter 2 and Chapter 4, reserve **AttackDRO++** for the final uniform-anchored Cluster-DRO with gradient fingerprints. Use **Cluster-DRO** for the cluster-only intermediate baseline and **AttackDRO** for fixed attack-identity Group DRO.

[1]: https://openreview.net/forum?id=kklr_MTHMRQjG "https://openreview.net/forum?id=kklr_MTHMRQjG"
[2]: https://iclr.cc/virtual/2018/poster/67 "https://iclr.cc/virtual/2018/poster/67"
[3]: https://papers.nips.cc/paper/8821-adversarial-training-and-robustness-for-multiple-perturbations "https://papers.nips.cc/paper/8821-adversarial-training-and-robustness-for-multiple-perturbations"
[4]: https://proceedings.mlr.press/v97/zhang19p.html "https://proceedings.mlr.press/v97/zhang19p.html"
[5]: https://papers.nips.cc/paper/6040-stochastic-gradient-methods-for-distributionally-robust-optimization-with-f-divergences "https://papers.nips.cc/paper/6040-stochastic-gradient-methods-for-distributionally-robust-optimization-with-f-divergences"
[6]: https://openreview.net/forum?id=ryxGuJrFvS "https://openreview.net/forum?id=ryxGuJrFvS"
[7]: https://icml.cc/virtual/2021/spotlight/10604 "https://icml.cc/virtual/2021/spotlight/10604"
[8]: https://www.researchgate.net/publication/353836244_Generalizing_to_Unseen_Domains_A_Survey_on_Domain_Generalization "https://www.researchgate.net/publication/353836244_Generalizing_to_Unseen_Domains_A_Survey_on_Domain_Generalization"
[9]: https://academic.oup.com/biomet/article/6/1/1/225634 "https://academic.oup.com/biomet/article/6/1/1/225634"
[10]: https://proceedings.mlr.press/v80/athalye18a "https://proceedings.mlr.press/v80/athalye18a"
[11]: https://iclr.cc/virtual/2019/poster/1032 "https://iclr.cc/virtual/2019/poster/1032"
[12]: https://www.catalyzex.com/paper/improving-multi-domain-generalization-through "https://www.catalyzex.com/paper/improving-multi-domain-generalization-through"
[13]: https://openlibrary.org/works/OL4623796W/Statistical_power_analysis_for_the_behavioral_sciences "https://openlibrary.org/works/OL4623796W/Statistical_power_analysis_for_the_behavioral_sciences"
[14]: https://aclanthology.org/D17-1035/ "https://aclanthology.org/D17-1035/"
[15]: https://www.ieee-security.org/TC/SP2017/papers/518.pdf "https://www.ieee-security.org/TC/SP2017/papers/518.pdf"
[16]: https://research.google/pubs/explaining-and-harnessing-adversarial-examples/ "https://research.google/pubs/explaining-and-harnessing-adversarial-examples/"
[17]: https://openaccess.thecvf.com/content_cvpr_2016/html/Moosavi-Dezfooli_DeepFool_A_Simple_CVPR_2016_paper.html "https://openaccess.thecvf.com/content_cvpr_2016/html/Moosavi-Dezfooli_DeepFool_A_Simple_CVPR_2016_paper.html"
[18]: https://openaccess.thecvf.com/content_CVPR_2019/html/Rony_Decoupling_Direction_and_Norm_for_Efficient_Gradient-Based_L2_Adversarial_Attacks_CVPR_2019_paper.html "https://openaccess.thecvf.com/content_CVPR_2019/html/Rony_Decoupling_Direction_and_Norm_for_Efficient_Gradient-Based_L2_Adversarial_Attacks_CVPR_2019_paper.html"
[19]: https://openaccess.thecvf.com/content_cvpr_2018/html/Dong_Boosting_Adversarial_Attacks_CVPR_2018_paper.html "https://openaccess.thecvf.com/content_cvpr_2018/html/Dong_Boosting_Adversarial_Attacks_CVPR_2018_paper.html"
[20]: https://proceedings.mlr.press/v119/croce20b.html "https://proceedings.mlr.press/v119/croce20b.html"

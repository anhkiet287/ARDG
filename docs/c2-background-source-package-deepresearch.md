# Chapter 2 Background Source Package

## Citation map

The table below maps the current Chapter 2 structure to high-confidence primary sources and a small number of framing references. I prioritized official proceedings pages, publisher pages, and canonical arXiv or dblp records when a final proceedings page was not readily available. citeturn3search2turn3search8turn4search1turn4search5turn5search0turn6search1turn6search2turn6search5turn7search3turn10search0turn10search8turn11search1turn18search0turn22search5turn25search0turn26search24turn29search0turn30search0turn31search1turn32search1

| Chapter 2 subsection | Concept | Essential citations | Recommended citations | What each citation supports |
|---|---|---|---|---|
| 2.1.1 | Deep neural networks and supervised classification | `goodfellow2016deep` | Recommended: none. Optional: `wang2021generalizing` for DG terminology touching ERM | Goodfellow et al. provides standard notation for deep networks, logits, softmax, cross-entropy, and ERM-oriented supervised learning background. citeturn28search0 |
| 2.1.2 | Adversarial examples | `szegedy2014intriguing`, `goodfellow2015explaining` | Recommended: `madry2018towards` | Szegedy et al. established the modern adversarial-example phenomenon and transferability; Goodfellow et al. introduced FGSM and the linearity-based explanation; Madry et al. reframed robustness through robust optimization. citeturn19search0turn5search0turn3search8 |
| 2.1.3 | Threat models | `madry2018towards`, `carlini2017towards` | Recommended: `croce2020reliable`; Optional: `kurakin2017adversarial` | Madry et al. formalize norm-bounded first-order threat models; Carlini and Wagner emphasize strong-attack evaluation; Croce and Hein show why robust evaluation must be attack-diverse and parameter-insensitive. citeturn3search8turn22search5turn3search2 |
| 2.2.1–2.2.2 | Min-max adversarial training and PGD-AT | `madry2018towards` | Recommended: `kurakin2017adversarial`, `tramer2018ensemble`, `wong2020fast` | Madry et al. give the canonical min-max formulation and PGD training view; Kurakin et al. discuss scaling AT and label leaking; Tramèr et al. analyze degenerate single-step behavior; Rice et al. show FGSM with random start can work but also motivate care around fast adversaries. citeturn3search8turn23search0turn6search1turn6search2 |
| 2.2.3–2.2.4 | Multi-attack AT and trade-offs across perturbation models | `tramer2019adversarial`, `maini2020adversarial`, `zhang2019theoretically` | Recommended: `kang2019transfer` | Tramèr and Boneh show robustness trade-offs across perturbation types and difficulties in composing defenses; Maini et al. propose a union-of-threat-model optimization view; Zhang et al. formalize the robustness-accuracy trade-off via TRADES; Kang et al. provide additional empirical evidence that robustness does not transfer uniformly across perturbation families. citeturn7search3turn25search0turn32search1turn21search0 |
| 2.3.1 | Classical DRO formulation | `sinha2018certifiable`, `duchi2021learning` | Recommended: none | Sinha et al. connect adversarial robustness to Wasserstein-style distributional robustness; Duchi and Namkoong give a clean distributionally robust objective for uniform performance under distributional shift. citeturn34search2turn26search24 |
| 2.3.2–2.3.4 | Group DRO, exponentiated-gradient updates, and regularization | `sagawa2019distributionally`, `kivinen1997exponentiated` | Recommended: `liu2021just`; Optional: `sohoni2020no` | Sagawa et al. provide the group DRO objective, the practical online minimax optimizer, and the key observation that regularization matters in overparameterized models; Kivinen and Warmuth give the canonical exponentiated-gradient update; Liu et al. and Sohoni et al. help motivate what happens when group labels are absent or noisy. citeturn33search5turn18search0turn30search0turn31search1 |
| 2.3.5 | DRO in the adversarial-training context | `sinha2018certifiable`, `madry2018towards`, `sagawa2019distributionally` | Recommended: `duchi2021learning` | The background chapter can safely connect adversarial inner maximization to distributional worst-case risk and then narrow from ambiguity-set DRO to finite-group worst-case objectives. citeturn34search2turn3search8turn33search5turn26search24 |
| 2.4.1 | Clustering-based domain discovery and hidden groups | `sohoni2020no`, `creager2021environment`, `liu2021just` | Recommended: `oakdenrayner2020hidden` | Sohoni et al. show clustering learned representations can recover latent subclasses for worst-group optimization; Creager et al. infer environments for invariant learning when labels are absent; Liu et al. use error-based discovery; Oakden-Rayner et al. motivate hidden stratification as a real failure mode. citeturn31search1turn29search0turn30search0turn11search1 |
| 2.4.2 | Domain generalization and the attack-as-domains lens | `arjovsky2019invariant`, `gulrajani2021search` | Recommended: `wang2021generalizing`; Optional: `kang2019transfer`, `tramer2019adversarial` | IRM gives the environment-invariance language; DomainBed clarifies the standard DG setting and the importance of model selection; the DG survey supplies broad terminology; adversarial multi-perturbation papers justify why “attack-induced domain shift” is a useful but specialized analogy rather than a claim of general DG. citeturn27search8turn10search8turn10search0turn21search0turn7search3 |
| 2.5 | Statistical foundations for multi-seed reporting | `student1908probable`, `wilcoxon1945individual`, `cohen1988statistical`, `cumming2014new` | Recommended: none | Student supports the paired-difference t framework; Wilcoxon supports the signed-rank alternative; Cohen supports effect-size reporting; Cumming supports emphasizing effect sizes and confidence intervals, not only p-values. citeturn13search0turn13search4turn13search7turn14search6 |

## Technical background notes

**2.1.1 Deep Neural Networks and Classification.**  
For this report, a classifier can be introduced as a parameterized map \(f_\theta: \mathcal{X}\to\mathbb{R}^K\) that outputs class logits, with probabilities obtained through the softmax and training commonly performed by minimizing cross-entropy over labeled data. At the level needed for the thesis, it is enough to state that modern deep neural networks are compositions of differentiable layers, so gradient-based optimization can be applied both to model parameters and, in adversarial settings, to the input. This is the technical reason that adversarial-example generation and adversarial training fit naturally into the same computational pipeline as ordinary empirical risk minimization. citeturn28search0

**2.1.2 Adversarial Examples.**  
An adversarial example is an input modified by a small, intentionally chosen perturbation that changes the model’s prediction or sharply increases task loss while remaining within a prescribed perturbation budget. Szegedy et al. exposed the phenomenon in modern deep networks and highlighted transferability across models, while Goodfellow et al. argued that vulnerability can arise from locally linear behavior in high-dimensional spaces and introduced the fast gradient sign method as a simple first-order construction. For Chapter 2, that history matters mainly because it motivates the later choice to treat the attack generator as part of the learning problem rather than as a separate post hoc diagnostic. citeturn19search0turn5search0

**2.1.3 Threat Models.**  
The thesis should distinguish clearly between the adversary’s knowledge and the admissible perturbation set. In the whitebox setting the attacker has gradients and parameters; in transfer or blackbox settings the attacker does not, and success may rely on transferability. Orthogonally, the perturbation model specifies the geometry of allowed changes, often with \(\ell_\infty\), \(\ell_2\), or related constraints, together with image-domain clipping. Madry et al. make this separation operational in a robust-optimization framework, Carlini and Wagner show why weak attacks can create false confidence, and Croce and Hein demonstrate that reliable evaluation must combine strong, diverse attacks instead of a single tuned baseline. citeturn3search8turn22search5turn3search2

**2.2.1 Min-max Formulation.**  
The canonical formulation of adversarial training is a min-max problem: the inner problem searches for a perturbation that maximizes loss within the threat model, and the outer problem updates the network to minimize that worst-case loss. Madry et al. are the standard citation here because they crystallize the robust-optimization interpretation that now anchors most empirical adversarial-training work. For a Chapter 2 treatment, it is useful to add that Sinha et al. show a close conceptual relationship between adversarial robustness and distributional robustness, so the min-max view is not only a practical algorithmic recipe but also a principled worst-case-risk perspective. citeturn3search8turn34search2

**2.2.2 PGD-AT and Its Limitations.**  
Projected gradient descent is the standard first-order solver for the inner maximization under norm constraints. The practical appeal of PGD is that it repeatedly takes gradient-ascent steps on the input and then projects back into the admissible set, making it a strong attack and a strong training adversary under the chosen geometry. Madry et al. therefore describe robustness to first-order adversaries as a concrete empirical security target. The limitation, which Chapter 2 should state carefully, is not that PGD is unimportant, but that PGD-based adversarial training is tied to the specific perturbation set and can be computationally costly; single-step approximations can also fail through label leaking or degenerate local behavior unless special care such as random starts is used. citeturn3search8turn23search0turn6search1turn6search2

**2.2.3 Multi-attack Adversarial Training Approaches.**  
Once robustness is evaluated against more than one attack family, the single-threat-model formulation becomes incomplete. Tramèr and Boneh show that defenses trained for one perturbation type can remain vulnerable to others and that jointly optimizing against several perturbation models is difficult. Maini et al. push this line further by defining robustness against the union of multiple perturbation models and by proposing a generalized PGD-style attack that searches across several geometries. The background chapter can therefore define multi-attack adversarial training as any procedure that exposes the model to more than one training adversary, while emphasizing that different procedures optimize different robust objectives and need not achieve balanced performance across attacks. citeturn7search3turn25search0

**2.2.4 Trade-off Analysis.**  
Two distinct trade-offs matter later in the report. The first is the familiar natural-accuracy versus robust-accuracy trade-off formalized by TRADES, which decomposes robust error into natural error plus a boundary term and motivates a regularized objective rather than a single undifferentiated robust loss. The second is the cross-attack allocation problem emphasized by multi-perturbation work: when several perturbation models are present, training pressure can concentrate unevenly, yielding robustness gains for some attacks and weaker performance for others. This is the conceptual opening for your later Chapter 4 design choices, because balancing worst-case risk across attacks is not the same objective as maximizing average robustness under a single fixed attack. citeturn32search1turn7search3turn25search0turn21search0

**2.3.1 Classical DRO Formulation.**  
Classical distributionally robust optimization replaces the empirical distribution used by ERM with an ambiguity set of plausible distributions and then minimizes worst-case expected loss over that set. Duchi and Namkoong provide a clean learning-theoretic version of this idea for uniform performance under distributional shift, while Sinha et al. connect it specifically to adversarial perturbations through Wasserstein-style neighborhoods around the data distribution. In Chapter 2, this subsection can define DRO at an abstract level as “learn the model that performs best against the most adverse distribution in a chosen ambiguity set,” and then reserve the finite-group specialization for the next subsection. citeturn26search24turn34search2

**2.3.2 Group DRO.**  
Group DRO specializes the ambiguity set to mixtures over a finite set of groups or environments. The resulting objective minimizes the worst-case group loss, or equivalently minimizes the maximum over simplex-weighted group averages. This is the version most relevant to the thesis because it provides the formal template for reweighting hard attack groups later on. Sagawa et al. are the key citation here: they treat group losses as the object to be optimized, develop a practical stochastic optimization procedure, and frame worst-group generalization as distinct from average test performance. That distinction is exactly the one your later attack-group formulations inherit. citeturn33search5

**2.3.3 Exponentiated Gradient on the Simplex.**  
When the outer maximization of Group DRO is parameterized with simplex weights \(q\), the natural update is multiplicative rather than additive: high-loss groups are upweighted exponentially and then renormalized. In machine learning language this is often described as exponentiated-gradient or multiplicative-weights updating. Kivinen and Warmuth are the classical reference for exponentiated-gradient updates, while Sagawa et al. provide the group-DRO-specific stochastic version used in modern deep learning pipelines. The practical interpretation for your chapter is simple: the group weights are not fixed coefficients, but adaptive adversarial priorities that shift mass toward whatever group currently incurs the largest loss. citeturn18search0turn33search5

**2.3.4 Regularization in Overparameterized Models.**  
A subtle but important point is that worst-group optimization can fail to improve worst-group test performance if the network simply interpolates all groups during training. Sagawa et al. show that in overparameterized neural networks, poor worst-group performance often arises from group-specific generalization gaps rather than from inability to drive training loss down. Their empirical conclusion is that Group DRO becomes substantially more effective when paired with stronger regularization, including larger-than-usual weight decay or early stopping. This point belongs in Chapter 2 because it justifies later design decisions that stabilize or anchor adaptive reweighting, rather than presenting group reweighting as sufficient by itself. citeturn33search5

**2.3.5 DRO in the Adversarial-training Context.**  
For this thesis, the most useful bridge is the observation that adversarial robustness has two different “worst-case” axes. The first axis is perturbation-level worst-case risk inside the inner maximization, as in PGD adversarial training. The second axis is group-level worst-case risk across predefined or inferred domains, as in Group DRO. Sinha et al. justify the first axis through distributional robustness around data points; Sagawa et al. justify the second axis through worst-group performance under group shift. Once attacks are organized as source groups, the thesis can combine these views without claiming they are identical: adversarial training handles within-group perturbation search, and Group DRO handles across-group allocation of training pressure. citeturn34search2turn33search5turn3search8

**2.4.1 Clustering-based Domain Discovery.**  
When group labels are missing, several lines of work try to recover them or approximate them. Oakden-Rayner et al. motivate the problem through hidden stratification, showing that coarse aggregate performance can conceal severe subgroup failures. Sohoni et al. operationalize this insight in GEORGE: they cluster learned representations to estimate latent subclasses and then optimize a group-robust objective over those pseudo-groups. Creager et al. infer environments for invariant learning, and Liu et al. use high-loss examples detected after an ERM warm start as implicit minority-group signals. Chapter 2 should present these as three related but distinct strategies: representation clustering, environment inference, and error-based group discovery. citeturn11search1turn31search1turn29search0turn30search0

**2.4.2 Attack-as-domains Perspective.**  
Domain generalization typically assumes multiple source environments and seeks predictors that transfer to unseen environments. Arjovsky et al. frame this as learning invariant predictors across environments, while Gulrajani and Lopez-Paz show through DomainBed that the DG setting is highly sensitive to implementation details and model selection. For your report, the relevant background claim is narrower than standard DG rhetoric: attack families can be treated as attack-induced domains because they generate systematically different perturbation distributions and difficulty patterns, but adversarial robustness still requires attack-grounded evaluation rather than purely average-domain performance. This makes DG a useful lens for structuring the problem, not a license to claim general out-of-distribution robustness. citeturn27search8turn10search8turn10search0turn21search0turn7search3

**2.5 Statistical Foundations.**  
Because your report compares methods across repeated seeds, the clean basic unit for inference is the paired seedwise difference \(d_i = m_i^{(A)} - m_i^{(B)}\). The paired \(t\)-test treats those differences as approximately normal and tests whether their mean is zero; the Wilcoxon signed-rank test instead uses the signed ranks of the nonzero differences and is less reliant on Gaussian assumptions. Cohen’s standardized effect-size framework remains the standard reference for reporting magnitude, and Cumming’s “new statistics” perspective is especially useful for a thesis because it argues that p-values should be accompanied by effect sizes and confidence intervals rather than reported alone. In practice, the chapter can recommend reporting seedwise paired differences, a confidence interval for the mean difference, a p-value, and one standardized effect size. citeturn13search0turn13search4turn13search7turn14search6

**2.6 Chapter Summary.**  
The chapter summary can close by stating that later methods in the report combine four technical ingredients that are now formally grounded: min-max adversarial training over explicit threat models, group-wise worst-case optimization from DRO, latent-group discovery from hidden-group and DG literature, and paired statistical reporting for seedwise comparisons. That summary does not need to preview Chapter 3’s “gap argument”; it only needs to establish the notation and conceptual tools that make the later method definition readable. citeturn3search8turn33search5turn31search1turn14search6

## Equations to include

**Supervised ERM.**  
Use this in **2.1.1 Deep Neural Networks and Classification**:
\[
\hat{\theta}_{\mathrm{ERM}}
=
\arg\min_{\theta}\;
\frac{1}{n}\sum_{i=1}^{n}\ell\!\left(f_{\theta}(x_i),y_i\right).
\]
This is the baseline objective from which adversarial training and DRO are contrasted. A cross-entropy instantiation is standard for classification. citeturn28search0turn26search24

**Adversarial example definition.**  
Use this in **2.1.2 Adversarial Examples**:
\[
x^{\mathrm{adv}} = x + \delta,
\qquad
\delta \in \mathcal{S}(x),
\qquad
f_\theta(x^{\mathrm{adv}})\neq y
\]
for untargeted attacks, or \(f_\theta(x^{\mathrm{adv}})=y_t\) for targeted attacks. This expresses the idea that the perturbation is constrained but intentionally harmful. citeturn19search0turn5search0turn22search5

**Perturbation set.**  
Use this in **2.1.3 Threat Models**:
\[
\mathcal{S}_p(x;\epsilon)
=
\left\{
\delta\in\mathbb{R}^{d}:
\lVert \delta\rVert_p \le \epsilon,\;
x+\delta\in[0,1]^d
\right\}.
\]
This is the standard norm-bounded threat model for images, with box constraints added to preserve valid pixel range. citeturn3search8turn22search5

**Adversarial inner maximization.**  
Use this in **2.2.1 Min-max Formulation**:
\[
\delta^\star(x,y;\theta)
=
\arg\max_{\delta\in\mathcal{S}_p(x;\epsilon)}
\ell\!\left(f_\theta(x+\delta),y\right).
\]
This is the attack-generation problem solved approximately by FGSM, PGD, CW-style optimization, DDN, and related methods under different objectives and constraints. citeturn3search8turn4search1turn22search5

**Adversarial-training min-max objective.**  
Use this in **2.2.1 Min-max Formulation** and refer back in **2.2.2 PGD-AT**:
\[
\hat{\theta}_{\mathrm{AT}}
=
\arg\min_{\theta}\;
\frac{1}{n}\sum_{i=1}^{n}
\max_{\delta\in\mathcal{S}_p(x_i;\epsilon)}
\ell\!\left(f_\theta(x_i+\delta),y_i\right).
\]
This is the canonical objective associated with Madry-style PGD adversarial training. citeturn3search8

**Group DRO objective.**  
Use this in **2.3.2 Group DRO**:
\[
\hat{\theta}_{\mathrm{gDRO}}
=
\arg\min_{\theta}
\max_{q\in\Delta^{G-1}}
\sum_{g=1}^{G} q_g\,\hat{L}_g(\theta),
\qquad
\hat{L}_g(\theta)=\frac{1}{|D_g|}\sum_{(x,y)\in D_g}\ell(f_\theta(x),y).
\]
This is the finite-group worst-case objective that later motivates attack-group reweighting. citeturn33search5

**Exponentiated-gradient update on group weights.**  
Use this in **2.3.3 Exponentiated Gradient on the Simplex**:
\[
q_g^{(t+1)}
=
\frac{
q_g^{(t)}
\exp\!\big(\eta\,\hat{L}_g(\theta^{(t)})\big)
}{
\sum_{h=1}^{G}
q_h^{(t)}
\exp\!\big(\eta\,\hat{L}_h(\theta^{(t)})\big)
}.
\]
This shows how hard groups get multiplicatively upweighted while the weights remain on the simplex. citeturn18search0turn33search5

**Paired difference, paired \(t\)-statistic, confidence interval, and paired standardized effect.**  
Use this in **2.5 Statistical Foundations**:
\[
d_i = m_i^{(A)} - m_i^{(B)},
\qquad
\bar d = \frac{1}{n}\sum_{i=1}^{n} d_i,
\qquad
s_d^2 = \frac{1}{n-1}\sum_{i=1}^{n}(d_i-\bar d)^2,
\]
\[
t = \frac{\bar d}{s_d/\sqrt{n}},
\qquad
\mathrm{CI}_{95\%}:
\bar d \pm t_{n-1,\,0.975}\frac{s_d}{\sqrt n},
\qquad
d_z = \frac{\bar d}{s_d}.
\]
This is the most direct way to report seedwise paired comparisons between two methods. If you prefer a nonparametric significance test, pair this with the Wilcoxon signed-rank test in prose rather than adding another main equation. citeturn13search0turn13search4turn13search7turn14search6

## Attack summary

The table below is calibrated to the report context you provided. The only source-training attacks explicitly confirmed by the prompt are PGD-\(\ell_\infty\) and DDN-\(\ell_2\). AutoAttack-\(\ell_\infty\) is explicitly confirmed as an evaluation tool. Other “used for evaluation” flags are best treated as likely or intended Chapter 2 background entries unless your experiment scripts say otherwise. citeturn3search2turn3search8turn4search1turn4search5turn5search0turn6search1turn6search2turn6search5turn22search5turn23search0turn32search1

| Attack | Full name | Norm / threat model | Main idea | Used for training in this report? | Used for evaluation in this report? | Primary citation |
|---|---|---|---|---|---|---|
| FGSM-RS | Fast Gradient Sign Method with random start | Usually \(\ell_\infty\) | Add a small random initialization, then take one FGSM step to avoid some label-leaking and degenerate one-step behavior | No | Likely diagnostic only | `tramer2018ensemble`; `wong2020fast` citeturn6search1turn6search2 |
| PGD-\(\ell_\infty\) | Projected Gradient Descent | \(\ell_\infty\)-bounded whitebox | Iterative gradient ascent on input loss with projection back to the \(\ell_\infty\) ball | Yes | Yes | `madry2018towards` citeturn3search8 |
| PGD-\(\ell_2\) | Projected Gradient Descent | \(\ell_2\)-bounded whitebox | Same iterative projected ascent idea, but with \(\ell_2\) geometry and projection | No | Likely yes | `madry2018towards` citeturn3search8 |
| CW-\(\ell_2\) | Carlini–Wagner attack | Typically \(\ell_2\) whitebox | Optimize a margin-based attack objective designed to find strong low-distortion adversarial examples | No | Likely yes | `carlini2017towards` citeturn22search5 |
| DeepFool-\(\ell_2\) | DeepFool | Usually small \(\ell_2\) perturbations | Iteratively linearize the classifier and step toward the nearest decision boundary | No | Likely yes | `moosavidezfooli2016deepfool` citeturn4search5 |
| DDN-\(\ell_2\) | Decoupled Direction and Norm | \(\ell_2\)-bounded whitebox | Decouple the perturbation direction from norm adjustment to get efficient strong \(\ell_2\) attacks | Yes | Yes | `rony2019decoupling` citeturn4search1 |
| MI-FGSM | Momentum Iterative FGSM | Usually \(\ell_\infty\), sometimes transferable blackbox | Add momentum to iterative gradient updates to stabilize directions and improve transferability | No | Likely yes, especially for transfer-style checks | `dong2018boosting` citeturn6search5 |
| TPGD | TRADES-style PGD attack | KL-based inner maximization, often under \(\ell_\infty\) | Maximize divergence between clean and perturbed predictions rather than plain loss on the true label | No | Likely yes if TRADES-style diagnostics are included | `zhang2019theoretically` citeturn32search1 |
| AutoAttack-\(\ell_\infty\) | AutoAttack | \(\ell_\infty\) evaluation suite | Parameter-free ensemble of complementary strong attacks for reliable robustness evaluation | No | Yes | `croce2020reliable` citeturn3search2 |

## BibTeX

The entries below were normalized from official proceedings pages, publisher pages, and canonical bibliographic records used throughout the note. Where venue metadata remains ambiguous in the literature ecosystem, I use the safest high-confidence form and flag the uncertainty in the final section. citeturn3search2turn3search8turn4search1turn4search5turn5search0turn6search1turn6search2turn6search5turn7search3turn10search0turn10search8turn11search1turn18search0turn22search5turn25search0turn26search24turn29search0turn30search0turn31search1turn32search1turn33search5turn34search2

```bibtex
@book{goodfellow2016deep,
  title={Deep Learning},
  author={Goodfellow, Ian and Bengio, Yoshua and Courville, Aaron},
  publisher={MIT Press},
  year={2016}
}

@inproceedings{szegedy2014intriguing,
  title={Intriguing Properties of Neural Networks},
  author={Szegedy, Christian and Zaremba, Wojciech and Sutskever, Ilya and Bruna, Joan and Erhan, Dumitru and Goodfellow, Ian and Fergus, Rob},
  booktitle={International Conference on Learning Representations},
  year={2014}
}

@inproceedings{goodfellow2015explaining,
  title={Explaining and Harnessing Adversarial Examples},
  author={Goodfellow, Ian J. and Shlens, Jonathon and Szegedy, Christian},
  booktitle={International Conference on Learning Representations},
  year={2015}
}

@inproceedings{kurakin2017adversarial,
  title={Adversarial Machine Learning at Scale},
  author={Kurakin, Alexey and Goodfellow, Ian and Bengio, Samy},
  booktitle={International Conference on Learning Representations},
  year={2017}
}

@inproceedings{tramer2018ensemble,
  title={Ensemble Adversarial Training: Attacks and Defenses},
  author={Tram{\`e}r, Florian and Kurakin, Alexey and Papernot, Nicolas and Goodfellow, Ian and Boneh, Dan and McDaniel, Patrick},
  booktitle={International Conference on Learning Representations},
  year={2018}
}

@inproceedings{wong2020fast,
  title={Fast Is Better Than Free: Revisiting Adversarial Training},
  author={Wong, Eric and Rice, Leslie and Kolter, J. Zico},
  booktitle={International Conference on Learning Representations},
  year={2020}
}

@inproceedings{madry2018towards,
  title={Towards Deep Learning Models Resistant to Adversarial Attacks},
  author={Madry, Aleksander and Makelov, Aleksandar and Schmidt, Ludwig and Tsipras, Dimitris and Vladu, Adrian},
  booktitle={International Conference on Learning Representations},
  year={2018}
}

@inproceedings{carlini2017towards,
  title={Towards Evaluating the Robustness of Neural Networks},
  author={Carlini, Nicholas and Wagner, David},
  booktitle={2017 IEEE Symposium on Security and Privacy},
  pages={39--57},
  year={2017},
  doi={10.1109/SP.2017.49}
}

@inproceedings{moosavidezfooli2016deepfool,
  title={DeepFool: A Simple and Accurate Method to Fool Deep Neural Networks},
  author={Moosavi-Dezfooli, Seyed-Mohsen and Fawzi, Alhussein and Frossard, Pascal},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={2574--2582},
  year={2016},
  doi={10.1109/CVPR.2016.282}
}

@inproceedings{dong2018boosting,
  title={Boosting Adversarial Attacks With Momentum},
  author={Dong, Yinpeng and Liao, Fangzhou and Pang, Tianyu and Su, Hang and Zhu, Jun and Hu, Xiaolin and Li, Jianguo},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={9185--9193},
  year={2018},
  doi={10.1109/CVPR.2018.00957}
}

@inproceedings{rony2019decoupling,
  title={Decoupling Direction and Norm for Efficient Gradient-Based L2 Adversarial Attacks and Defenses},
  author={Rony, Jerome and Hafemann, Luiz G. and Oliveira, Luiz S. and Ben Ayed, Ismail and Sabourin, Robert and Granger, Eric},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={4322--4330},
  year={2019},
  doi={10.1109/CVPR.2019.00445}
}

@inproceedings{zhang2019theoretically,
  title={Theoretically Principled Trade-off between Robustness and Accuracy},
  author={Zhang, Hongyang and Yu, Yaodong and Jiao, Jiantao and Xing, Eric P. and El Ghaoui, Laurent and Jordan, Michael I.},
  booktitle={Proceedings of the 36th International Conference on Machine Learning},
  pages={7472--7482},
  year={2019},
  volume={97},
  series={Proceedings of Machine Learning Research}
}

@inproceedings{croce2020reliable,
  title={Reliable Evaluation of Adversarial Robustness with an Ensemble of Diverse Parameter-Free Attacks},
  author={Croce, Francesco and Hein, Matthias},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={2206--2216},
  year={2020},
  volume={119},
  series={Proceedings of Machine Learning Research}
}

@inproceedings{tramer2019adversarial,
  title={Adversarial Training and Robustness for Multiple Perturbations},
  author={Tram{\`e}r, Florian and Boneh, Dan},
  booktitle={Advances in Neural Information Processing Systems},
  volume={32},
  year={2019}
}

@inproceedings{maini2020adversarial,
  title={Adversarial Robustness Against the Union of Multiple Perturbation Models},
  author={Maini, Pratyush and Wong, Eric and Kolter, J. Zico},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={6640--6650},
  year={2020},
  volume={119},
  series={Proceedings of Machine Learning Research}
}

@article{kang2019transfer,
  title={Transfer of Adversarial Robustness Between Perturbation Types},
  author={Kang, Daniel and Sun, Yi and Brown, Tom and Hendrycks, Dan and Steinhardt, Jacob},
  journal={arXiv preprint arXiv:1905.01034},
  year={2019}
}

@article{sinha2018certifiable,
  title={Certifiable Distributional Robustness with Principled Adversarial Training},
  author={Sinha, Aman and Namkoong, Hongseok and Duchi, John C.},
  journal={arXiv preprint arXiv:1710.10571},
  year={2018}
}
```

```bibtex
@article{duchi2021learning,
  title={Learning Models with Uniform Performance via Distributionally Robust Optimization},
  author={Duchi, John C. and Namkoong, Hongseok},
  journal={The Annals of Statistics},
  volume={49},
  number={3},
  pages={1378--1406},
  year={2021},
  doi={10.1214/20-AOS2004}
}

@article{sagawa2019distributionally,
  title={Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization},
  author={Sagawa, Shiori and Koh, Pang Wei and Hashimoto, Tatsunori B. and Liang, Percy},
  journal={arXiv preprint arXiv:1911.08731},
  year={2019}
}

@article{kivinen1997exponentiated,
  title={Exponentiated Gradient Versus Gradient Descent for Linear Predictors},
  author={Kivinen, Jyrki and Warmuth, Manfred K.},
  journal={Information and Computation},
  volume={132},
  number={1},
  pages={1--63},
  year={1997},
  doi={10.1006/inco.1996.2612}
}

@article{arjovsky2019invariant,
  title={Invariant Risk Minimization},
  author={Arjovsky, Martin and Bottou, L{\'e}on and Gulrajani, Ishaan and Lopez-Paz, David},
  journal={arXiv preprint arXiv:1907.02893},
  year={2019}
}

@inproceedings{gulrajani2021search,
  title={In Search of Lost Domain Generalization},
  author={Gulrajani, Ishaan and Lopez-Paz, David},
  booktitle={International Conference on Learning Representations},
  year={2021}
}

@inproceedings{wang2021generalizing,
  title={Generalizing to Unseen Domains: A Survey on Domain Generalization},
  author={Wang, Jindong and Lan, Cuiling and Liu, Chang and Ouyang, Yidong and Qin, Tao},
  booktitle={Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence},
  pages={4627--4635},
  year={2021},
  doi={10.24963/ijcai.2021/628}
}

@inproceedings{creager2021environment,
  title={Environment Inference for Invariant Learning},
  author={Creager, Elliot and Jacobsen, Joern-Henrik and Zemel, Richard},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={2189--2200},
  year={2021},
  volume={139},
  series={Proceedings of Machine Learning Research}
}

@inproceedings{sohoni2020no,
  title={No Subclass Left Behind: Fine-Grained Robustness in Coarse-Grained Classification Problems},
  author={Sohoni, Nimit and Dunnmon, Jared and Angus, Geoffrey and Gu, Albert and R{\'e}, Christopher},
  booktitle={Advances in Neural Information Processing Systems},
  volume={33},
  year={2020}
}

@inproceedings{oakdenrayner2020hidden,
  title={Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging},
  author={Oakden-Rayner, Luke and Dunnmon, Jared and Carneiro, Gustavo and R{\'e}, Christopher},
  booktitle={Proceedings of the ACM Conference on Health, Inference, and Learning},
  pages={151--159},
  year={2020},
  doi={10.1145/3368555.3384468}
}

@inproceedings{liu2021just,
  title={Just Train Twice: Improving Group Robustness without Training Group Information},
  author={Liu, Evan Z. and Haghgoo, Behzad and Chen, Annie S. and Raghunathan, Aditi and Koh, Pang Wei and Sagawa, Shiori and Liang, Percy and Finn, Chelsea},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={6781--6792},
  year={2021},
  volume={139},
  series={Proceedings of Machine Learning Research}
}
```

```bibtex
@article{student1908probable,
  title={The Probable Error of a Mean},
  author={{Student}},
  journal={Biometrika},
  volume={6},
  number={1},
  pages={1--25},
  year={1908},
  doi={10.1093/biomet/6.1.1}
}

@article{wilcoxon1945individual,
  title={Individual Comparisons by Ranking Methods},
  author={Wilcoxon, Frank},
  journal={Biometrics Bulletin},
  volume={1},
  number={6},
  pages={80--83},
  year={1945},
  doi={10.2307/3001968}
}

@book{cohen1988statistical,
  title={Statistical Power Analysis for the Behavioral Sciences},
  author={Cohen, Jacob},
  edition={2},
  publisher={Lawrence Erlbaum Associates},
  year={1988}
}

@article{cumming2014new,
  title={The New Statistics: Why and How},
  author={Cumming, Geoff},
  journal={Psychological Science},
  volume={25},
  number={1},
  pages={7--29},
  year={2014},
  doi={10.1177/0956797613504966}
}
```

## Risks and uncertainty

- **Sinha et al. venue normalization.** The paper *Certifiable Distributional Robustness with Principled Adversarial Training* is widely cited as an ICLR 2018 paper, but the most directly accessible records in this session were arXiv and bibliographic mirrors. If your thesis bibliography prefers final conference metadata, manually verify whether you want the ICLR form or the arXiv form and make it consistent everywhere. citeturn34search2turn34search3
- **Sagawa et al. venue normalization.** *Distributionally Robust Neural Networks for Group Shifts* is frequently used as the canonical Group DRO deep-learning citation, but the accessible high-confidence record here was the arXiv version. If your department prefers only archival peer-reviewed venues in BibTeX, manually confirm whether you want an associated workshop or conference form instead of the arXiv entry. citeturn33search5
- **TPGD naming.** “TPGD” is not a universally canonical paper title in the same way FGSM, PGD, CW, or DDN are. In many codebases it refers to the TRADES-style KL-divergence PGD inner maximization. If you use the label in Chapter 2, define it explicitly the first time and cite TRADES. citeturn32search1
- **Evaluation-use flags beyond the explicit prompt.** Only PGD-\(\ell_\infty\), DDN-\(\ell_2\), and AutoAttack-\(\ell_\infty\) were directly confirmed by the prompt as source-training or evaluation tools. The other “used for evaluation” entries in the attack table are informed background suggestions and should be checked against your actual experiment scripts before they are copied verbatim into the thesis.
- **Paired effect-size notation.** The standardized paired effect reported as \(d_z=\bar d/s_d\) is common, but notation varies across fields. If your thesis or lab style guide uses a different label for paired standardized mean differences, keep the formula but normalize the name.
- **Group-DRO optimizer details.** If Chapter 4 reuses a specific exponentiated-gradient schedule, smoothing constant, or loss normalization, those implementation details should be documented from your own method section rather than borrowed from background literature.
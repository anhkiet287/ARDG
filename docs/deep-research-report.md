# Related Work Research Package for Domain Generalization for Adversarial Robustness

The source base below is organized around five lines of literature that are directly relevant to your Chapter 3 argument: threat-model-specific adversarial training and reliable evaluation, multi-attack robustness, worst-group optimization, domain generalization, and hidden-group discovery with clustering or dynamics-aware signals. The synthesis prioritizes primary publication pages, official OpenReview records, PMLR/CVF proceedings, and arXiv records for arXiv-only works. citeturn24view0turn9search1turn19search1turn19search0turn7search0turn22search1turn22search2turn17search0turn7search1turn2search0turn15search1turn2search3turn2search1turn3search0turn16view0turn4search0turn4search1turn20view0turn6search0turn23search0turn6search1turn21view0turn13search0turn12search0

## Research map

| Section | Key papers | Main contribution | Limitation relevant to this report | How it supports our gap argument |
|---|---|---|---|---|
| Multi-Attack Adversarial Training | Goodfellow et al. 2015; Madry et al. 2018; Tramèr and Boneh 2019; Maini et al. 2020; Madaan et al. 2021; Maini et al. 2022; Croce and Hein 2020; Dai et al. 2023. citeturn24view0turn9search1turn22search1turn22search2turn22search3turn17search0turn7search0turn7search1 | Establishes that adversarial training is defined relative to a chosen threat model, motivates training against multiple perturbation types, and clarifies that robust evaluation must be strong enough to avoid inflated claims. | Multi-attack methods still rely on predeclared attack sets or attack categories, so they broaden coverage without discovering whether robust failure modes cut across attack identities. | Justifies why Multi-AT is a necessary baseline, but also why uniform coverage over source attacks may still leave a latent hard-group problem unresolved. |
| Group DRO Applied to Robustness | Hashimoto et al. 2018; Sagawa et al. 2020; Sohoni et al. 2020; Liu et al. 2021; Creager et al. 2021. citeturn2search0turn15search1turn2search3turn2search1turn3search0 | Shows why average-risk training can neglect minority or atypical groups, and why explicit worst-group optimization can improve robustness to group shifts when groups are meaningful. | Group DRO depends critically on the group definition. Known or coarse groups can misalign with the true failure structure, and hidden-group work arose precisely because the grouping variable is often missing or noisy. | Motivates AttackDRO as a natural fixed-group baseline over attack identities, while simultaneously motivating a move beyond fixed identities toward discovered latent groups. |
| Domain Generalization and Adversarial Robustness | Arjovsky et al. 2019; Krueger et al. 2021; Gulrajani and Lopez-Paz 2021; Song et al. 2019; Stutz et al. 2019; Stutz et al. 2020; Alhamoud et al. 2023; Zou and Liu 2023. citeturn16view0turn4search0turn4search1turn20view0turn6search0turn23search0turn6search1turn21view0 | Supplies the conceptual lens that attacks can be read as environment or domain shifts, and that stable performance across source domains matters more than average fit alone. | Standard DG objectives target invariance or average OOD performance, whereas adversarial robustness also requires explicit worst-case attack evaluation and threat-model-aware testing. | Supports the report’s claim that attack-induced domains are a useful abstraction, but not a complete solution to adversarial robustness. |
| Cluster Discovery in Robust Training Pipelines | Sohoni et al. 2020; Creager et al. 2021; Liu et al. 2021; Charpiat et al. 2019; Paul et al. 2021. citeturn2search3turn3search0turn2search1turn12search0turn13search0 | Shows that hidden groups can sometimes be discovered from representation geometry, inferred environments, losses, or gradient-based example scores rather than supplied labels. | Most of this work is not designed around adversarial attack objectives. Representation-only grouping may identify semantic similarity without capturing optimization-level robust difficulty. | Directly motivates the move from attack labels to latent clusters, and from pure representation clustering to augmented features that include optimization-aware signals such as gradient fingerprints. |
| The Remaining Gap and Motivation for This Work | Synthesis of the four rows above, especially Tramèr and Boneh 2019; Maini et al. 2020; Sagawa et al. 2020; Gulrajani and Lopez-Paz 2021; Sohoni et al. 2020; Croce and Hein 2020; Dai et al. 2023. citeturn22search1turn22search2turn15search1turn4search1turn2search3turn7search0turn7search1 | Identifies the missing combination: a strong multi-attack baseline, adaptive worst-group emphasis, discovered latent groups, optimization-aware grouping features, and robust evaluation that does not overstate generalization. | No single prior line of work combines all of these ingredients for adversarial training on attack-induced domains. | Makes Chapter 4 feel necessary by showing that each prior strand solves only part of the problem your report is addressing. |

## Recommended citation set

| Section | Essential | Recommended | Optional |
|---|---|---|---|
| Multi-Attack Adversarial Training | `madry2018towards`, `tramer2019adversarial`, `maini2020adversarial`, `croce2020reliable`, `dai2023multirobustbench` | `goodfellow2015explaining`, `uesato2018adversarial`, `athalye2018obfuscated`, `maini2022perturbation` | `madaan2021learning`, `stutz2020confidence` |
| Group DRO Applied to Robustness | `hashimoto2018fairness`, `sagawa2020distributionally` | `sohoni2020no`, `liu2021just`, `creager2021environment` | `paul2021deep` |
| Domain Generalization and Adversarial Robustness | `arjovsky2019invariant`, `krueger2021rex`, `gulrajani2021search` | `song2019improving`, `stutz2019disentangling`, `alhamoud2023generalizability`, `zou2023adversarial` | `stutz2020confidence` |
| Cluster Discovery in Robust Training Pipelines | `sohoni2020no`, `creager2021environment` | `liu2021just`, `paul2021deep`, `charpiat2019input` | `song2019improving` |
| The Remaining Gap and Motivation for This Work | `tramer2019adversarial`, `sagawa2020distributionally`, `gulrajani2021search`, `sohoni2020no`, `croce2020reliable` | `maini2022perturbation`, `dai2023multirobustbench`, `paul2021deep` | `uesato2018adversarial`, `athalye2018obfuscated` |

The priority assignments above reflect which works are load-bearing for your specific gap argument, namely: first, robustness is threat-model-specific and weak evaluation is dangerous; second, multiple attacks improve a baseline but do not remove worst-case imbalance; third, Group DRO is only as good as the grouping variable; fourth, DG gives a useful attacks-as-domains lens but not a robustness-specific grouping mechanism; and fifth, hidden groups can be discovered from features or training dynamics, though prior methods were not designed around adversarial robust difficulty. citeturn9search1turn19search1turn19search0turn7search0turn22search1turn22search2turn17search0turn7search1turn2search0turn15search1turn2search3turn2search1turn3search0turn16view0turn4search0turn4search1turn13search0turn12search0

## Draft Chapter 3 in LaTeX

\chapter{Related Work}
\label{chap:related_work}

\section{Multi-Attack Adversarial Training}

Adversarial training became the dominant empirical defense because it converts robustness into an optimization problem over explicitly specified perturbation sets. The line from FGSM to PGD-style min-max training was also clarifying in a second sense: it showed that robust accuracy is always conditional on the threat model used during training and evaluation, rather than a universal property of the classifier. Work on adversarial risk, weak-attack failure modes, and gradient masking then reinforced that robust evaluation cannot be separated from method design, because defenses that appear strong under weak or misconfigured attacks can collapse under stronger evaluation. \cite{goodfellow2015explaining,madry2018towards,uesato2018adversarial,athalye2018obfuscated,croce2020reliable} citeturn24view0turn9search1turn19search1turn19search0turn7search0

Once robustness was recognized as threat-model-specific, the natural next question was whether a single model could be trained to withstand several perturbation types at once. Tramèr and Boneh formalized the robustness trade-offs that arise across different \(\ell_p\)-bounded and spatial perturbations, and they proposed multi-perturbation adversarial training schemes to study that regime. Maini et al.\ later argued that simple aggregations of separate attacks can produce imbalanced robustness across perturbation models, and introduced a worst-case steepest-descent formulation over the union of perturbation sets. Madaan et al.\ addressed the computational cost of simultaneous multi-attack training through a meta-learned noise generator that stochastically exposes the classifier to diverse attacks. \cite{tramer2019adversarial,maini2020adversarial,madaan2021learning} citeturn22search1turn22search2turn22search3

This literature established an important baseline principle for the present report: broader attack coverage during training is stronger than single-attack specialization when the evaluation target spans heterogeneous attacks. At the same time, the same literature repeatedly reports that balanced robustness remains difficult. Maini et al.\ show that adversarial examples from different perturbation types can form distinguishable distributions and propose perturbation-type categorization as a routing mechanism, while MultiRobustBench expands the evaluation space to heterogeneous attack types and demonstrates that improved average performance still leaves worst-case failures largely unresolved. The practical lesson is that multi-attack robustness is not only a coverage problem, but also a balancing problem. \cite{maini2022perturbation,dai2023multirobustbench} citeturn17search0turn7search1

For this thesis, uniform multi-attack adversarial training is therefore a necessary baseline rather than an endpoint. It directly addresses the weakness of single-attack training by exposing the model to multiple source attacks during optimization. However, the grouping unit in this line of work remains fixed in advance: one trains against a chosen set of attacks, a chosen union of perturbation models, or a chosen categorization of attack types. What these approaches do not ask is whether the most consequential robust failure modes cut across attack identities, or whether some examples produced by different attacks belong to the same latent hard region for optimization. That unresolved granularity problem motivates the move from broader attack coverage to group-aware optimization in the next section. \cite{tramer2019adversarial,maini2020adversarial,maini2022perturbation,dai2023multirobustbench} citeturn22search1turn22search2turn17search0turn7search1

\section{Group DRO Applied to Robustness}

Group distributionally robust optimization addresses a different weakness than multi-attack training. Its central observation is that minimizing average loss can hide severe underperformance on minority or atypical groups, even when aggregate accuracy looks satisfactory. Hashimoto et al.\ developed a DRO perspective for representation disparity, and Sagawa et al.\ showed that, in overparameterized neural networks, worst-group optimization can improve substantially over ERM when it is paired with enough regularization and early stopping to prevent poor worst-group generalization. The conceptual contribution of this literature is to replace average-case fit with explicit protection against the currently weakest group. \cite{hashimoto2018fairness,sagawa2020distributionally} citeturn2search0turn15search1

A second contribution from this line of work is methodological rather than purely objective-based: the value of worst-group optimization depends on the quality of the group definition. Sohoni et al.\ treat hidden stratification as a latent subclass problem, cluster deep representations into approximate subclasses, and then apply DRO over the inferred groups. Liu et al.\ reduce reliance on group labels by using a first-stage ERM model to surface high-loss examples that often correspond to minority groups. Creager et al.\ similarly infer environments for invariant learning when group annotations are unavailable. Taken together, these methods show that robust group optimization is inseparable from the problem of identifying groups that meaningfully align with failure. \cite{sohoni2020no,liu2021just,creager2021environment} citeturn2search3turn2search1turn3search0

This framing transfers naturally to adversarial robustness. If source attacks are treated as known groups, then a fixed-group robust objective over attack identities is an immediate extension of Group DRO to adversarial training. Such a baseline is attractive because it offers adaptive emphasis on whichever training attack is currently weakest, rather than assigning all source attacks equal weight at all times. Yet the hidden-group literature also suggests the main limitation of that construction. Attack labels are externally supplied categories, not guaranteed to coincide with the true structure of robust failure. Two examples crafted by different attacks may be difficult for the same underlying reason, while two examples from the same attack family may belong to very different robust regimes. \cite{sagawa2020distributionally,sohoni2020no,liu2021just,creager2021environment} citeturn15search1turn2search3turn2search1turn3search0

The implication for this report is precise. Group DRO supplies the correct optimization instinct, namely to focus training pressure on weak groups rather than only on the average. But attack identity is only one possible grouping variable, and likely a coarse one. Prior worst-group work shows that better-aligned groups can matter as much as the reweighting rule itself. For an adversarial training pipeline, this means that the relevant question is not only whether to upweight hard attacks, but also whether the groups being upweighted should be attack identities at all. That question carries the discussion from fixed groups to discovered latent groups. \cite{sagawa2020distributionally,sohoni2020no,liu2021just,creager2021environment} citeturn15search1turn2search3turn2search1turn3search0

\section{Domain Generalization and Adversarial Robustness}

Domain generalization offers a useful conceptual lens because it studies how to learn from several source environments while preserving performance on unseen ones. IRM frames this in terms of representations whose optimal classifier is invariant across environments, while REx penalizes disparities in risk across training environments as a way of encouraging stability under extrapolated shifts. At the same time, DomainBed showed that DG claims are sensitive to implementation details, model selection, and experimental protocol, to the point that carefully tuned ERM is often a stronger baseline than broad DG surveys would suggest. That result is especially relevant here because it cautions against treating any domain-based framing as automatically superior to a strong baseline. \cite{arjovsky2019invariant,krueger2021rex,gulrajani2021search} citeturn16view0turn4search0turn4search1

Several robustness papers intersect with this agenda in ways that are directly relevant to the present thesis. Song et al.\ cast adversarial training with FGSM as a domain adaptation problem between clean and adversarial data, using domain-alignment ideas to improve generalization beyond the generating attack. Stutz et al.\ argue that off-manifold adversarial robustness and on-manifold generalization should be analytically separated, thereby clarifying one source of confusion in the robustness literature. Stutz et al.\ later propose confidence-calibrated adversarial training, which seeks better generalization to unseen attacks by lowering confidence on adversarial inputs rather than only enforcing correctness on one training threat model. \cite{song2019improving,stutz2019disentangling,stutz2020confidence} citeturn20view0turn6search0turn23search0

More recent work pushes the connection toward explicit OOD and distribution-shift evaluation. Alhamoud et al.\ study how empirical and certified robustness transfer to unseen domains and show that robustness under domain shift deserves separate measurement rather than being inferred from in-domain evaluation alone. Zou and Liu, from the opposite direction, study adversarial robustness of OOD generalization models and show that methods designed for unseen-domain generalization can still be vulnerable to adversarial perturbation. These papers collectively reinforce that cross-domain stability and adversarial robustness overlap, but neither notion subsumes the other. \cite{alhamoud2023generalizability,zou2023adversarial} citeturn6search1turn21view0

For this report, the attacks-as-domains perspective is therefore illuminating but incomplete. It is illuminating because it explains why training against multiple attacks should be analyzed as a structured heterogeneity problem rather than as a single scalar defense score. It is incomplete because standard DG objectives usually target average performance on unseen domains or invariance across training environments, whereas adversarial robustness additionally demands rigorous worst-case evaluation under explicit threat models and strong attack suites. The report borrows the DG intuition that attacks induce distinct domains, but it still requires a robustness-specific mechanism for discovering and emphasizing the hard groups that matter most during adversarial training. \cite{arjovsky2019invariant,krueger2021rex,gulrajani2021search,uesato2018adversarial,croce2020reliable,dai2023multirobustbench,maini2022perturbation} citeturn16view0turn4search0turn4search1turn19search1turn7search0turn7search1turn17search0

\section{Cluster Discovery in Robust Training Pipelines}

Cluster discovery becomes relevant when visible group labels are absent or too coarse to reflect actual failures. Sohoni et al.\ provide one of the clearest precedents for this move: GEORGE clusters representation space to estimate latent subclasses and then applies a worst-group objective over those discovered groups. Creager et al.\ pursue a related goal in invariant learning by inferring environments that are maximally informative for downstream invariant objectives. These works matter here because they show that group-aware learning need not be restricted to preannotated environments; groups can be discovered from the data representation itself. \cite{sohoni2020no,creager2021environment} citeturn2search3turn3search0

A second theme is that failure structure can also be surfaced through training dynamics rather than only through representation geometry. Liu et al.\ use high-loss examples from a first-stage model to identify informative samples for a second-stage robust learner, arguing that training behavior can reveal the minority groups that average-risk training overlooks. Paul et al.\ show, from a different angle, that gradient-based and error-based scores computed early in training can identify important or difficult examples with surprising consistency across architectures and hyperparameters. In both cases, the operative signal is not merely semantic similarity, but how the optimization process itself treats different examples. \cite{liu2021just,paul2021deep} citeturn2search1turn13search0

This suggests an important refinement for robust clustering. Representation-only clustering is well suited to surfacing semantic or subclass structure, but adversarial difficulty is also shaped by local loss geometry, gradient behavior, and attack objectives. Charpiat et al.\ define input similarity in terms of how a parameter update intended to affect one input influences another, which is an explicitly optimization-sensitive view of sample relations. Paul et al.'s GraNd score similarly operationalizes example salience through gradients. These works do not solve adversarial clustering directly, but they indicate that gradients can carry information about sample-level structure that penultimate-layer features alone may miss. \cite{charpiat2019input,paul2021deep} citeturn12search0turn13search0

The limitation, from the perspective of this thesis, is that none of these hidden-group or example-difficulty methods were designed around the robust failure modes created by heterogeneous attacks. A cluster that is meaningful for hidden stratification or invariant prediction is not automatically the right unit for adversarial robustness. Nonetheless, this literature establishes the two premises needed for Chapter 4: first, discovered groups can be preferable to supplied coarse labels; and second, optimization-aware signals can reveal structure that pure representation clustering overlooks. That is exactly the opening for augmenting adversarial clustering with gradient fingerprints rather than relying on representation features alone. \cite{sohoni2020no,creager2021environment,liu2021just,charpiat2019input,paul2021deep} citeturn2search3turn3search0turn2search1turn12search0turn13search0

\section{The Remaining Gap and Motivation for This Work}

The literature thus leaves a layered gap rather than a single missing method. Single-attack adversarial training is vulnerable to specialization. Multi-attack training improves coverage, but it still organizes heterogeneity through fixed source attacks or fixed perturbation sets. Group DRO contributes the right optimization principle by emphasizing weak groups, yet its success depends on whether the chosen groups reflect the actual failure structure. Read together, these lines of work imply that the open problem is not merely how to add more attacks, but how to decide what the relevant robust groups actually are. \cite{madry2018towards,tramer2019adversarial,maini2020adversarial,sagawa2020distributionally} citeturn9search1turn22search1turn22search2turn15search1

Domain generalization and hidden-group discovery make a partial answer plausible. They suggest that attacks can be treated as attack-induced domains, and that useful environments or subgroups can sometimes be inferred rather than supplied. But the adversarial setting adds requirements that ordinary DG does not resolve. Robustness must be evaluated under strong attacks, often by worst-case rather than average criteria, and the grouping mechanism should be sensitive to optimization hardness rather than only to semantic clustering. A latent partition that is sensible for OOD classification can still be unhelpful for robust training if it ignores which adversarial examples remain persistently difficult across attacks. \cite{gulrajani2021search,krueger2021rex,creager2021environment,sohoni2020no,uesato2018adversarial,croce2020reliable,dai2023multirobustbench} citeturn4search1turn4search0turn3search0turn2search3turn19search1turn7search0turn7search1

This is the point of departure for the methodology in Chapter 4. The report does not need a claim of universal adversarial robustness, nor a claim to solve domain generalization in full. What it needs is a practical construction that starts from a strong uniform multi-attack baseline, replaces fixed attack identities with discovered latent groups when those groups are more informative, enriches the grouping signal with optimization-aware cues such as gradient fingerprints, and preserves training stability through a uniform anchor so that adaptive reweighting does not overcommit to a brittle partition. That specific combination is not supplied by the prior work reviewed above, and it is the niche to which AttackDRO++ is addressed. \cite{sagawa2020distributionally,sohoni2020no,liu2021just,charpiat2019input,paul2021deep} citeturn15search1turn2search3turn2search1turn12search0turn13search0

Framed this way, the novelty claim of the report is deliberately conservative. The intended contribution is to improve robustness balance inside a concrete multi-attack adversarial training setting, not to establish universal transfer across all attacks or all domains. That conservative framing is consistent with the literature, which repeatedly shows that robust claims are sensitive to evaluation strength, to the chosen threat model, and to the distinction between average and worst-case performance. Chapter 4 is therefore necessary because none of the prior strands alone combines strong multi-attack coverage, adaptive worst-group emphasis, latent robust-group discovery, optimization-aware grouping features, and a stabilizing uniform anchor within a single adversarial training pipeline. \cite{uesato2018adversarial,athalye2018obfuscated,croce2020reliable,dai2023multirobustbench} citeturn19search1turn19search0turn7search0turn7search1

## Citation notes

| Paragraph | Citation note |
|---|---|
| 3.1 ¶1 | Supports the threat-model-specific reading of adversarial training and the need for reliable evaluation. Uses `goodfellow2015explaining` for the FGSM origin, `madry2018towards` for min-max adversarial training, `uesato2018adversarial` and `athalye2018obfuscated` for weak-attack and obfuscation pitfalls, and `croce2020reliable` for AutoAttack-style reliable evaluation. |
| 3.1 ¶2 | Supports the transition from single-threat adversarial training to simultaneous multi-perturbation training. Uses `tramer2019adversarial`, `maini2020adversarial`, and `madaan2021learning`. |
| 3.1 ¶3 | Supports the claim that broader coverage does not remove balancing problems and that perturbation types can be distributionally distinct. Uses `maini2022perturbation` and `dai2023multirobustbench`. |
| 3.1 ¶4 | Supports the limitation that fixed attack sets improve coverage but do not discover latent hard groups. Uses `tramer2019adversarial`, `maini2020adversarial`, `maini2022perturbation`, and `dai2023multirobustbench`. |
| 3.2 ¶1 | Supports the statement that average-risk training can neglect minority groups and that Group DRO can improve worst-group behavior with proper regularization. Uses `hashimoto2018fairness` and `sagawa2020distributionally`. |
| 3.2 ¶2 | Supports the claim that group quality matters and that hidden groups can be approximated by clustering, loss signals, or environment inference. Uses `sohoni2020no`, `liu2021just`, and `creager2021environment`. |
| 3.2 ¶3 | Supports the analogy between attack identities and known groups, while motivating caution from the hidden-group literature. Uses `sagawa2020distributionally`, `sohoni2020no`, `liu2021just`, and `creager2021environment`. |
| 3.2 ¶4 | Supports the conclusion that Group DRO provides the optimization principle but not necessarily the right partition. Uses `sagawa2020distributionally`, `sohoni2020no`, `liu2021just`, and `creager2021environment`. |
| 3.3 ¶1 | Supports the DG framing, including invariance, risk extrapolation, and DomainBed’s caution about ERM baselines. Uses `arjovsky2019invariant`, `krueger2021rex`, and `gulrajani2021search`. |
| 3.3 ¶2 | Supports the bridge between robustness and domain methods through ATDA, the manifold view, and CCAT’s unseen-attack generalization framing. Uses `song2019improving`, `stutz2019disentangling`, and `stutz2020confidence`. |
| 3.3 ¶3 | Supports the claim that robustness under distribution shift and adversarial vulnerability of OOD models are now explicit research topics. Uses `alhamoud2023generalizability` and `zou2023adversarial`. |
| 3.3 ¶4 | Supports the distinction between DG objectives and robustness-specific worst-case evaluation. Uses `arjovsky2019invariant`, `krueger2021rex`, `gulrajani2021search`, `uesato2018adversarial`, `croce2020reliable`, `dai2023multirobustbench`, and `maini2022perturbation`. |
| 3.4 ¶1 | Supports the claim that latent groups can be discovered from representation structure and then used by worst-group or invariant objectives. Uses `sohoni2020no` and `creager2021environment`. |
| 3.4 ¶2 | Supports the use of training behavior as a group-discovery signal. Uses `liu2021just` and `paul2021deep`. |
| 3.4 ¶3 | Supports the argument that gradients can encode optimization-sensitive relations between examples. Uses `charpiat2019input` and `paul2021deep`. |
| 3.4 ¶4 | Supports the limitation that existing hidden-group methods were not designed around adversarial robust failure modes. Uses `sohoni2020no`, `creager2021environment`, `liu2021just`, `charpiat2019input`, and `paul2021deep`. |
| 3.5 ¶1 | Synthesizes the limitations of single-attack AT, multi-attack AT, and fixed-group DRO. Uses `madry2018towards`, `tramer2019adversarial`, `maini2020adversarial`, and `sagawa2020distributionally`. |
| 3.5 ¶2 | Supports the claim that attacks-as-domains is plausible but not sufficient, because robust training still requires worst-case evaluation and optimization-aware grouping. Uses `gulrajani2021search`, `krueger2021rex`, `creager2021environment`, `sohoni2020no`, `uesato2018adversarial`, `croce2020reliable`, and `dai2023multirobustbench`. |
| 3.5 ¶3 | Supports the motivation for combining latent clusters, optimization-aware features, and a uniform anchor. Uses prior hidden-group and example-difficulty work rather than a direct precursor to the full method, specifically `sagawa2020distributionally`, `sohoni2020no`, `liu2021just`, `charpiat2019input`, and `paul2021deep`. |
| 3.5 ¶4 | Supports the conservative novelty framing and the need for strong evaluation. Uses `uesato2018adversarial`, `athalye2018obfuscated`, `croce2020reliable`, and `dai2023multirobustbench`. |

## BibTeX

**Foundational adversarial robustness and evaluation**

@article{goodfellow2015explaining,
  title={Explaining and Harnessing Adversarial Examples},
  author={Goodfellow, Ian J. and Shlens, Jonathon and Szegedy, Christian},
  journal={arXiv preprint arXiv:1412.6572},
  year={2015},
  url={https://arxiv.org/abs/1412.6572}
}

@inproceedings{madry2018towards,
  title={Towards Deep Learning Models Resistant to Adversarial Attacks},
  author={Madry, Aleksander and Makelov, Aleksandar and Schmidt, Ludwig and Tsipras, Dimitris and Vladu, Adrian},
  booktitle={International Conference on Learning Representations},
  year={2018},
  url={https://openreview.net/forum?id=rJzIBfZAb}
}

@inproceedings{uesato2018adversarial,
  title={Adversarial Risk and the Dangers of Evaluating Against Weak Attacks},
  author={Uesato, Jonathan and O'Donoghue, Brendan and Kohli, Pushmeet and van den Oord, Aaron},
  booktitle={Proceedings of the 35th International Conference on Machine Learning},
  pages={5025--5034},
  year={2018},
  volume={80},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v80/uesato18a.html}
}

@inproceedings{athalye2018obfuscated,
  title={Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples},
  author={Athalye, Anish and Carlini, Nicholas and Wagner, David},
  booktitle={Proceedings of the 35th International Conference on Machine Learning},
  pages={274--283},
  year={2018},
  volume={80},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v80/athalye18a.html}
}

@inproceedings{croce2020reliable,
  title={Reliable Evaluation of Adversarial Robustness with an Ensemble of Diverse Parameter-Free Attacks},
  author={Croce, Francesco and Hein, Matthias},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={2206--2216},
  year={2020},
  volume={119},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v119/croce20b.html}
}

Verified against primary publication records. citeturn24view0turn9search1turn19search1turn19search0turn7search0

**Multi-attack robustness**

@inproceedings{tramer2019adversarial,
  title={Adversarial Training and Robustness for Multiple Perturbations},
  author={Tramer, Florian and Boneh, Dan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2019},
  url={https://proceedings.neurips.cc/paper/2019/hash/5d4ae76f053f8f2516ad12961ef7fe97-Abstract.html}
}

@inproceedings{maini2020adversarial,
  title={Adversarial Robustness Against the Union of Multiple Perturbation Models},
  author={Maini, Pratyush and Wong, Eric and Kolter, Zico},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={6640--6650},
  year={2020},
  volume={119},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v119/maini20a.html}
}

@inproceedings{madaan2021learning,
  title={Learning to Generate Noise for Multi-Attack Robustness},
  author={Madaan, Divyam and Shin, Jinwoo and Hwang, Sung Ju},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={7279--7289},
  year={2021},
  volume={139},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v139/madaan21a.html}
}

@inproceedings{maini2022perturbation,
  title={Perturbation Type Categorization for Multiple Adversarial Perturbation Robustness},
  author={Maini, Pratyush and Chen, Xinyun and Li, Bo and Song, Dawn},
  booktitle={Proceedings of the Thirty-Eighth Conference on Uncertainty in Artificial Intelligence},
  pages={1317--1327},
  year={2022},
  volume={180},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v180/maini22a.html}
}

@inproceedings{dai2023multirobustbench,
  title={MultiRobustBench: Benchmarking Robustness Against Multiple Attacks},
  author={Dai, Sihui and Mahloujifar, Saeed and Xiang, Chong and Sehwag, Vikash and Chen, Pin-Yu and Mittal, Prateek},
  booktitle={Proceedings of the 40th International Conference on Machine Learning},
  pages={6760--6785},
  year={2023},
  volume={202},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v202/dai23c.html}
}

Verified against primary publication records. citeturn22search1turn22search2turn22search3turn17search0turn7search1

**Group DRO and hidden groups**

@inproceedings{hashimoto2018fairness,
  title={Fairness Without Demographics in Repeated Loss Minimization},
  author={Hashimoto, Tatsunori and Srivastava, Megha and Namkoong, Hongseok and Liang, Percy},
  booktitle={Proceedings of the 35th International Conference on Machine Learning},
  pages={1929--1938},
  year={2018},
  volume={80},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v80/hashimoto18a.html}
}

@inproceedings{sagawa2020distributionally,
  title={Distributionally Robust Neural Networks},
  author={Sagawa, Shiori and Koh, Pang Wei and Hashimoto, Tatsunori B. and Liang, Percy},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://openreview.net/forum?id=ryxGuJrFvS}
}

@inproceedings{sohoni2020no,
  title={No Subclass Left Behind: Fine-Grained Robustness in Coarse-Grained Classification Problems},
  author={Sohoni, Nimit and Dunnmon, Jared and Angus, Geoffrey and Gu, Albert and Re, Christopher},
  booktitle={Advances in Neural Information Processing Systems},
  year={2020},
  url={https://proceedings.neurips.cc/paper/2020/hash/e0688d13958a19e087e123148555e4b4-Abstract.html}
}

@inproceedings{liu2021just,
  title={Just Train Twice: Improving Group Robustness without Training Group Information},
  author={Liu, Evan Z and Haghgoo, Behzad and Chen, Annie S and Raghunathan, Aditi and Koh, Pang Wei and Sagawa, Shiori and Liang, Percy and Finn, Chelsea},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={6781--6792},
  year={2021},
  volume={139},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v139/liu21f.html}
}

@inproceedings{creager2021environment,
  title={Environment Inference for Invariant Learning},
  author={Creager, Elliot and Jacobsen, Joern-Henrik and Zemel, Richard},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={2189--2200},
  year={2021},
  volume={139},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v139/creager21a.html}
}

Verified against primary publication records. citeturn2search0turn15search1turn2search3turn2search1turn3search0

**Domain generalization and robustness bridges**

@article{arjovsky2019invariant,
  title={Invariant Risk Minimization},
  author={Arjovsky, Martin and Bottou, Leon and Gulrajani, Ishaan and Lopez-Paz, David},
  journal={arXiv preprint arXiv:1907.02893},
  year={2019},
  url={https://arxiv.org/abs/1907.02893}
}

@inproceedings{krueger2021rex,
  title={Out-of-Distribution Generalization via Risk Extrapolation (REx)},
  author={Krueger, David and Caballero, Ethan and Jacobsen, Joern-Henrik and Zhang, Amy and Binas, Jonathan and Zhang, Dinghuai and Le Priol, Remi and Courville, Aaron},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={5815--5826},
  year={2021},
  volume={139},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v139/krueger21a.html}
}

@inproceedings{gulrajani2021search,
  title={In Search of Lost Domain Generalization},
  author={Gulrajani, Ishaan and Lopez-Paz, David},
  booktitle={International Conference on Learning Representations},
  year={2021},
  url={https://openreview.net/forum?id=lQdXeXDoWtI}
}

@inproceedings{song2019improving,
  title={Improving the Generalization of Adversarial Training with Domain Adaptation},
  author={Song, Chuanbiao and He, Kun and Wang, Liwei and Hopcroft, John E.},
  booktitle={International Conference on Learning Representations},
  year={2019},
  url={https://openreview.net/forum?id=SyfIfnC5Ym}
}

@inproceedings{stutz2019disentangling,
  title={Disentangling Adversarial Robustness and Generalization},
  author={Stutz, David and Hein, Matthias and Schiele, Bernt},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={6976--6987},
  year={2019},
  url={https://openaccess.thecvf.com/content_CVPR_2019/html/Stutz_Disentangling_Adversarial_Robustness_and_Generalization_CVPR_2019_paper.html}
}

@inproceedings{stutz2020confidence,
  title={Confidence-Calibrated Adversarial Training: Generalizing to Unseen Attacks},
  author={Stutz, David and Hein, Matthias and Schiele, Bernt},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={9155--9166},
  year={2020},
  volume={119},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR},
  url={https://proceedings.mlr.press/v119/stutz20a.html}
}

@article{alhamoud2023generalizability,
  title={Generalizability of Adversarial Robustness Under Distribution Shifts},
  author={Alhamoud, Kumail and Hammoud, Hasan Abed Al Kader and Alfarra, Motasem and Ghanem, Bernard},
  journal={Transactions on Machine Learning Research},
  year={2023},
  url={https://openreview.net/forum?id=XNFo3dQiCJ}
}

@inproceedings{zou2023adversarial,
  title={On the Adversarial Robustness of Out-of-Distribution Generalization Models},
  author={Zou, Xin and Liu, Weiwei},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023},
  url={https://openreview.net/forum?id=IiwTFcGGTq}
}

Verified against primary publication records. citeturn16view0turn4search0turn4search1turn20view0turn6search0turn23search0turn6search1turn21view0

**Optimization-aware grouping signals**

@inproceedings{paul2021deep,
  title={Deep Learning on a Data Diet: Finding Important Examples Early in Training},
  author={Paul, Mansheej and Ganguli, Surya and Dziugaite, Gintare Karolina},
  booktitle={Advances in Neural Information Processing Systems},
  year={2021},
  url={https://proceedings.neurips.cc/paper/2021/hash/ac56f8fe9eea3e4a365f29f0f1957c55-Abstract.html}
}

@inproceedings{charpiat2019input,
  title={Input Similarity from the Neural Network Perspective},
  author={Charpiat, Guillaume and Girard, Nicolas and Felardos, Loris and Tarabalka, Yuliya},
  booktitle={Advances in Neural Information Processing Systems},
  year={2019},
  url={https://openreview.net/forum?id=B1lCtNreLr}
}

Verified against primary publication records. citeturn13search0turn12search0

## Risks and uncertainty

- The strongest accessible primary record for `goodfellow2015explaining` is the arXiv record, while many theses cite the work as an ICLR 2015 conference paper. If your department requires a conference-style record rather than an arXiv record, you should replace that entry with the official ICLR-formatted bibliographic version during final cleanup. citeturn24view0turn10search12

- The Sagawa Group DRO paper appears under a shorter ICLR 2020 title on OpenReview, while many bibliographies and later references use the longer subtitle “for Group Shifts: On the Importance of Regularization for Worst-Case Generalization.” The two records refer to the same underlying work, but you should keep one title convention consistently throughout the thesis. citeturn15search1turn15search0

- The official OpenReview record for ATDA lists the authors as Chuanbiao Song, Kun He, Liwei Wang, and John E. Hopcroft. Some secondary bibliographies and older BibTeX files circulate a different author list. The Chapter 3 draft and BibTeX above follow the official OpenReview record. citeturn20view0

- `arjovsky2019invariant` is an arXiv preprint rather than a flagship proceedings paper. It is still appropriate to cite because IRM is foundational in DG, but if your advisor prefers an all-peer-reviewed bibliography, this is one of the entries to discuss explicitly. citeturn16view0

- `charpiat2019input` and `paul2021deep` are not adversarial-robustness papers. They are included narrowly to support the claim that optimization-sensitive signals, especially gradients and early-training dynamics, can reveal structure that feature-only grouping misses. If you want a stricter robustness-only related-work chapter, these are the first citations to downgrade or move into Chapter 4 motivation instead. citeturn12search0turn13search0

- OpenReview source pages for several conference papers do not expose page numbers as cleanly as PMLR or CVF pages. The bibliographic core, authors, title, venue, and year, is verified above, but if your thesis template or reference manager requires exact page ranges for every conference paper, you may need one final pass against the official proceedings export or DBLP record before submission. citeturn4search1turn15search1turn20view0turn21view0

- If you later decide to add an explicit “attacks as domains” citation beyond the works already used here, `Towards Out-of-Distribution Adversarial Robustness` is directly on point but is a workshop/OpenReview paper rather than a flagship archival venue, so it should be treated as optional and clearly marked as such. citeturn18search0
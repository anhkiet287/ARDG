"""Draw the actual CIFAR-10 ResNet-18 model used by the training pipeline.

This script intentionally does not define a ResNet-18 template. It reads
``src/datn_final.py``, executes only the real configuration/model-builder
definitions needed for ``TrainConfig`` and ``build_model(cfg)``, instantiates the
same CIFAR-10/ResNet-18 training configuration, and draws diagrams from that
instantiated PyTorch model.

Required runtime packages:
    pip install torch torchvision torchinfo torchview graphviz
    # plus the Graphviz executable, e.g. `brew install graphviz` on macOS.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from collections import OrderedDict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRAINING_SOURCE = ROOT / "src" / "datn_final.py"
DEFAULT_OUTPUT_DIR = ROOT / "report" / "figures" / "model_architecture"
INPUT_SIZE = (1, 3, 32, 32)


def _die_missing_dependency(missing: list[str]) -> None:
    install_lines = [
        "pip install torch torchvision torchinfo torchview graphviz",
        "brew install graphviz  # macOS, for the `dot` renderer used by graphviz",
    ]
    print("\nMissing dependencies for architecture drawing:", file=sys.stderr)
    for item in missing:
        print(f"  - {item}", file=sys.stderr)
    print("\nInstall example:", file=sys.stderr)
    for line in install_lines:
        print(f"  {line}", file=sys.stderr)
    raise SystemExit(2)


def check_dependencies(require_full_graph: bool) -> dict[str, Any]:
    missing: list[str] = []

    try:
        import torch
    except Exception as exc:  # pragma: no cover - depends on local environment
        missing.append(f"torch ({exc})")
        torch = None

    try:
        import torchvision  # noqa: F401
    except Exception as exc:  # pragma: no cover
        missing.append(f"torchvision ({exc})")

    try:
        import graphviz
    except Exception as exc:  # pragma: no cover
        missing.append(f"graphviz Python package ({exc})")
        graphviz = None

    if shutil.which("dot") is None:
        missing.append("Graphviz executable `dot`")

    torchview = None
    torchviz = None
    if require_full_graph:
        try:
            from torchview import draw_graph

            torchview = draw_graph
        except Exception:
            try:
                from torchviz import make_dot

                torchviz = make_dot
            except Exception as exc:  # pragma: no cover
                missing.append(f"torchview or torchviz ({exc})")

    if missing:
        _die_missing_dependency(missing)

    return {"torch": torch, "graphviz": graphviz, "torchview": torchview, "torchviz": torchviz}


def _extract_between(source: str, start_token: str, end_token: str) -> str:
    try:
        start = source.index(start_token)
        end = source.index(end_token, start)
    except ValueError as exc:
        raise RuntimeError(f"Could not locate expected code block in {DEFAULT_TRAINING_SOURCE}: {exc}") from exc
    return source[start:end]


def _extract_function(source: str, function_name: str) -> str:
    lines = source.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(f"def {function_name}(")), None)
    if start is None:
        raise RuntimeError(f"Could not locate function {function_name} in training source.")

    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if line.startswith("def ") or line.startswith("class ") or line.startswith("@dataclass"):
            end = i
            break
    return "\n".join(lines[start:end]) + "\n"


def load_actual_training_builders(training_source: Path) -> dict[str, Any]:
    """Execute only the real datn_final.py builder definitions needed here."""
    source = training_source.read_text(encoding="utf-8")

    config_block = _extract_between(
        source,
        "@dataclass\nclass AttackSpec:",
        'print("✅  Config dataclasses defined.")',
    )
    image_size_block = _extract_function(source, "_get_image_size")
    backbone_block = _extract_between(
        source,
        "from torchvision.models import resnet18, ResNet18_Weights",
        "# Quick test (no GPU needed)",
    )

    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    ns: dict[str, Any] = {
        "__name__": "datn_final_architecture_loader",
        "Any": Any,
        "Dict": Dict,
        "List": List,
        "Optional": Optional,
        "Path": Path,
        "dataclass": dataclass,
        "field": field,
        "torch": torch,
        "nn": nn,
        "F": F,
        # TrainConfig default paths are not used for drawing, but the class
        # definition references these names at class-definition time.
        "CHECKPOINT_DIR": ROOT / "ardg_project" / "checkpoints",
        "RESULTS_DIR": ROOT / "ardg_project" / "results",
        "FIG_DIR": ROOT / "ardg_project" / "figures",
    }
    exec(config_block, ns)
    exec(image_size_block, ns)
    exec(backbone_block, ns)

    for name in ("TrainConfig", "EarlyStoppingConfig", "build_model", "build_resnet18"):
        if name not in ns:
            raise RuntimeError(f"{name} was not loaded from {training_source}.")
    return ns


def make_default_training_config(ns: dict[str, Any]) -> Any:
    """Instantiate the report's CIFAR-10/ResNet-18 training configuration."""
    TrainConfig = ns["TrainConfig"]
    EarlyStoppingConfig = ns["EarlyStoppingConfig"]
    return TrainConfig(
        experiment_name="attackdro_pp_anchor035_gradfp_online_k4_cifar10_rn18",
        method="groupdro_cluster_online_difficulty",
        dataset_name="cifar10",
        num_classes=10,
        backbone="resnet18",
        pretrained=False,
        group_label_mode="cluster",
        source_attack_names=["pgd20_ce", "ddn_l2"],
        heldout_attack_names=["fgsm_rs", "tpgd", "deepfool_l2", "cw_l2", "mifgsm", "pgd_l2"],
        eval_attack_names=[
            "clean",
            "fgsm_rs",
            "pgd20_ce",
            "tpgd",
            "cw_l2",
            "mifgsm",
            "deepfool_l2",
            "autoattack_linf",
            "ddn_l2",
            "pgd_l2",
        ],
        batch_size=128,
        epochs=50,
        lr=0.1,
        scheduler="multistep",
        scheduler_milestones=[30, 40],
        scheduler_gamma=0.1,
        amp=False,
        grad_clip_norm=1.0,
        cluster_num_clusters=4,
        cluster_dro_lambda=0.35,
        cluster_use_gradient_fingerprints=True,
        cluster_gradient_proj_dim=128,
        cluster_gradient_weight=0.1,
        cluster_refresh_epoch_interval=2,
        cluster_stratify_by_label=True,
        cluster_label_weight=0.1,
        early_stopping=EarlyStoppingConfig(
            monitor="val_seen_avg_robust_acc",
            mode="max",
            patience=50,
            warmup_epochs=5,
            save_best=True,
            save_last=True,
        ),
    )


def load_config_from_json(path: Path, ns: dict[str, Any]) -> Any:
    TrainConfig = ns["TrainConfig"]
    EarlyStoppingConfig = ns["EarlyStoppingConfig"]
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw.get("early_stopping"), dict):
        raw["early_stopping"] = EarlyStoppingConfig(**raw["early_stopping"])
    return TrainConfig(**raw)


def shape_of(value: Any) -> str:
    if hasattr(value, "shape"):
        return "x".join(str(dim) for dim in value.shape)
    if isinstance(value, (tuple, list)) and value:
        return shape_of(value[0])
    return "?"


def summarize_top_level_modules(model: Any, dummy: Any, torch: Any) -> OrderedDict[str, dict[str, str]]:
    records: OrderedDict[str, dict[str, str]] = OrderedDict()
    handles = []

    for name, module in model.named_children():
        def _hook(mod: Any, inputs: tuple[Any, ...], output: Any, module_name: str = name) -> None:
            records[module_name] = {
                "class": mod.__class__.__name__,
                "repr": compact_module_repr(mod),
                "input": shape_of(inputs[0] if inputs else None),
                "output": shape_of(output),
            }

        handles.append(module.register_forward_hook(_hook))

    model.eval()
    with torch.no_grad():
        model(dummy)
    for handle in handles:
        handle.remove()
    return records


def compact_module_repr(module: Any) -> str:
    cls = module.__class__.__name__
    if cls == "Conv2d":
        return (
            f"Conv2d {module.in_channels}->{module.out_channels}, "
            f"k={module.kernel_size}, s={module.stride}, p={module.padding}"
        )
    if cls == "BatchNorm2d":
        return f"BatchNorm2d({module.num_features})"
    if cls == "Linear":
        return f"Linear {module.in_features}->{module.out_features}"
    if cls == "AdaptiveAvgPool2d":
        return f"AdaptiveAvgPool2d({module.output_size})"
    if hasattr(module, "__len__") and cls == "Sequential":
        children = list(module.children())
        block_name = children[0].__class__.__name__ if children else "block"
        stride = getattr(getattr(children[0], "conv1", None), "stride", "?") if children else "?"
        return f"{len(children)} x {block_name}, first stride={stride}"
    return cls


def draw_block_diagram(model: Any, dummy: Any, output_base: Path, graphviz: Any, torch: Any) -> None:
    records = summarize_top_level_modules(model, dummy, torch)
    graph = graphviz.Digraph("resnet18_actual_model_blocks", format="png")
    graph.attr(
        rankdir="LR",
        bgcolor="white",
        pad="0.2",
        nodesep="0.38",
        ranksep="0.55",
        splines="ortho",
        label=(
            "Actual CIFAR-10 ResNet-18 from datn_final.py build_model(cfg)\\n"
            "conv1/maxpool/fc reflect the instantiated PyTorch model"
        ),
        labelloc="t",
        fontsize="18",
        fontname="Helvetica",
    )
    graph.attr("node", shape="box", style="rounded,filled", fillcolor="#F8FAFC", color="#334155",
               fontname="Helvetica", fontsize="10", margin="0.08,0.06")
    graph.attr("edge", color="#64748B", arrowsize="0.7")

    graph.node("input", "Input\\n1x3x32x32", fillcolor="#DCFCE7")
    previous = "input"
    for name, rec in records.items():
        label = f"{name}\\n{rec['repr']}\\n{rec['input']} -> {rec['output']}"
        fill = "#DBEAFE" if name in {"layer1", "layer2", "layer3", "layer4"} else "#F8FAFC"
        if name in {"conv1", "maxpool", "fc"}:
            fill = "#FEF3C7"
        graph.node(name, label, fillcolor=fill)
        graph.edge(previous, name)
        previous = name
    graph.node("output", "Logits\\n1x10", fillcolor="#FEE2E2")
    graph.edge(previous, "output")

    render_graphviz(graph, output_base)


def render_graphviz(graph: Any, output_base: Path) -> None:
    output_base.parent.mkdir(parents=True, exist_ok=True)
    for fmt in ("png", "pdf"):
        graph.render(filename=str(output_base), format=fmt, cleanup=True)


def draw_full_graph(model: Any, dummy: Any, output_base: Path, deps: dict[str, Any]) -> None:
    torch = deps["torch"]
    if deps["torchview"] is not None:
        draw_graph = deps["torchview"]
        graph_model = draw_graph(
            model,
            input_size=INPUT_SIZE,
            device="cpu",
            graph_name="Actual CIFAR-10 ResNet-18 computational graph",
            expand_nested=False,
        )
        graph_model.visual_graph.attr(rankdir="TB", size="10,14", ratio="compress")
        render_graphviz(graph_model.visual_graph, output_base)
        return

    make_dot = deps["torchviz"]
    model.eval()
    output = model(dummy.clone().requires_grad_(True))
    graph = make_dot(output, params=dict(model.named_parameters()))
    graph.attr(rankdir="TB", size="10,14", ratio="compress")
    render_graphviz(graph, output_base)


def print_model_summary(model: Any, input_size: tuple[int, int, int, int]) -> None:
    try:
        from torchinfo import summary

        print("\nTorchinfo summary:")
        print(
            summary(
                model,
                input_size=input_size,
                depth=3,
                col_names=("input_size", "output_size", "num_params", "kernel_size"),
                verbose=0,
            )
        )
    except Exception as exc:
        print(f"\nTorchinfo unavailable; printing compact parameter summary instead ({exc}).")
        total = sum(p.numel() for p in model.parameters())
        trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(model)
        print(f"\nParameters: total={total:,}, trainable={trainable:,}")


def validate_cifar_resnet18_stem(model: Any) -> None:
    conv1 = model.conv1
    maxpool = model.maxpool
    fc = model.fc
    print("\nInstantiated architecture checks:")
    print(f"  conv1   : {conv1}")
    print(f"  maxpool : {maxpool}")
    print(f"  fc      : {fc}")
    assert tuple(conv1.kernel_size) == (3, 3)
    assert tuple(conv1.stride) == (1, 1)
    assert tuple(conv1.padding) == (1, 1)
    assert conv1.bias is None
    assert maxpool.__class__.__name__ == "Identity"
    assert fc.out_features == 10


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate PNG/PDF diagrams from the actual CIFAR-10 ResNet-18 instantiated by datn_final.py."
    )
    parser.add_argument("--training-source", type=Path, default=DEFAULT_TRAINING_SOURCE,
                        help="Path to the Colab-exported training source containing TrainConfig/build_model.")
    parser.add_argument("--config-json", type=Path, default=None,
                        help="Optional saved TrainConfig JSON. Defaults to the final CIFAR-10 ResNet-18 setup.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
                        help="Directory for generated PNG/PDF diagrams.")
    parser.add_argument("--skip-full-graph", action="store_true",
                        help="Only draw the simplified major-block diagram.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    deps = check_dependencies(require_full_graph=not args.skip_full_graph)
    torch = deps["torch"]

    ns = load_actual_training_builders(args.training_source)
    cfg = load_config_from_json(args.config_json, ns) if args.config_json else make_default_training_config(ns)

    print("Architecture-affecting config:")
    for key in ("experiment_name", "method", "dataset_name", "num_classes", "backbone", "pretrained"):
        print(f"  {key}: {getattr(cfg, key)}")
    print(f"  source_attack_names: {getattr(cfg, 'source_attack_names', None)}")

    model = ns["build_model"](cfg).cpu().eval()
    validate_cifar_resnet18_stem(model)

    dummy = torch.zeros(INPUT_SIZE)
    print_model_summary(model, INPUT_SIZE)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    block_base = args.output_dir / "resnet18_actual_model_blocks"
    draw_block_diagram(model, dummy, block_base, deps["graphviz"], torch)
    print(f"\nSaved simplified block diagram:\n  {block_base}.png\n  {block_base}.pdf")

    if not args.skip_full_graph:
        graph_base = args.output_dir / "resnet18_actual_model_graph"
        draw_full_graph(model, dummy, graph_base, deps)
        print(f"\nSaved computational graph:\n  {graph_base}.png\n  {graph_base}.pdf")

    print("\nConfig snapshot used for model instantiation:")
    cfg_dict = asdict(cfg)
    for key in ("backbone", "dataset_name", "num_classes", "pretrained", "source_attack_names"):
        print(f"  {key}: {cfg_dict.get(key)}")


if __name__ == "__main__":
    main()

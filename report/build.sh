#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"
latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex


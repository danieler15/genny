#!/bin/bash

# Copyright 2019-present MongoDB Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TOOD: Keep?
set -o errexit
set -o pipefail
set -o nounset

SCRIPTS_DIR="$(dirname "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "${SCRIPTS_DIR}/.." && pwd)"
PYTHON_DIR="${ROOT_DIR}/src/python"
# VENV_DIR="${PYTHON_DIR}/venv"

cd "${PYTHON_DIR}"

# What if Python isn't installed?
# pyenv install
# pyenv rehash

python3 -m pip install virtualenv
# virtualenv -p python3 "${VENV_DIR}"
virtualenv venv
source ./venv/bin/activate
python3 -m pip install .

python3 -m pip install shrub.py

python3 genny_auto_tasks.py

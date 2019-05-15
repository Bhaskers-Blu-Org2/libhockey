#!/bin/bash

pushd "${VIRTUAL_ENV}" > /dev/null

python -m pylint --rcfile=pylintrc libhockey
python -m mypy --ignore-missing-imports libhockey/

python -m pylint --rcfile=pylintrc tests
python -m mypy --ignore-missing-imports tests/

popd > /dev/null


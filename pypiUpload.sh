#!/bin/bash

rm -rf build || true
rm -rf dist || true
python3 setup.py sdist bdist_wheel

# https://twine.readthedocs.io/en/stable/

token=$(cat /Users/morpheous/Tresors/Misc/Personal/7435171-PyPiToken.txt)
python3 -m twine upload \
-u "__token__" \
-p "$token" \
--repository-url https://upload.pypi.org/legacy/ dist/*
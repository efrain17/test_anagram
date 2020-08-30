Install
-----------
virtualenv --python=python3 venv
source venv/bin/activate
pip install -e .

Run test
-----------
pytest test_algorit.py

Run lint 
-----------
pylint domain/ --disable=missing-docstring
pylint routes/ --disable=missing-docstring
pylint db/ --disable=missing-docstring

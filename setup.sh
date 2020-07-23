#! /bin/bash
python3 -m venv env
source env/bin/activate
wait
pip3 install -r requirements.txt
pip3 install pytest

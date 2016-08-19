#!/bin/bash

rm -fr env
python3.5 -m venv env
. env/bin/activate
pip install matplotlib
echo ". env/bin/activate"

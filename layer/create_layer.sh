#!/bin/bash
rm -rf *.zip python
pip install fastapi==0.99.0 mangum pydantic -t python
zip -r fastapi.zip python
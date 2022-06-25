#!/bin/bash

# This is the script to run automation. The only parameter is: <tag name>
# Examples:
#            ./RUN.sh => This runs all tests:
#            ./RUN.sh login => This runs only login tests
#            ./RUN.sh high_priority => # This will run testcases marked as high_priority


if [ "$1" != "" ]; then
  python -m pytest -c setup.cfg --html=./reports/html_report.html --self-contained-html -n 2 -m $1
else
  python -m pytest -c setup.cfg --html=./reports/html_report.html --self-contained-html -n 2
fi


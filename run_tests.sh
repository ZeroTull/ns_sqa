#!/bin/bash

# Define the directories for tests, Allure results, and Allure reports

ALLURE_RESULTS_DIR="src/allure-results"
ALLURE_REPORT_DIR="src/allure-report"

# Remove previous Allure results and reports if they exist
rm -rf $ALLURE_RESULTS_DIR
rm -rf $ALLURE_REPORT_DIR

# Run all tests from the tests directory and generate Allure report data
pytest -n 10 --alluredir=$ALLURE_RESULTS_DIR

# Generate the Allure report
allure generate $ALLURE_RESULTS_DIR --clean -o $ALLURE_REPORT_DIR

# Open the Allure report
allure open $ALLURE_REPORT_DIR
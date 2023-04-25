# Autotests for nopcommerce

### Prerequisites
- [python](https://www.python.org/downloads/) (v3.7+) installed,
- [allure commandline](https://docs.qameta.io/allure-report/#_installing_a_commandline) installed,

### Setup

1. Clone the repository with `git clone https://github.com/Siyavush91/auto_test_project.git`
2. Install and activate virtual environment for just clonned repository:
```commandline
python3 -m venv venv
source venv/bin/activate
```

3. Install project dependencies:
Mandatory:
```commandline
./venv/bin/pip install -r requirements.txt
```

### Execution

To run autotests use following commands:
- for all tests: `pytest -s -v tests --alluredir=test-results`
- for a specific scope (for example, smoke): `pytest -sv -m smoke tests --alluredir=test-results` Only 'smoke' and 'debug' marks are available for now, we will add more options (like 'ota' - for OTA tests, etc.) in future.

Note: allure test results will be placed in the `test-results` folder in the current directory.

### Gathering test results

To generate and show test report locally use the following command:
```commandline
allure serve /path/to/test-results
```


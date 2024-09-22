
# Javidan Individual Project 1

### CI/CD Badges:
- **Test Status**: [![Run Tests](https://github.com/nogibjj/Javidan_Individual_Project_1/actions/workflows/run-tests.yml/badge.svg)](https://github.com/nogibjj/Javidan_Individual_Project_1/actions/workflows/run-tests.yml)
- **Code Formatting**: [![Format Code](https://github.com/nogibjj/Javidan_Individual_Project_1/actions/workflows/format-code.yml/badge.svg)](https://github.com/nogibjj/Javidan_Individual_Project_1/actions/workflows/format-code.yml)
- **Linting**: [![Run Lint](https://github.com/nogibjj/Javidan_Individual_Project_1/actions/workflows/run-lint.yml/badge.svg)](https://github.com/nogibjj/Javidan_Individual_Project_1/actions/workflows/run-lint.yml)


## Project Overview
This project demonstrates the setup of continuous integration for a Python data science project using Gitlab CI/CD pipelines. It includes a Jupyter Notebook performing descriptive statistics with Pandas, test scripts and jupyter notebook, a shared library, and a Makefile to automate tasks such as formatting, linting, and testing. Gitlab Actions run these tasks, with badges reflecting their status.

---


### 1. **Jupyter Notebook**
- The notebook performs **descriptive statistics** using **Pandas**.
- It is tested using the `nbval` plugin for `pytest` to validate the correctness of the results.

### 2. **Python Scripts**
- `test_script.py`: Contains tests for a standalone script.
- `test_lib.py`: Tests the shared code in `lib.py`.
- `lib.py`: Shared utility code used in both the notebook and scripts.

### 3. **Makefile**
The `Makefile` includes the following commands:

- **Run all tests**: Executes tests on the notebook, script, and library.
- **Code formatting**: Formats the Python code using **black**.
- **Linting**: Lints the code using **Ruff**.
- **Install dependencies**: Installs all required packages listed in `requirements.txt`.

### 4. **requirements.txt**
A pinned list of dependencies for the project to ensure consistent environments across systems.

---

## Gitlab Actions
Tasks from the Makefile are automated using Gitlab CI/CD pipelines. The `.gitlab-ci.yml` file contains jobs that:
- Run tests on the Jupyter Notebook, scripts, and library.
- Format the code using **black**.
- Lint the code using **Ruff**.
- Install the dependencies via `pip`.

---

## Setup and Usage Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/nogibjj/Javidan_Individual_Project_1.git
cd Javidan_Individual_Project_1
```

### 2. Install the dependencies:
```bash
make install
```

### 3. Run the Makefile commands:
- **Run all tests**:
  ```bash
  make test
  ```
- **Format code with black**:
  ```bash
  make format
  ```
- **Lint code with Ruff**:
  ```bash
  make lint
  ```


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


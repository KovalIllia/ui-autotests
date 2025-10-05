**About (GitHub description):**
UI test automation framework with **Python, Pytest, Selenium, Allure reporting, and Docker integration** for running end-to-end tests against [automationexercise.com](http://automationexercise.com).

**GitHub Topics (tags):**
`python` `pytest` `selenium` `allure` `docker` `automation` `qa` `testing` `test-automation` `ui-testing`

---

# UI Autotests Project

## 📌 Overview

This project is a **UI test automation framework** built with:

* **Python 3 + Pytest** – test runner & fixtures
* **Selenium WebDriver** – browser automation
* **Faker** – test data generation
* **Allure** – rich test reports
* **Docker** – containerized execution

The tests are written against [automationexercise.com](http://automationexercise.com) and cover scenarios such as:

* Opening Home Page
* User Signup & Registration
* Validating banners and page flows

---

## 🚀 Features

* Structured Page Object Model (POM) for maintainability
* Logging via custom `Logger` utility
* Allure steps in page methods for clear test reports
* Parallel execution support with `pytest-xdist`
* CI/CD-ready with Docker integration

---

## 📂 Project Structure

```
ui-autotests/
│── pages/                  # Page Object classes
│── tests/                  # Test cases
│── utils/                  # Helpers (logger, data generators, etc.)
│── output/
│   ├── allure/             # Allure results & reports
│   ├── reports/            # HTML reports
│   └── scripts/            # Run scripts (pytest + allure)
│── pytest.ini              # Pytest configuration
│── requirements.txt        # Python dependencies
│── Dockerfile              # Docker setup
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Local environment

```bash
git clone https://github.com/<your-username>/ui-autotests.git
cd ui-autotests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run tests locally

```bash
pytest -v -s --alluredir=output/allure/allure-results
```

### 3. Generate Allure report

```bash
allure generate output/allure/allure-results --clean -o output/allure/allure-report
allure open output/allure/allure-report
```

Or simply run prepared script:

```bash
./output/scripts/run_tests.sh
```

---

## 🐳 Run in Docker

### 1. Build Docker image

```bash
docker build -t pytest_runner .
```

### 2. Run tests in container

```bash
docker run -v $(pwd)/output/test_result:/output/test_result pytest_runner
```

### 3. Open Allure report

After container run:

```bash
allure serve output/test_result
```

---

## 🧩 Pytest Configuration (`pytest.ini`)

* `testpaths = tests` → where tests are located
* `addopts` → default options (allure results, HTML report, verbosity)
* `markers` → custom tags for test selection (smoke, regression, run)

---

## 📊 Example Allure Report

Each page action is logged as a separate **Allure step**:

* "Open home page"
* "Click Signup/Login button"
* "Enter email and password"
* "Verify account info banner is visible"


📌 Live example: [Allure Report](https://kovalillia.github.io/ui-autotests/)


---

## ✅ Roadmap

* Add GitHub Actions workflow for CI/CD runs
* Add parallel cross-browser testing (Firefox, Edge)
* Integrate with cloud grids (e.g. BrowserStack, Selenoid)

---

## 🤝 Contribution

1. Fork the repo
2. Create feature branch (`git checkout -b feature/my-feature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feature/my-feature`)
5. Open Pull Request

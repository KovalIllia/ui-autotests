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

## ⚙️ Setup & Installation

### 1. Local environment

```bash
git clone https://github.com/<your-username>/ui-autotests.git
cd ui-autotests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 2.Install Chrome & ChromeDriver
```
## Install Google Chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install -y google-chrome-stable

## Install ChromeDriver (automatically detects Chrome version)
CHROME_VERSION=$(google-chrome-stable --version | awk '{print $3}' | cut -d '.' -f 1)
BASE_URL="https://googlechromelabs.github.io/chrome-for-testing"
CHROMEDRIVER_VERSION=$(curl -s "${BASE_URL}/LATEST_RELEASE_${CHROME_VERSION}")
DOWNLOAD_URL="https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip"

wget -q "$DOWNLOAD_URL" -O chromedriver.zip
unzip -q chromedriver.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```

### 3.Install Allure CLI
```
sudo apt-get install -y default-jre
wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz
sudo tar -xzf allure-2.27.0.tgz -C /opt/
sudo ln -sf /opt/allure-2.27.0/bin/allure /usr/bin/allure
```


### 4. Run tests locally

```bash
pytest -v -s --alluredir=output/allure/allure-results
```

### 5. Generate Allure report

```bash
allure generate output/allure/allure-results --clean -o output/allure/allure-report
allure open output/allure/allure-report
```

Or simply run prepared script:

```bash
./output/scripts/run_tests.sh
```



# ☁️ CI/CD Workflow Simulation (Advanced)

To test GitHub Actions Workflow locally before pushing to the master branch, the act tool is used. This allows you to simulate the entire CI pipeline in a Docker environment, ensuring that the CI configuration works flawlessly.

This is a best practice to speed up the development cycle and avoid "CI bugs".

### 1. Install act

`curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash`

This command downloads and installs the act binary.

### 2. Image preparation Runner'а

`act`--- uses Docker images to simulate a GitHub environment. This image (catthehacker/ubuntu:act-latest) is an optimized version for faster startup.

`sudo docker pull catthehacker/ubuntu:act-latest`


### 3. Launching a specific _**`Job`**_ with the correct **_`Runner`_**

This command runs only the necessary job (`test`) from our Workflow `(.github/workflows/pytest.yml)`, використовуючи попередньо завантажений Docker-образ.

`act:` The main command is `act.`

`-P ubuntu-latest=...: ` -- Determines which Docker image to use for simulation `ubuntu-latest Runner'а`.

`-j test:` Runs only the `job` named test (not all of the jobs in the file).

`act -P ubuntu-latest=catthehacker/ubuntu:act-latest -j test`


### 4.Restart (Fast Rerun)

After the first run, act creates a container. To run Workflow again without recreating this container (and save time), use the flag `--reuse.`

`act --reuse`


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

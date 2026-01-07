# 🚀 Unified Mobile Python Engine (SOTA 2025-2026)

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Appium](https://img.shields.io/badge/appium-2.x-orange)
![License](https://img.shields.io/badge/license-MIT-green)
[![Python Quality Check](https://github.com/GitHubMaster07/Unified-Mobile-Python-Engine/actions/workflows/main_check.yml/badge.svg)](https://github.com/GitHubMaster07/Unified-Mobile-Python-Engine/actions/workflows/main_check.yml)

A high-performance, strictly typed mobile automation engine built for the 2025-2026 tech landscape. Designed with a **Modular High-End Architecture**, this project focuses on industrial-grade scalability, containerization, and observability.

---

## 🏗 Modular Architecture
The engine follows a decoupled layered approach to ensure zero-leakage between logic and infrastructure:
* **`framework/`**: Core engine, WebDriver lifecycles, and robust Driver Factory.
* **`app/`**: Application-specific logic (Page Object Model / Screen Objects).
* **`config/`**: **Fail-fast** environment validation via **Pydantic v2**.
* **`tests/`**: Atomic test execution powered by Pytest fixtures.

## 🛠 Tech Stack & DevOps
* **Core**: Python 3.12+ (Strict Type Hinting)
* **Driver**: Appium 2.x (UiAutomator2)
* **Infrastructure**: BrowserStack Real Device Cloud
* **Validation**: Pydantic v2 (Settings validation at runtime)
* **CI/CD**: GitHub Actions (Automated PEP8 Quality Gates)
* **Containerization**: Docker-ready for cross-platform orchestration
* **Observability**: **Allure Reports** for advanced execution analytics

## 🚀 Quick Start

### 1. Environment Setup (Local)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
---

### 2. Containerized Execution (Docker)
```PowerShell
docker build -t mobile-engine .
docker run mobile-engine
```

---

### 3. Run Tests & Generate Reports
``` PowerShell
# Run tests
$env:PYTHONPATH="."; pytest --alluredir=allure-results

# Serve Allure Report
allure serve allure-results
```
---

### 📊 Cloud Monitoring & Observability
Integration with BrowserStack App Automate provides:

🎥 Live Video Streams of test execution.

📋 Device Logs & Appium Inspector data.

📈 Allure Dashboards for stakeholder reporting.

### 🌌 Roadmap to "QA Space Program"
This foundation is built to evolve. The following phases define the transition from Senior-level automation to an autonomous ecosystem:
```
[x] Phase 1: Foundation — Robust Driver Factory, Base Screen abstractions, CI/CD, and Dockerization.

[ ] Phase 2: Self-Healing AI — Integration of local LLMs/Computer Vision to recover broken selectors.

[ ] Phase 3: Visual Regression 2.0 — Pixel-perfect layout testing using OpenCV and Figma API.

[ ] Phase 4: Contract-Driven UI Testing — Aligning mobile UI tests with Backend API schemas.
```
Developed by **Sergei Volodin**

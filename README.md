![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Appium](https://img.shields.io/badge/appium-2.x-orange)
![License](https://img.shields.io/badge/license-MIT-green)
[![Python Quality Check](https://github.com/GitHubMaster07/Unified-Mobile-Python-Engine/actions/workflows/main_check.yml/badge.svg)](https://github.com/GitHubMaster07/Unified-Mobile-Python-Engine/actions/workflows/main_check.yml)


# 🚀 Unified Mobile Python Engine (SOTA 2025-2026)

A high-performance, strictly typed mobile automation framework built with Python 3.12+ and Appium 2.x. This engine is designed with a **Modular High-End Architecture**, focusing on scalability, fail-fast configuration, and future AI integration.



## 🏗 Modular Architecture

The project follows a decoupled layered approach to ensure maintainability and clean code:

* **`framework/`**: The core infrastructure layer. Handles WebDriver lifecycles, base element interactions, and advanced W3C Actions.
* **`app/`**: Application-specific logic. Implements the Page Object Model (Screens) and reusable UI components.
* **`config/`**: Environment validation via **Pydantic v2**. Ensures settings are validated at runtime before any tests execute.
* **`tests/`**: Atomic test cases powered by Pytest fixtures and parallel execution.

## 🛠 Tech Stack (2025+ Standards)

* **Core**: Python 3.12+ (Strict Type Hinting)
* **Driver**: Appium 2.x (UiAutomator2)
* **Infrastructure**: BrowserStack Real Device Cloud
* **Validation**: Pydantic v2 (Fail-fast Settings validation)
* **Execution**: Pytest with customized `conftest.py` hooks

## 🚀 Quick Start

### 1. Environment Setup
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
---

### 2. Configure Cloud Credentials
- Copy config/env.yaml.example to config/env.yaml.

- Insert your userName and accessKey obtained from the BrowserStack dashboard.

---

### 3. Run Smoke Tests:
``` PowerShell
$env:PYTHONPATH="."; pytest tests/smoke/test_sample.py -s
```
---

### 📊 Cloud Monitoring
Once execution begins, live video streams, device logs, and Appium inspector data are available via the BrowserStack App Automate Dashboard.

### 🌌 Roadmap to "QA Space Program"
This foundation is built to evolve. The following phases define the transition from Senior-level automation to an autonomous ecosystem:
```
[x] Phase 1: Foundation (Current) — Robust Driver Factory, Base Screen abstractions, and Typed Configs.

[ ] Phase 2: Self-Healing AI — Integration of local LLMs/Computer Vision to recover broken selectors.

[ ] Phase 3: Visual Regression 2.0 — Pixel-perfect layout testing using OpenCV and Figma API.

[ ] Phase 4: Contract-Driven UI Testing — Aligning mobile UI tests with Backend API schemas.
```
Developed by **Sergei Volodin**

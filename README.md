# 🛒 Sauce Hero: E-commerce Automation Framework

An End-to-End (E2E) test automation framework built with **Python** and **Playwright**, designed to validate critical business flows on the *SauceDemo* e-commerce platform.

## 🏗️ Architecture: Page Object Model (POM)
This project moves away from simple scripting to a scalable, object-oriented architecture:
* **`pages/`**: Encapsulates UI locators and interactions (Login, Inventory, Checkout).
* **`tests/`**: Contains pure business logic and assertions, decoupled from UI details.
* **`config/`**: Centralized configuration via `pytest.ini`.

## 🚀 Key Scenarios Automated
1.  **Authentication:** Valid login & Locked-out user validation.
2.  **Shopping Flow:** Dynamic item selection and cart management.
3.  **Checkout Process:** Form filling, payment flow, and "Thank You" page validation.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **Core:** Playwright (Sync API)
* **Runner:** Pytest
* **Pattern:** Page Object Model (POM)

## ⚙️ How to Run
1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```
2.  **Execute Tests:**
    ```bash
    # Runs all tests in headed mode with slow-mo for visualization
    python -m pytest
    ```
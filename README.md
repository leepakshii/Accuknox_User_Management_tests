# OrangeHRM User Management Automation (Playwright + Python)

##  Overview
This project automates end-to-end testing of the **User Management module** in the [OrangeHRM Demo Application](https://opensource-demo.orangehrmlive.com/).

It was developed as part of the **AccuKnox QA Trainee Practical Assessment** to demonstrate manual and automation testing skills using Playwright and the Page Object Model (POM) design.

---

##  Features Covered

| Test Case ID | Description |
|---------------|-------------|
| TC01 | Login with valid credentials |
| TC02 | Navigate to Admin Module |
| TC03 | Add a new user |
| TC04 | Search for the newly created user |
| TC05 | Edit user details |
| TC06 | Validate updated details |
| TC07 | Delete user |

---

##  Tech Stack
- **Language:** Python  
- **Automation Tool:** Playwright  
- **Test Runner:** Pytest  
- **Design Pattern:** Page Object Model (POM)

---

##  Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/orangehrm_automation.git
   cd orangehrm_automation
2. Create Virtual Environment

python -m venv venv
source venv/Scripts/activate

3. Install Dependencies

pip install playwright pytest
playwright install

4. Run Tests

pytest tests/ -v
Playwright v1.47+ (Python)
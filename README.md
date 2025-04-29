
1. How to run the scrip: 
   pytest -v -s tests/test_login.py
   pytest -v -s tests/test_form_submission.py
   pytest -v -s tests/test_checkout.py

2. Generate the allure report: 
   pytest -v -s tests/test_form_submission.py --alluredir=reports/allureReport

3. View the allure report: 
   allure serve reports/allureReport

4. View the Html Report
   pytest --html=reports/report.html


    





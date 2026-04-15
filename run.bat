python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pytest -s -v --html=./reports.html test_cases/ --browser chrome
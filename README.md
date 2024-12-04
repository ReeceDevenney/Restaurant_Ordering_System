### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Populate table
at api/mockDataScript.sql there is an sql script to populate your table with mock data.  run it inside of mysql workbench to populate your tables.

Intentionally left out orders and reviews information for you to fill out and test yourself using our CRUD operations.

### Video Presentation:
https://github.com/user-attachments/assets/7ef226d3-acd4-439a-b7c8-1215562b2eee

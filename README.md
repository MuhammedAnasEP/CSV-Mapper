# CSV Mapper

This is a FastAPI project that allows users to upload a CSV file, map the Name and Age columns on the frontend, and save the data to an SQLite database.

### Setup

1. Clone the repository:

   git clone https://github.com/MuhammedAnasEP/CSV-Mapper.git
   
2. Navigate to Project foder
    cd CSV-Mapper

3. Create Virtual Environment

    virtualenv venv

3. Activate Virtual environment

    source venv/bin/activate

4. Install dependencies

    pip install -r requirements.txt

### Run Appliction

1. uvicorn main:app --reload

2. Open your browser and go to http://127.0.0.1:8000 to access the application.

### Usage

1. Visit the root endpoint http://127.0.0.1:8000 to access the CSV upload form.

2. Choose the CSV file.

3. Click the "Submit" button to submit the form.


### Dependencies

1. fastapi
2. uvicorn[standard]
3. sqlalchemy
4. python-multipart
5. jinja2


###### Note :

I not uploaded virtual environment folder to github so create it if needed also not uploaded sqlite dabase file it will create automatically in runtime otherwise just create csv.db file inside the CSV-Mapper.
        
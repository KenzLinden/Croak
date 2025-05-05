import os
from dotenv import load_dotenv
from fastapi import FastAPI
import psycopg2

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

app = FastAPI()

@app.get('/')
async def root():
    return{'message': "Hello World"}

@app.get('/test-conn')
def test_conn():
    try:
        conn = psycopg2.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        conn.close()
        return{"message": f"Connected successfully! PSQL Version: {db_version}"}
    except Exception as e:
        return {"error": str(e)}
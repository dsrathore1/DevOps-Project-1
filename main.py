from fastapi import FastAPI
import csv

app = FastAPI()


@app.get("/")
async def root_page():
    return {
        "message": "Hello, World. I am DevOps Project",
        "goto data check on server": "http://3.7.47.188/data",
        "local data check" : "http://127.0.0.1:8000/data",
        "status": 200,
    }


@app.get("/data")
async def data_check():
    with open("MOCK_DATA.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        data = {row["id"]: row for row in reader}
    return {"Data": data}

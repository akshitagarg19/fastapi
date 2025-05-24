from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students = []
with open("q-fastapi.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
def get_students(class_: Optional[str] = Query(default=None, alias="class")):
    if class_:
        classes = class_.split(",")  # Split comma-separated string into list
        filtered = [s for s in students if s["class"] in classes]
        return {"students": filtered}
    return {"students": students}

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, crud, database
import uuid

app = FastAPI()

@app.on_event("startup")
def startup_event():
    database.Base.metadata.create_all(bind=database.engine)

@app.post("/trigger_report/")
def trigger_report(db: Session = Depends(database.get_db)):
    report_id = str(uuid.uuid4())
    # Logic to start the report generation process
    return {"report_id": report_id}

@app.get("/get_report/")
def get_report(report_id: str, db: Session = Depends(database.get_db)):
    # Logic to check report status or return the report
    return {"status": "Running" or "Complete", "report": "file.csv"}

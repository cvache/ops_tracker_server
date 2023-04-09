from fastapi import FastAPI
from pydantic import BaseModel

class TrackerItem(BaseModel):
    id: str
    project: str
    level: str
    timestamp: str | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/tracker")
async def tracker(trackerData: TrackerItem):
    return trackerData


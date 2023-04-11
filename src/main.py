from fastapi import FastAPI
from pydantic import BaseModel

class TrackerItem(BaseModel):
    id: str
    project: str
    level: str
    timestamp: str | None = None

eventTracker = {}
inProgress = []

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/tracker")
async def tracker(trackerData: TrackerItem):
    id = trackerData.id
    level = trackerData.level
    timestamp = trackerData.timestamp
    
    #add start
    if level == "START":
        inProgress.append(id)
        eventTracker[id] = []
        eventTracker[id].push({
        "level": level,
        "timestamp": timestamp
        })
        return {
            "statusCode": "200",
            "message": "Operation started"
        }

    if id not in inProgress:
        return {
            "statusCode": "404",
            "message": "Operation is not being tracked. Has it been started?"
        }
    
    eventTracker[id].push({
        "level": level,
        "timestamp": timestamp
    })

    if level == "END":
        payload = eventTracker[id].reverse()
        inProgress.remove(id)
        eventTracker.pop(id)

        return {
            "statusCode": "200",
            "message": "Operation finished"
        }


        
        
    return {
        "statusCode": "200",
        "message": "Operation added"
    }



import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

db = [
    {"id": 1, "name": "Run Game Price Checks", "state": "not_started", "priority": 5},
    {"id": 2, "name": "Run Show Price Checks", "state": "running", "priority": 5},
    {"id": 3, "name": "Run GPU Price Checks", "state": "complete", "priority": 1}
]


@app.get("/")
def home():
    return {'message': "FastAPI Demo"}


@app.get("/api/workflows")
def get_workflows(state: str = None, priority: int = None) -> list:
    result = db

    if priority:
        result = [wf for wf in result if wf['priority'] >= priority]

    if state:
        result = [wf for wf in result if wf['state'] == state]

    return result


@app.get("/api/workflows/{id}")
def workflow_by_id(id: int) -> dict:
    result = [wf for wf in db if wf['id'] == id]
    if result:
        return result[0]

    raise HTTPException(status_code=404, detail=f"No workflow found for id '{id}'")


if __name__ == "__main__":
    uvicorn.run("workflows:app", reload=True)

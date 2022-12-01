import uvicorn
from fastapi import FastAPI

from routers.workflow_router import WorkflowRouter

app = FastAPI(title="FastAPI Demo")

# Add Routers
app.include_router(WorkflowRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

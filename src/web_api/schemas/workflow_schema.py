from pydantic import BaseModel


class WorkflowResponseSchema(BaseModel):
    id: int
    name: str
    state: str
    priority: int

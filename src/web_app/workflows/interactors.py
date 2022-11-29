class GetAllWorkflowsInteractor:

    def __init__(self, workflows_repo):
        self.workflows_repo = workflows_repo

    def execute(self):
        return self.workflows_repo.list()

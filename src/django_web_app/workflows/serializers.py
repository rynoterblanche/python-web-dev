class WorkflowsListSerializer:

    @staticmethod
    def serialize(workflows):
        return [WorkflowSerializer.serialize(workflow) for workflow in workflows]


class WorkflowSerializer:

    @staticmethod
    def serialize(workflow):
        return {
            'name': str(workflow.name)
        }

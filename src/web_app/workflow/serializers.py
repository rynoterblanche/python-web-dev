class WorkflowsListSerializer:

    @staticmethod
    def serialize(workflows):
        return [WorkflowSerializer.serialize(workflow) for workflow in workflows]


class WorkflowSerializer:

    @staticmethod
    def serialize(workflow):
        return {
            'id': str(workflow.id),
            'name': str(workflow.name),
            'is_complete': str(workflow.is_complete)
        }

class Task:
    def __init__(self, task_id, label, completed=False):
        self.task_id = task_id
        self.label = label
        self.completed = completed

    
    def mark_completed(self):
        self.completed = True


    def serialize(self):
        return {
            "id": self.task_id,
            "label": self.label,
            "completed": self.completed
        }
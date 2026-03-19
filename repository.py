import csv
import os

from models import Task

class TaskRepository:
    def __init__(self, filename):
        self.filename = filename
        self.task = []
        # consultar si existen tareas en un csv (DB)
        self.load_task()

    def get_next_id(self):
        if not self.task:
            return 1
        return max(task.task_id for task in self.task) + 1 

    def load_task(self):
        if not os.path.exists(self.filename):
            self.task = []
            return

        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.task = [
                Task(
                    task_id=int(row["id"]),
                    label=row["label"],
                    completed=row["completed"].strip().lower() == "true"
                ) for row in reader
            ]

    def save_task(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'label', 'completed']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.task:
                writer.writerow(task.serialize())

    def get_tasks(self):
        return self.task

    def add_task(self, label):
        task = Task(task_id=self.get_next_id(), label=label, completed=False)
        self.task.append(task)
        self.save_task() # guarda la tarea 

        


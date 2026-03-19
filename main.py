from app import TodoApp
from repository import TaskRepository


if __name__ =="__main__":
    # correr nuestra app
    repository = TaskRepository("tasks.csv")
    app = TodoApp(repository)
    app.run()
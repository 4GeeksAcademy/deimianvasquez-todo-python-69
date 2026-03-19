class TodoApp:
    def __init__(self, repository=None):
        self.repository = repository # La data la guarda este repositorio

    def show_menu(self):
        width = 55
        border = "+" + "-" * width + "+"

        print("\n" + border)
        print("|" + "TO DO LIST APP".center(width) + "|")
        print(border)
        print("|" + "Bienvenido. Selecciona una opcion del menu:".ljust(width) + "|")
        print("|" + "".ljust(width) + "|")
        print("|" + " 1) Agregar tarea".ljust(width) + "|")
        print("|" + " 2) Ver tareas".ljust(width) + "|")
        print("|" + " 3) Marcar tarea como completada".ljust(width) + "|")
        print("|" + " 4) Eliminar tarea".ljust(width) + "|")
        print("|" + " 5) Salir".ljust(width) + "|")
        print(border)

    def add_task(self):
        label = input("Ingrese la descripción de la tarea: ").strip()

        if not label:
            print("La tarea no debe estar vacía")
            return

        self.repository.add_task(label)
        print("Tarea guardada exitosamente.")

    def show_tasks(self):
        if not self.repository.get_tasks():
            print("NO hay tareas para mostrar")
            return

        print("\nTareas:")
        for task in self.repository.get_tasks():
            status = "✓" if task.completed else "✗"
            print(f"{task.task_id}. [{status}] {task.label}")


    def run(self):
        while True:
            self.show_menu()

            choice = input("Selecciona una opción: ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                print("Marcarla como completada")
            elif choice == "4":
                print("Eliminarla")
            elif choice == "5":
                print("Saliendo de la aplicación...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")




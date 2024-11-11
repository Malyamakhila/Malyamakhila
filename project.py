import json

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        self.tasks.append(Task(len(self.tasks) + 1, title))

    def view_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f"{task.id}. {task.title} - {status}")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def mark_task_complete(self):
        task_id = int(input("Enter task ID to mark as complete: "))
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True

    def save_tasks(self):
        tasks_json = json.dumps([{"id": task.id, "title": task.title, "completed": task.completed} for task in self.tasks])
        with open("tasks.json", "w") as file:
            file.write(tasks_json)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_json = file.read()
                tasks = json.loads(tasks_json)
                self.tasks = [Task(task["id"], task["title"], task["completed"]) for task in tasks]
        except FileNotFoundError:
            pass

def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.delete_task()
        elif choice == "4":
            task_manager.mark_task_complete()
        elif choice == "5":
            task_manager.save_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import json
import os

class TodoList:
    def _init_(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "✓" if task['completed'] else "✗"
                print(f"{index}. [{status}] {task['task']}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
            self.save_tasks()
        else:
            print("Task not found.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Task not found.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
        else:
            print("Task not found.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task description: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.view_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if _name_ == "_main_":
    main()

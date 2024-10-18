class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_complete(self):
        self.is_completed = True

    def update(self, title=None, description=None):
        if title:
            self.title = title
        if description:
            self.description = description

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"Task: {self.title} | Description: {self.description} | Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n--- To-Do List ---")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def update_task(self, index, title=None, description=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.update(title, description)
            print(f"Task {index + 1} updated successfully!")
        else:
            print("Invalid task number!")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.mark_complete()
            print(f"Task {index + 1} marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' deleted successfully!")
        else:
            print("Invalid task number!")


def user_interface():
    to_do_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            task = Task(title, description)
            to_do_list.add_task(task)

        elif choice == '2':
            to_do_list.view_tasks()

        elif choice == '3':
            to_do_list.view_tasks()
            try:
                index = int(input("Enter task number to update: ")) - 1
                title = input("Enter new task title (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                to_do_list.update_task(index, title, description)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == '4':
            to_do_list.view_tasks()
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                to_do_list.mark_task_complete(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == '5':
            to_do_list.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                to_do_list.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == '6':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    user_interface()


# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task ():

    def __init__(self, description, term):
        self.description = description
        self.term = term
        self.status = False

    def mark_status(self):
        self.status=True

    def __str__(self):
        status_completed = 'выполнено' if self.status else 'не выполнено'
        return f"Задача: {self.description}, Срок {self.term}, Статус {status_completed}"

def addition(task_list, description, term):
    task = Task(description, term)
    task_list.append(task)


def complete_task(task_list, index):
    if 0<= index < len(task_list):
        task_list[index].mark_status()
    else:
        print('Неверный номер задачи')

def show_current_tasks(task_list):
    print("Текущие задачи:")
    for task in task_list:
        if not task.status:
            print(task)
tasks = []


addition(tasks, "Купить молоко", "2024-12-31")
addition(tasks, "Позвонить другу", "2024-12-31")
addition(tasks, "Починить машину", "2024-12-31")

show_current_tasks(tasks)

complete_task(tasks, 0)

show_current_tasks(tasks)
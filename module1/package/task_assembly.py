from package.constants import STATUS, PRIORITY
from package.save_tasks import save_tasks

def task_assembly(tasks):
    task_number = len(tasks) + 1
    task_title = input("Введите заголовок задачи: ")
    task_description = input("Введите описание задачи: ")
    task_priority = input("Введите приоритет (1 - низкий, 2 - средний, 3 - высокий): ")
    task_status = input("Введите статус задачи (1 - новая, 2 - в процессе, 3 - завершена): ")

    tasks[task_number] = {
        "Заголовок": task_title,
        "Описание": task_description,
        "Приоритет": PRIORITY.get(task_priority, "low"),
        "Статус": STATUS.get(task_status, "new")
    }
    save_tasks(tasks)
    print(f"Задача номер {task_number} была успешно добавлена")
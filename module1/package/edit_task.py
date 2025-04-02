from package.constants import STATUS, PRIORITY
from package.view_task import view_task
from package.save_tasks import save_tasks


def edit_task(tasks):
    view_task(tasks)
    task_to_edit = input("Выберите задачу для редактирования: ")

    if task_to_edit in tasks:
        task_title = input("Введите заголовок задачи: ")
        task_description = input("Введите описание задачи: ")
        task_priority = input("Введите приоритет (1 - низкий, 2 - средний, 3 - высокий): ")
        task_status = input("Введите статус задачи (1 - новая, 2 - в процессе, 3 - завершена): ")

        tasks[task_to_edit] = {
            "Заголовок": task_title,
            "Описание": task_description,
            "Приоритет": PRIORITY.get(task_priority, "low"),
            "Статус": STATUS.get(task_status, "new")
        }
        save_tasks(tasks)
        print("Задача была успешно обновлена!")
    else:
        print("Такой задачи нет(")

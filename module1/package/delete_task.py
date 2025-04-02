from package.view_task import view_task
from package.save_tasks import save_tasks
def delete_task(tasks):
    view_task(tasks)
    task_to_delete = input("Выберите задачу для удаления: ")

    if task_to_delete in tasks:
        del tasks[task_to_delete]
        save_tasks(tasks)
        print("Задача была успешно удалена!")
    else:
        print("Такой задачи нет( ")

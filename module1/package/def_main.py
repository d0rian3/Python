from package.load_tasks import load_tasks
from package.task_assembly import task_assembly
from package.view_task import view_task
from package.edit_task import edit_task
from package.delete_task import delete_task


def main():
    tasks = load_tasks()
    while True:
        first_choice = input(
            "Выберите действие:\n- 1 - Создать новую задачу\n- 2 - Просмотреть задачи\n- 3 - Обновить задачу\n- 4 - Удалить задачу\n- 0 - Выйти из программы\n")
        match first_choice:
            case "1":
                print("Вы выбрали функцию создания новой задачи, сделайте следующие действия.")
                task_assembly(tasks)
            case "2":
                print("Вы выбрали функцию просмотра всех задач:")
                view_task(tasks)
            case "3":
                print("Вы выбрали функцию обновления задачи. Доступные задачи:\n")
                edit_task(tasks)
            case "4":
                print("Вы выбрали функцию удаления задачи. Доступные задачи:\n")
                delete_task(tasks)
            case "0":
                print("Выход из программы...")
                break
            case _:
                print("Ошибка: Некорректный ввод. Попробуйте снова.")
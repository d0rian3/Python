def view_task(tasks):
    if not tasks:
        print("Данной задачи нет, увы(")
    for task_id, task_info in tasks.items():

        print(f"Задача {task_id}: \n{task_info['Заголовок']}: {task_info['Описание']}, \n Приоритет задачи: {task_info['Приоритет']},\n Статус задачи: {task_info['Статус']}")

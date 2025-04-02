def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task_id, task in tasks.items():
            file.write(
                f"{task_id} | {task['Заголовок']} | {task['Описание']} | {task['Приоритет']} | {task['Статус']}\n")
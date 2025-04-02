"""
    Функция загрузки задач
"""

def load_tasks():
    tasks = {}
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    task_id, title,description, priority, status =parts
                    tasks[task_id] = {
                        "Заголовок": title,
                        "Описание": description,
                        "Приоритет": priority,
                        "Статус": status
                    }
    except FileNotFoundError:
        pass
    return tasks
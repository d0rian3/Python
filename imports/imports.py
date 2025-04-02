from test.a import func_1
from test.b import func_2
from test import a,b
import os

# Получить текущую рабочую директорию
current_dir = os.getcwd()
print("Текущая рабочая директория:", current_dir)

# Изменить текущую рабочую директорию
new_dir = '/tmp'
os.chdir(new_dir)
print("Рабочая директория изменена на:", os.getcwd())

# Список файлов и директорий в текущей директории
files = os.listdir('.')
print("Файлы и директории в текущей директории:", files)

# Создание новой директории
new_dir_name = 'new_dir'
if not os.path.exists(new_dir_name):
    os.mkdir(new_dir_name)
    print("Создана директория:", new_dir_name)

# Удаление файла
file_name = 'test.txt'
if os.path.exists(file_name):
    os.remove(file_name)
    print("Файл удален:", file_name)
else:
    print("Файл не существует:", file_name)


from collections import Counter, defaultdict, deque, namedtuple

# Counter
text = "abracadabra"
counter = Counter(text)
print("Подсчет символов в строке 'abracadabra':", counter)

# defaultdict
def_dict = defaultdict(int)
def_dict['apple'] += 1
print("defaultdict с начальным значением int:", def_dict)

# deque
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print("Очередь deque после добавления элементов:", queue)

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("Координаты точки:", p.x, p.y)

from datetime import date, datetime, timedelta

# Текущая дата
today = date.today()
print("Текущая дата:", today)

# Текущее время
now = datetime.now()
print("Текущее время:", now)

# Вычисление разницы во времени
delta = timedelta(days=7)
next_week = today + delta
print("Дата через неделю:", next_week)

# Форматирование даты
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Форматированная дата и время:", formatted_date)

# Парсинг даты из строки
date_str = "2024-07-23"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Парсинг даты из строки:", parsed_date)



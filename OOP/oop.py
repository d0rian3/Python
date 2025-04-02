"""
Создайте класс Student с такими полями:

Имя
Возраст
Список оценок

И класс Group:
список Student
название
Эти два класса нам понадобятся на следующем занятии


1)К созданному на прошлом занятии классу студент,
задаем ему имя, возраст и оценки, через __init__

2)Добавляем метод для добавления оценки
3)Добавляем метод(ы) вычисления среднего балла

4)Прописываем меджик метод (или методы) которые
позволяют найти студента с наилучшим средним балом из списка

5)Берем класс группы из прошлого занятия
6)Добавляем возможность добавить студента к группе
7)Добавляем возможность удалить студента из группы
8)Добавляем возможность найти группу в которой учится студент
с самым высоким средним баллом
"""

class Student:

    def __init__(self, name: str, age: int, marks:list[int]) -> None:
        self.marks = marks
        self.name = name
        self.age = age

    def is_possible_to_add_new_mark(self, marks: list) -> bool:
        if len(self.marks) >= 7:
            print("У этого студента слишком много оценок")
            return False
        else:
            print("Добавление оценки разрешено")
            return True

    def _append_marks(self, marks:list, mark:int)->None:
        if self.is_possible_to_add_new_mark(self.marks):
            self.marks.append(mark)
        else:
            raise ValueError("Нельзя добавить оценку")

    def average_mark(self, marks:list) -> float:
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def __gt__(self, other: "Student") -> bool:
        return self.average_mark() > other.average_mark()

class Group:

    def __init__(self, name: str, students: list[Student] = None) -> None:
        self.name = name
        self.students = students if students else []

    def add_student(self, student: Student) -> None:
        self.students.append(student)
    def delete_student(self, student: Student)->None:
        self.students.remove(student)
    def best_student(self)-> Student:
        return max(self.students, key=lambda student: student.average_mark())



"""
Описываем телефон:

Класс телефон. У него должны быть:

Поле для описания номера.
Метод, чтобы задать номер телефона.
Защищенное поле для счетчика входящих звонков.
Метод, который вернет нам количество принятых звонков.
Метод принять звонок, который добавляет к счетчику единицу.
Создайте три разных объекта телефона.

Поменяйте всем изначальный номер.

Примите по несколько звонков на каждом (разное количество)

Напишите функцию, которая принимает список из объектов телефонов, а возвращает общее количество принятых звонков со всех телефонов.
"""


class Phone:
    number: str = ""
    _call_count: int = 0

    def set_number(self, new_number:str)->None:
        self.number = new_number

    def calls(self) -> int:
        return self._call_count

    def call_accept(self) -> None:
        self._call_count+=1

ph1 = Phone
ph2 = Phone
ph3 = Phone

ph1.set_number("13123")
ph2.set_number("31318")
ph3.set_number("86970")


def make_n_calls(n:int, ph:Phone)->None:
    for _ in range(n):
        ph.call_accept()

make_n_calls(4, ph1)
make_n_calls(6, ph2)
make_n_calls(8, ph3)

def total_calls(phones: list[Phone]) -> int:
    return sum(ph.calls() for ph in phones) #! Разобраться
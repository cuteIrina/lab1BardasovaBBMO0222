# Часть 2

class Student:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.transcript = []

class TranscriptEntry:
    def __init__(self, subject, exam_date, professor, grade):
        self.subject = subject
        self.exam_date = exam_date
        self.professor = professor
        self.grade = grade

# Функция для сортировки списка студентов по оценке по указанному предмету
def sort_students_by_grade(students, subject):
    return sorted(students, key=lambda student: get_grade_by_subject(student, subject), reverse=True)

# Функция для получения оценки студента по указанному предмету
def get_grade_by_subject(student, subject):
    for entry in student.transcript:
        if entry.subject == subject:
            return entry.grade
    return None

# Ввод данных о студентах
def input_students(num_students):
    students = []
    for _ in range(num_students):
        first_name = input("Введите имя студента: ")
        last_name = input("Введите фамилию студента: ")
        birth_date = input("Введите дату рождения студента (гггг-мм-дд): ")
        student = Student(first_name, last_name, birth_date)
        num_subjects = int(input("Введите количество предметов в зачетке студента: "))
        for _ in range(num_subjects):
            subject = input("Введите название предмета: ")
            exam_date = input("Введите дату экзамена (гггг-мм-дд): ")
            professor = input("Введите ФИО преподавателя: ")
            grade = float(input("Введите оценку по предмету: "))
            entry = TranscriptEntry(subject, exam_date, professor, grade)
            student.transcript.append(entry)
        students.append(student)
    return students

# Вывод таблицы студентов
def print_students_table(students):
    print("ФИО\t\t\tДата рождения")
    print("----------------------------------------")
    for student in students:
        full_name = student.last_name + " " + student.first_name
        birth_date = student.birth_date
        print(f"{full_name:<20}\t{birth_date}")

# Ввод количества студентов
num_students = int(input("Введите количество студентов: "))

# Ввод данных о студентах
students = input_students(num_students)

# Ввод предмета для сортировки
subject_to_sort = input("Введите название предмета для сортировки: ")

# Сортировка студентов по указанному предмету
sorted_students = sort_students_by_grade(students, subject_to_sort)

# Вывод таблицы студентов
print_students_table(sorted_students)

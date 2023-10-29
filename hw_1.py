class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lr:
                lecturer.grades_lr[course] += [grade]
            else:
                lecturer.grades_lr[course] = [grade]
        else:
            return 'Ошибка'
        
    def arith_mean_st(self):
        for key, values in self.grades.items():
            avg = sum(values) / len(values)
            return avg

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.arith_mean_st()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')  
    
    def __lt__(self, other):
        return self.arith_mean_st() < other.arith_mean_st()
 
     
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lr = {}
        

class Lecturer(Mentor):

    def arith_mean(self):
        for key, values in self.grades_lr.items():
            avg = sum(values) / len(values)
            return avg         
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.arith_mean()}')
    
    def __lt__(self, other):
        return self.arith_mean() < other.arith_mean()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname} ')
    
 
students = [Student('Alex', 'Shchelokov', 'male'), Student('Alisa', 'Petrova', 'female')]
students[0].courses_in_progress += ['Python', 'Git']
students[1].courses_in_progress += ['Python', 'Git']
students[0].finished_courses += ['Введение в программирование']
students[1].finished_courses += ['Компьютерная грамотность']

lecturers = [Lecturer('Aleksey', 'Frolov'), Lecturer('Seva', 'Cherepanov')]
lecturers[0].courses_attached += ['Python', 'Компьютерная грамотность']
lecturers[1].courses_attached += ['Python', 'Git']
 
cool_reviewer = Reviewer('Roman', 'Lomin')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(students[0], 'Python', 10)
cool_reviewer.rate_hw(students[0], 'Python', 10)
cool_reviewer.rate_hw(students[0], 'Python', 10)

cool_reviewer.rate_hw(students[1], 'Python', 9)
cool_reviewer.rate_hw(students[1], 'Python', 9)
cool_reviewer.rate_hw(students[1], 'Python', 9)

students[0].rate_lr(lecturers[0], 'Python', 5)
students[0].rate_lr(lecturers[0], 'Python', 5)
students[0].rate_lr(lecturers[0], 'Python', 5)

students[1].rate_lr(lecturers[1], 'Python', 6)
students[1].rate_lr(lecturers[1], 'Python', 6)
students[1].rate_lr(lecturers[1], 'Python', 6)

print(students[0].grades['Python'])
print(students[1].grades['Python'])
print(lecturers[0].grades_lr)
print(lecturers[1].grades_lr)
print(cool_reviewer)
print(lecturers[0])
print(lecturers[1])
print(lecturers[0] < lecturers[1])
print(students[0] < students[1])
print(students[0])
print(students[1])


def mean_hw(students_list, course):
    students_list = students
    all_grades = 0
    a = 0
    for student in students_list:
        for grade in student.grades[course]:
            all_grades += grade
            a += 1  
    mean_grades = all_grades / a
    return mean_grades
  
print(mean_hw(students, 'Python'))


def mean_lec(lecturers_list, course):
    lecturers_list = lecturers
    course = 'Python'
    all_grades = 0
    a = 0
    for lecturer in lecturers_list:
        for grade in lecturer.grades_lr[course]:
            all_grades += grade
            a += 1  
    mean_grades = all_grades / a
    return mean_grades    

print(mean_lec(lecturers, 'Python'))
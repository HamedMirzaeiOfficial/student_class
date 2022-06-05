class Student:
    student_list = list()
    def __init__(self):
        self.name = str()
        self.code = str()
        self.average = float()
        Student.student_list.append({'name': self.name, 'code': self.code, 'average': self.average})
        self.index = 0

    def set_data(self):
        self.name = input("Enter name of student: ")
        self.code = input("Enter code of student: ")
        self.average = float(input("Enter average of student: "))

    def set_average(self, average):
        self.average = average

    def get_code(self):
        return self.code

    def __str__(self):
        return f"name: {self.name}\tcode: {self.code}\taverage: {self.average}"

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(Student.student_list):
            student = self.student_list[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


def max_average(students):
    max_avg_student = Student()
    max_avg_student.set_average(0)
    for student in students:
        if student.average > max_avg_student.average:
            max_avg_student = student

    return max_avg_student


def print_students(students):
    for student in students:
        print(student)


def search(students, code):
    for student in students:
        if student.code == code:
            return student

    return False


def delete(students, code):
    student = search(students, code)
    if not student:
        print("there is no student with this code!!!")
    else:
        students.remove(student)
        print("student removed successfully")


def main():
    students = list()
    while True:
        choice = int(input("\n1-add student\n2-maximum average\n3-show all students\n4-search\n5-delete\n6-exit\n"))
        if choice == 1:
            student = Student()
            student.set_data()
            students.append(student)
            print("student add successfully\n")

        elif choice == 2:
            print('student with max average: ', max_average(students))

        elif choice == 3:
            print_students(students)

        elif choice == 4:
            code = input("Enter a code for search student: ")
            student = search(students, code)
            if not student:
                print("not found!!!")
            else:
                print(student)
        elif choice == 5:
            code = input("Enter a code for search student: ")
            delete(students, code)

        elif choice == 6:
            return 0

        else:
            print("wrong choice!!! try again.")


if __name__ == '__main__':
    main()


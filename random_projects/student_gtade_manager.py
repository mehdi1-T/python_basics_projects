def add_student():
    name = input("Enter student's name: ")
    grade = float(input("Enter student's grade: "))
    students[name] = grade

def show_student():
    print("Here's students :", students)

def show_top_student():
    print(max(students, key=students.get))

def show_average_grade():
    print('average grade: ',sum(students.values()) / len(students))

students = {}
   
while True:
    print("=====================================")
    print("🎓 STUDENT GRADE MANAGER")
    print("=====================================")
    print("1️⃣ Add a new student")
    print("2️⃣ Show all students")
    print("3️⃣ Show average grade")
    print("4️⃣ Show top student")
    print("5️⃣ Exit")
    print("=====================================")

    user = int(input("Please selcet one of these options: "))

    if user == 5:
        print("good, byyye")
        break
    elif user == 1:
        add_student()
    elif user == 2:
        show_student()
    elif user == 3:
        show_average_grade()
    elif user == 4:
        show_top_student()
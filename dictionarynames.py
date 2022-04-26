def get_student_names(students):
    lst = []
    for keys, val in students.items():
        lst.append(val)

    lst.sort()

    print(lst)

get_student_names({"Student 1" : "Steve", "Student 2" : "Becky", "Student 3" : "John"})

# method #2

def get_student_names(students):
    return sorted(students.values())
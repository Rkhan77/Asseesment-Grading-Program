
print('Welcome to Exam Evaluation Program')
assessments_num = int(input("How many assessments do you want to mark?: "))  # store number of assessments
print('No. of assessments saved:', assessments_num)

#list of variables
assessment_names = []  # a list to store assessment names e.g. Exams/Essay/Project
assessment_values = []  # a list to store assessment worth (100)
students = []  # a list to store number of students
student_names = []  # a list to store student names
std_marks = []  # a list to store total of student's marks
assessment_marks = []  # a student marks list for each subject
ind = 0


# function to calculate student grade
def calculate_grade(marks, total_marks):
    score = 100 * marks / total_marks
    if score < 50:
        return (str(marks) + " out of " + str(total_marks) + " is a Fail")
    elif 50 <= score < 60:
        return (str(marks) + " out of " + str(total_marks) + " is a Pass")
    elif 60 < score < 70:
        return (str(marks) + " out of " + str(total_marks) + " is a Credit")
    elif 70 < score < 80:
        return (str(marks) + " out of " + str(total_marks) + " is a Distinction")
    else:
        return (str(marks) + " out of " + str(total_marks) + " is a High Distinction")


# define function to return highest score in std_marks list
def max_in(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


# define function to return the index of highest mark
def el_in(list, element):
    if element in list:
        pos = list.index(element)
        return list.index(element)


def average_grade(avg_sc):
    if avg_sc < 50:
        return str("The class average is " + str(avg_sc) + " (Fail).")
    elif 50 <= avg_sc < 65:
        return str("The class average is " + str(avg_sc) + " (Pass).")
    elif 65 < avg_sc < 75:
        return str("The class average is " + str(avg_sc) + " (Credit).")
    elif 75 < avg_sc < 85:
        return str("The class average is " + str(avg_sc) + " (Distinction).")
    else:
        return str("The class average is " + str(avg_sc) + " (High Distinction).")

# Loop number of assessment time
for i in range(assessments_num):
    name = input("Enter name of assessments " + str(i + 1) + " : ")
    assessment_names.append(name)
    value = int(input("How many marks is the " + assessment_names[i] + " worth?: "))
    assessment_values.append(value)
    print(assessment_values[i])

if sum(assessment_values) == 100:
    print(" sum is equal to 100 so we continue...")
    students = int(input("How many students?: "))
    for row in range(students):
        std_name = input("What is the name of student " + str(row + 1) + ":")
        student_names.append(std_name)
        t_score = 0
        for i in range(assessments_num):
            assessment_marks.append(int(
                input("What did " + student_names[row] + " get in out of " + str(assessment_values[i]) + " in the " +
                      assessment_names[i] + "?")))
            k = i + (row * assessments_num)
            t_score += assessment_marks[i]
            std_marks.append(t_score)
            print(calculate_grade(t_score, assessment_values[i]))

    # average class performance/top student
    avg_sc = sum(std_marks) / students
    print(" All marks entered !")
    print(average_grade(avg_sc))
    max_val = max_in(std_marks)
    ind = el_in(std_marks, max_val)
    print(" The top student is " + student_names[ind] + " with a total mark of " + str(max_val) + "in" + assessment_names[ind])


#Prompt error if sum of assessment values not = 100
else:
    print(" Error:The sum of the assessment values do not add up to 100")

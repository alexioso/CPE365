# Mitchel Davis
# Alex Braksator

# April 7 2017
# Lab01 CPE 365

# Trivial Requirements Satisfied
# R1 - Python runs on lab machines
# R2 - No command line parameters are needed
# R3 - Language for Search instructions is implemented  See main loop and functions

import time

# Initializing arrays to store attributes of students
sLast = []
sFirst = []
grade = []
classroom = []
bus = []
gpa = []
tLast = []
tFirst = []

# Read the students.txt file and catch any exceptions
# Satisfies requirement R12
try:
    f = open('students.txt', 'r')
except Exception:
    print("Unable to open file\n")
    exit()
# Reads through the file and fills arrays with student info
for line in f.readlines():
    student = line.upper().split(',')
    sLast.append(student[0])
    sFirst.append(student[1])
    grade.append(student[2])
    classroom.append(student[3])
    bus.append(student[4])
    gpa.append(student[5])
    tLast.append(student[6])
    tFirst.append(student[7].rstrip())

f.close()


# Helper function to search an array with a given input string
# @param arr: the array to search through
# @param str1: the search string
# @return a subset of objects from arr that match str1
def search(arr, str1):
    inds = []
    for i in range(len(arr)):
        if arr[i].lower() == str1.lower():
            inds.append(i)
    return inds


# Prints the average GPA for the specified grade or gives
# error message if there are no students in that grade

# Satisfies requirement R10 and R11

# Also prints the time it took to complete the search
# @param gradenum: the grade to look for
def getavg(gradenum):
    start = time.time()
    gpas = search(grade, gradenum)
    elapsed = time.time() - start
    sum = 0
    for i in gpas:
        sum += float(gpa[i])
    if len(gpas) == 0:
        print('No students in this grade')
        return
    avg = sum / len(gpas)
    print 'Grade: ' + gradenum + ' Average GPA: ' + str(avg)
    print str(elapsed) + "\n"
    return


# Prints the information outlined in R8 or gives
# error message if there are no results to show

# Satisfies requirements R8 and R11

# Also prints the time it took to complete the search
# @param busnum: the number of the bus route to search for
def bussearch(busnum):
    start = time.time()
    buses = search(bus, busnum)
    elapsed = time.time() - start
    if len(buses) == 0:
        print"Bus entered yielded no results"
    else:
        for i in buses:
            print'Student:' + sLast[i] + ", " + sFirst[i] + ' Grade: ' + grade[i] +  ' Classroom: ' + classroom[i]
    print str(elapsed) + "\n"
    return


# Prints the student info outlined in R7 and R9 of students in the specified grade
# or an error message showing that no students are in that grade

# Satisfies requirements R7 R9 and R11

# Also prints the time it took to complete the search
# @param number: the grade number to search for
# @parm optarg: an optional argument.  Represents either "H[igh]" or "L[ow]"
#   default parameter value is ""
def gradesearch(number, optarg=""):
    start = time.time()
    grades = search(grade, number)
    elapsed = time.time() - start
    if len(grades) == 0:
        print("Grade entered yielded no results")
    elif optarg == "":
        for i in grades:
            print sLast[i] + ', ' + sFirst[i]
    else:
            if optarg == 'HIGH' or optarg == 'H':
                maxGPA = 0
                maxInd = -1
                for j in range(len(grades)):
                    if float(gpa[j]) > maxGPA:
                        maxGPA = float(gpa[j])
                        maxInd = j
                print 'Student:' + sLast[maxInd] + ', ' + sFirst[maxInd] + ' GPA: ' + gpa[maxInd] + ' Teacher: ' + tLast[maxInd] + ", " + tFirst[maxInd] + ' Bus: ' + bus[maxInd]
            elif optarg == 'LOW' or optarg == 'L':
                minGPA = 4.0
                minInd = -1
                for i in range(len(grades)):
                    if float(gpa[i]) < minGPA:
                        minGPA = float(gpa[i])
                        minInd = i
                print 'Student:' + sLast[minInd] + ', ' + sFirst[minInd] + ' GPA: ' + gpa[minInd] + ' Teacher: ' + tLast[minInd] + ", " + tFirst[minInd] + ' Bus: ' + bus[minInd]
    print str(elapsed) + "\n"
    return


# Prints out the students with the specified teacher
# or an error message stating no teacher with that name was found

# Satisfies requirements R6 and R11

# Also prints the time it took to complete the search
# @param t_lname: the last name of the teacher to search for
def teachersearch(t_lname):
    start = time.time()
    teach = search(tLast, t_lname)
    elapsed = time.time() - start
    if len(teach) == 0:
        print("Last name not found")
    else:
        for i in teach:
            print sLast[i], ', ', sFirst[i]
    print str(elapsed) + "\n"
    return


# Prints the student info outlined in R4 and R5 of students with specified last name
# or an error message stating no student with that name was found

# Satisfies requirements R4 R5 and R11

# Also prints the time it took to complete the search
# @param stu_lname: the last name of the student to search for
# @parm optarg: an optional argument.  Represents either "B[us]"
#   default parameter value is ""
def studentsearch(stu_lname, optarg = ""):
    start = time.time()
    stu = search(sLast, stu_lname)
    elapsed = time.time() - start
    if len(stu) == 0:
        print("Last name not found")
        return
    if optarg == "BUS" or optarg == "B":
        for i in stu:
            print sLast[i] + ", " + sFirst[i] + " " + bus[i]
    elif optarg == "":
        for i in stu:
            print sLast[i], sFirst[i], ', Grade: ' + grade[i], ', Classroom: ' + classroom[i], ', Teacher:', tLast[i] + ',', tFirst[i]
    print str(elapsed) + "\n"
    return

# main loop of program
while True:
    inp = raw_input('Enter a search Instruction or \'Q\' to quit: ')
    args = inp.strip().upper().split(' ')
    print

    if args[0] == 'S:' or args[0] == 'STUDENT:':
        option = ""
        if len(args) == 3:
            option = args[2]
        if len(args) > 3:
            continue
        studentsearch(args[1], option)

    elif args[0] == 'T:' or args[0] == 'TEACHER:':
        if len(args) > 2:
            continue
        teachersearch(args[1])

    elif args[0] == 'G:' or args[0] == 'GRADE:':
        number = args[1]
        option = ""
        if len(args) == 3:
            option = args[2]
        if len(args) > 3:
            continue
        gradesearch(number, option)

    elif args[0] == 'B:' or args[0] == 'BUS:':
        if len(split) > 2:
            continue
        else:
            bussearch(args[1])

    elif args[0] == 'A:' or args[0] == 'AVERAGE:':
        if len(args) > 2:
            continue
        getavg(args[1])

    elif args[0] == 'Q' or args[0] == 'QUIT':
        break;

    else:
        print('Enter a valid instruction')

exit()

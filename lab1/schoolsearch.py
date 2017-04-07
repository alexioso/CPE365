import time

# This is the set-up of the data structures to be used to collect and organize the studentInfo
sLast = []
sFirst = []
grade = []
classroom = []
bus = []
gpa = []
tLast = []
tFirst = []

# Now we read the file
try:
    f = open('students.txt', 'r')
except Exception:
    print("Unable to open file\n")
    exit()
# This loop extracts the lines from the file and distributes each bit of info to the correct array
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


def search(arr, str1):
    inds = []
    for i in range(len(arr)):
        if arr[i].lower() == str1.lower():
            inds.append(i)
    return inds


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

running = True

while running:
    inp = raw_input('Enter a search Instruction or \'Q\' to quit: ')
    args = inp.strip().upper().split(' ')
    print

    if args[0] == 'S:' or args[0] == 'STUDENT:':
        option = ""
        # This implements R5
        if len(args) == 3:
            option = args[2]
        if len(args) > 3:
            continue
        # This implements R4
        studentsearch(args[1], option)

    elif args[0] == 'T:' or args[0] == 'TEACHER:':
        # implement R6
        if len(args) > 2:
            continue
        teachersearch(args[1])

    elif args[0] == 'G:' or args[0] == 'GRADE:':
        # implement R7 and R9
        number = args[1]
        option = ""
        if len(args) == 3:
            option = args[2]
        if len(args) > 3:
            continue
        gradesearch(number, option)

    elif args[0] == 'B:' or args[0] == 'BUS:':
        # implement R8
        if len(split) > 2:
            continue
        else:
            bussearch(args[1])

    elif args[0] == 'A:' or args[0] == 'AVERAGE:':
        # implement R10
        if len(args) > 2:
            continue
        getavg(args[1])

    elif args[0] == 'Q' or args[0] == 'QUIT':
        running = False
        break

    else:
        print('Enter a valid instruction')

exit()

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
except:
    print("Unable to open fille\n")
    exit()
# This loop extracts the lines from the file and distributes each bit of info to the correct array
for line in f.readlines():
    student = line.split(',')
    sLast.append(student[0])
    sFirst.append(student[1])
    grade.append(student[2])
    classroom.append(student[3])
    bus.append(student[4])
    gpa.append(student[5])
    tLast.append(student[6])
    tFirst.append(student[7].rstrip())

inp = input('Enter a search Instruction or \'Q\' to quit: ')
while inp != 'Q' or input != 'Quit':
    if inp[0:2] == 'S:' or inp[0:8] == 'Student:':
        split = inp.strip().split(' ')

        # This implements R5
        if len(split) == 3 and (split[2] == 'Bus' or split[2] == 'B'):
            inds = search(sLast, split[1])
            if len(inds) == 0:
                print("Last name not found")
                inp = input('Enter a search Instruction or \'Q\' to quit: ')
                continue
            for i in inds:
                print(sLast[i], sFirst[i], bus[i])
        # This implements R4
        if len(split) == 2:
            inds = search(sLast, split[1])
            if len(inds) == 0:
                print("Last name not found")
                inp = input('Enter a search Instruction or \'Q\' to quit: ')
                continue
            for i in inds:
                print(sLast[i], sFirst[i], ', Grade: ' + grade[i], ', Classroom: ' + classroom[i], ', Teacher:',
                      tLast[i] + ',', tFirst[i])

    elif inp[0:2] == 'T:' or inp[0:8] == 'Teacher:':
        # implement R6
        split = inp.strip().split()
        inds = search(tLast, split[1])
        if len(inds) == 0:
            print("Last name not found")
            inp = input('Enter a search Instruction or \'Q\' to quit: ')
            continue
        for i in inds:
            print(sLast[i], ',', sFirst[i])

    elif inp[0:2] == 'G:' or inp[0:6] == 'Grade:':
        # implement R7 and R9
        split = inp.strip().split()
        number = split[1]

        if len(split) == 2:
            inds = search(grade, number)
            if len(inds) == 0:
                print("Grade entered yielded no results")
                inp = input('Enter a search Instruction or \'Q\' to quit: ')
                continue
            for i in inds:
                print(sLast[i], ',', sFirst[i])

        if len(split) == 3:
            if split[2] == 'High' or split[2] == 'H':
                inds = []
                for j in range(len(grade)):
                    if grade[j] == number:
                        inds.append(j)
                maxGPA = 0
                maxInd = -1
                for i in inds:
                    if float(gpa[i]) > maxGPA:
                        maxGPA = float(gpa[i])
                        maxInd = i
                print('Student:', sLast[maxInd] + ',', sFirst[maxInd], 'GPA:', gpa[maxInd], 'Teacher:',
                      tLast[maxInd], tFirst[maxInd], 'Bus:', bus[maxInd])

            elif split[2] == 'Low' or split[2] == 'L':
                inds = []
                for j in range(len(grade)):
                    if grade[j] == number:
                        inds.append(j)
                minGPA = 4.0
                minInd = -1
                for i in inds:
                    if float(gpa[i]) < minGPA:
                        minGPA = float(gpa[i])
                        minInd = i
                print('Student:', sLast[minInd] + ',', sFirst[minInd], 'GPA:', gpa[minInd], 'Teacher:',
                      tLast[minInd], tFirst[minInd], 'Bus:', bus[minInd])

    elif inp[0:2] == 'B:' or inp[0:4] == 'Bus:':
        # implement R8
        split = inp.strip().split(' ')
        if len(split) != 2:
            print("Invalid input")
            inp = input('Enter a search Instruction or \'Q\' to quit: ')
            continue
        inds = search(bus, split[1])
        if len(inds) == 0:
            print("Bus entered yielded no results")
            inp = input('Enter a search Instruction or \'Q\' to quit: ')
            continue
        for i in inds:
            print('Student:', sLast[i], sFirst[i], ', Grade:', grade[i], ', Classroom:', classroom[i])



    elif inp[0:2] == 'A:' or inp == 'Average:':
        # implement R10
        split = inp.strip().split(' ')
        inds = search(grade, split[1])
        sum = 0
        for i in inds:
            sum += float(gpa[i])
        if len(inds) == 0:
            print('No students in this grade')
            inp = input('Enter a search Instruction or \'Q\' to quit: ')
            continue
        avg = sum / len(inds)
        print('Grade:', split[1], 'Average GPA:', avg)


    elif inp == 'I' or inp == 'Info':
        # implement R11
        print("I")
    else:
        if inp == 'Q' or inp == 'Quit':
            break
        else:
            print('Enter a valid instruction')

    inp = input('Enter a search Instruction or \'Q\' to quit: ')
exit()


def search(arr, str1):
    inds = []
    for i in range(len(arr)):
        if arr[i].lower() == str1.lower():
            inds.append(i)
    return inds


def teachersearch(t_lname):
    teach = search(tLast, t_lname)
    if len(teach) == 0:
        print("Last name not found")
    else:
        for i in teach:
            print(sLast[i], ',', sFirst[i])
    return


def studentsearch(stu_lname, optarg = ""):
    stu = search(sLast, stu_lname)
    if len(stu) == 0:
        print("Last name not found")
        return
    if optarg == "Bus:" or optarg == "B:":
        for i in stu:
            print(sLast[i], sFirst[i], bus[i])
    else:
        for i in inds:
            print(sLast[i], sFirst[i], ', Grade: ' + grade[i], ', Classroom: ' + classroom[i], ', Teacher:',
                  tLast[i] + ',', tFirst[i])
    return

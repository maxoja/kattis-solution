students = []

while True :
    try :
        line = input()
        if line == '':
            break
        students.append(line)
    except EOFError :
        break

students = sorted(students)
students = [ s.split() for s in students ]

for i in range(len(students)) :
    name = students[i][0]
    last_name = students[i][1]

    if i > 0 and name == students[i-1][0] :
        students[i].append('with_last_name')
    elif i < len(students)-1 and name == students[i+1][0] :
        students[i].append('with_last_name')
    else :
        students[i].append('without_last_name')

students = [ s[1] + ' ' + s[0] + ' ' + s[2] for s in students ]
students = sorted(students)

for s in students :
    s = s.split()
    if s[2] == 'with_last_name' :
        print(s[1],s[0])
    else :
        print(s[1])

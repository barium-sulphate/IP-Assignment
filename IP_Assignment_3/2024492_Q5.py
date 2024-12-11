def doGrading(students,policy):
    temp=list(students.items())
    temp.sort(key=lambda x:x[1][-1],reverse=True)
    track=0
    policy_calc=dict.fromkeys(policy,0)
    key=list(policy_calc.keys())
    for i in range(len(policy)):
        policy_calc[key[i]]=[]
    for i in range(len(temp)):
        if track<=3:
            if temp[i][1][-1]<policy[track]+2 and temp[i][1][-1]>policy[track]-2:
                policy_calc[policy[track]].append(temp[i][1][-1])
            elif temp[i][1][-1]<policy[track]-2:
                track+=1
    for i in range(len(policy_calc)):
        if len(policy_calc[key[i]])==1:
            for x in range(len(policy)):
                if policy[x]==key[i]:
                    policy[x]=policy_calc[key[i]]
        else:
            start=[policy_calc[key[i]][0],policy_calc[key[i]][1]]
            for j in range(1,len(policy_calc[key[i]])-1):
                if round(start[0]-start[1],1)<round(policy_calc[key[i]][j]-policy_calc[key[i]][j+1],1):
                    start=[policy_calc[key[i]][j],policy_calc[key[i]][j+1]]
            for x in range(len(policy)):
                if policy[x]==key[i]:
                    policy[x]=round(sum(start)/2,2)

def summary(students,course):
    sumo={"A":0,"B":0,"C":0,"D":0,"F":0}
    temp=list(students.items())
    for i in range(len(temp)):
        sumo[temp[i][1][-1]]+=1
    return [course[0],course[1],course[2],course[3],sumo]

def grade(students,policy):
    key=list(students.keys())
    for i in range(len(students)):
        if students[key[i]][-1]>=policy[0]:
            students[key[i]].append("A")
        elif students[key[i]][-1]>=policy[1]:
            students[key[i]].append("B")
        elif students[key[i]][-1]>=policy[2]:
            students[key[i]].append("C")
        elif students[key[i]][-1]>=policy[3]:
            students[key[i]].append("D")
        else:
            students[key[i]].append("F")

def print_all(students):
    temp=students.copy()
    key=list(students.keys())
    ans=[]
    for i in range(len(students)):
        ans.append([key[i],temp[key[i]][-2],temp[key[i]][-1]])
    return ans

def finder(rollno,students):
    if rollno in students:
        return students[rollno]
    else:
        return -1

cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
policy = [80, 65, 50, 40]

with open("marks.txt","r") as m:
    total=m.readlines()

students={}

for i in range(len(total)):
    total[i]=total[i].strip("\n")
    total[i]=total[i].split()
    for j in range(1,len(total[i])):
        total[i][j]=round(float(total[i][j]),1)
    students[total[i][0]]=total[i][1:]
    students[total[i][0]].append(round(sum(total[i][1:]),1))

course=[cname,credits,assessments,policy]
doGrading(students,course[3])
grade(students,course[3])

def test():
    assert summary(students,course)==['IP', 4, [('labs', 30), ('midsem', 15), ('assignments', 30), ('endsem', 25)], [80.9, 65.9, 51.0, 41.2], {'A': 19, 'B': 136, 'C': 305, 'D': 245, 'F': 294}]
    assert finder("2024492",students)==[28.7, 9.4, 22.9, 14.1, 75.1, 'B']
    assert finder("2024999",students)==[10.7, 14.0, 27.3, 0.1, 52.1, 'C']
    assert finder("2024001",students)==[23.1, 2.2, 28.6, 1.2, 55.1, 'C']

test()

while True:
    print()
    print("1 - Generate a summary")
    print("2 - Print the grades of all the students in a file")
    print("3 - Search for a student record")
    print("4 - Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        other_lst=summary(students,course)
        print("Course Name:",other_lst[0])
        print("Course Credits:",other_lst[1])
        print("Course Assessments:",other_lst[2])
        print("Course Cutoffs:")
        for i in range(len(other_lst[3])):
            if i==0:
                print("Cutoff for A grade:",other_lst[3][i])
            elif i==1:
                print("Cutoff for B grade:",other_lst[3][i])
            elif i==2:
                print("Cutoff for C grade:",other_lst[3][i])
            elif i==3:
                print("Cutoff for D grade:",other_lst[3][i])
        print("Grading Summary:")
        key=list(other_lst[4].keys())
        for i in range(len(other_lst[4])):
            print(key[i],": ",other_lst[4][key[i]],sep="")
    elif choice==2:
        lst=print_all(students)
        with open("grade.txt","w") as g:
            for i in range(len(lst)):
                lst[i]=list(map(str,lst[i]))
                g.write(" ".join(lst[i])+"\n")
    elif choice==3:
        rollno=input("Enter roll no: ")
        lst=finder(rollno,students)
        if lst==-1:
            print("Roll No. not found in database")
        else:
            print("Marks in lab:",lst[0])
            print("Marks in midsem:",lst[1])
            print("Marks in assignment:",lst[2])
            print("Marks in endsem:",lst[3])
            print("Total Marks:",lst[4])
            print("Grade:",lst[5])

    elif choice==4:
        break
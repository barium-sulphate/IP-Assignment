with open("sorted_data.txt","r") as s:
    collection=s.readlines()

log={}
for i in range(1,len(collection)):
    temp=collection[i]
    temp.strip("\n")
    temp=temp.split(",")
    for j in range(len(temp)):
        temp[j]=temp[j].strip()
    temp[-1]=list(map(int,temp[-1].split(":")))
    temp[-2]=int(temp[-2])
    try:
        k=log[temp[0]]
    except KeyError:
        log[temp[0]]=[]
        log[temp[0]].append([temp[2],temp[1],temp[3].copy()])
    else:
        if log[temp[0]][-1][1]==temp[1]:
            if log[temp[0]][-1][1]=="EXIT":
                log[temp[0]].pop()
                log[temp[0]].append(log[temp[0]])
        else:
            log[temp[0]].append([temp[2],temp[1],temp[3].copy()])
key=list(log.keys())
for i in range(len(key)):
    temp={}
    for j in range(len(log[key[i]])):
        try:
            k=temp[log[key[i]][j][0]]
        except KeyError:
            temp[log[key[i]][j][0]]=[]
            temp[log[key[i]][j][0]].append([log[key[i]][j][2],log[key[i]][j][1]])
        else:
            temp[log[key[i]][j][0]].append([log[key[i]][j][2],log[key[i]][j][1]])
    log[key[i]]=temp.copy()

def gate(gate,log):
    key=list(log.keys())
    enter=0
    exit=0
    for i in range(len(key)):
        try:
            k=log[key[i]][gate]
        except KeyError:
            pass
        else:
            for j in range(len(log[key[i]][gate])):
                if log[key[i]][gate][j][1]=="ENTER":
                    enter+=1
                else:
                    exit+=1
    return (enter,exit)

def start(start,end,log):
    total=[]
    start=list(map(int,start.split(":")))
    end=list(map(int,end.split(":")))
    key=list(log.keys())
    for i in range(len(key)):
        another=list(log[key[i]].keys())
        for j in range(len(another)):
            for k in range(len(log[key[i]][another[j]])):
                if log[key[i]][another[j]][k][0]>=start and log[key[i]][another[j]][k][0]<=end:
                    total.append([log[key[i]][another[j]][k][0],key[i],log[key[i]][another[j]][k][1],another[j],])
    total.sort()
    total=[[total[i][1],total[i][2],total[i][3],total[i][0]] for i in range(len(total))]

    with open("output.txt","w") as s:
        for i in range(len(total)):
            temp=total[i].copy()
            temp[2]=str(temp[2])
            temp[3]=temp[3].copy()
            temp[3]=list(map(str,temp[3]))
            for i in range(3):
                if len(temp[3][i])==1:
                    temp[3][i]="0"+temp[3][i]
            temp[3]=":".join(temp[3])
            temp=", ".join(temp)
            temp+="\n"
            s.write(temp)
    return total

def student(student,time,log):
    total=[]
    time=list(map(int,time.split(":")))
    key=list(log[student].keys())
    for i in range(len(key)):
        for j in range(len(log[student][key[i]])):
            if log[student][key[i]][j][0]<=time:
                total.append((log[student][key[i]][j][0].copy(),key[i],log[student][key[i]][j][1]))
    total.sort()
    for i in range(len(total)):
        total[i]=(total[i][1],total[i][2],total[i][0])
    with open("student.txt","w") as s:
        for i in range(len(total)):
            temp=list(total[i])
            temp[0]=str(temp[0])
            temp[2]=temp[2].copy()
            temp[2]=list(map(str,temp[2]))
            for i in range(3):
                if len(temp[2][i])==1:
                    temp[2][i]="0"+temp[2][i]
            temp[2]=":".join(temp[2])
            temp.insert(0,student)
            temp[1],temp[2]=temp[2],temp[1]
            temp=", ".join(temp)
            temp+="\n"
            s.write(temp)
    return total

def test():
    assert gate(1,log)==(1563, 1624)
    assert gate(3,log)==(1499, 1573)
    assert student('Smiti Singhal','1:17:20',log)==[(1, 'EXIT', [0, 2, 27]), (3, 'ENTER', [0, 11, 20]), (3, 'EXIT', [0, 32, 34]), (1, 'ENTER', [0, 34, 52]), (1, 'EXIT', [0, 50, 18]), (5, 'ENTER', [1, 2, 2]), (3, 'EXIT', [1, 15, 17])]
    assert start('1:17:20','01:32:11',log)==[['Smiti Singhal', 'ENTER', 5, [1, 17, 24]], ['Karan Baboota', 'EXIT', 5, [1, 17, 27]], ['Sahil Goyal', 'ENTER', 3, [1, 17, 46]], ['Khushdev Pandit', 'ENTER', 3, [1, 18, 9]], ['Swati Jha', 'ENTER', 3, [1, 18, 14]], ['Khushdev Pandit', 'EXIT', 5, [1, 18, 25]], ['Swatantra kumar nigam', 'EXIT', 5, [1, 18, 39]], ['Khushdev Pandit', 'ENTER', 3, [1, 19, 3]], ['Aditya Raj Singh', 'EXIT', 1, [1, 19, 6]], ['Smiti Singhal', 'EXIT', 1, [1, 19, 8]], ['Sushil Kumar', 'ENTER', 5, [1, 19, 10]], ['Khushdev Pandit', 'EXIT', 1, [1, 19, 12]], ['Aditya Raj Singh', 'ENTER', 1, [1, 19, 15]], ['Bhavya Jain', 'EXIT', 3, [1, 19, 16]], ['Khushdev Pandit', 'ENTER', 5, [1, 19, 19]], ['Karan Baboota', 'ENTER', 5, [1, 19, 23]], ['Khushdev Pandit', 'EXIT', 1, [1, 19, 32]], ['Swatantra kumar nigam', 'ENTER', 1, [1, 19, 44]], ['Anuj Yadav', 'EXIT', 3, [1, 19, 51]], ['Khushdev Pandit', 'ENTER', 3, [1, 19, 57]], ['Khushdev Pandit', 'EXIT', 3, [1, 20, 16]], ['Kartik Gupta', 'ENTER', 1, [1, 20, 20]], ['Bhavya Jain', 'ENTER', 5, [1, 20, 24]], ['Swaib Ilias Mazumder', 'EXIT', 3, [1, 20, 29]], ['Yuvraj Singh', 'ENTER', 5, [1, 20, 29]], ['Ankita Mahato', 'ENTER', 5, [1, 20, 34]], ['Khushdev Pandit', 'ENTER', 3, [1, 20, 39]], ['Yuvraj Singh', 'EXIT', 3, [1, 20, 39]], ['Dhruv Mishra', 'EXIT', 3, [1, 20, 40]], ['Khushdev Pandit', 'EXIT', 5, [1, 20, 45]], ['Dhruv Mishra', 'ENTER', 1, [1, 20, 48]], ['Anuj Yadav', 'ENTER', 5, [1, 20, 53]], ['Swati Jha', 'EXIT', 3, [1, 20, 55]], ['Khushdev Pandit', 'ENTER', 5, [1, 21, 2]], ['Gayam Shivakanth Reddy', 'EXIT', 5, [1, 21, 7]], ['Ankita Mahato', 'EXIT', 5, [1, 21, 49]], ['Karan Baboota', 'EXIT', 3, [1, 21, 57]], ['Swati Jha', 'ENTER', 5, [1, 22, 14]], ['Rishika Jain', 'ENTER', 3, [1, 22, 22]], ['Anuj Yadav', 'EXIT', 5, [1, 22, 25]], ['Snehal', 'ENTER', 1, [1, 22, 25]], ['Vibhor Agarwal', 'ENTER', 1, [1, 22, 32]], ['Ujjwal Garg', 'ENTER', 3, [1, 22, 55]], ['Anuj Yadav', 'ENTER', 3, [1, 23, 6]], ['Khushdev Pandit', 'EXIT', 1, [1, 23, 13]], ['Ujjwal Garg', 'EXIT', 5, [1, 23, 14]], ['Khushdev Pandit', 'ENTER', 5, [1, 23, 22]], ['Anuj Yadav', 'EXIT', 1, [1, 23, 37]], ['Vibhor Agarwal', 'EXIT', 5, [1, 23, 49]], ['Ankita Mahato', 'ENTER', 1, [1, 23, 52]], ['Sahil Goyal', 'EXIT', 1, [1, 24, 4]], ['Manas', 'EXIT', 5, [1, 24, 30]], ['Dhruv Mishra', 'EXIT', 1, [1, 24, 49]], ['Swati Jha', 'EXIT', 5, [1, 24, 56]], ['Mohammed Kaif', 'EXIT', 5, [1, 25, 18]], ['Snehal', 'EXIT', 1, [1, 25, 19]], ['Ankita Mahato', 'EXIT', 1, [1, 25, 20]], ['Khushdev Pandit', 'EXIT', 5, [1, 25, 28]], ['Khushdev Pandit', 'ENTER', 1, [1, 25, 36]], ['Khushdev Pandit', 'EXIT', 5, [1, 25, 58]], ['Ayush Srivastava', 'ENTER', 3, [1, 26, 1]], ['Khushdev Pandit', 'ENTER', 5, [1, 26, 1]], ['Khushdev Pandit', 'EXIT', 5, [1, 26, 23]], ['Swatantra kumar nigam', 'EXIT', 3, [1, 26, 37]], ['Shashank Dargar', 'ENTER', 1, [1, 26, 38]], ['Rishika Jain', 'EXIT', 5, [1, 26, 39]], ['Khushdev Pandit', 'ENTER', 1, [1, 26, 52]], ['Khushdev Pandit', 'EXIT', 3, [1, 27, 20]], ['Ujjwal Garg', 'ENTER', 5, [1, 27, 29]], ['Vamshi Krishna Vannekala', 'ENTER', 3, [1, 27, 38]], ['Khushdev Pandit', 'ENTER', 3, [1, 27, 43]], ['Gayam Shivakanth Reddy', 'ENTER', 5, [1, 27, 46]], ['Khushdev Pandit', 'EXIT', 5, [1, 28, 2]], ['Kartik Gupta', 'EXIT', 5, [1, 28, 8]], ['Rohan Dhar', 'ENTER', 3, [1, 28, 9]], ['Sahil Goyal', 'ENTER', 3, [1, 28, 15]], ['Karan Baboota', 'ENTER', 1, [1, 28, 17]], ['Swati Jha', 'ENTER', 5, [1, 28, 17]], ['Khushdev Pandit', 'ENTER', 5, [1, 28, 28]], ['Thanmayee Matha', 'EXIT', 5, [1, 28, 33]], ['Rishika Jain', 'ENTER', 1, [1, 28, 38]], ['Shambhavi Sharma', 'ENTER', 5, [1, 28, 38]], ['Anuj Yadav', 'ENTER', 3, [1, 29, 1]], ['Khushdev Pandit', 'EXIT', 5, [1, 29, 3]], ['Swatantra kumar nigam', 'ENTER', 1, [1, 29, 24]], ['Khushdev Pandit', 'ENTER', 1, [1, 29, 36]], ['Shambhavi Sharma', 'EXIT', 3, [1, 29, 49]], ['Swatantra kumar nigam', 'EXIT', 3, [1, 30, 3]], ['Rishabh Oberoi', 'ENTER', 1, [1, 30, 5]], ['Surbhi Goyal', 'EXIT', 1, [1, 30, 11]], ['Dhruv Mishra', 'ENTER', 3, [1, 30, 12]], ['Khushdev Pandit', 'EXIT', 5, [1, 30, 12]], ['Dhruv Mishra', 'EXIT', 1, [1, 30, 24]], ['Khushdev Pandit', 'ENTER', 3, [1, 30, 34]], ['Khushdev Pandit', 'EXIT', 1, [1, 30, 38]], ['Aryan Chaudhary', 'ENTER', 1, [1, 30, 54]], ['Khushdev Pandit', 'ENTER', 5, [1, 31, 1]], ['Shambhavi Sharma', 'ENTER', 3, [1, 31, 10]], ['Aditya Raj Singh', 'EXIT', 5, [1, 31, 25]], ['Khushdev Pandit', 'EXIT', 5, [1, 31, 33]], ['Gayam Shivakanth Reddy', 'EXIT', 3, [1, 31, 34]], ['Bharat Goyal', 'ENTER', 1, [1, 31, 38]], ['Aditya Raj Singh', 'ENTER', 5, [1, 31, 48]], ['Khushdev Pandit', 'ENTER', 3, [1, 31, 58]], ['Shambhavi Sharma', 'EXIT', 3, [1, 31, 58]], ['Shambhavi Sharma', 'ENTER', 1, [1, 31, 59]], ['Sushil Kumar', 'EXIT', 5, [1, 32, 0]]]

test()
while True:
    print("1 - Show the record of a student moving in/out of campus in the day")
    print("2 - Determine all the students who entered and exited the campus in a given timeframe")
    print("3 - Determine the number of times students have entered and exited the campus through a given gate")
    choice=input("Enter choice: ")
    if choice=="1":
        student_name=input("Enter student name: ")
        time=input("Enter current time (in format HH:MM:SS): ")
        status=student(student_name,time,log)
        if status!=[]:
            if status[-1][1]=="ENTER":
                print("Student is in the campus")
            else:
                print("Student is not in the campus")
        else:
            new_status=student(student_name,"23:59:59",log)
            if new_status[0][1]=="ENTER":
                print("Student is not in the campus")
            else:
                print("Student is in the campus")
    elif choice=="2":
        start_time=input("Enter start time (in format HH:MM:SS): ")
        end_time=input("Enter end time (in format HH:MM:SS): ")
        start(start_time,end_time,log)
    elif choice=="3":
        gate_no=int(input("Enter gate no.: "))
        number=gate(gate_no,log)
        print("Students entered through gate no.:",gate_no,number[0],"times")
        print("Students exited through gate no.:",gate_no,number[1],"times")
    elif choice=="":
        break
    else:
        print("Invalid choice")
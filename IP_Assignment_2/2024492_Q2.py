def sgpacalc(courses):
    sumo=0
    credits=0
    k=0
    for i in courses:
        if i[2]=="A+" or i[2]=="A":
            k=10
        elif i[2]=="A-":
            k=9
        elif i[2]=="B":
            k=8
        elif i[2]=="B-":
            k=7
        elif i[2]=="C":
            k=6
        elif i[2]=="C-":
            k=5
        elif i[2]=="D":
            k=4
        elif i[2]=="F":
            k=2
        i.append(k)
        credits+=i[1]
        sumo+=k*i[1]
    if credits!=0:
        return sumo/credits
    else:
        return 0
def test():
    assert sgpacalc([["CSSS21", 4 ,"B"],["CSE101", 4 ,"A"]])==9.0
    assert sgpacalc([["CSSS21", 4 ,"B"],["CSE101", 4 ,"A-"],["ECE111", 4 ,"A"],["DES102", 4 ,"B-"]])==8.5

test()
courses=[]
while True:
    desc=input("Enter course details in format (Course_No Number_of_Credits Grade_Received): ")
    if desc=="":
        break
    else:
        desc=desc.split()
        if len(desc)==3:
            if desc[0].isalnum()==False or desc[1].isdigit()==False or desc[2].isalpha()==False:
                if desc[0].isalnum()==False:
                    print("Improper Course No.")
                if desc[1].isdigit()==False:
                    print("Incorrect Credit")
                if desc[2].isalpha()==False:
                    print("Incorrect Grade")
            else:
                desc[1]=int(desc[1])
                courses.append(desc)
        else:
            print("Incorrectly inputted course details")
sgpa=sgpacalc(courses)
courses.sort()
for i in courses:
    print(i[0],": ",i[2]," (",i[3],")",sep="")
print("SGPA:",sgpa)
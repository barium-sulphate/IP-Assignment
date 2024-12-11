import random

database=['FILE1.txt','FILE2.txt','FILE3.txt','FILE4.txt','FILE5.txt']

def f1(file):
    with open(file,"r") as f:
        temp=f.read()
    unique=set()
    temp=temp.split()
    total=[]
    for i in range(len(temp)):
        temp[i]=temp[i].strip("-")
        temp[i]=temp[i].strip(".")
        temp[i]=temp[i].strip(",")
        temp[i]=temp[i].strip(":")
        temp[i]=temp[i].strip(";")
        temp[i]=temp[i].lower()
        if temp[i]!="":
            total.append(temp[i])
            if temp[i] not in unique:
                unique.add(temp[i])
    return len(unique)/len(total)

def f2(file):
    with open(file,"r") as f:
        temp=f.read()
    frequent={}
    temp=temp.split()
    total=[]
    for i in range(len(temp)):
        temp[i]=temp[i].strip("-")
        temp[i]=temp[i].strip(".")
        temp[i]=temp[i].strip(",")
        temp[i]=temp[i].strip(":")
        temp[i]=temp[i].strip(";")
        temp[i]=temp[i].lower()
        if temp[i]!="":
            total.append(temp[i])
            try:
                k=frequent[temp[i]]
            except KeyError:
                frequent[temp[i]]=1
            else:
                frequent[temp[i]]+=1
    frequent=list(frequent.items())
    frequent=[[frequent[i][1],frequent[i][0]] for i in range(len(frequent))]
    frequent.sort(reverse=True)
    sumo=0
    for i in range(min(len(frequent),5)):
        sumo+=frequent[i][0]
    returner=frequent[:min(len(frequent),5):]
    returner=[returner[i][1] for i in range(len(returner))]
    ransom=[]
    while len(ransom)<5:
        k=temp[random.randint(0,len(temp)-1)]
        if k not in ransom:
            ransom.append(k)
    return (sumo/len(total),returner,ransom)

def f3(file):
    with open(file,"r") as f:
        temp=f.read()
    new=[]
    temp=temp.split(".")
    ultimate=[]
    for i in range(len(temp)):
        temp[i]=temp[i].strip("-")
        temp[i]=temp[i].strip(".")
        temp[i]=temp[i].strip(",")
        temp[i]=temp[i].strip(":")
        temp[i]=temp[i].strip(";")
        if temp[i]!="":
            bruh=temp[i].split()
            new=[]
            for j in range(len(bruh)):
                bruh[j]=bruh[j].strip("-")
                bruh[j]=bruh[j].strip(".")
                bruh[j]=bruh[j].strip(",")
                bruh[j]=bruh[j].strip(":")
                bruh[j]=bruh[j].strip(";")
                if bruh[j]!="":
                    new.append(bruh[j])
            temp[i]=new.copy()
            ultimate.append(temp[i].copy())
    count=0
    for i in range(len(ultimate)):
        if len(ultimate[i])>35 or len(ultimate[i])<5:
            count+=1
    return count/len(ultimate)

def f4(file):
    with open(file,"r") as f:
        temp=f.read()
    count=0
    another=temp
    temp=temp.split()
    total=[]
    for i in range(len(temp)):
        temp[i]=temp[i].strip("-")
        temp[i]=temp[i].strip(".")
        temp[i]=temp[i].strip(",")
        temp[i]=temp[i].strip(":")
        temp[i]=temp[i].strip(";")
        temp[i]=temp[i].lower()
        if temp[i]!="":
            total.append(temp[i])
    for i in range(1,len(another)):
        if another[i] in ';:-,.' and another[i-1] in ';:-,.' and (i==1 or another[i-2] not in ';:-,.'):
            count+=1
    return count/len(total)

def f5(file):
    with open(file,"r") as f:
        temp=f.read()
    temp=temp.split()
    total=[]
    for i in range(len(temp)):
        temp[i]=temp[i].strip("-")
        temp[i]=temp[i].strip(".")
        temp[i]=temp[i].strip(",")
        temp[i]=temp[i].strip(":")
        temp[i]=temp[i].strip(";")
        temp[i]=temp[i].lower()
        if temp[i]!="":
            total.append(temp[i])
    if len(total)>750:
        return 1
    else:
        return 0

def test():
    score=4+f1("FILE1.txt")*6+f2("FILE1.txt")[0]*6-f3("FILE1.txt")-f4("FILE1.txt")-f5("FILE1.txt")
    assert score==9.588785046728972
    assert f2("FILE1.txt")[1]==["to","the","that","it","his"]

    score=4+f1("FILE2.txt")*6+f2("FILE2.txt")[0]*6-f3("FILE2.txt")-f4("FILE2.txt")-f5("FILE2.txt")
    assert score== 9.16
    assert f2("FILE2.txt")[1]==['a', 'was', 'to', 'his', 'there']

test()
for i in range(len(database)):
    print(database[i])
    score=4+f1(database[i])*6+f2(database[i])[0]*6-f3(database[i])-f4(database[i])-f5(database[i])
    print("Score:",round(score,2))
    print("5 most used words in descending order:",", ".join(f2(database[i])[1]))
    print("5 most randomly selected words from the submission:",", ".join(f2(database[i])[2]))
    print()
def maxi(book):
    key=list(book.keys())
    ans=[]
    printer=[]
    maxi=0
    for i in range(len(book)):
        k=sum(list(book[key[i]].values()))
        ans.append([k,key[i]])
        if k>maxi:
            maxi=k
    for i in range(len(book)):
        if ans[i][0]==maxi:
            printer.append(ans[i][1])
    return sorted(printer)

def mini(book):
    key=list(book.keys())
    ans=[]
    printer=[]
    mini=len(book)
    for i in range(len(book)):
        k=sum(list(book[key[i]].values()))
        ans.append([k,key[i]])
        if k<mini:
            mini=k
    for i in range(len(book)):
        if ans[i][0]==mini:
            printer.append(ans[i][1])
    return sorted(printer)

def test():
    yearbook={'name1': {'name2': 1, 'name3': 0, 'name4': 1}, 'name2': {'name1': 0, 'name3': 0, 'name4': 0}, 'name3': {'name1': 0, 'name2': 0, 'name4': 0}, 'name4': {'name1': 1, 'name3': 0, 'name4': 1}}
    assert mini(yearbook)==["name2","name3"]
    assert maxi(yearbook)==["name1","name4"]

test()
with open("Yearbook.txt","r") as reader:
    temp=reader.readlines()
yearbook={}
another=[]
for i in range(len(temp)):
    temp[i]=temp[i].strip("\n")
    if temp[i][-1]==":":
        temp[i]=temp[i][:-1]
        another.append([])
    another[-1].append(temp[i])
for i in range(len(another)):
    yearbook[another[i][0]]={}
    for j in range(1,len(another[i])):
        person=another[i][j].split(", ")
        yearbook[another[i][0]][person[0]]=int(person[1])
# yearbook={'name1': {'name2': 1, 'name3': 0, 'name4': 1}, 'name2': {'name1': 0, 'name3': 0, 'name4': 0}, 'name3': {'name1': 0, 'name2': 0, 'name4': 0}, 'name4': {'name1': 1, 'name3': 0, 'name4': 1}}
print("Students with maximum signatures: ",end="")
maximum=maxi(yearbook)
for i in range(len(maximum)):
    if i!=len(maximum)-1:
        print(maximum[i],end=", ")
    else:
        print(maximum[i])
print("Students with minimum signatures: ",end="")
minimum=mini(yearbook)
for i in range(len(minimum)):
    if i!=len(minimum)-1:
        print(minimum[i],end=", ")
    else:
        print(minimum[i])
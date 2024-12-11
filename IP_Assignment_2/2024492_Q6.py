phone_book={"Adi":[{"address":"Noida","phone":9999999999,"email":"a@gmail.com"},{"address":"Gurgaon","phone":9999999998,"email":"adi@gmail.com"}],"Aditya":[{"address":"Vasant Kunj","phone":9999999997,"email":"aditya@gmail.com"}],"Siddhartha":[{"address":"Munirka","phone":9999999996,"email":"s@gmail.com"}]}
def add(phone_book,name,email,phone,address):
    try:
        k=phone_book[name]
    except KeyError:
        phone_book[name]=[{"address":address,"phone":phone,"email":email}]
    else:
        phone_book[name].append({"address":address,"phone":phone,"email":email})

def delete(phone_book,name):
    try:
        k=phone_book[name]
    except KeyError:
        return -1
    else:
        phone_book.pop(name)
        return 0

def finder(substring,phone_book):
    ans=[]
    key=list(phone_book.keys())
    for i in key:
        if substring in i:
            ans.extend(phone_book[i])
    return ans

def certain(phone_book,weird,target):
    temp=list(phone_book.items())
    ans=[]
    for i in range(len(temp)):
        for j in range(len(temp[i][1])):
            if temp[i][1][j][weird]==target:
                ans=[temp[i][0],temp[i][1][j]] 
                break
    return ans

def test():
    assert finder("Adi",{"Adi":[{"address":"Noida","phone":9999999999,"email":"a@gmail.com"},{"address":"Gurgaon","phone":9999999998,"email":"adi@gmail.com"}],"Aditya":[{"address":"Vasant Kunj","phone":9999999997,"email":"aditya@gmail.com"}],"Siddhartha":[{"address":"Munirka","phone":9999999996,"email":"s@gmail.com"}]})==[{"address":"Noida","phone":9999999999,"email":"a@gmail.com"},{"address":"Gurgaon","phone":9999999998,"email":"adi@gmail.com"},{"address":"Vasant Kunj","phone":9999999997,"email":"aditya@gmail.com"}]
    assert certain({"Adi":[{"address":"Noida","phone":9999999999,"email":"a@gmail.com"},{"address":"Gurgaon","phone":9999999998,"email":"adi@gmail.com"}],"Aditya":[{"address":"Vasant Kunj","phone":9999999997,"email":"aditya@gmail.com"}],"Siddhartha":[{"address":"Munirka","phone":9999999996,"email":"s@gmail.com"}]},"phone",9999999999)==["Adi",{"address":"Noida","phone":9999999999,"email":"a@gmail.com"}]

test()
while True:
    print("1 - Insert a new entry")
    print("2 - Delete an entry ")
    print("3 - Find all matching entries given a partial name")
    print("4 - Find the entry with a phone number or email")
    print("5 - View Phone Book")
    print("6 - Exit")
    choice=int(input())
    if choice==1:
        name=input("Enter name: ")
        email=input("Enter email: ")
        phone=int(input("Enter phone: "))
        address=input("Enter address: ")
        add(phone_book,name,email,phone,address)
    elif choice==2:
        name=input("Enter name: ")
        k=delete(phone_book,name)
        if k==0:
            print("Entry has been deleted")
        else:
            print("Entry not found in phone book")
    elif choice==3:
        partial=input("Enter partial name: ")
        ans=finder(partial,phone_book)
        if ans==[]:
            print("No entries with that substring")
        else:
            print("Entries with the following partial name are as follow:")
            for i in ans:
                print(i)
    elif choice==4:
        print("1 - Phone Number")
        print("2 - Email")
        print("3 - Address")
        choice=int(input("Enter parameter to search by: "))
        target=input("Enter search parameter: ")
        if choice==1 or choice==2 or choice==3:
            if choice==1:
                ans=certain(phone_book,"phone",int(target))
            elif choice==2:
                ans=certain(phone_book,"email",target)
            elif choice==3:
                ans=certain(phone_book,"address",target)
            if ans==[]:
                print("No entry with said parameter")
            else:
                print("Entry with said parameter is: ",ans)
        else:
            print("Incorrect choice")
    elif choice==5:
        print(phone_book)
    elif choice==6:
        break
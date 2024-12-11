menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
dict_menu={}
track=1
print("MENU")
print()
for (item,cost) in menu:
    dict_menu[item]=cost
    print(track,". ",item,": ",str(cost),sep="")
    track+=1
def price(item,quant,dict_menu):
    try:
        k=dict_menu[item]
    except KeyError:
        return -1
    else:
        return dict_menu[item]*quant
def test():
    assert price("Maggie",1,dict_menu)==50
    assert price("Samosa",5,dict_menu)==75
    assert price("Burger",1,dict_menu)==-1
    assert price("Sandwich",3,dict_menu)==105
    
test()
sumo=0
track=0
while True:
    choice=input("Buy another item? (Y/N): ")
    if choice=="Y" or choice=="y":
        item=input("Enter item: ")
        quant=int(input("Enter quantity of item: "))
        cost=price(item,quant,dict_menu)
        if cost==-1:
            print("Item not available")
        else:
            print("Cost of items is Rs",cost)
            sumo+=cost
            track+=quant
    elif choice=="N" or choice=="n":
        break
print("Total no. of items:",track)
print("Total cost of items:",sumo)
def ans(pgrowth):
    global pop
    limit=pgrowth*10
    if limit%1!=0:
        limit=int(limit)
        limit+=1
    else:
        limit=int(limit)
    sumo=0
    num=0
    for x in pop:
        sumo+=x
        num+=1
    maxi=sumo
    year=0
    for j in range(1,limit+2):
        temp_sum=0
        track=0
        for i in pop:
            mult=(100+pgrowth-track*0.4)/100
            track+=1
            another=1
            for k in range(j):
                another*=mult
                mult=((mult*100)-0.1)/100
            temp_sum+=another*i
        print(temp_sum)
        if temp_sum>maxi:
            maxi=temp_sum
            year=j
    return maxi,year

pop=[50,1450,1400,1700,1500,600,1200]
def _test():
    # Haven't used round function to get precise value
    assert ans(1.5)==(7926.271453200001,3)
    assert ans(2.5)==(8574.178836808424,13)
    assert ans(3.0)==(9269.386084139103,18)
    assert ans(5.0)==(16339.64473925505,39)

_test()
pgrowth=float(input("Enter pgrowth: "))
maxi,year=ans(pgrowth)
sumo=0
for i in pop:
    sumo+=i
print("Current Total Population:",sumo,"millions")
print("Maximum Total Population:",maxi,"millions")
print("Maximum population is reached after",year,"years")
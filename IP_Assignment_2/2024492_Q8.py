def timing(total):
    inter=[]
    for i in range(len(total)):
        for j in range(len(total[i])):
            inter.append(total[i][j][::-1])
    inter.sort()
    inter=[inter[i][::-1] for i in range(len(inter))]
    inter.sort()
    track=[inter[0]]
    for x in range(1,len(inter)):
        if inter[x][0]>track[-1][1]:
            track.append(inter[x])
        else:
            track[-1][1]=max(track[-1][1],inter[x][1])
    another=[]
    if track[0][0]!=[9,0]:
        another.append([[9,0],track[0][0]])
    for i in range(0,len(track)-1):
        another.append([track[i][1],track[i+1][0]])
    if track[-1][1]!=[17,0]:
        another.append([track[-1][1],[17,0]])
    printer=[]
    for i in range(len(another)):
        duration=[another[i][1][0]-another[i][0][0],another[i][1][1]-another[i][0][1]]
        if duration[1]<0:
            duration[0]-=1
            duration[1]+=60
        if duration>=[0,30]:
            printer.append(another[i])
    return printer

def printable(random_list):
    for i in range(len(random_list)):
        random_list[i][0][0]=str(random_list[i][0][0])
        random_list[i][1][0]=str(random_list[i][1][0])
        if random_list[i][0][1]<10:
            random_list[i][0][1]="0"+str(random_list[i][0][1])
        else:
            random_list[i][0][1]=str(random_list[i][0][1])
        if random_list[i][1][1]<10:
            random_list[i][1][1]="0"+str(random_list[i][1][1])
        else:
            random_list[i][1][1]=str(random_list[i][1][1])
        random_list[i][0]=":".join(random_list[i][0])
        random_list[i][1]=":".join(random_list[i][1])
        random_list[i]="-".join(random_list[i])
    return random_list

def working_copy(chain):
    give=chain.copy()  
    for i in range(len(chain)):
        give[i]=chain[i].copy()
        for j in range(len(chain[i])):
            give[i][j]=chain[i][j].copy()
    return give

def overlap(x,y):
    if (y[0]>x[0] and y[0]>=x[1]) or (y[1]<x[1] and y[1]<=x[0]):
        return True
    else:
        return False
def bonus(basic):
    possible=[]
    for i in range(3):
        possible.append([])
        for j in range(len(basic[i])):
            for x in range(basic[i][j][0][0],basic[i][j][1][0]+1):
                for y in range(60):
                    tempx=x
                    tempy=y
                    start=[tempx,tempy]
                    end=[tempx,tempy+30]
                    if end[1]>=60:
                        end[1]-=60
                        end[0]+=1
                    if start>=basic[i][j][0] and end<=basic[i][j][1]:
                        possible[i].append([start,end])
    breaker=False
    ans=[]
    for x in range(len(possible[0])):
        for y in range(len(possible[1])):
            for z in range(len(possible[2])):
                if overlap(possible[0][x],possible[1][y]) and overlap(possible[2][z],possible[1][y]) and overlap(possible[0][x],possible[2][z]):
                    ans=[possible[0][x],possible[1][y],possible[2][z]]
                    breaker=True
                    break
            if breaker:
                break
        if breaker:
            breaker
    return ans
def test():
    assert timing([[[[15, 0], [16, 0]], [[12, 0], [13, 15]]], [[[14, 0], [14, 30]], [[12, 30], [13, 30]]], [[[9, 0], [10, 0]], [[15, 30], [16, 30]]]])==[[[10, 0], [12, 0]], [[13, 30], [14, 0]], [[14, 30], [15, 0]], [[16, 30], [17, 0]]]
    assert printable([[[10, 0], [12, 0]], [[13, 30], [14, 0]], [[14, 30], [15, 0]], [[16, 30], [17, 0]]])==['10:00-12:00', '13:30-14:00', '14:30-15:00', '16:30-17:00']

test()
print("Main Question: ")
print()
alice= ["15:00-16:00", "12:00-13:15"]
bob = ["14:00-14:30", "12:30-13:30"]
cameron = ["09:00-10:00", "15:30-16:30"]
inter=[]
for i in range(len(alice)):
    alice[i]=alice[i].split("-")
    for j in range(len(alice[i])):
        alice[i][j]=list(map(int,alice[i][j].split(":")))
for i in range(len(bob)):
    bob[i]=bob[i].split("-")
    for j in range(len(bob[i])):
        bob[i][j]=list(map(int,bob[i][j].split(":")))
for i in range(len(cameron)):
    cameron[i]=cameron[i].split("-")
    for j in range(len(cameron[i])):
        cameron[i][j]=list(map(int,cameron[i][j].split(":")))
free=timing([working_copy(alice),working_copy(bob),working_copy(cameron)])
aintnoway=0
if free!=[]:
    print("One possible 30 min slot where all three are free: ",end="")
    start=free[0][0].copy()
    end=free[0][0].copy()
    end[1]+=30
    if end[1]>=60:
        end[1]-=60
        end[0]+=1
    product=printable([[start,end]])
    print(product[0])
    print()
    print("Other possible time frames where all three are free for atleast 30 minutes:")
    product2=printable(free)
    for i in range(len(product2)):
        if i!=len(product2)-1:
            print(product2[i],end=", ")
        else:
            print(product2[i])
    print()
else:
    print("No time frame where all three are free for atleast 30 minutes")
    print()
    a=timing([working_copy(alice),working_copy(bob)])
    if a!=[]:
        print("Time frames where Alice and Bob are free for atleast 30 minutes:")
        ab=printable(a)
        for i in range(len(ab)):
            if i!=len(ab)-1:
                print(ab[i],end=", ")
            else:
                print(ab[i])
    else:
        print("No time frames where Alice and Bob are free for atleast 30 minutes")
        aintnoway+=1
    print()
    b=timing([working_copy(bob),working_copy(cameron)])
    if b!=[]:
        print("Time frames where Bob and Cameron are free for atleast 30 minutes:")
        bc=printable(b)
        for i in range(len(bc)):
            if i!=len(bc)-1:
                print(bc[i],end=", ")
            else:
                print(bc[i])
    else:
        print("No time frames where Bob and Cameron are free for atleast 30 minutes")
        aintnoway+=1
    print()
    c=timing([working_copy(alice),working_copy(cameron)])
    if c!=[]:
        print("Time frames where Cameron and Alice are free for atleast 30 minutes:")
        ac=printable(c)
        for i in range(len(ac)):
            if i!=len(ac)-1:
                print(ac[i],end=", ")
            else:
                print(ac[i])
    else:
        print("No time frames where Cameron and Alice are free for atleast 30 minutes")
        aintnoway+=1
    print()
if aintnoway==3:
    print("There is no available time for all participants")

print("Bonus Question: ")
alice_free=timing(working_copy([alice]))
bob_free=timing(working_copy([bob]))
cameron_free=timing(working_copy([cameron]))
final=[alice_free,bob_free,cameron_free]
ans=bonus(final)
if ans==[]:
    print("No three unique non-overlapping unique slots available for all three people involved")
else:
    ans=printable(ans)
    print("Three unique non-overlapping slots available for all three people involved are as follows")
    print("Alice Schedule:",ans[0])
    print("Bob Schedule:",ans[1])
    print("Cameron Schedule:",ans[2])
    print("Sorry these people today are not free")
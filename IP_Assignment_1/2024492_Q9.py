import random
n=int(input("Enter x coordinate (n): "))
m=int(input("Enter y coordinate (m): "))
freq=0
sumo=0
while True:
    start=0
    end=1
    x=0
    y=0
    track=0
    while start==0 or end==1:
        dir=random.randint(start,end)
        step=random.randint(0,5)
        if dir==0:
            x+=step
        else:
            y+=step
        track+=1
        # Satisfying condition of man having reached point (n,m) when he is either at distance n from y axis or when he is at a distance more than n from y axis
        if y>=m:
            end=0
        if x>=n:
            start=1
    if freq!=0:
        old=sumo/freq
        new=(sumo+track)/(freq+1)
        change=abs((old-new)*100/old)
        if change<10:
            print("Average steps taken:",new)
            break
    sumo+=track
    freq+=1
def sum_list(a,b):
    sumo=0
    for i in range(len(a)):
        sumo+=a[i]*b[i]
    return sumo

def multiply(coordinates,matrix):
    for i in range(len(coordinates)):
        coordinates[i]=[coordinates[i][0],coordinates[i][1],1]
    column=[]
    for i in range(len(matrix[0])):
        column.append([])
        for j in range(len(matrix)):
            column[-1].append(matrix[j][i])
    ans=[]
    for i in coordinates:
        ans.append([])
        for j in range(len(i)):
            ans[-1].append(sum_list(column[j],i))
    return ans
coordinates=[]
while True:
    n=input("Enter coordinates: ")
    if n=="":
        break
    else:
        x,y=map(int(n.split()))
        coordinates.append((x,y))

def test():
    assert multiply([(5,4),(9,2),(1,3),(6,10)],[[4,0,0],[0,3,0],[0,0,1]])==[[20, 12, 1], [36, 6, 1], [4, 9, 1], [24, 30, 1]]
    assert multiply([(1,2),(3,4),(5,10),(6,4),(1,7),(8,6),(9,10)],[[2,0,0],[0,2,0],[0,0,1]])==[[2, 4, 1], [6, 8, 1], [10, 20, 1], [12, 8, 1], [2, 14, 1], [16, 12, 1], [18, 20, 1]]
    assert sum_list([1,2,3],[4,3,2])==16
    assert sum_list([3,9,1,2],[2,3,6,4])==47

test()
coordinates=[(1,2),(3,4),(5,10),(6,4),(1,7),(8,6),(9,10)]
coordinates=[(5,4),(9,2),(1,3),(6,10)]
cx=int(input("Scaling Parameter (x-axis): "))
cy=int(input("Scaling Parameter (x-axis): "))
matrix=[[cx,0,0],[0,cy,0],[0,0,1]]
ans=multiply(coordinates,matrix)
for i in range(len(ans)):
    ans[i]=(ans[i][0],ans[i][1])
print(ans)
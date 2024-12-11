from random import *
check=True
print(r"""
                 .___      __
  ________ __  __| _/____ |  | ____ __
 /  ___/  |  \/ __ |/  _ \|  |/ /  |  \
 \___ \|  |  / /_/ (  <_> )    <|  |  /
/____  >____/\____ |\____/|__|_ \____/   v2.0
     \/           \/           \/
                """)
print()
counter=1
while check==True:
  d=input("Sudoku Solver or Player (S/P): ")
  e=int(input("Type of Sudoku (4/6/9): "))
  a,b=0,0
  if e==4:
    a,b=2,2
  elif e==6:
    a,b=2,3
  elif e==9:
    a,b=3,3
  if d=="P":
    n=0
    print("Easy = E")
    print("Medium - M")
    print("Hard - H")
    diff=input("Enter prefered difficulty (E/M/H): ")
    if diff=="E":
      if e==4:
        n=8
      elif e==6:
        n=18
      elif e==9:
        n=32
    elif diff=="M":
      if e==4:
        n=6
      elif e==6:
        n=14
      elif e==9:
        n=28
    elif diff=="H":
      if e==4:
        n=4
      elif e==6:
        n=10
      elif e==9:
        n=24
    breaker=0
    sudoku=[]
    for i in range(a*b):
      sudoku.append([])
      for j in range(a*b):
        sudoku[i].append(-1)
    while breaker==0:
      breaker1=0
      for i in range(a*b):
        if breaker1==1:
          break
        for j in range(a*b):
          if breaker1==1:
           break
          poss=[]
          row=sudoku[i]
          column=[]
          for q in range(a*b):
            column.append(sudoku[q][j])
          grid=[]
          for w in range(b):
            for e in range(a):
              grid.append(sudoku[((i//a)*a)+e][((j//b)*b)+w])
          for p in range(1,a*b+1):
            if p not in grid and p not in column and p not in row:
              poss.append(p)
          if len(poss)!=0:
            k=randrange(len(poss))
            sudoku[i][j]=poss[k]
          elif len(poss)==0:
            breaker1=1
      if breaker1==1:
        sudoku=[]
        for i in range(a*b):
          sudoku.append([])
          for j in range(a*b):
            sudoku[i].append(-1)
      else:
        for i in range(a*b):
          if -1 in sudoku[i]:
            break
        else:
          breaker=1
    sol=sudoku.copy()
    for r in range(a*b):
      sol[r]=sudoku[r].copy()
    sud1=[]
    sud2=[]
    listy=[]
    sud3=[]
    breakwhile=False
    while True:
      if breakwhile==True:
        break
      while True:
           g=randint(0,a*b-1)
           h=randint(0,a*b-1)
           if (g,h) not in listy and (a*b-1-g,a*b-1-h) not in listy:
              break
      sudoku[g][h]=-1
      sudoku[a*b-1-g][a*b-1-h]=-1
      t=(g,h)
      s=(a*b-1-g,a*b-1-h)
      listy.append(s)
      listy.append(t)
      sud3=sudoku.copy()
      for i in range(a*b):
        sud3[i]=sudoku[i].copy()
      counter=True
      while counter==True:
        sud2=sudoku.copy()
        for h in range(a*b):
          sud2[h]=sudoku[h].copy()
        L=[]
        remover=[]
        for i in range(a*b):
          L.append([])
          for k in range(a*b):
            for l in range(a*b):
              L[i].append((k,l))
        for i in range(a*b):
          remover.append([])
        for i in range(a*b):
          for j in range(a*b):
            if sudoku[i][j]!=-1:
              l=sudoku[i][j]
              column=[]
              row=[]
              grid=[]
              for h in range(a*b):
                column.append((h,j))
                row.append((i,h))
              for t in range(b):
                for u in range(a):
                  grid.append((((i//a)*a)+u,((j//b)*b)+t))
              total=[]
              total.extend(row)
              total.extend(column)
              total.extend(grid)
              for e in range(len(total)):
                if total[e] not in remover[l-1]:
                  L[l-1].remove(total[e])
                  remover[l-1].append(total[e])
              for k in range(a*b):
                if (i,j) not in remover[k]:
                  L[k].remove((i,j))
                  remover[k].append((i,j))
            elif sudoku[i][j]==-1:
              no=[]
              column=[]
              row=[]
              grid=[]
              for k in range(a*b):
                column.append(sudoku[k][j])
                row.append(sudoku[i][k])
              for t in range(b):
                for u in range(a):
                  grid.append(sudoku[((i//a)*a)+u][((j//b)*b)+t])
              for k in range(1,a*b+1):
                if k not in row and k not in column and k not in grid:
                  no.append(k)
              if len(no)==1:
                sudoku[i][j]=no[0]
        gridl=[]
        greed=[]
        rowan=[]
        colin=[]
        for i in range(a*b):
          for j in range(a*b):
            if i%a==0 and j%b==0:
              gridl.append((i,j))
        for i in range(a*b):
          greed.append([])
          for t in range(b):
            for u in range(a):
              greed[i].append((((gridl[i][0]//a)*a)+u,((gridl[i][1]//b)*b)+t))
        for i in range(a*b):
          rowan.append([])
          colin.append([])
          for j in range(a*b):
            rowan[i].append((i,j))
            colin[i].append((j,i))
        for k in range(a*b):
          for i in range(a*b):
            poss=[]
            for j in range(a*b):
              if rowan[i][j] in L[k]:
                poss.append(rowan[i][j])
            if len(poss)==1:
              sudoku[poss[0][0]][poss[0][1]]=k+1
        for k in range(a*b):
          for i in range(a*b):
            poss=[]
            for j in range(a*b):
              if colin[i][j] in L[k]:
                poss.append(colin[i][j])
            if len(poss)==1:
              sudoku[poss[0][0]][poss[0][1]]=k+1
        for k in range(a*b):
          for i in range(a*b):
            poss=[]
            for j in range(a*b):
              if greed[i][j] in L[k]:
                poss.append(greed[i][j])
            if len(poss)==1:
              sudoku[poss[0][0]][poss[0][1]]=k+1
        if sud2==sudoku:
          counter=False
          breakwhile=True
        if sudoku==sol:
          sud1=sud3.copy()
          for t in range(a*b):
            sud1[t]=sud3[t].copy()
          sudoku=sud3.copy()
          for t in range(a*b):
            sudoku[t]=sud3[t].copy()
          counter=False
    k=0
    while sud1!=sol:
      for i in range(a*b):
        if i%a==0 and i!=0:
          print("  ","-"*((5*a*b)+(a-1)))
        print((a*b)-i,end="| ")
        for j in range(a*b):
          if j%b==0 and j!=0:
            print("|",end="")
          if sud1[i][j]==-1:
            print(" ","_"," ",end="")
          else:
            print(" ",sud1[i][j]," ",end="")
        print()
      print(3*" ","_"*((5*a*b)+(a-1)))
      print(3*" ",end="")
      for k in range(a*b):
        if k%b==0 and k!=0:
          print(" ",end="")
        print(" ",k+1," ",end="")
      print()
      row=int(input("Row: "))
      column=int(input("Column: "))
      num=int(input("Number: "))
      if row>a*b or column>a*b or num>a*b:
        print("Can't be more than",a*b)
      elif sol[a*b-row][column-1]==num:
        sud1[a*b-row][column-1]=num
        print("Nice")
      else:
        print("Wrong number")
      if sud1==sol:
        print("Well Done !")
  if d=="S":
    sudoku=[]
    for i in range(a*b):
      sudoku.append([])
      for j in range(a*b):
        sudoku[i].append(-1)
    v=0
    while v!=a*b:
        n=input("Enter the sudoku row-wise: ")
        if len(n)!=a*b:
          print("Invalid row as row cannot have less/more than",a*b,"spaces")
        else:
          for j in range(a*b):
            if n[j]!=" ":
              sudoku[v][j]=int(n[j])
          v+=1
    remover=[]
    L=[]
    for i in range(a*b):
      L.append([])
      for k in range(a*b):
        for l in range(a*b):
          L[i].append((k,l))
    for i in range(a*b):
      remover.append([])
    counter=True
    while counter==True:
      for i in range(a*b):
        for j in range(a*b):
          if sudoku[i][j]!=-1:
            l=sudoku[i][j]
            column=[]
            row=[]
            grid=[]
            for h in range(a*b):
              column.append((h,j))
              row.append((i,h))
            for t in range(b):
              for u in range(a):
                grid.append((((i//a)*a)+u,((j//b)*b)+t))
            total=[]
            total.extend(row)
            total.extend(column)
            total.extend(grid)
            for e in range(len(total)):
              if total[e] not in remover[l-1]:
                L[l-1].remove(total[e])
                remover[l-1].append(total[e])
            for k in range(a*b):
              if (i,j) not in remover[k]:
                L[k].remove((i,j))
                remover[k].append((i,j))
          elif sudoku[i][j]==-1:
            no=[]
            column=[]
            row=[]
            grid=[]
            for k in range(a*b):
              column.append(sudoku[k][j])
              row.append(sudoku[i][k])
            for t in range(b):
              for u in range(a):
                grid.append(sudoku[((i//a)*a)+u][((j//b)*b)+t])
            for k in range(1,a*b+1):
              if k not in row and k not in column and k not in grid:
                no.append(k)
            if len(no)==1:
              sudoku[i][j]=no[0]
      gridl=[]
      greed=[]
      rowan=[]
      colin=[]
      for i in range(a*b):
        for j in range(a*b):
          if i%a==0 and j%b==0:
            gridl.append((i,j))
      for i in range(a*b):
        greed.append([])
        for t in range(b):
          for u in range(a):
            greed[i].append((((gridl[i][0]//a)*a)+u,((gridl[i][1]//b)*b)+t))
      for i in range(a*b):
        rowan.append([])
        colin.append([])
        for j in range(a*b):
          rowan[i].append((i,j))
          colin[i].append((j,i))
      for k in range(a*b):
        for i in range(a*b):
          poss=[]
          for j in range(a*b):
            if rowan[i][j] in L[k]:
              poss.append(rowan[i][j])
          if len(poss)==1:
            sudoku[poss[0][0]][poss[0][1]]=k+1
      for k in range(a*b):
        for i in range(a*b):
          poss=[]
          for j in range(a*b):
            if colin[i][j] in L[k]:
              poss.append(colin[i][j])
          if len(poss)==1:
            sudoku[poss[0][0]][poss[0][1]]=k+1
      for k in range(a*b):
        for i in range(a*b):
          poss=[]
          for j in range(a*b):
            if greed[i][j] in L[k]:
              poss.append(greed[i][j])
          if len(poss)==1:
            sudoku[poss[0][0]][poss[0][1]]=k+1
      c=0
      for i in sudoku:
        for j in range(a*b):
          if i[j]==-1:
            c+=1
      if c==0:
        counter=False
    for i in range(a*b):
      if i%a==0 and i!=0:
        print("-"*((5*a*b)+(a-1)))
      for j in range(a*b):
        if j!=0 and (j)%b==0:
          print("|",end="")
        if j==a*b-1:
          if sudoku[i][j]==-1:
            print(" ","_"," ")
          else:
            print(" ",sudoku[i][j]," ")
        else:
          if sudoku[i][j]==-1:
            print(" ","_"," ",end="")
          else:
            print(" ",sudoku[i][j]," ",end="")
  n=input("Would you like to try again ? (Y/N):")
  if n=="N" or n=="No" or n=="NO" or n=="n":
    print("Thank You")
    check=False
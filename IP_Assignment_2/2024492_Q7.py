urls = {}
initial_imps = {}
final_imps = {}

n = int(input("Enter n: "))

with open("pages.txt","r") as file:
    input_lst = file.readlines()

for i in input_lst:
    s = i.strip("\n")
    s = s.split(": ")
    imp = s[0].split(", ")
    initial_imps[imp[0]] = initial_imps.get(imp[0],float(imp[1]))

    for j in range(len(s[1])):
        if s[1][j:j+3]=="URL" and (s[1][j+3]).isnumeric() and s[1][j+4].isnumeric():
            urls[imp[0]] = urls.get(imp[0],[]) 
            if s[1][j:j+5] not in urls[imp[0]]:
                urls[imp[0]] += [s[1][j:j+5]] 

for i in urls:
    temp = initial_imps[i]/len(urls[i])
    for j in urls[i]:
        final_imps[j] = final_imps.get(j,0) + temp

sorted_final_imps_by_value = sorted(final_imps.items(), key=lambda x:x[1], reverse=True)
printout = list(sorted_final_imps_by_value)

for i in printout[:n]:
    print(i)
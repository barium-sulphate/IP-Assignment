def top(count,n,collect):
    if count==n:
        return []
    temp=""
    temp+=(n-count)*"* "
    temp+=count*"  "
    cont=temp[0:len(temp)-1]
    temp+=cont[::-1]
    collect.append(temp)
    top(count+1,n,collect)
    return collect

def bottom(count,n,collect):
    if count==n+1:
        return []
    temp=""
    temp+=count*"* "
    temp+=(n-count)*"  "
    cont=temp[0:len(temp)-1]
    temp+=cont[::-1]
    collect.append(temp)
    bottom(count+1,n,collect)
    return collect

def perform(n):
    ans=[]
    collect=[]
    ans.extend(top(0,n,collect))
    collect=[]
    ans.extend(bottom(2,n,collect))
    return ans

def test():
    assert perform(1)==['* *']
    assert perform(2)==['* * * *', '*     *', '* * * *']
    assert perform(3)==['* * * * * *', '* *     * *', '*         *', '* *     * *', '* * * * * *']
    assert perform(5)==['* * * * * * * * * *', '* * * *     * * * *', '* * *         * * *', '* *             * *', '*                 *', '* *             * *', '* * *         * * *', '* * * *     * * * *', '* * * * * * * * * *']
    assert perform(10)==['* * * * * * * * * * * * * * * * * * * *', '* * * * * * * * *     * * * * * * * * *', '* * * * * * * *         * * * * * * * *', '* * * * * * *             * * * * * * *', '* * * * * *                 * * * * * *', '* * * * *                     * * * * *', '* * * *                         * * * *', '* * *                             * * *', '* *                                 * *', '*                                     *', '* *                                 * *', '* * *                             * * *', '* * * *                         * * * *', '* * * * *                     * * * * *', '* * * * * *                 * * * * * *', '* * * * * * *             * * * * * * *', '* * * * * * * *         * * * * * * * *', '* * * * * * * * *     * * * * * * * * *', '* * * * * * * * * * * * * * * * * * * *']

test()
n=int(input("Enter side length: " ))
if n==0:
    pass
else:
    ans=perform(n)
    for i in ans:
        print(i)

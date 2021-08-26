def generatepalindrome(a,n):
    mid=n//2
    left=False
    i=mid-1
    if n%2==1:
        j=mid+1
    else:
        j=mid
    while(i>=0 and a[i]==a[j]):
        i=i-1
        j=j+1
    if i<0 or a[i]<a[j]:
        left=True
    while(i>=0):
        a[j]=a[i]
        j=j+1
        i=i-1
    if left==True:
        c=1
        i=mid-1
        if n%2==1:
            a[mid]=a[mid]+c
            c=int(a[mid]/10)
            a[mid]=a[mid]%10
            j=mid+1
        else:
            j=mid
        while i>=0:
            a[i]=a[i]+c
            c=int(a[i]/10)
            a[i]=a[i]%10
            a[j]=a[i]
            j=j+1
            i=i-1
    return a   
            
            
l=str(input())
a=[]
n=len(l)
for i in range(n):
    a.append(int(l[i]))
f=0
for i in range(1,n):
    if a[i]!=9:
        f=1
        h=(generatepalindrome(a,n))
        for i in h:
            print(i,end="")
        break
if f==0:
    q="1"+(n-1)*"0"+"1"
    print(q)

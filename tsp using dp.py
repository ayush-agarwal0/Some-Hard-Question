#Traveling salesman problem using dp


G=[[0,20,42,25],[20,0,30,34],[42,30,0,10],[25,34,10,0]]
n=len(G)
dp=[[0]*(n) for i in range(2**n)]
for i in range(0,1<<n,1):
    for j in range(0,n,1):
        dp[i][j]=-1
visited=(1<<n)-1
def tsp(ma,pos,G):
    if ma==visited:
        return G[pos][0]
    if dp[ma][pos]!=-1:
        return dp[ma][pos]
    a=np.inf
    for i in range(0,n,1):
        if (ma & (1<<i))==0:
            na=G[pos][i]+tsp((ma | (1<<i)),i,G)
            a=min(a,na)
    dp[ma][pos]=a    
    return dp[ma][pos]
print(tsp(1,0,G))

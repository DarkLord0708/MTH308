def backSubs(A,B,P):
    n = len(B)
    x = [0]*n
    for i in range(n):
        temp = 0
        for j in range(n-i,n):
            temp+=A[P[n-i-1]][j]*x[j]
        x[n-1-i] = (B[P[n-1-i]]-temp)/A[P[n-1-i]][n-1-i]
    return x


def gauss(A,B):
    n = len(B)
    P = [i for i in range(n)]
    for i in range(n):
        t = A[i][i]
        ref = (i,i)
        for w in range(n):
            t_old = t
            t = max(abs(A[w][i]),abs(t_old))
            if(t==t_old):
                pass
            else:
                t_old = t
                ref = (w,i)
        P[ref[0]],P[ref[1]] = P[ref[1]],P[ref[0]]

        t = A[P[i]][i]

        for j in range(i+1,n):
            u = A[P[j]][i]
            for k in range(n):
                # print(A)
                A[P[j]][k] = A[P[j]][k]*(1)-A[P[i]][k]*(u/t)
            B[P[j]] = B[P[j]]*(1) - B[P[i]]*(u/t)  
    return A,B,P


A = [[25,5,1],[64,8,1],[144,12,1]]

B = [106.8,177.2,279.2]

# A1 = [[1,2,3],[0,4,5],[0,0,6]]
# B1 = [6,9,6]

# A3 = [[1,2,3],[4,5,6],[7,8,9]]
# B3 = [1,2,3]

# print(backSubs(A1,B1))
# A = [[2,1,-1],[-3,-1,2],[-2,1,2]]
# B = [8,-11,-3]

A1,B1,P = gauss(A,B)
print(backSubs(A1,B1,P))
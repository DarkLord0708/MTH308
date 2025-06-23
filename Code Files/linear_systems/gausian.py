def backSubs(A,B):
    n = len(B)
    x = [0]*n
    for i in range(n):
        temp = 0
        for j in range(n-i,n):
            temp+=A[n-i-1][j]*x[j]
        x[n-1-i] = (B[n-1-i]-temp)/A[n-1-i][n-1-i]
    return x


def gauss(A,B):
    n = len(B)
    for i in range(n):
        t = A[i][i]
        for j in range(i+1,n):
            u = A[j][i]
            for k in range(n):
                # print(A)
                A[j][k] = A[j][k]*(1)-A[i][k]*(u/t)
            B[j] = B[j]*(1) - B[i]*(u/t)  
    return A,B


A = [[25,5,1],[64,8,1],[144,12,1]]

B = [106.8,177.2,279.2]

# A1 = [[1,2,3],[0,4,5],[0,0,6]]
# B1 = [6,9,6]

# A3 = [[1,2,3],[4,5,6],[7,8,9]]
# B3 = [1,2,3]

# print(backSubs(A1,B1))
# A = [[2,1,-1],[-3,-1,2],[-2,1,2]]
# B = [8,-11,-3]

A1,B1 = gauss(A,B)
print(backSubs(A1,B1))
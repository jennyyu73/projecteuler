#gaussianElimination

def gaussianElimination(M):
    #make upper triangular
    for col in range(len(M[0])-2):
        index=col
        for i in range(col+1,len(M)):
            num=-M[i][col]/M[index][col]
            for k in range(index,len(M[0])):
                M[i][k]=M[i][k]+M[index][k]*num
    #print(M)
    #diagonal to 1's
    for col in range(len(M[0])-2,-1,-1):
        row=col
        num=M[row][col]
        for i in range(len(M[0])):
            M[row][i]=(M[row][i])/num
    #reduced row echelon form      
    for col in range(len(M[0])-2,0,-1):
        index=col
        for row in range(col-1,-1,-1):
            num=-M[row][col]/M[index][col]
            for k in range(index,len(M[0])):
                M[row][k]=M[row][k]+M[index][k]*num
    solution=[]
    for i in range(len(M)): #backsub
        if round(M[i][len(M[0])-1],4)==round(M[i][len(M[0])-1],5):
            solution.append(round(M[i][len(M[0])-1],4))
        else:
            solution.append(M[i][len(M[0])-1])
    return solution

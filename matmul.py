A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

C=[[A[0][0]+B[0][0],A[0][1]+B[0][1]],[A[1][0]+B[1][0],A[1][1]+B[1][1]]]

D = [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],\
     [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

print "The sum of matrices A and B is: "
print C

print "The product of matrices A and B is: "
print D

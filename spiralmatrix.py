def generateMatrix(n):
        if n<=0:
            return [] 

        matrix=[row[:] for row in [[0]*n]*n]
        
        a=0
        b=n-1

        x=0
        z=n-1
        current=1
        
        while (True):
            if current>n*n:
                break
            for c in range (x, z+1):
                matrix[a][c]=current
                current+=1
            a+=1
            for r in range (a, b+1):
                matrix[r][z]=current
                current+=1
            z-=1
            for c in range (z, x-1, -1):
                matrix[b][c]=current
                current+=1
            b-=1
            for r in range (b, a-1, -1):
                matrix[r][x]=current
                current+=1
            x+=1
        return matrix
print(list(generateMatrix(n)))
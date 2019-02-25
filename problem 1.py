n = 5
end = 0
matrix = []


while n != 0:

    n = int(input('Matrisin qiymetlerini daxil edin: '))

    matrix.append(n)

    n -= 1
       
print(matrix)
print (max(matrix))

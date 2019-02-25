n = 5
end = 0
matrix = []


while n != 0:

    num = int(input('Matrise daxil etmek istediyiniz ededleri girin: '))

    matrix.append(num)

    
    n -= 1
       
print(matrix)
print (max(matrix))
print (min(matrix))
print (min(matrix) + max(matrix))

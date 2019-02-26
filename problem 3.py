a = input("sozu daxil edin")
b = input("sozu daxil edin")
c = input("sozu daxil edin")
d = input("sozu daxil edin")
e = input("sozu daxil edin")
list = [a,b,c,d,e]

for word in list[:]:
  if len(word) <=2:
    list.remove(word) 
    print (list)

print (list)

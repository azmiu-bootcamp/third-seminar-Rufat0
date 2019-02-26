a = input("sozu daxil edin")
b = input("sozu daxil edin")
c = input("sozu daxil edin")
d = input("sozu daxil edin")
e = input("sozu daxil edin")
list = [a,b,c,d,e]

for soz in list[:]:
  if len(soz) <=2:
    list.remove(soz) 
    print (list)

print (list)

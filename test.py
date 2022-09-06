from ecc import FieldElement

a = FieldElement(3,13)
b = FieldElement(1,13)
c = FieldElement(5,13)

#print(a==b)
#print(a==a)


print(b-a==c)
print(a**3==b)
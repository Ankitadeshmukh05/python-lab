x=int(input('given number'))
q1=x%10
y=x//10
q2=y%10
q3=y//10
print(q3,q2,q1)
z =(q3*q3*q3)+(q2*q2*q2)+(q1*q1*q1)
if x==z:
    print("armstrong")
else:
    print("not armstrong")

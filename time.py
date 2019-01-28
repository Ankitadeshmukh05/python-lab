x=int(input('time'))
q1=x//86400
r1=x%86400
q2=r1//3600
r2=r1%3600
q3=r2//60
r3=r2%60
print(q1, 'days',q2, 'hours',q3,'min' ,r3,'seconds')


print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21],reverse=True))
print(sorted([36,5,-12,9,-21],key=abs))

print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))


from operator import itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students,key=lambda t:t[1]))
print(sorted(students,key=itemgetter(1),reverse=True))
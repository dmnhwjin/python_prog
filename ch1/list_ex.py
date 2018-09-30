"""This is a list example"""


bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

bob[0], sue[2]


bob[0].split()[-1]

sue[2] *= 1.25

sue


people = [bob, sue]
for person in people:
    print(person)
    
people[1][0]

for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20
    
for person in people: print(person[2])
    
    
pays = [person[2] for person in people]

pays

pays = map((lambda x: x[2]), people)

list(pays)

sum(person[2] for person in people)


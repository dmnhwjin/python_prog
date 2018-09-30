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

NAME, AGE, PAY = range(3)
bob = ['Bob Smith', 42, 10000]
bob[NAME]
PAY, bob[PAY]

bob =[['name', 'Bob Smith'], ['age', 42], ['pay', 10000] ]
sue = [['name', 'Sue Smith'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
    print(person[0][1], person[2][1])
    
[person[0][1] for person in people]

for person in people:
    print(person[0][1].split()[-1])
    person[2][1] *= 1.10
    
for person in people: print(person[2])

for person in people:
    for (name, value) in person:
        if name == 'name': print(value)
        
        
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue
        
for rec in people:
    print(field(rec, 'age'))

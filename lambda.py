#### The first way : ###

"""
    def sorter(item):
        return item['age']

    students = [
        {'name':'Bakr','age':16},
        {'name':'Carlos','age':16}
    ]

    students.sort(key=sorter)
    print(students)
"""

### The second way : ###

students = [
    {'name':'Bakr','age':16},
    {'name':'Carlos','age':16}
]

students.sort(key = lambda item : item['name'])
print(students)


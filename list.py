#creating a list of students
students = ["leroy","teddy","collins","gabriel","steve","sossie"]
print(students)

#creating an empty list
#students = []
print(students)

#indexing
print(students[1])#displays the second student in the list
print(students[0])#displays the first student in the list
print(students[-5:-1])#displays the fifth  student starting from the back of the list upto the second last student in the list
print(students[2:])#displays the thrid student in the list
print(students[2:5])#displays the second student in the list to the fifth stuent

# replacing a student in a list
students[1]="sonko1" 
print(students)

#loop through the list
for student in students:
    print(student)

#check if item exists
if "gabriel" in students:
    print("gabriel is there")

#methods
print(len(students))
students.append("gabriel")
print (students)
#adding  a name in the list by insertion
students.insert(3,"grace")
print (students)
#The pop() method removes the element at the specified position.
students = ["leroy","teddy","collins","gabriel","steve","sossie"]
x = students.pop(1)
print(x)
#The reverse() method reverses the sorting order of the elements.
students = ["leroy","teddy","collins","gabriel","steve","sossie"]
students.reverse()

print(students)
#The remove() method removes the first occurrence of the element with the specified value.
students = ["leroy","teddy","collins","gabriel","steve","sossie"]

students.remove("collins")

print(students)
#The sort() method sorts the list ascending by default.
students = ["leroy","teddy","collins","gabriel","steve","sossie"]

students.sort()

print(students)
#The clear() method removes all the elements from a list.
students.clear()
print(student)





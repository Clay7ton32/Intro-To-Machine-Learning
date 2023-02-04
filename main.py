"""
Clayton Carlson
1/25/2023
Intro to Machine Learning Assignment 1
"""
"""
#Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort, re add 2 values, and print
ages.sort()
ages.insert(0, ages[0])
ages.append(ages[len(ages) - 1])
print("Ages Sorted with min and max added again:\n" + str(ages))
#print the median value
median =  ages[int(len(ages)/2)] if len(ages) % 2 == 0 else (ages[int(len(ages)/2)] + ages[len(ages)-int(len(ages)/2)])/2
print("Median: " + str(median))

#Print the average
average_age = 0
for age in ages:
    average_age += age
average_age = average_age/len(ages)
print("Average: " + str(average_age))

#print the range
range = ages[len(ages)-1] - ages[0]
print("Range: " + str(range))
"""
"""
#Question 2
dog = {}
dog['name'] = ''
dog['color'] = ''
dog['breed'] = ''
dog['legs'] = ''
dog['age'] = ''
#first_name, last_name, gender, age, marital status,skills, country, city and address as keys for the dictionary
student = {'first_name' : '', 'last_name' : '', 'gender' : '',
           'age' : '', 'marital_status' : '', 'skills' : [],
           'country' : '', 'city' : '', 'address' : ''}
print(f"Length of student dict: {len(student)}")
print(f"DataType of Skills: {type(student['skills'])}")
student['skills'].append("Python")
student['skills'].append("Driving")
print(f"Dictionary Keys: {student.keys()}")
print(f"Dictionary Values: {student.values()}")
"""
"""
#Question 3
brothers = ('Wyatt', 'Ricky', 'Murphy')
sisters = ('Denise', 'Izzy', 'Lauryn')
siblings = brothers + sisters
print(f"I have {len(siblings)} siblings")
family_members = siblings + ('David', 'Jaime')
"""
"""
#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(f"The length of IT Companies = {len(it_companies)}")
it_companies.add('Twitter')
it_companies.update(['Samsung', 'Sony'])
it_companies.remove('Sony')
#The remove method will raise an error if the item doesn't exist, the discard method will not
print(f"Joining A & B {str(A.union(B))}")
print(f"Is A subset of B {str(A.issubset(B))}")
print(f"Is A disjoint set of B {A.isdisjoint(B)}")
C = A.update(B)
D = B.update(A)
print(f"Join A with B: {str(C)} \n Join B with A: {str(D)}")
print(f"Symmetric Difference of A & B: {A.symmetric_difference(B)}")
A.clear()
B.clear()
age_set = set()
age_set.update(age)
print(f"Comparing lengths set: {len(age_set)} list: {len(age)}")
"""
"""
#Question 5
print("The Radius is: ")
radius = int(input())
_area_of_circle_ = 3.14 * (radius ** 2)
_circum_of_circle_ = 2 * 3.14 * radius
print(f"The Circumference is: {_circum_of_circle_} and the area is: {_area_of_circle_}")
"""
"""
#Question 6
str_val = "I am a teacher and I love to inspire and teach people"
words = str_val.split(' ')
unique_words = set()
unique_words.update(words)
print(f"Unique Words: {len(unique_words)}")
"""

"""
#Question 7
str = "Name\t Age\t Country\t City\nAsabench\t 250\t Finland\t Helsinki"
print(str)
"""

"""
#Question 8
radius = 10
area = 3.14 * radius ** 2
print(f"The e area of a circle with radius {radius} is {area} meters square.")
"""
"""
#Question 9
weight_in = []
weight_kg = []
print("Please enter the number of elements")
elements = int(input())
for i in range(0, elements):
    new = int(input())
    weight_in.append(new)
for weight in weight_in:
    weight_kg.append(round(weight/2.205, 2))
print(f"Weight in pounds: {weight_in}")
print(f"Weight in Kg: {weight_kg}")
"""

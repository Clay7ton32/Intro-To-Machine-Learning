"""Assignment 2,
done in class on February 4, 2023
Clayton Carlson
"""
"""part 1"""
x = 1
for i in range(0, 11):
    if i < 4:
        print("* " * x)
        x += 1
    if i > 5:
        print("* " * x)
        x -= 1

"""part 2"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0, 10):
    if i % 2 == 1:
        print(my_list[i])

"""part 3"""
def getTypes(inList):
    return_list = []
    for item in inList:
        return_list.append(type(item))
    return return_list


x = [23, 'python', 23.98]
typeList = getTypes(x)
print(typeList)

"""part 4"""

def getUniqueVals(inList):
    return_list = []
    for item in inList:
        if not return_list.__contains__(item):
            return_list.append(item)
    return return_list

sample_list = [1,2,3,3,3,3,4,5]
output_list = getUniqueVals(sample_list)
print(output_list)

"""part 5"""
def upperAndLowerCase(strIn):
    upper_count = 0
    lower_count = 0
    for letter in strIn:
        if ord(letter) > 64 and ord(letter) < 91:
            upper_count += 1
        if ord(letter) > 96 and ord(letter) < 123:
            lower_count += 1
    print(f"The uppercase count is {upper_count}")
    print(f"The lowercase count is {lower_count}")


input_string = "The quick Brow Fox"
upperAndLowerCase(input_string)

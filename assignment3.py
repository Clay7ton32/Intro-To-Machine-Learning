import matplotlib.pyplot
import numpy as np
import matplotlib as mpl

#Question 1
#Part A
a = np.random.randint(1, 20, 15)
print(a)
b = a.reshape(3, 5)
print(b)
print()

for i in b:
    i[np.argmax(i)] = 0

print(b)
print()
c = np.random.randint(1, 20, (4, 3))
print(c)
print(c.shape)
print(type(c))
print(c.dtype)
print()

#part B
print("The start of part B")
twoByTwo = np.array([[3, -2], [1, 0]])
eigenVals, eigenVects = np.linalg.eig(twoByTwo)
print(eigenVals)
print(eigenVects)
print()
#part C
print("The start of part C")
threeByThree = np.array([[0, 1, 2], [3, 4, 5]])
diagSums = np.trace(threeByThree)
print(diagSums)
print()
#Part D
print("The start of part D")
dArr = np.array([1, 2, 3, 4, 5, 6])
print(dArr.reshape(2, 3))
print()
print(dArr.reshape(3, 2))
print()

#Start of Question 2
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])

matplotlib.pyplot.pie(popularity, labels=languages, autopct='%1.1f%%')
mpl.pyplot.show()

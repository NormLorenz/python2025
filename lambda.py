squared = lambda x: x ** 2
print (squared(5))

cubed = lambda x: x ** 3
print(cubed(3))

muliply = lambda x, y: x * y
print(muliply(3, 7))

nums = [1, 2, 3, 4, 5]
doubled_nums = map(lambda x: x * 2, nums)
print(list(doubled_nums)) 

words = ['hi', 'hello', 'cat', 'dog', 'elephant']
long_words = filter(lambda word: len(word) > 3, words)
print(list(long_words))

students = [('Alice', 88), ('Bob', 72), ('Charlie', 95), ('David', 85), ('Eve', 9)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=False)
print(sorted_students)

from functools import reduce

a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b) 
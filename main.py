numbers = [4, 2345345, 5555, 4, 5, 6, 7, 8, 9, 10]

iteratorr = numbers.__iter__()

print(iteratorr.__next__())
print(iteratorr.__next__())
print(iteratorr.__next__())
print(iteratorr.__next__())
print(iteratorr.__next__())
print(iteratorr.__next__())

print("Сокрытый итератор")
for i in numbers:
    print(i)

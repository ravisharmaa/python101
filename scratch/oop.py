from scratch.max_list_size import MaxListSize

a = MaxListSize(4)


a.push("hi")\
    .push("bye")\
    .push("nepal")\
    .push("yes")\
    .push("no")

print(a.get_list())

b = MaxListSize(1)

b.push('hey')
b.push('hi')
b.push('lets')

print(b.get_list())


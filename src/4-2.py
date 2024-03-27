def doh2():
    yield "Homer: D'oh!"
    yield "Lisa: A deer!"
    yield "Marge: A female deer!"


for line in doh2():
    print(line)

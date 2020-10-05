def myFunction(data):
    return data


data = [1.0, 5.0, 2.0, 3.5]

result = myFunction(data)

print(len(result))
assert len(result) > 100
print(result[99])


result[0] = 1.0

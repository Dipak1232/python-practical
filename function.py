def cube(number):
    result = number * number * number
    return result

value = int(input("Enter a number: "))

answer = cube(value)

print("Cube is:", answer)
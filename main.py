def test(city,name,age):
    print(city, name, age)


test('Волжск', 'Коля', 35)


print()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = 7
print('Факториал', (n), '=', factorial(n))

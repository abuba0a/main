def test(*params):
    print(8)
    print('dog', 'cat')
    print(True)


test()

print()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = 7
print('Факториал', (n), '=', factorial(n))

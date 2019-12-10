def my_func(x):
    i = 0
    while i < x:
        yield i
        i += 1

if __name__ == '__main__':
    print('String')
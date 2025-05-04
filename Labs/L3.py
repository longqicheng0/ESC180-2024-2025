def f():
    global x
    return x+3
    
if __name__ == '__main__':
    x = 10
    print(f())
    print(x)
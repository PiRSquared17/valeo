def foo(start=0):
    counter = [start]
    def bar():
        counter[0] = counter[0] + 1
        return counter[0]
    return bar

count = foo(10)
print count()
print count()

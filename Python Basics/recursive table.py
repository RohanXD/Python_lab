def table(n, i=1):
    if i < 10:
        print(f"{n} x {i} = {n * i}")
        table(n, i + 1)
    else:
        return
def series(a,b):
    if a<=b:
        table(a)
        series(a+1,b)

series(3,7)

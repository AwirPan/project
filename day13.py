def outer(num1):
    def inner(num2):
        nonlocal num1
        num1+=num2
        print(num1)
    return inner
fn=outer(10)
fn(10)
fn(10)
fn(10)
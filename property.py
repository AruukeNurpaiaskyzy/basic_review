def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("something is happening before the function is called")
        result=func(*args, **kwargs)
        print("something is happening after the function is called")

        return result
    return wrapper
    
@my_decorator
def add_numbers(*, a: int,  b: int) -> int:
    print("Adding numbers...")
    return a+b

result = add_numbers(a=1, b=2)
print(result)
    
import time

def my_decarator_time_checker(func):
    def wrapper():
        start_time=time.time()
        func()
        time_for_work=time.time()-start_time
        return  time_for_work, "Seconds for working: ", func()
    return wrapper

@my_decarator_time_checker
def hello():
    return "Hello, my name is ABbbubbgkakllalllar Abeba"

print(hello()) 
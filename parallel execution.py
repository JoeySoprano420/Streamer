import concurrent.futures

def task(num):
    return num * num

numbers = {1, 2, 3, 4, 5}

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(task, numbers)

print(list(results))

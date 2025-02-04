set concurrent_tasks:
    task1 = fetch_data()
    task2 = process_data(task1)
    task3 = store_data(task2)

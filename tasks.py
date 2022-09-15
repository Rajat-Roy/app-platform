from time import sleep
from huey.contrib.djhuey import periodic_task, task

# huey = SqliteHuey(results=True, filename='tasks.sqlite3')
# huey = MemoryHuey(results=True)


@task()
def add_numbers(a, b):
    return a + b


@task()
def sync_function():
    sleep(5)
    f = open("demofile2.txt", "a")
    f.write("Now the file has more more content!")
    f.close()
    print("task complete")

from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    # backend="redis://localhost:6379/1",
    backend="db+sqlite:///celery.sqlite",
)
app.conf.update(
    task_serializer="json",
    result_serializer="json",
    ignore_result=False,
)


@app.task(name="Task 1")
def teste(x, y):
    return x + y

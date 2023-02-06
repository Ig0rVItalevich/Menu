from celery import Celery

app = Celery(
    "celery_app",
    broker="amqp://guest@localhost//",
    backend="rpc://",
    include=["tasks.tasks"],
)

app.set_default()


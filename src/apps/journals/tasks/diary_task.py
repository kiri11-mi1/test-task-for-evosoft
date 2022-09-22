from celery import shared_task


@shared_task
def print_hello():
    print(40*'*', flush=True)
    print('HELLO', flush=True)
    print(40*'*', flush=True)


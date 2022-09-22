import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("apps")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(packages=['apps'])


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    from apps.journals.tasks import delete_old_diary
    from apps.journals.constants import TIME_DELETING_OLD_DIARY

    sender.add_periodic_task(TIME_DELETING_OLD_DIARY, delete_old_diary.s())


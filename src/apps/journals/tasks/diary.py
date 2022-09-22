from config import celery_app


@celery_app.task
def delete_old_diary():
    from ..models import Diary
    from datetime import datetime

    today = datetime.now().date()
    diaries = Diary.objects.filter(expiration__lte=today)
    for diary in diaries:
        diary.delete()
        print(f'Deleting {diary} - {diary.expiration}')

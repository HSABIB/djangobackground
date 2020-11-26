from workers import task

from workers.util import autodiscover

from core.models import BaseModel

from datetime import datetime

autodiscover()

@task(schedule=2)
def say_hello():
    bm = BaseModel.objects.first()
    bm.title = str(datetime.now())
    bm.save()
    print( datetime.now() )
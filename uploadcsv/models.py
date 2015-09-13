from django.db import models
from datetime import datetime

class UploadCsv(models.Model):
    class Meta:
        app_label = 'uploadcsv'
        db_table = 'uploadcsv'

    title = models.CharField(max_length = 200)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d')
    city = models.CharField(max_length = 100)
    user_id = models.IntegerField(default="1")
    created_date = models.DateTimeField(default=datetime.now)
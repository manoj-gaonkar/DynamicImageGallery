from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Images(models.Model):
    user = models.ForeignKey( User, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'imagegallery/' )
    caption = models.CharField(max_length=500)
    date = models.DateTimeField( auto_now_add= datetime.now() )
    

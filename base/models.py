from django.db import models


class BaseDateModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class BaseTextDateModel(BaseDateModel):
    text = models.TextField()
    
    class Meta:
        abstract = True

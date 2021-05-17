from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=1000)
    labels = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    priority = models.IntegerField(validators=[ MinValueValidator(1), MaxValueValidator(3) ])


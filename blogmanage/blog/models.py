from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16, null=True)
    password = models.CharField(max_length=16, null=True)

    class Meta:
        db_table = 'user'

class Acticle
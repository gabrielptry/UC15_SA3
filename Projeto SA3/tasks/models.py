from django.db import models


class Task(models.Model):
    titulo = models.CharField(max_length=30, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    terminado_em = models.DateTimeField(null=True)

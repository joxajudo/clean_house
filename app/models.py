from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

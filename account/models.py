from django.db import models

class Account(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.user_name
        
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


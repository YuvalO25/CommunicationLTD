from django.db import models
from django.contrib.auth.models import User

class Sector(models.Model):
    user_type= models.CharField(max_length=100)

    def __str__(self):
        return self.user_type

class Package(models.Model):
    package_name = models.CharField(max_length=100)
    package_size = models.IntegerField()  # Size in MB

    def __str__(self):
        return self.package_name
        
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class PasswordHistory(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        hashed_password = models.CharField(max_length=300)
        changed_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user.username} - {self.changed_at}"
    
    password_hash = models.CharField(max_length=256)
    password_salt = models.CharField(max_length=256)
    password_history = models.JSONField(default=list)
    login_attempts = models.IntegerField(default=0)

    def str(self):
        return self.username




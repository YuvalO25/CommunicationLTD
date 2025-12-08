from django.contrib.auth.models import User
from django.db import models


class Sector(models.Model):
    user_type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user_type


class Package(models.Model):
    package_name = models.CharField(max_length=100)
    package_size = models.IntegerField()  # Size in MB

    def __str__(self) -> str:
        return self.package_name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    password_hash = models.CharField(max_length=256, blank=True)
    password_salt = models.CharField(max_length=256, blank=True)
    password_history = models.JSONField(default=list, blank=True)
    login_attempts = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class PasswordHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="password_history",
    )
    password_hash = models.CharField(max_length=300)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-changed_at",)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.changed_at:%Y-%m-%d %H:%M:%S}"





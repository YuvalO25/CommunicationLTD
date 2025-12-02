from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from core.models import PasswordHistory

@receiver(post_save, sender=User)
def save_password_to_history(sender, instance, created, **kwargs):
    """
    Signal to save the password hash to history whenever a user is saved.
    """
    last_history = PasswordHistory.objects.filter(user=instance).first()

    if not last_history or last_history.password_hash != instance.password:
        PasswordHistory.objects.create(user=instance, password_hash=instance.password)
        history_ids = PasswordHistory.objects.filter(user=instance).values_list('id', flat=True)[:3]
        PasswordHistory.objects.filter(user=instance).exclude(id__in=history_ids).delete()


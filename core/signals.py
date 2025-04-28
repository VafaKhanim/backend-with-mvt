from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Blog, Subscribe


@receiver(post_save, sender=Blog)
def send_notification_to_subscribers(sender, instance, created,  **kwargs):
    if created:  # yeni blog əlavə olunanda
        subject = f"Yeni Blog: {instance.title}"
        message = f"Salam,\n\nYeni blogumuz yayımlandı: {instance.title}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [sub.email for sub in Subscribe.objects.all()]

        if recipient_list:
            send_mail(subject, message, from_email, recipient_list)

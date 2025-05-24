from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length = 100)
    sub_title = models.CharField(max_length = 150)
    context  = models.TextField()
    blog_image = models.ImageField(upload_to = 'blog_images/')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return self.title



class Furnitures(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    furniture_image = models.ImageField(upload_to = 'furnitures_image/')


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email





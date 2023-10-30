from django.db import models

# Create your models here.
class User(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    mail = models.EmailField()

class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
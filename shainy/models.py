from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=30)
    event_date = models.DateField(null=True)
    description = models.CharField(max_length=500)
    date_pub = models.DateField(auto_now_add=True)

class ResponseModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user1')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author_id')

from django.db import models
from contas.models import User
from kits.models import Kit

class Tutorial(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, related_name='tutorials')
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    video_url = models.TextField()
    duration_seconds = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self): return self.title

class TutorialComment(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutorial_comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
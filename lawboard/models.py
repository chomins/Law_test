from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LawBoard(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published', null = True)
    writer = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    scrap  = models.ManyToManyField(User, blank= True, related_name="LawBoard_scrap")


    def __str__(self):
        return self.title

class MeetingBoard(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published', null = True)
    writer = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

class LB_comment(models.Model):
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()
    lbcomment = models.ForeignKey(LawBoard, on_delete=models.CASCADE)

class MB_comment(models.Model):
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()
    mbcomment = models.ForeignKey(MeetingBoard, on_delete=models.CASCADE)

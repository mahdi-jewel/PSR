from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=2000, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-upload_date']
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} : {}'.format(self.user, self.post)


class OJStanding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='standing')
    uva_id = models.CharField(max_length=250, blank=True,null=True)
    uva_username = models.CharField(max_length=250, blank=True,null=True)
    uva_ranking = models.CharField(max_length=250, blank=True,null=True,default=0)
    uva_submission = models.CharField(max_length=250, blank=True,null=True,default=10)
    codeforces_id = models.CharField(max_length=250, blank=True,null=True)
    codeforces_username = models.CharField(max_length=250, blank=True,null=True)
    codeforces_ranking = models.CharField(max_length=250, blank=True,null=True,default=0)
    codeforces_submission = models.CharField(max_length=250, blank=True,null=True,default=10)
    total_submission = models.IntegerField(blank=True,null=True,default=0)

    def save(self, *args, **kwargs):
        self.total_submission = int(self.codeforces_submission) + int(self.uva_submission)
        super(OJStanding, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.user.username)

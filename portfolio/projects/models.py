from django.db import models


class Job(models.Model):
    # summary
    title = models.CharField(max_length=50, default='Python')
    summary = models.CharField(max_length=500)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.summary


class PostImage(models.Model):
    post = models.ForeignKey(Job, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.post.title

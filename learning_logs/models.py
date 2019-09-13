from django.db import models


class Topic(models.Model):
    """Theme, which user is learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string model view"""
        return self.text


class Entry(models.Model):
    """Info about certain users topic"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns string model view"""
        return self.text[:50] + "..."

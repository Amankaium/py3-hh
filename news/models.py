from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class New(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=55)
    views_count = models.IntegerField(default=0)
    user_views = models.ManyToManyField(
        to=User,
        related_name='new_views',
        blank=True,
    )


class NewsViews(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    new = models.ForeignKey(
        to=New,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        unique_together = [['user', 'new']]

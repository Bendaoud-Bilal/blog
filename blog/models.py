# blog/models.py
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


# Username (leave blank to use 'mytekdz'): bilo
# Email address: bendaoudbilal717@gmail.com
# Password: BILObend123


#   to delete a superuser/admin
# python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> user=User.objects.get(username='the actual username')
# >>> user.delete()

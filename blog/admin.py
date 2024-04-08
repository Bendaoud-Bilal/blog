# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)


# Username (leave blank to use 'mytekdz'): bilo
# Email address: bendaoudbilal717@gmail.com
# Password: BILObend123


# second user : bilal / bendaoud123


#   to delete a superuser/admin
# python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> user=User.objects.get(username='the actual username')
# >>> user.delete()

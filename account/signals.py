from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group



@receiver(post_save, sender=User)
# user create edildiğinde onun için token da create edilecek böylece user register olduğunda tekrar login olmasına gerek kalmayacak
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)  
        user= User.objects.get(username = instance)
        # eğer user super user değilse Read_Only grubuna alacağız 
        if not user.is_superuser:
            group = Group.objects.get(name='Read_Only') 
            user.groups.add(group)
            user.save()
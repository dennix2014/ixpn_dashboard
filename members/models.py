from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from allauth.account.signals import Signal
from django.dispatch import receiver
from django.contrib import messages
from django.utils.text import slugify
User = get_user_model()
from members.all_choices import states_in_nigeria, ports, status, membership



class Editor(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()

    class Meta:
        abstract = True


class POP(Editor):
    name = models.CharField(max_length=50)
    state_located = models.CharField(max_length=20, choices=states_in_nigeria)
   

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name) + '-' + (self.state_located).lower()

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {self.state_located}'


class Member(Editor):
    short_name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=status, default='Active')
    membership = models.CharField(max_length=20, choices=membership, default='Full')
    
   

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.short_name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.short_name


class PortConnection(Editor):
    member_name = models.ForeignKey(Member, on_delete=models.CASCADE, default=1, related_name='memcon')
    pop = models.ForeignKey(POP, on_delete=models.CASCADE)
    port_capacity = models.CharField(max_length=10, choices=ports)
    no_of_port = models.IntegerField(choices=list(zip(range(1, 16), range(1, 16))))
    port_fee = models.IntegerField(default=0)
    membership_fee = models.IntegerField(default=0)
    date_connected = models.DateField(default=timezone.now)
    

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.member_name.short_name + "-" + self.pop.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.member_name}, {self.pop},'

# def switch(Editor):
#     manufacturer = models.CharField(max_length=30)
#     model = models.CharField(max_length=30)
#     ports = models.ma

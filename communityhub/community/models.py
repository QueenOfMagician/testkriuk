from django.db import models
from accounts.models import Users
from django.utils import timezone
# Create your models here.

class Group(models.Model):
    owner = models.OneToOneField(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    createdfrom = models.DateField(auto_created=True, default=timezone.now)
    members = models.ManyToManyField(Users, through='GroupMember', related_name='group_memberships')
    def __str__(self):
        return self.name

class GroupMember(models.Model):
    status_cho = [("Members","Members"),("Admin","admin")]
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_cho)
    joins = models.DateField(auto_created=True, default=timezone.now)
    class Meta:
        unique_together = ('group', 'member')
    def __str__(self):
        return (f"group: {self.group} | member: {self.member}")
    
class PesanGrup(models.Model):
    pengirim = models.ForeignKey(Users, on_delete=models.CASCADE)
    grup = models.ForeignKey(Group,on_delete=models.CASCADE)
    text_pesan = models.TextField(null=False)
    kirim = models.DateTimeField(null=False, auto_now_add=True)
    def __str__(self):
        return (f"{self.pengirim} || {self.grup}")
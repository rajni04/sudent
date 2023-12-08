from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class ClassDetail(models.Model):
    name=models.CharField(max_length=30,null=True, blank=True)
    total_student=models.IntegerField()
    def __str__(self):
        return self.name or ''

STATUS_CHOICES =(
    (1, ("inactive")),
    (2, ("active")),

)
class CustomUser(AbstractUser):
    username=None
    phone_number=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=20,blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    dob=models.DateField(blank=True, null=True)
    profile_image=models.ImageField(upload_to="student/")
    stdclass=models.ForeignKey(ClassDetail,on_delete=models.DO_NOTHING,default=1)
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects = UserManager()

    def __str__(self):
        return f"{self.id}--{self.phone_number}"


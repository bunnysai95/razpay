from django.db import models

# Create your models here.
class ApplicationFormClass(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=False)
    board = models.CharField(max_length=20, default=False)
    fatherName = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    qualification = models.CharField(max_length=30)
    schoolName = models.CharField(max_length=30)
    schoolAddress = models.CharField(max_length=200)
    homeAddress = models.CharField(max_length=200)
    state = models.CharField(max_length=30)
    aadharNumber = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=12)
    emailID = models.EmailField(max_length=40)
    personPhoto = models.ImageField(upload_to='images/')
    signaturePhoto = models.ImageField(upload_to='images/')
    username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.firstName

class Qrcode(models.Model):
    TRANSACTION_ID = models.CharField(max_length=50)
    PHONE_NUMBER = models.IntegerField()
    name = models.CharField(max_length=30)
    
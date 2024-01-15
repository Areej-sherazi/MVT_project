from django.db import models

# Create your models here.
# creating a student model

class students(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(null=True)
    id=models.AutoField(primary_key=True)
    grade=models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = "students"


    def __str__(self):
        return self.name


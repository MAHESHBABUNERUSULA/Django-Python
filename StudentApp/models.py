from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=150)
    course_duration=models.CharField(max_length=150)
    course_fees=models.IntegerField()

    def __str__(self):
        return self.course_name

class City(models.Model):
    city_name=models.CharField(max_length=150)

    def __str__(self):
        return self.city_name

class Student(models.Model):
    stud_name=models.CharField(max_length=150)
    stud_phno=models.BigIntegerField()
    stud_email=models.EmailField(max_length=150)
    paid_fee=models.IntegerField()
    pending_fee=models.IntegerField()
    stud_course=models.ForeignKey(Course,on_delete=models.CASCADE)   # if we delete any records in parent table the records of child table data will be delete
    stud_city=models.ForeignKey(City,on_delete=models.CASCADE)



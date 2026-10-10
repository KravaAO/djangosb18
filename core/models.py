from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    courses_id = models.ManyToManyField('Course', related_name='students', blank=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name}'s Profile"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students_id = models.ManyToManyField(Student, related_name='courses', blank=True)
    teachers_id = models.ManyToManyField('Teacher', related_name='courses', blank=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
   
    def __str__(self):
        return self.name


class Lesson(models.Model):
    STATUS_CHOICES = [
        ('progress', 'В процесі'),
        ('finished', 'Завершено'),
        ('not_started', 'Не розпочато'),
        ('closed', 'Закрито'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    def __str__(self):
        return self.title
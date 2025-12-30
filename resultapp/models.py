from django.db import models

# Create your models here.
class Class(models.Model):
    Year = models.CharField(max_length=100)
    Semester = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True) #when the class is created
    updation_date = models.DateTimeField(auto_now=True) #when the class is updated

    def __str__(self): #string representation of the class
        return f"{self.Year} - {self.Semester}"
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True) #when the class is created
    updation_date = models.DateTimeField(auto_now=True) #when the class is updated

    def __str__(self): #string representation of the class
        return f"{self.subject_name} - {self.subject_code}"

class Student(models.Model):
    GENDER_CHOICES=(
        ('Male','Male'),
        ('Female','Female'),
    )
    name = models.CharField(max_length=100)
    roll_id = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) #gender field with choices
    dob = models.CharField(max_length=50)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True) #Class sanga relationship
    creation_date = models.DateTimeField(auto_now_add=True) #when the class is created
    updation_date = models.DateTimeField(auto_now=True) #when the class is updated
    status=models.IntegerField(default=1) #to check if the student is active or inactive

    def __str__(self): #string representation of the class
        return self.name 
    
class SubjectCombination(models.Model):
    student_year = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True) #Class sanga relationship
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True) #Subject sanga relationship
    status=models.IntegerField(default=1) #to check if the student is active or inactive
    creation_date = models.DateTimeField(auto_now_add=True) #when the class is created
    updation_date = models.DateTimeField(auto_now=True) #when the class is updated
    
    def __str__(self): #string representation of the class
        return f" {self.student_year} - {self.subject} " 
    
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    student_year = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True) 
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    marks = models.FloatField()
    posting_date = models.DateTimeField(auto_now_add=True) #when the class is created
    updation_date = models.DateTimeField(auto_now=True) #when the class is updated
    
    def __str__(self): #string representation of the class
        return f" {self.student} - {self.subject} - {self.marks} " 


class Notice(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True) #when the class is created
    updation_date = models.DateTimeField(auto_now=True) #when the class is updated
    
    def __str__(self): #string representation of the class
        return self.title

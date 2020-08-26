from django.db import models

class Exam(models.Model):
    qnumber = models.IntegerField(default=1, primary_key=True)
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)

    def __str__(self):
        return self.Question
        
    


from django.db import models

# Create your models here.

class data(models.Model):
    name = models.CharField(max_length=50)
    add = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Question(models.Model):
    question= models.CharField(max_length=300)

    def __str__(self):
        return self.question
    
class choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
    option = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option
    
class Voter(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    voter=models.CharField(max_length=50)

    def __str__(self):
        return self.voter
from django.db import models
'''
This file define the models(tables) that will be in use to match a job to candidate.
Note- an ID attribute is generated for each model automaticaly
'''

class Skill(models.Model):
    name = models.CharField(max_length=255, unique= True)

    def __str__(self) -> str:
        return self.name

class Candidate(models.Model):
     title = models.CharField(max_length=255)
     skills = models.ManyToManyField(Skill) 
    
     def __str__(self) -> str:
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill) 

    def __str__(self) -> str:
        return self.title
        
# class CandidatesByTitle(models.Model):
#     title = models.CharField(max_length=255, unique=True)
#     candidates = models.ManyToManyField(Candidate)

#     def __str__(self) -> str:
#         return self.title

# class CandidateBySkill(models.Model):
#     skill = models.CharField(max_length= 255, unique=True)
#     candidates = models.ManyToManyField(Candidate)
    
#     def __str__(self) -> str:
#         return self.skill

    

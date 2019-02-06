from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name = "position", null=True, blank=True)
    birthdate = models.DateField("Birthdate")
    platform = models.TextField(max_length=100)

    def __str__(self):
        return self.firstname + ", " + self.lastname

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="candidate", null=True, blank=True)
    vote_datetime = models.DateTimeField("Date Voted", auto_now_add=True)

    # def __str__(self):
    #     return self.vote_datetime
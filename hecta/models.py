from django.db import models


class GameResult(models.Model):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = [(GENDER_MALE, "Male"), (GENDER_FEMALE, "Female")]

    person_name = models.CharField(max_length=100)
    person_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.person_name

from otree.api import models

class ExitSurvey(models.Group):
    capital_city = models.StringField(
        label="What is the capital city of Kenya?",
        choices=["Kisumu", "Nairobi", "Mombasa"],
    )
    addition_result = models.PositiveIntegerField(
        label="What is 14 + 15?",
        min=29,
        max=29,
    )
    population = models.PositiveIntegerField(
        label="What is the population of Kenya?",
        min=1,
        max=80000000,
    )

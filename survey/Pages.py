from otree.api import Page

class ExitSurveyPage(Page):
    form_model = 'player'
    form_fields = ['capital_city', 'addition_result', 'population']

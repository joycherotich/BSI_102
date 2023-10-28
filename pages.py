from otree.api import Page;

class Page1(Page):
    form_model = 'player'
    form_fields = ['offer']

class Page2(Page):
    pass

class Results(Page):
    pass

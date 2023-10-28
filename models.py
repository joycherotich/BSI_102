from otree.api import models, BaseSubsession, BaseGroup, BasePlayer;

class Constant:
    endowment = 200

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    punish = models.BooleanField(
        initial=False,
        doc="True if Player 3 punishes Player 1, otherwise False",
    )
    offer_accepted = models.CurrencyField(
        doc="Amount sent by Player 1 and accepted by Player 2",
    )

class Player(BasePlayer):
    offer = models.CurrencyField(
        min=0,
        max=Constant.endowment,
        doc="Amount offered by Player 1 to Player 2",
        label="How much money to offer to Player 2?",
    )
    decision = models.StringField(
        choices=['Punish', 'Not Punish'],
        doc="Player 3's decision to punish or not",
        label="Do you want to punish Player 1?",
    )

    def set_payoffs(self):
        if self.group.punish:
            self.payoff = 0
        else:
            self.payoff = Constant.endowment - self.offer

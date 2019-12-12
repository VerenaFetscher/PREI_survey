from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'leftright']


class Inequality(Page):
    form_model = 'player'
    form_fields = ['system']

class Earnings(Page):
    form_model = 'player'
    form_fields = ['doctor',
                   'chairman',
                   'shopassistant',
                   'unskilled',
                   'minister']

class WealthPoverty(Page):
    form_model = 'player'
    form_fields = ['wealth',
                   'poverty',
                   'avgwage',
                   'famincome',
                   'change']

class Redistribution(Page):
    form_model = 'player'
    form_fields = ['redistribution']

class Final(Page):
    pass

class Welcome(Page):
    pass



page_sequence = [
    Welcome,
    Demographics,
    Inequality,
    WealthPoverty,
    Redistribution,
    Final
]

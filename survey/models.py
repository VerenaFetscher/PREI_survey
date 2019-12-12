from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)



class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        label='What is your age?',
        min=13, max=125)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    leftright = models.IntegerField(
        label = 'Here we have a scale which runs from left to right. Thinking of your own political views, where would you place these on this scale?',
        widget = widgets.RadioSelectHorizontal,
        choices=[
            [1, 'left'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, ''],
            [8, ''],
            [9, ''],
            [10, 'right']
        ])

    system = models.IntegerField(
        label = 'Please choose',
        widget = widgets.RadioSelectHorizontal,
        choices=[
            [1, 'System A'],
            [2, 'System B'],
            [3, 'System C'],
            [4, 'System D'],
            [5, 'System E'],
        ])

    doctor = models.IntegerField(
        label = 'About how much do you think a doctor in general practice earns?',
        min=0, max=10000000
    )

    chairman = models.IntegerField(
        label='How much do you think a chairman of a large national corporation earns?',
        min=0, max=10000000
    )

    shopassistant = models.IntegerField(
        label='How much do you think a shop assistant earns?',
        min=0, max=10000000
    )

    unskilled = models.IntegerField(
        label='How much do you think an unskilled worker in a factory earns?',
        min=0, max=10000000
    )

    minister = models.IntegerField(
        label='How much do you think a cabinet minister in the national government earns?',
        min=0, max=10000000
    )

    wealth = models.IntegerField(
        label='What proportion of adult wealth do you think the wealthiest 1% in Germany own? (in %)',
        min=0, max=100
    )

    poverty = models.IntegerField(
        label='What proportion of people in Germany do you think are poor? (in %)',
        min=0, max=100
    )

    avgwage = models.IntegerField(
        label='What do you think the average annual wage for a full-time worker is in Germany? (in euros)',
        min=0, max=10000000
    )

    famincome = models.IntegerField(
        label='Which decile of the income distribution do you think your family belongs to?',
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'no answer'],
    )

    change = models.IntegerField(
        label='Do you think the gap between the rich and the poor in Germany has increased, '
              'decreased, or stayed the same in the last five years?',
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'increased'],
            [2, 'decreased'],
            [3, 'stayed the same'],
        ],
    )

    redistribution = models.IntegerField(
        label='Do you think it is the responsibility of the government to reduce the differences in income between '
              'people with high incomes and those with low incomes?',
        widget=widgets.RadioSelect,
        choices=[
            [1, 'strongly agree'],
            [2, 'agree'],
            [3, 'neither agree nor disagree'],
            [4, 'disagree'],
            [5, 'strongly disagree'],
        ],
    )








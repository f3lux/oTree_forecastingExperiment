from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Felix Reinfurt'

doc = """
Experiment with entirely explicit feedback (First experiment in thesis)
"""


class Constants(BaseConstants):
    name_in_url = 'intro_chart'
    path_capture = 'xai1_intro/Capture.PNG'
    path_x1 = 'xai1_intro/xplainUnderstand1.png'
    path_x2 = 'xai1_intro/xplainUnderstand2.png'
    path_x3 = 'xai1_intro/xplainUnderstand3.png'
    players_per_group = None
    num_rounds = 1

    endowment = c(0)

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.ctrl_treat = p.role()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sequence_of_apps = models.LongStringField()
    ctrl_treat = models.StringField()

    aim = models.IntegerField(
        label="What should you aim for in this experiment?",
        choices=[
            [0, 'Finish first.'],
            [1, 'Achieve the highest forecast accuracy.'],
            [2, 'Checking my mails secretly without anyone noticing.'],
        ],
        widget=widgets.RadioSelect,
    )
    aim_wrong = models.IntegerField(initial=0)

    mechanism1 = models.IntegerField(
        label="Which information is available during the first decision stage?",
        choices=[
            [0, 'Only a forecast from a ML algorithm.'],
            [1, 'Only historical data of the demand.'],
            [2, 'Both.']
        ],
        widget=widgets.RadioSelect,
    )
    mechanism1_wrong = models.IntegerField(initial=0)

    mechanism2 = models.IntegerField(
        label="Which information is available during the second decision stage?",
        choices=[
            [0, 'Only a forecast from a ML algorithm.'],
            [1, 'Only historical data of the demand.'],
            [2, 'Both.']
        ],
        widget=widgets.RadioSelect,
    )
    mechanism2_wrong = models.IntegerField(initial=0)

    accuracy1 = models.IntegerField(
       label="How do you make your decision in the first decision stage?",
      choices=[
            [0,'I have to adopt the forecast of the ML algorithm.'],
            [1,'I make a forecast and can take the additional historical information as support into account.'],
            [2,'I ask my neighbour what the right value might be.']
         ],
        widget=widgets.RadioSelect
    )
    accuracy1_wrong = models.IntegerField(initial=0)

    accuracy2 = models.IntegerField(
        label="How do you make your decision in the second decision stage?",
        choices=[
            [0, 'I have to adopt the forecast of the ML algorithm.'],
            [1, 'I change my initial forecast, no matter what.'],
            [2, 'I can decide whether I change the initial forecast or not, taking into account the available'
                ' additional information or not.']
        ],
        widget=widgets.RadioSelect
    )
    accuracy2_wrong = models.IntegerField(initial=0)

    procedure = models.IntegerField(
        label="How will the entire forecasting procedure over all time steps look like?",
        choices=[
            [0, 'First, I make all first decision stage forecasts for all time steps, then I get into the second '
                'decision stage for all of them.'],
            [1, 'I make a forecast in the first decision stage and then go on to the next time step.'],
            [2, 'I make a forecast in the first decision stage, then I have the chance to revise the forecast '
                'in the second decision stage. I repeat this procedure for each time step.']
        ],
        widget=widgets.RadioSelect
    )
    procedure_wrong = models.IntegerField(initial=0)

    x1 = models.IntegerField(
        label="Which statements are true?",
        choices=[
            [0, '1. & 2.'],
            [1, 'Only 2.'],
            [2, '1. & 3.']
        ],
        widget=widgets.RadioSelect
    )
    x1_wrong = models.IntegerField(initial=0)

    x2 = models.IntegerField(
        label="Which statements are true?",
        choices=[
            [0, '1. & 3.'],
            [1, 'Only 3.'],
            [2, 'All.']
        ],
        widget=widgets.RadioSelect
    )
    x2_wrong = models.IntegerField(initial=0)

    x3 = models.IntegerField(
        label="Which statements are true?",
        choices=[
            [0, '1. & 3.'],
            [1, 'Only 1.'],
            [2, '1. & 2.']
        ],
        widget=widgets.RadioSelect
    )
    x3_wrong = models.IntegerField(initial=0)

    def role(self):
        if self.id_in_group % 2 == 1:
            return 'control'
#        elif self.id_in_group % 4 == 2:
#            return 'treatment1'
#        elif self.id_in_group % 4 == 3:
#            return 'treatment2'
        else:
            return 'treatment3'

    def is_treat(self):
        return self.role() == 'treatment'
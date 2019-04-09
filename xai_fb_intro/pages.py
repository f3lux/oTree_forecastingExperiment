from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass

class Instructions(Page):
    pass

class SampleScreen(Page):
    pass

class Algorithm(Page):
    def is_displayed(self):
        if self.player.role() in ('treatment1', 'treatment2', 'treatment3_fb'):
            return True
        else:
            return False

class Understanding1(Page):
    form_model = 'player'
    form_fields = ['aim']

    def aim_error_message(self, choice):
        if choice != 1:
            self.player.aim_wrong = self.player.aim_wrong+1
            return 'Please choose the correct answer!'

class Understanding2(Page):
    form_model = 'player'
    form_fields = ['mechanism1']

    def mechanism1_error_message(self, choice):
        if choice != 1:
            self.player.mechanism1_wrong = self.player.mechanism1_wrong + 1
            return 'Please choose the correct answer!'

class Understanding3(Page):
    form_model = 'player'
    form_fields = ['mechanism2']

    def mechanism2_error_message(self, choice):
        if choice != 2:
            self.player.mechanism2_wrong = self.player.mechanism2_wrong + 1
            return 'Please choose the correct answer!'

class Understanding4(Page):
    form_model = 'player'
    form_fields = ['accuracy1']

    def accuracy1_error_message(self, choice):
        if choice != 1:
            self.player.accuracy1_wrong = self.player.accuracy1_wrong + 1
            return 'Please choose the correct answer!'

class Understanding5(Page):
    form_model = 'player'
    form_fields = ['accuracy2']

    def accuracy2_error_message(self, choice):
        if choice != 2:
            self.player.accuracy2_wrong = self.player.accuracy2_wrong + 1
            return 'Please choose the correct answer!'

class Understanding6(Page):
    form_model = 'player'
    form_fields = ['procedure']

    def procedure_error_message(self, choice):
        if choice != 2:
            self.player.procedure_wrong = self.player.procedure_wrong + 1
            return 'Please choose the correct answer!'

class IntroX(Page):
    def is_displayed(self):
        return self.player.role() == 'treatment3_fb'

class InX(Page):
    def is_displayed(self):
        return self.player.role() == 'treatment3_fb'

class UnderstandingX1(Page):
    def is_displayed(self):
        return self.player.role() == 'treatment3_fb'

    form_model = 'player'
    form_fields = ['x1']

    def x1_error_message(self, choice):
        if choice != 0:
            self.player.x1_wrong = self.player.x1_wrong + 1
            return 'Please choose the correct answer!'

class UnderstandingX2(Page):
    def is_displayed(self):
        return self.player.role() == 'treatment3_fb'

    form_model = 'player'
    form_fields = ['x2']

    def x2_error_message(self, choice):
        if choice != 1:
            self.player.x2_wrong = self.player.x2_wrong + 1
            return 'Please choose the correct answer!'

class UnderstandingX3(Page):
    def is_displayed(self):
        return self.player.role() == 'treatment3_fb'

    form_model = 'player'
    form_fields = ['x3']

    def x2_error_message(self, choice):
        if choice != 2:
            self.player.x3_wrong = self.player.x3_wrong + 1
            return 'Please choose the correct answer!'

class Wait(Page):
    pass

class Wait1(Page):
    pass


class Wait2(Page):
    pass


page_sequence = [
    Welcome,
    Instructions,
    SampleScreen,
    Understanding1,
    Understanding2,
    Understanding3,
    Understanding4,
    Understanding5,
    Understanding6,
    Wait1,
    Algorithm,
    InX,
#    IntroX,
    UnderstandingX1,
    UnderstandingX2,
    UnderstandingX3,
    Wait2,
]

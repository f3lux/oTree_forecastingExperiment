from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class P1(Page):
    pass

class P2(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'nationality', 'education', 'study1', 'study2', 'edu_background', 'occupation']


class P3(Page):
    form_model = 'player'
    form_fields = ['experiment1', 'experiment2', 'knowledge1', 'knowledge2', 'experience']


class P3_(Page):
    form_model = 'player'
    form_fields = ['course', 'forecasting_years']

    def is_displayed(self):
        return self.player.experience == True

class P4 (Page):
    form_model = 'player'
    form_fields = ['interaction', 'adjustment_frequency', 'additional_info1', 'additional_info2', 'feedback']

class P5(Page):
    def is_displayed(self):
        return self.player.ctrl_treat == "control_fb"
    form_model = 'player'
    form_fields = ['algorithm_insights', 'algorithm_insights1', 'algorithm_insights5', 'algorithm_insights6']

class P6(Page):
    def is_displayed(self):
        return self.player.ctrl_treat == "treatment1"
    form_model = 'player'
    form_fields = ['algorithm_insights', 'algorithm_insights2', 'algorithm_insights5', 'algorithm_insights6', 'algorithm_insights7', 'algorithm_insights8']

class P7(Page):
    def is_displayed(self):
        return self.player.ctrl_treat == "treatment2"
    form_model = 'player'
    form_fields = ['algorithm_insights', 'algorithm_insights3', 'algorithm_insights5', 'algorithm_insights6', 'algorithm_insights7', 'algorithm_insights8']

class P8(Page):
    def is_displayed(self):
        return self.player.ctrl_treat == "treatment3_fb"
    form_model = 'player'
    form_fields = ['algorithm_insights', 'algorithm_insights4', 'algorithm_insights4_1', 'algorithm_insights5', 'algorithm_insights6']

class P8_(Page):
    form_model = 'player'
    form_fields = ['algorithm_insights7', 'algorithm_insights8', 'algorithm_insights8_1', 'algorithm_insights8_2', 'algorithm_insights8_3']


class P9 (Page):
    form_model = 'player'
    form_fields = ['algorithm_insights9', 'algorithm_insights9_1', 'algorithm_insights10', 'algorithm_insights11']

class P10 (Page):
    form_model = 'player'
    form_fields = ['final_comment']







class Goodbye(Page):
    pass

class End(Page):
    pass
    #def is_displayed(self):
        #if hasattr(self.participant.vars, 'rounds'):
           #return True
        #else:
            #return False



page_sequence = [
    P1,
    P2,
    P3,
    P3_,
    P4,
    P5,
    P6,
    P7,
    P8,
    P8_,
    P9,
    P10,
    Goodbye,
    End
]
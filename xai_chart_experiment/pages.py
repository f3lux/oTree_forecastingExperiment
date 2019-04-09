from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Scenario1_Description(Page):
    pass

class Scenario1_Forecast(Page):
    form_model = 'player'
    form_fields = ['S1Forecast']


class Forecast1_Init(Page):
    form_model = 'player'
    form_fields = ['F1_Initial']

    def vars_for_template(self):
        return self.subsession.vars_for_template()

class Forecast1_Rev(Page):
    #def is_displayed(self):
     #   return not self.player.is_treat()

    form_model = 'player'
    form_fields = ['F1_Revised']


    def vars_for_template(self):
        return self.subsession.vars_for_template()

    def before_next_page(self):
        self.player.calc_ape()

class Forecast1_Rev_Treat(Page):
    def is_displayed(self):
        return self.player.is_treat()

    form_model = 'player'
    form_fields = ['F1_Revised_Treat']

    def vars_for_template(self):
        return self.subsession.vars_for_template()

    def before_next_page(self):
        self.player.calc_ape()

class Feedback(Page):
    def vars_for_template(self):
        context = self.subsession.vars_for_template()
        context.update(self.player.vars_for_template())
        return context

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.player.get_final_accuracy()
            self.player.participant_vars_dump = str(self.participant.vars)

class Fb(Page):
    def vars_for_template(self):
        context = self.subsession.vars_for_template()
        context.update(self.player.vars_for_template())
        return context

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.player.get_final_accuracy()
            self.player.participant_vars_dump = str(self.participant.vars)


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.player.get_final_accuracy()
        self.player.participant_vars_dump = str(self.participant.vars)


class Wait(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

page_sequence = [
    Forecast1_Init,
    Forecast1_Rev,
    #Forecast1_Rev_Treat,
    Fb,
#    Feedback,
    #Results,
    Wait
]

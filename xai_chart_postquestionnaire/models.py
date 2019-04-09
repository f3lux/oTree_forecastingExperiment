from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#from otree_tools.forms.fields import OtherFormField
author = 'Felix Reinfurt'

doc = """
Experiment with entirely explicit feedback (First experiment in thesis)
"""


class Constants(BaseConstants):
    name_in_url = 'xf_post_chart'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.ctrl_treat = p.role()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ctrl_treat = models.StringField()
    def role(self):
        if self.id_in_group % 2 == 1:
            return 'control'
#        elif self.id_in_group % 4 == 2:
#           return 'treatment1'
#      elif self.id_in_group % 4 == 3:
#         return 'treatment2'
        else:
            return 'treatment3'




    gender = models.IntegerField(
        label='1. What is your gender?',
        choices=[
            [0, 'Female.'],
            [1, 'Male.'],
            [2, 'Other.'],
        ],
        widget=widgets.RadioSelect,
    )
    age = models.IntegerField(
        label='2 What is your age?',
        choices=[
            [0, '<18'],
            [1, '18-19'],
            [2, '20-21'],
            [3, '22-23'],
            [4, '24-25'],
            [5, '26-27'],
            [6, '28-29'],
            [7, '30-31'],
            [8, '32-33'],
            [9, '34-35'],
            [10, '36-37'],
            [11, '38-39'],
            [12, '40-41'],
            [13, '42-43'],
            [14, '44-45'],
            [15, '46-47'],
            [16, '48-49'],
            [17, '50-51'],
            [18, '52-53'],
            [19, '54-55'],
            [20, '56-57'],
            [21, '58-59'],
            [22, '60-61'],
            [23, '62-63'],
            [24, '64-65'],
            [25, '66-67'],
            [26, '68-69'],
            [27, '70-71'],
            [28, '72-73'],
            [29, '74-75'],
            [30, '76-77'],
            [31, '78-79'],
            [32, '80-81'],
            [33, '>81']
        ]
    )

    nationality = models.StringField(
        label='3 What is your nationality?'
    )


#    nationality = OtherFormField(
#        label='3. What is your nationality?',
#        choices=[
#            "America (USA)",
#            "France",
#            "Germany",
#            "Turkey",
#            'Spain'
#        ],
#        other_label=['Something else'],
#        widget=widgets.RadioSelect,
#    )

    education = models.IntegerField(
        label='4. What is your highest education?',
        choices=[
            [0,"Highschool (Abitur)."],
            [1,"Apprenticeship (Ausbildung)."],
            [2,"Bachelor's degree or equivalent."],
            [3,"Master's degree or equivalent (e.g. Magister, MBA)."],
            [4,'PhD/Doctorate and above.'],
        ],
        widget=widgets.RadioSelect,
    )

    study1 = models.StringField(
        label='4.1. If you do or did study, what is/was your field of study?',
        blank=True
    )

    study1_old = models.IntegerField(
        label='4.1. If you do or did study, what is/was your field of study?',
        choices=[
            [0, "Humanities (e.g. History, Philosophy, Arts)"],
            [1, "Social sciences (e.g. Economics, Politics, Psychology)"],
            [2, "Natural sciences (e.g. Biology, Chemistry, Physics)"],
            [3, "Formal sciences (e.g. Computer sciences, Mathematics, Logic)"],
            [4, 'Professions and applied sciences (e.g. Architecture, Engineering, Business, Education, Law, Medicine)'],
            [5, "Others"],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )

    study2 = models.StringField(
        label='4.1b If you chose "others" in the question before, please specify.',
        blank=True
    )

    edu_background = models.StringField(
        label='4.2. If you do/did not study, what is your educational background?',
        blank=True
    )

    occupation = models.StringField(
        label='5. What is your current occupation?'
    )

    experiment1 = models.BooleanField(
        label = '6. Have you been part of a similar experiment before?',
        choices=[[True, 'Yes. (Proceed with question 6.1)'],
                 [False, 'No. (Proceed with question 7.)']
                 ],
        widget=widgets.RadioSelect,
    )

    experiment2 = models.StringField(
        label='6.1. Please describe the experiment shortly.',
        blank = True
    )

    knowledge1 = models.IntegerField(
        label='7. How would you characterize your knowledge about machine learning and machine learning algorithms?',
        choices=[
            [0, 'Excellent.'],
            [1, 'Solid.'],
            [2, 'Basic.'],
            [4, 'Limited.'],
            [5, 'Hardly any.'],
            [6, 'None. (Proceed with question 8.)']],
        widget=widgets.RadioSelect,
    )

    knowledge2 = models.StringField(
        label='7.1. How did you gain this knowledge?',
        blank = True
    )

#experience

    experience = models.BooleanField(
        label = '8. Have you had any experience in forecasting?',
        choices=[[True, 'Yes.'],
                 [False, 'No.']
                 ],
        widget=widgets.RadioSelect,
    )
    course = models.IntegerField(
        label='8.1. Where have you gained the experience in forecasting?',
        choices=[
            [0, 'From courses or trainings.'],
            [1, 'From work.'],
            [2, 'From both.'],
            [3, 'Others.']],
        widget=widgets.RadioSelect
    )

    forecasting_years = models.IntegerField(
        label='8.2. How many years of forecasting experience in total do you have?',
        choices=[
            [0,'No experience in forecasting'],
            [1,'Up to 1 year'],
            [2,'1-2 years'],
            [3,'2-5 years'],
            [4,'more than 5 years']
        ],
        widget=widgets.RadioSelect,
    )

# Adjustment

    interaction = models.IntegerField(
        label='9. How often did you interact with the interactive historical time series chart?',
        choices=[
            [0, 'Never.'],
            [1, 'A few times.'],
            [2, 'About half of the times.'],
            [3, 'More often than not.'],
            [4, 'Always.']
        ],
        widget=widgets.RadioSelect,
    )
    adjustment_frequency = models.IntegerField(
        label='10. How often did you change your initial forecast in a second decision stage when you entered a final '
              'forecast?',
        choices=[
            [0, 'Never.'],
            [1, 'A few times.'],
            [2, 'About half of the times.'],
            [3, 'More often than not.'],
            [4, 'Always.']
        ],
        widget=widgets.RadioSelect,
    )
    additional_info1 =models.IntegerField(
        label='11. Did you change your initial forecasts due to additional information available?',
        choices=[
            [0, 'Yes.'],
            [1, 'No, I did not change my initial forecast.'],
            [2, 'No, but I changed it due to other reasons. (Proceed with question 11.1.)'],
        ],
        widget=widgets.RadioSelect,
    )

    additional_info2 = models.StringField(
        label='11.1. Please specify what the other reasons were.',
        blank=True
    )

    feedback = models.IntegerField(
        label='12. How often did you have a detailed look at the round summary page, examining the actual value'
              ' your forecasts and the one of the ML algorithm?',
        choices=[
            [0, 'Never'],
            [1, 'A few times'],
            [2, 'About half of the times'],
            [3, 'More often than not'],
            [4, 'Always']
        ],
        widget=widgets.RadioSelect,
    )

# Trust
    algorithm_insights = models.IntegerField(
        label='13. To which extent did you understand how the ML algorithm arrives at its forecast?',
        choices=[
            [0, 'Entirely.'],
            [1, 'Largely.'],
            [2, 'Slightly.'],
            [3, 'Barely.'],
            [4, 'Not at all.'],
       ],
        widget=widgets.RadioSelect,
    )
    algorithm_insights1 = models.IntegerField(
        label="13.1 How much did knowing the ML algorithm's output contribute to understanding (trusting?) the ML algorithm?",
        choices=[
            [0, 'A lot'],
            [1, 'Slightly'],
            [2, 'No contribution'],
            [3, 'It confused more than it helped'],
        ],
        widget=widgets.RadioSelect,
    )
    algorithm_insights2 = models.IntegerField(
        label="13.1 How much did knowing about the ML algorithm's input features contribute to understanding (trusting?) the ML algorithm?",
        choices=[
            [0, 'A lot'],
            [1, 'Slightly'],
            [2, 'No contribution'],
            [3, 'It confused more than it helped'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights3 = models.IntegerField(
        label="13.1 How much did knowing about the ML algorithm's input features and their realizations contribute to understanding (trusting?) the ML algorithm?",
        choices=[
            [0, 'A lot'],
            [1, 'Slightly'],
            [2, 'No contribution'],
            [3, 'It confused more than it helped'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights4 = models.IntegerField(
        label='13.1 How much did the information on how the ML algorithm arrives at its forecast contribute to your '
              'understanding of the ML algorithm? ',
        choices=[
            [0, 'To a great extent.'],
            [1, 'To a medium extent.'],
            [2, 'To a small extent.'],
            [3, 'To no extent.'],
            [4, 'It confused more than it helped.'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights5 = models.IntegerField(
        label='14. How did your level of trust towards the ML algorithm change during the experiment?',
        choices=[
            [0, 'It only increased.'],
            [1, 'It only decreased.'],
            [2, 'It did both increase and decrease.'],
            [3, 'It stayed the same throughout the experiment.'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights6 = models.StringField(
        label='14.1 Please describe why or why not your level of trust towards the ML algorithm changed.',
    )

    algorithm_insights7 = models.IntegerField(
        label='14.2 Did your level of trust towards the ML algorithm decrease after the ML algorithm performed badly?',
        choices=[
            [0, 'Yes'],
            [1, 'No'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights8 = models.IntegerField(
        label='14.3 Did your level of trust towards the ML algorithm increase after the ML algorithm performed well?',
        choices=[
            [0, 'Yes'],
            [1, 'No'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights9 = models.IntegerField(
        label='15. Did you see the ML algorithm more as a support or more as a competitor?',
        choices=[
            [0, 'Support.'],
            [1, 'Competitor.'],
            [2, 'Neither / Both.'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights9_1 = models.StringField(
        label='15.1. Please describe your procedure of making a forecast in the first and second decision stage respectively '
              'throughout the experiment.',
    )

    algorithm_insights10 = models.IntegerField(
        label='16. Have you had any bad encounter with ML algorithms in your life?',
        choices=[
            [0, 'Yes. (Proceed with question 16.1.)'],
            [1, 'No.'],
        ],
        widget=widgets.RadioSelect,
    )

    algorithm_insights11 = models.StringField(
        label='16.1 Please specify the encounter.',
        blank=True
    )


#personality
    personality1 = models.IntegerField(
        label='8. What is more important for you at work?',
        choices=[
            [0, 'Details of a specific task'],
            [1, 'General overview of possible solution approaches'],
        ],
        widget=widgets.RadioSelect,
    )
    personality2 = models.IntegerField(
        label='9. Which situation do you prefer?',
        choices=[
            [0, 'Individual coaching for the duration of a project'],
            [1, 'Independent work on a project'],
        ],
        widget=widgets.RadioSelect,
    )

    personality3 = models.IntegerField(
        label='10. What type of work do you enjoy most?',
        choices=[
            [0, 'Rapidly changing tasks that create progress'],
            [1, 'Focusing alone on the task to create excellence'],
            [2, 'Comfortable and predictable tasks that support the team'],
            [3, 'Interacting with many people to create new ideas and energy'],
        ],
        widget=widgets.RadioSelect,
    )

    personality4 = models.IntegerField(
        label='11. How do you behave at an event at which are mostly people you haven`t met before?',
        choices=[
            [0, 'Finding a small group of people you already know'],
            [1, 'Seeking a good point to observe the event'],
            [2, 'Meeting and talking to as many people as possible'],
            [3, 'Going to the people who are the reason why you are here'],
        ],
        widget=widgets.RadioSelect,
    )

# final open question
    final_comment = models.LongStringField(
        label='17. Please leave any comment you have regarding the experiment.',
        #blank=True
    )

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as go
import random as rnd
author = 'Felix Reinfurt'

doc = """
Experiment with partial explicit feedback (Second experiment in thesis)
"""


class Constants(BaseConstants):
    name_in_url = 'ex_fb'
    path = '_static/global/'
    players_per_group = None
    num_rounds = 30
    start_data = 228
    start_of_test = 1460

    df_data_total_reduced = pd.read_csv(path + "full_dataset_reduced.csv", index_col = 0)
    df_data_date_and_sales = pd.read_csv(path + "full_dataset_date_and_sales.csv", usecols=[1, 2])
    df_data_test = pd.read_csv(path + "experiment.csv", header=None, usecols=[1])
    df_predict = pd.read_csv(path + "predictions_final.csv", usecols=[1])
    df_shap_values = pd.read_csv(path + "shap.csv", header=None)
    list_date_and_sales = pd.read_csv(path + "chart.csv", header=None).values.tolist()

    rnd.seed(41)
    random_draw = rnd.sample(range(1,num_rounds+1), 5)
    #date_and_sales = df_data_total.tolist()

    forecasts = df_data_test.iloc[start_data:start_data+num_rounds, 0].tolist()
    predictions = df_predict.iloc[start_data:start_data+num_rounds, 0].tolist()
    # forecasts = data_df[1].tolist()
    #forecasts = [40, 45, 38]

    def ape_metric(self, actual, predict):
        ac = float(actual)
        pr = float(predict)
        return (1-(abs(ac-pr)/ac))*100



class Subsession(BaseSubsession):
    ape_round_ml = models.FloatField()
    ape_total_ml = models.FloatField(initial=0)
    mape_ml = models.FloatField()
    #plot_div = models.StringField()

    def creating_session(self):
        for p in self.get_players():
            p.ctrl_treat = p.role()

        actual = Constants.forecasts[self.round_number-1]
        ml_predict = round(Constants.predictions[self.round_number-1])
        self.ape_round_ml = Constants.ape_metric(self, actual, ml_predict)
        self.ape_total_ml = sum([s.ape_round_ml for s in self.in_all_rounds()])
        self.mape_ml = self.ape_total_ml / self.round_number


    def vars_for_template(self):
        return {'x_str': "global/x/x" + str(self.round_number-1) + ".png",
                'fcst_actual': Constants.forecasts[self.round_number-1],
                'ml_prediction': int(round(Constants.predictions[self.round_number-1])),
                'ape_round_ml_rounded': round(self.ape_round_ml, 1),
                'mape_ml_rounded': round(self.mape_ml, 1),
                'highcharts_series': Constants.list_date_and_sales[:Constants.start_of_test+Constants.start_data+self.round_number - 1],
                'Avg_total': round(Constants.df_data_total_reduced['Avg_total'][Constants.start_of_test+Constants.start_data+self.round_number - 1],1),
                'Avg_year': round(Constants.df_data_total_reduced['Avg_year'][Constants.start_of_test+Constants.start_data+self.round_number - 1],1),
                'Avg_quarter': round(Constants.df_data_total_reduced['Avg_quarter'][Constants.start_of_test+Constants.start_data+self.round_number - 1],1),
                'Avg_month': round(Constants.df_data_total_reduced['Avg_month'][Constants.start_of_test+Constants.start_data+self.round_number - 1],1),
                'Avg_week': round(Constants.df_data_total_reduced['Avg_week'][Constants.start_of_test+Constants.start_data+self.round_number - 1],1),
                'Avg_weekday': round(Constants.df_data_total_reduced['Avg_weekday'][Constants.start_of_test+Constants.start_data+self.round_number - 1],1),
                '1_day_ago': int(Constants.df_data_total_reduced['1_day_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '2_days_ago': int(Constants.df_data_total_reduced['2_days_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '3_days_ago': int(Constants.df_data_total_reduced['3_days_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '4_days_ago': int(Constants.df_data_total_reduced['4_days_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '5_days_ago': int(Constants.df_data_total_reduced['5_days_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '6_days_ago': int(Constants.df_data_total_reduced['6_days_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '1_week_ago': int(Constants.df_data_total_reduced['1_week_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '1_month_ago': int(Constants.df_data_total_reduced['1_month_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                '1_year_ago': int(Constants.df_data_total_reduced['1_year_ago'][Constants.start_of_test+Constants.start_data+self.round_number - 1]),
                'Shap_Avg_total': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][0], 1),
                'Shap_Avg_year': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][1], 1),
                'Shap_Avg_quarter': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][2], 1),
                'Shap_Avg_month': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][3], 1),
                'Shap_Avg_week': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][4], 1),
                'Shap_Avg_weekday': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][5], 1),
                'Shap_1_day_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][6], 1),
                'Shap_2_days_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][7], 1),
                'Shap_3_days_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][8], 1),
                'Shap_4_days_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][9], 1),
                'Shap_5_days_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][10], 1),
                'Shap_6_days_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][11], 1),
                'Shap_1_week_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][12], 1),
                'Shap_1_month_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][13], 1),
                'Shap_1_year_ago': round(Constants.df_shap_values.iloc[Constants.start_data + self.round_number - 1][14], 1),
                }


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ctrl_treat = models.StringField()
    ape_round = models.FloatField()
    ape_total = models.FloatField(initial=0)
    mape = models.FloatField()
    ape_round_rev= models.FloatField()
    ape_total_rev = models.FloatField(initial=0)
    mape_rev = models.FloatField()
    participant_vars_dump = models.StringField()

    F1_Initial = models.IntegerField(
        label="Enter your forecast here",
        min=0, max=1000
    )

    F1_Revised = models.IntegerField(
        label="Enter your forecast here",
        min=0, max=1000
    )

    F1_Revised_Treat = models.IntegerField(
        label="Enter your forecast here",
        min=0, max=1000
    )

    def vars_for_template(self):
        return {'ape_round_rounded': round(self.ape_round, 2),
                'mape_rounded': round(self.mape, 2),
                'ape_round_rev_rounded': round(self.ape_round_rev, 2),
                'mape_rev_rounded': round(self.mape_rev, 2)
                }

    def role(self):
        if self.id_in_group % 2 == 1:
            return 'control_fb'
        #        elif self.id_in_group % 4 == 2:
        #           return 'treatment1'
        #      elif self.id_in_group % 4 == 3:
        #         return 'treatment2'
        else:
            return 'treatment3_fb'

    def is_treat(self):
        return self.role() == 'treatment'


    def calc_ape(self):
        self.ape_round = Constants.ape_metric(self, Constants.forecasts[self.round_number-1], self.F1_Initial)
        self.ape_total = sum([p.ape_round for p in self.in_all_rounds()])
        self.mape = self.ape_total/self.round_number

        self.ape_round_rev = Constants.ape_metric(self, Constants.forecasts[self.round_number - 1], self.F1_Revised)
        self.ape_total_rev = sum([p.ape_round_rev for p in self.in_all_rounds()])
        self.mape_rev = self.ape_total_rev / self.round_number

    def get_final_accuracy(self):
        accuracy1 = self.in_round(Constants.random_draw[0]).ape_round_rev
        accuracy2 = self.in_round(Constants.random_draw[1]).ape_round_rev
        accuracy3 = self.in_round(Constants.random_draw[2]).ape_round_rev
        accuracy4 = self.in_round(Constants.random_draw[3]).ape_round_rev
        accuracy5 = self.in_round(Constants.random_draw[4]).ape_round_rev
        self.participant.vars['rounds'] = [Constants.random_draw[0], Constants.random_draw[1], Constants.random_draw[2], Constants.random_draw[3], Constants.random_draw[4]]
        self.participant.vars['payout'] = [round(accuracy1, 2), round(accuracy2, 2), round(accuracy3, 2), round(accuracy4, 2), round(accuracy5, 2)]
        accuracy_total = sum(self.participant.vars['payout'])/5
        self.participant.vars['payout_total'] = round(accuracy_total, 2)

    #def ape_metric(self):
        #actual = Constants.forecasts[self.round_number-1]
        #return (1-abs(self.F1_Initial-actual)/actual) * 100

   # def vars_for_template(self):
   #     return {'ctrl_treat': self.role()}
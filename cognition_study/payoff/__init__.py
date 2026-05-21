from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'payoff'
    players_per_group = None
    num_rounds = 1
    completion_code = '273940'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass 

class Player(BasePlayer):
    pass

class 報酬(Page):
    pass

class WaitForInstruction(Page):
    pass

page_sequence = [報酬]



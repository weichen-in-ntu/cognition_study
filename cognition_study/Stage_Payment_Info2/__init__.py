from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1
    completion_code = '273940'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass # 妳的實驗不需要算什麼碳排，所以這裡空著就好

class Player(BasePlayer):
    pass

class 報酬(Page):
    pass


class WaitForInstruction(Page):
    pass

page_sequence = [報酬]



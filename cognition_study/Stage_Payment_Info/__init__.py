from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'wait_start'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Player(BasePlayer):
    total_payment = models.IntegerField()
    # === 基本資料 ===
    name = models.StringField(label="您的名字")
    school = models.StringField(
        label="您的學校",
        choices=[
            ('國立臺灣大學', '國立臺灣大學'),
            ('國立政治大學', '國立政治大學'),
            ('國立臺北大學', '國立臺北大學'),
            ('國立臺灣師範大學', '國立臺灣師範大學'),
            ('國立臺北教育大學', '國立臺北教育大學'),
            ('國立臺灣科技大學', '國立臺灣科技大學'),
            ('國立成功大學', '國立成功大學'),
        ],
        widget=widgets.RadioSelectHorizontal,
        initial='國立臺灣大學',
    )
    student_id = models.StringField(label="您的學號")
    id_number = models.StringField(label="您的身份證字號", blank=True)
    address = models.StringField(label="您的戶籍地址（含鄰里，需與身分證一致）")
    is_foreign = models.StringField(
        label="您是否為外籍生？",
        choices=[('是', '是'), ('否', '否')],
        widget=widgets.RadioSelect
    )
    arc = models.StringField(label="居留證號碼", blank=True)
    passport = models.StringField(label="護照號碼", blank=True)
    nation = models.StringField(label="國籍", blank=True)
    stay = models.StringField(
        label="是否在台滿 183 天",
        choices=[('是', '是'), ('否', '否')],
        widget=widgets.RadioSelect,
        blank=True
    )

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Consent(Page):
    form_model = None

    @staticmethod
    def vars_for_template(player: Player):
        return {}


class WaitStart(Page):
    form_model = None

class Intro1(Page):
    pass

class Intro2(Page):
    pass

class Intro3(Page):
    pass
class 等(Page):
    pass
class BasicInfo(Page):
    form_model = 'player'
    form_fields = [
        'name',
        'school',
        'student_id',
        'is_foreign',
        'id_number',
        'address',
        'arc',
        'passport',
        'nation',
        'stay'
    ]

    @staticmethod
    def error_message(player: Player, values):
        if values['is_foreign'] == '否':
            id_number = (values['id_number'] or '').strip()
            if not id_number:
                return '請填寫身份證字號'
            if len(id_number) != 10:
                return '身份證字號長度不正確'
            if not id_number[0].isalpha():
                return '身份證字號第 1 碼應為英文字母'
            if not id_number[1:9].isnumeric():
                return '身份證字號格式不正確'
        if values['is_foreign'] == '是':
            if not values['arc']:
                return '請填寫居留證號碼'
            if not values['passport']:
                return '請填寫護照號碼'
            if not values['nation']:
                return '請填寫國籍'
            if not values['stay']:
                return '請選擇是否在台滿 183 天'



page_sequence = [ WaitStart,Intro1, Intro2, Intro3,BasicInfo,等]

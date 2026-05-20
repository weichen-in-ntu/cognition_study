from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'policy_cognition'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    論點列表 = [
        "並非持有多戶房屋的人就是要炒作房市，一概課徵高稅率並不公平。有些人的房子是繼承來的，有些人則是用畢生積蓄買房養老，以收租維持退休生活。",
        "縱使住宅具投資獲利的「資本財」性質，但更重要的功用是滿足居住使用的「消費財」功能。當住宅此種民生必需品出現大量囤積空置，政府應該介入處理。",
        "房屋稅很容易就可以轉嫁給消費者，從學術研究來看，房屋稅轉嫁的幅度從 85％到 120％都有可能。也就是說有時還會超額轉嫁，也就是愈打愈漲。",
        "台灣高房價問題具備特殊性，房價高漲與大量餘屋並存顯然並非簡單的經濟學供給與需求能解釋，而是住宅市場「房子拿來炒不是用來住」的外部性效應。"
    ]
    景觀論點列表 = [
        "透過法規落實視覺管理，能有效整頓混亂招牌與違建，重塑具備地方特色的美學空間。許多國際城市如京都都出台嚴格的景觀法規。",
        "良好且統一的景觀環境能營造在地特色，吸引旅遊人潮，創造旅遊商機，進一步提升土地價值，讓城市更具競爭力與國際觀光接軌。",
        "建築物屬於私人財產，個人對其的所有權不應被侵犯。過度干預建築外觀或色彩，可能違背憲法保障的財產處分權，限制個人創作自由。",
        "美感具有主觀性，事實上，有些人也認為鐵皮屋與招牌充滿活力與感性。法條若缺乏客觀審查標準，易造成行政處分與核發執照的爭議。"
    ]

    九階選項 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        player.失調組別 = random.choice(['失調組', '中性組'])
        #player.推理組別 = random.choice(['動機性推理組', '中性推理組'])

        player.失調組別 =  '中性組'
        player.推理組別 = '動機性推理組' # '中性推理組'

        論點順序 = [1, 2, 3, 4]
        random.shuffle(論點順序)
        player.participant.vars['論點順序'] = 論點順序
        

        政見列表 = ['完全廢除景觀法', '建立更嚴格的景觀法']
        random.shuffle(政見列表)
        player.候選人A_景觀法政見 = 政見列表[0]
        player.候選人B_景觀法政見 = 政見列表[1]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    失調組別 = models.StringField()
    推理組別 = models.StringField()
    年齡 = models.IntegerField(label='請問您今年幾歲?', min=13, max=125)
    性別 = models.StringField(
        choices=[['男', '男'], ['女', '女']],
        label='請問您的性別為？',
        widget=widgets.RadioSelect,
    )
    學歷 = models.StringField(
        choices=['國中及以下', '高中/高職', '專科/大學', '碩士', '博士及以上'],
        label='請問您的最高學歷為？',
        widget=widgets.RadioSelect,
    )
    政治傾向 = models.StringField(
        choices=['民主進步黨', '中國國民黨', '台灣民眾黨', '時代力量', '台灣基進', '中立', '其他'],
        label='請問您的政治傾向較接近以下何者？',
        widget=widgets.RadioSelect,
    )

    政治傾向_其他 = models.StringField(
        label='若您選擇「其他」，請在此註明您的政治傾向：',
        blank=True 
    )
    關注社會議題時間 = models.StringField(
        choices=['幾乎沒有', '每週 1 到 3 小時', '每週 4 到 6 小時', '每週 7 到 10 小時', '每週 10 小時以上'],
        label='請問您平均每週大約花多少時間關注社會或政治議題（包含看新聞、社群媒體討論等）？',
        widget=widgets.RadioSelect,
    )
    
    初始囤房稅 = models.FloatField(label='', min=0)
    最終囤房稅 = models.FloatField(label='', min=0)
    初始景觀同意門檻 = models.FloatField(label='', min=0, max=100)
    最終景觀同意門檻 = models.FloatField(label='', min=0, max=100)
    
    初始囤房稅態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終囤房稅態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    初始囤房稅重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終囤房稅重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    
    初始景觀法態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終景觀法態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    初始景觀法重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終景觀法重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)

    囤房稅後續選擇 = models.FloatField(
        label='現在有兩位候選人正在競選T市市長\n請想像自己身為 T市公民，選擇你支持的候選人\n＊注意：這不是真實的選舉，您無需考量現實法規的上下限。',
        widget=widgets.RadioSelect
    )
    景觀法後續選擇 = models.FloatField(
        label='現在有兩位候選人正在競選T市市長\n請想像自己身為 T市公民，選擇你支持的候選人\n＊注意：這不是真實的選舉，您無需考量現實法規的上下限。',
        widget=widgets.RadioSelect
    )
    候選人A_景觀法政見 = models.StringField()
    候選人B_景觀法政見 = models.StringField()
    辯護文章 = models.LongStringField(label='')
    景觀法文章 = models.LongStringField(label='')
    
    論點1_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點1_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點2_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點2_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點3_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點3_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點4_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點4_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)

class 前測(Page):
    form_model = 'player'
    form_fields = ['初始囤房稅', '初始囤房稅態度', '初始囤房稅重要性', '初始景觀同意門檻', '初始景觀法態度', '初始景觀法重要性']

class 後測(Page):
    form_model = 'player'
    form_fields = ['最終囤房稅', '最終囤房稅態度', '最終囤房稅重要性', '最終景觀同意門檻', '最終景觀法態度', '最終景觀法重要性']

def get_tax_rates(player):
    if player.初始囤房稅 < 3.8:
        稅率一 = player.初始囤房稅 * (3/4)
        稅率二 = player.初始囤房稅 * (3/2)
    elif player.初始囤房稅 > 3.8:
        稅率一 = player.初始囤房稅 * (1/2)
        稅率二 = player.初始囤房稅 * (5/4)
    else:
        if random.choice([True, False]):
            稅率一 = player.初始囤房稅 * (3/4)
            稅率二 = player.初始囤房稅 * (3/2)
        else:
            稅率一 = player.初始囤房稅 * (1/2)
            稅率二 = player.初始囤房稅 * (5/4)
            
    低稅率 = round(min(稅率一, 稅率二), 2)
    高稅率 = round(max(稅率一, 稅率二), 2)
    return 低稅率, 高稅率

def get_renewal_rates(player):
    if player.初始景觀同意門檻 < 82.5:
        門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.5))
        門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.25))
    elif player.初始景觀同意門檻 > 82.5:
        門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.25))
        門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.5))
    else:
        if random.choice([True, False]):
            門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.5))
            門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.25))
        else:
            門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.25))
            門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.5))

    低門檻 = round(min(門檻一, 門檻二), 2)
    高門檻 = round(max(門檻一, 門檻二), 2)
    return 低門檻, 高門檻

def 囤房稅後續選擇_choices(player):
    低稅率, 高稅率 = get_tax_rates(player)
    第一個選項 = [低稅率, f'候選人A（主張囤房稅率：{低稅率}%）']
    第二個選項 = [高稅率, f'候選人B（主張囤房稅率：{高稅率}%）']
    return [第一個選項, 第二個選項]

def 景觀法後續選擇_choices(player):
    低門檻, 高門檻 = get_renewal_rates(player)
    第一個選項 = [低門檻, f'候選人A（主張：{低門檻}%居民同意即可都更）']
    第二個選項 = [高門檻, f'候選人B（主張：{高門檻}%居民同意即可都更）']
    return [第一個選項, 第二個選項]


class 選舉情境介紹(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'

class 候選人政見(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        return dict(候選人A_稅率=低稅率, 候選人B_稅率=高稅率)

class 投票選擇(Page):
    form_model = 'player'
    form_fields = ['囤房稅後續選擇']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        return dict(候選人A_稅率=低稅率, 候選人B_稅率=高稅率)
    

class 景觀法選舉情境介紹(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'

class 景觀法候選人政見(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        return dict(候選人A_門檻=低門檻, 候選人B_門檻=高門檻)

class 景觀法投票選擇(Page):
    form_model = 'player'
    form_fields = ['景觀法後續選擇']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        return dict(候選人A_門檻=低門檻, 候選人B_門檻=高門檻)
    
class 囤房稅介紹(Page):
    pass

class 景觀法介紹(Page):
    pass

class 第一階段介紹(Page):
    pass

class 人口背景調查(Page):
    form_model = 'player'
    form_fields = ['年齡', '性別', '學歷', '政治傾向', '政治傾向_其他', '關注社會議題時間']
    @staticmethod
    def error_message(player: Player, values):
        if values['政治傾向'] == '其他' and not values['政治傾向_其他']:
            return '請在下方欄位具體填寫您的政治傾向'

class 模擬選舉說明(Page):
    pass

class 囤房稅選項頁面(Page):
    form_model = 'player'
    form_fields = ['囤房稅後續選擇']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'

class 囤房稅寫作(Page):
    form_model = 'player'
    form_fields = ['辯護文章']
    timeout_seconds = 600
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        
        if player.囤房稅後續選擇 == 低稅率:
            支持的候選人 = "候選人A"
        else:
            支持的候選人 = "候選人B"
            
        return dict(
            選擇的稅率=player.囤房稅後續選擇,
            支持的候選人=支持的候選人
        )

    @staticmethod
    def error_message(player: Player, values):
        if len(values['辯護文章']) < 70:
            return '您的辯護文章字數不足，請至少輸入70個字！'

class 景觀法寫作(Page):
    form_model = 'player'
    form_fields = ['景觀法文章']
    timeout_seconds = 600
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        
        if player.景觀法後續選擇 == 低門檻:
            支持的候選人 = "候選人A"
            支持的政見 = f"{低門檻}%同意門檻"
        else:
            支持的候選人 = "候選人B"
            支持的政見 = f"{高門檻}%同意門檻"
            
        return dict(
            支持的政見=支持的政見,
            支持的候選人=支持的候選人
        )
    @staticmethod
    def error_message(player: Player, values):
        if len(values['景觀法文章']) < 70:
            return '您的辯護文章字數不足，請至少輸入70個字！'
class 動機性推理介紹(Page):
   pass

class 論點頁面一(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return dict(論點內容=C.論點列表[編號-1])

class 論點頁面二(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return dict(論點內容=C.論點列表[編號-1])

class 論點頁面三(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return dict(論點內容=C.論點列表[編號-1])

class 論點頁面四(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return dict(論點內容=C.論點列表[編號-1])
    
class 景觀論點頁面一(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return dict(論點內容=C.景觀論點列表[編號-1])

class 景觀論點頁面二(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return dict(論點內容=C.景觀論點列表[編號-1])

class 景觀論點頁面三(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return dict(論點內容=C.景觀論點列表[編號-1])

class 景觀論點頁面四(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return dict(論點內容=C.景觀論點列表[編號-1])

page_sequence = [
    第一階段介紹,囤房稅介紹, 景觀法介紹, 前測, 
    模擬選舉說明,選舉情境介紹, 候選人政見, 投票選擇, 囤房稅寫作, 
    景觀法選舉情境介紹, 景觀法候選人政見, 景觀法投票選擇, 景觀法寫作, 
    動機性推理介紹, 論點頁面一, 論點頁面二, 論點頁面三, 論點頁面四,
    景觀論點頁面一, 景觀論點頁面二, 景觀論點頁面三, 景觀論點頁面四,
    後測, 人口背景調查
]
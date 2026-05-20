from os import environ

SESSION_CONFIGS = [
    dict(
        name='policy_exp',  
        # 這裡就是排隊闖關的順序喔！
        app_sequence=['Stage_Payment_Info','policy_exp', 'Stage_Payment_Info2'], 
        num_demo_participants=10,
        display_name='認知失調與動機性推理' 
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'zh-hant'

REAL_WORLD_CURRENCY_CODE = 'TWD'
USE_POINTS = True
ROOMS = []

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
"""

SECRET_KEY = '6076730954186'

INSTALLED_APPS = ['otree']
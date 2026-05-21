from os import environ

SESSION_CONFIGS = [
    dict(
        name='policy_exp',  
    
        app_sequence=['Stage_Payment_Info','policy_exp', 'Stage_Payment_Info2'], 
        num_demo_participants=10,
        display_name='認知失調與動機性推理' 
    ),
]

SESSION_CONFIGS = [
    dict(
        name='full_experiment',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_隨機'
    ),

    # 1. 囤房稅、A+、囤房稅、A+
    dict(
        name='full_experiment_01',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、A+、囤房稅、A+',
        dissonance_1='失調組',
        reasoning_1='動機性推理組',
        dissonance_2='失調組2',
        reasoning_2='動機性推理組2'
    ),

    # 2. 囤房稅、A+、囤房稅、探索學分
    dict(
        name='full_experiment_02',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、A+、囤房稅、探索學分',
        dissonance_1='失調組',
        reasoning_1='動機性推理組',
        dissonance_2='失調組2',
        reasoning_2='中性推理組2'
    ),

    # 3. 囤房稅、A+、都更、A+
    dict(
        name='full_experiment_03',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、A+、都更、A+',
        dissonance_1='失調組',
        reasoning_1='中性推理組',
        dissonance_2='失調組2',
        reasoning_2='動機性推理組2'
    ),

    # 4. 囤房稅、A+、都更、探索學分
    dict(
        name='full_experiment_04',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、A+、都更、探索學分',
        dissonance_1='失調組',
        reasoning_1='中性推理組',
        dissonance_2='失調組2',
        reasoning_2='中性推理組2'
    ),

    # 5. 囤房稅、探索學分、囤房稅、A+
    dict(
        name='full_experiment_05',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、探索學分、囤房稅、A+',
        dissonance_1='失調組',
        reasoning_1='動機性推理組',
        dissonance_2='中性組2',
        reasoning_2='動機性推理組2'
    ),

    # 6. 囤房稅、探索學分、囤房稅、探索學分
    dict(
        name='full_experiment_06',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、探索學分、囤房稅、探索學分',
        dissonance_1='失調組',
        reasoning_1='動機性推理組',
        dissonance_2='中性組2',
        reasoning_2='中性推理組2'
    ),

    # 7. 囤房稅、探索學分、都更、A+
    dict(
        name='full_experiment_07',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、探索學分、都更、A+',
        dissonance_1='失調組',
        reasoning_1='中性推理組',
        dissonance_2='中性組2',
        reasoning_2='動機性推理組2'
    ),

    # 8. 囤房稅、探索學分、都更、探索學分
    dict(
        name='full_experiment_08',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_囤房稅、探索學分、都更、探索學分',
        dissonance_1='失調組',
        reasoning_1='中性推理組',
        dissonance_2='中性組2',
        reasoning_2='中性推理組2'
    ),

    # 9. 都更、A+、囤房稅、A+
    dict(
        name='full_experiment_09',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、A+、囤房稅、A+',
        dissonance_1='中性組',
        reasoning_1='動機性推理組',
        dissonance_2='失調組2',
        reasoning_2='動機性推理組2'
    ),

    # 10. 都更、A+、囤房稅、探索學分
    dict(
        name='full_experiment_10',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、A+、囤房稅、探索學分',
        dissonance_1='中性組',
        reasoning_1='動機性推理組',
        dissonance_2='失調組2',
        reasoning_2='中性推理組2'
    ),

    # 11. 都更、A+、都更、A+
    dict(
        name='full_experiment_11',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、A+、都更、A+',
        dissonance_1='中性組',
        reasoning_1='中性推理組',
        dissonance_2='失調組2',
        reasoning_2='動機性推理組2'
    ),

    # 12. 都更、A+、都更、探索學分
    dict(
        name='full_experiment_12',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、A+、都更、探索學分',
        dissonance_1='中性組',
        reasoning_1='中性推理組',
        dissonance_2='失調組2',
        reasoning_2='中性推理組2'
    ),

    # 13. 都更、探索學分、囤房稅、A+
    dict(
        name='full_experiment_13',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、探索學分、囤房稅、A+',
        dissonance_1='中性組',
        reasoning_1='動機性推理組',
        dissonance_2='中性組2',
        reasoning_2='動機性推理組2'
    ),

    # 14. 都更、探索學分、囤房稅、探索學分
    dict(
        name='full_experiment_14',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、探索學分、囤房稅、探索學分',
        dissonance_1='中性組',
        reasoning_1='動機性推理組',
        dissonance_2='中性組2',
        reasoning_2='中性推理組2'
    ),

    # 15. 都更、探索學分、都更、A+
    dict(
        name='full_experiment_15',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、探索學分、都更、A+',
        dissonance_1='中性組',
        reasoning_1='中性推理組',
        dissonance_2='中性組2',
        reasoning_2='動機性推理組2'
    ),

    # 16. 都更、探索學分、都更、探索學分
    dict(
        name='full_experiment_16',
        app_sequence=['Stage_Payment_Info', 'policy_exp', 'payoff'],
        num_demo_participants=10,
        display_name='正式實驗:認知失調與動機性推理_都更、探索學分、都更、探索學分',
        dissonance_1='中性組',
        reasoning_1='中性推理組',
        dissonance_2='中性組2',
        reasoning_2='中性推理組2'
    ),
    

    dict(
        name='policy_exp_only',
        app_sequence=['policy_exp'],
        num_demo_participants=1,
        display_name='主實驗'
    ),
    

    dict(
        name='start',
        app_sequence=['Stage_Payment_Info'],
        num_demo_participants=1,
        display_name='開場'
    ),
    
   
    dict(
        name='payoff',
        app_sequence=['payoff'],
        num_demo_participants=1,
        display_name='領報酬'
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
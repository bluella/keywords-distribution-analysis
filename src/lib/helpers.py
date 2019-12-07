"""Universal code blocks"""
import random
import os
import time
import logging
import json
import datetime as dt
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

###################################################################################################
# constants
###################################################################################################

PROJECT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
SRC_PATH = PROJECT_DIR + '/src/'
DATASETS_PATH = PROJECT_DIR + '/datasets/'

###################################################################################################
# constants
###################################################################################################

def p2f(x):
    """Conver percentage to float"""
    return float(x.strip('%'))/100

def random_sign(number):
    """Multiply number on 1 or -1"""
    return number*random.choice([-1, 1])




# df_10['Search keyword'] = 'anonymized_keyword'
# df_10['Ad group'] = 'anonymized_ad_group'
# for index, row in df_10.iterrows():
#     if 'Brand' in row['Campaign']:
#         df_10.at[index, 'Campaign'] = 'anonymized_Brand'
#     elif 'Generic' in row['Campaign']:
#         df_10.at[index, 'Campaign'] = 'anonymized_Generic'
#     elif 'Service' in row['Campaign']:
#         df_10.at[index, 'Campaign'] = 'anonymized_Service'
#     else:
#         df_10.at[index, 'Campaign'] = 'anonymized'
# df_10.to_csv(hlp.DATASETS_PATH + 'Accout_X. Keywords data. 10_2019.csv', index=False)

# df_09['Search keyword'] = 'anonymized_keyword'
# df_09['Ad group'] = 'anonymized_ad_group'
# for index, row in df_09.iterrows():
#     if 'Brand' in row['Campaign']:
#         df_09.at[index, 'Campaign'] = 'anonymized_Brand'
#     elif 'Generic' in row['Campaign']:
#         df_09.at[index, 'Campaign'] = 'anonymized_Generic'
#     elif 'Service' in row['Campaign']:
#         df_09.at[index, 'Campaign'] = 'anonymized_Service'
#     else:
#         df_09.at[index, 'Campaign'] = 'anonymized'
# df_09.to_csv(hlp.DATASETS_PATH + 'Accout_X. Keywords data. 09_2019.csv', index=False)

# df_08['Search keyword'] = 'anonymized_keyword'
# df_08['Ad group'] = 'anonymized_ad_group'
# for index, row in df_08.iterrows():
#     if 'Brand' in row['Campaign']:
#         df_08.at[index, 'Campaign'] = 'anonymized_Brand'
#     elif 'Generic' in row['Campaign']:
#         df_08.at[index, 'Campaign'] = 'anonymized_Generic'
#     elif 'Service' in row['Campaign']:
#         df_08.at[index, 'Campaign'] = 'anonymized_Service'
#     else:
#         df_08.at[index, 'Campaign'] = 'anonymized'
# df_08.to_csv(hlp.DATASETS_PATH + 'Accout_X. Keywords data. 08_2019.csv', index=False)

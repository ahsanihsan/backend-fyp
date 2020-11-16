import sys
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
root = os.path.abspath('../')
print >>sys.stderr, 'Loading models and encoders...'
encode_dict_who_will_win_nb = pickle.load(open(root+'/models/encoder_dict-who_will_win'))
encode_dict_runrate = pickle.load(open(root+'/models/encoder_dict-runrate'))
encoder_dict_scrore_of_team = pickle.load(open(root+'/models/encoder_dict-scrore_of_team'))
encoder_will_batsman_get_out = pickle.load(open(root+'/models/encoder_dict-will_batsman_get_out'))
encoder_what_score_will_batsman_make = pickle.load(open(root+'/models/encoder_dict-what_score_will_batsman_make'))

team_vs_team_dataset = pd.read_csv(root+'/notebook/csv/PKvsIND_ODI.csv').fillna('')
runrate_dataset = pd.read_csv(root+'/notebook/csv/runrates.csv').fillna('')
will_batsman_get_out_dataset = pd.read_csv(root+'/notebook/csv/total_batman_v_bowler.csv').fillna('')
what_score_will_batsman_make_dataset = pd.read_csv(root+'/notebook/csv/what_score_will_batsman_make.csv').fillna('')

who_will_win_nb = pickle.load(open(root+'/models/who_will_win-nb'))
# runrate_lr = pickle.load(open(root+'/models/runrate-lr'))
runrate_first_lr = pickle.load(open(root+'/models/runrate_first-lr'))
runrate_second_lr = pickle.load(open(root+'/models/runrate_second-lr'))
runrate_third_lr = pickle.load(open(root+'/models/runrate_third-lr'))
runrate_forth_lr = pickle.load(open(root+'/models/runrate_forth-lr'))
runrate_fifth_lr = pickle.load(open(root+'/models/runrate_fifth-lr'))
scrore_of_team_lr_a = pickle.load(open(root+'/models/scrore_of_team-a-LR'))
scrore_of_team_lr_b = pickle.load(open(root+'/models/scrore_of_team-b-LR'))
will_batsman_get_out_KN = pickle.load(open(root+'/models/will_batsman_get_out-KN'))
what_score_will_batsman_make_LR = pickle.load(open(root+'/models/what_score_will_batsman_make-LR'))
print >>sys.stderr, 'loaded'

import json
import sys
from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
import numpy as np
from . import *
import math
# Create your views here.


def who_will_win(request):
    body = json.loads(request.body)
    input = pd.DataFrame({
        'city': body['city'] or '',
        'month': body['month'] or '',
        'match_type': body['match_type'] or '',
        'team_a': body['team_a'] or '',
        'team_b': body['team_b'] or '',
        'toss_won': body['toss_won'] or body['team_a'],
        'toss_decision': body['toss_decision'] or '',
        'venue': body['venue'] or '',
    }, columns=['city', 'month', 'match_type', 'team_a', 'team_b', 'toss_won', 'toss_decision',  'venue'], index=[0])
    label_input = input.apply(
        lambda x: encode_dict_who_will_win_nb[x.name].transform(x))
    pred = who_will_win_nb.predict(label_input)
    pred = encode_dict_who_will_win_nb['winner'].inverse_transform(pred)
    data = team_vs_team_dataset[team_vs_team_dataset.city == str(
        input.city[0])]
    # data = data[data.month == str(input.month[0])]
    data = data[data.match_type == str(input.match_type[0])]
    data = data[data.team_a == str(input.team_a[0])]
    data = data[data.team_b == str(input.team_b[0])]
    # data = data[data.toss_won == str(input.toss_won[0])]
    # data = data[data.toss_decision == str(input.toss_decision[0])]
    data = data[data.venue == str(input.venue[0])]

    return HttpResponse(json.dumps({"error": False, "prediction": pred[0], "data": data.T.to_dict().values()}), content_type="application/json")


def score_of_teams(request):
    body = json.loads(request.body)
    input = pd.DataFrame({
        'city': body['city'] or '',
        'month': body['month'] or '',
        'match_type': body['match_type'] or '',
        'team_a': body['team_a'] or '',
        'team_b': body['team_b'] or '',
        'toss_won': body['toss_won'] or '',
    }, columns=['city', 'month', 'match_type', 'team_a', 'team_b', 'toss_won'], index=[0])
    label_input = input.apply(
        lambda x: encoder_dict_scrore_of_team[x.name].transform(x))
    pred_a = scrore_of_team_lr_a.predict(label_input)
    pred_b = scrore_of_team_lr_b.predict(label_input)
    data = team_vs_team_dataset[team_vs_team_dataset.city == str(
        input.city[0])]
    data = data[data.match_type == str(input.match_type[0])]
    data = data[data.team_a == str(input.team_a[0])]
    data = data[data.team_b == str(input.team_b[0])]

    return HttpResponse(json.dumps({"error": False, "prediction": {"team_a": math.floor(pred_a[0]), "team_b": math.floor(pred_b[0])}, "data": data.T.to_dict().values()}), content_type="application/json")


def runrate(request):
    body = json.loads(request.body)
    input = pd.DataFrame({
        'city': body['city'] or '',
        'month': body['month'] or '',
        'match_type': body['match_type'] or '',
        'batting_team': body['batting_team'] or '',
        'bowling_team': body['bowling_team'] or '',

    }, columns=['month', 'city', 'match_type', 'batting_team', 'bowling_team'], index=[0])
    label_input = input.apply(
        lambda x: encode_dict_runrate[x.name].transform(x))
    pred1 = runrate_first_lr.predict(label_input)
    pred2 = runrate_second_lr.predict(label_input)
    pred3 = runrate_third_lr.predict(label_input)
    pred4 = runrate_forth_lr.predict(label_input)
    pred5 = runrate_fifth_lr.predict(label_input)
    data = runrate_dataset[runrate_dataset.match_type ==
                           str(input.match_type[0])]
    data = data[data.batting_team == str(input.batting_team[0])]
    data = data[data.bowling_team == str(input.bowling_team[0])]
    data = data[data.month == str(input.month[0])]
    data = data[data.city == str(input.city[0])]
    return HttpResponse(json.dumps({"error": False, "prediction": [pred1[0], pred2[0], pred3[0], pred4[0], pred5[0]], "data": data.T.to_dict().values()}), content_type="application/json")


def will_batsman_get_out(request):
    body = json.loads(request.body)
    input = pd.DataFrame({
        'match_type': body['match_type'] or '',
        'month': body['month'] or '',
        'city': body['city'] or '',
        'position': body['position'] or '',
        'bat_team': body['bat_team'] or '',
        'batsman': body['batsman'] or '',
        'bowling_team': body['bowling_team'] or '',
        'bowler': body['bowler'] or '',
        'venue': body['venue'] or ''

    }, columns=['match_type', 'month', 'city', 'position', 'bat_team', 'batsman', 'bowling_team', 'bowler',  'venue'], index=[0])
    label_input = input.apply(
        lambda x: encoder_will_batsman_get_out[x.name].transform(x))
    pred = will_batsman_get_out_KN.predict(label_input)
    data = will_batsman_get_out_dataset[will_batsman_get_out_dataset.match_type == str(
        input.match_type[0])]
    data = data[data.month == str(input.month[0])]
    data = data[data.city == str(input.city[0])]
    data = data[data.bat_team == str(input.bat_team[0])]
    data = data[data.batsman == str(input.batsman[0])]
    data = data[data.bowling_team == str(input.bowling_team[0])]
    data = data[data.bowler == str(input.bowler[0])]
    data = data[data.venue == str(input.venue[0])]

    return HttpResponse(json.dumps({"error": False, "prediction": bool(pred[0]), "data": data.T.to_dict().values()}), content_type="application/json")


def what_score_will_batsman_make(request):
    body = json.loads(request.body)
    input = pd.DataFrame({
        'match_type': body['match_type'] or '',
        'month': body['month'] or '',
        'city': body['city'] or '',
        'position': body['position'] or '',
        'bat_team': body['bat_team'] or '',
        'batsman': body['batsman'] or '',
        'bowling_team': body['bowling_team'] or '',
        'venue': body['venue'] or ''

    }, columns=['match_type', 'month', 'city', 'position', 'bat_team', 'batsman', 'bowling_team', 'venue'], index=[0])
    label_input = input.apply(
        lambda x: encoder_what_score_will_batsman_make[x.name].transform(x))
    pred = what_score_will_batsman_make_LR.predict(label_input)
    data = what_score_will_batsman_make_dataset[what_score_will_batsman_make_dataset.match_type == str(
        input.match_type[0])]
    data = data[data.month == str(input.month[0])]
    data = data[data.city == str(input.city[0])]
    data = data[data.bat_team == str(input.bat_team[0])]
    data = data[data.batsman == str(input.batsman[0])]
    data = data[data.bowling_team == str(input.bowling_team[0])]
    data = data[data.venue == str(input.venue[0])]

    return HttpResponse(json.dumps({"error": False, "prediction": np.ceil(pred[0]), "data": data.T.to_dict().values()}), content_type="application/json")

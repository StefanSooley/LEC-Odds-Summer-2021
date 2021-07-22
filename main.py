import itertools
import pickle

teams = {
    "G2": 7,
    "XL": 4,
    "RGE": 10,
    "SK": 4,
    "FNC": 10,
    "MSF": 9,
    "MAD": 8,
    "AST": 5,
    "VIT": 5,
    "S04": 3
}
passes = {
    "G2": 0,
    "XL": 0,
    "RGE": 0,
    "SK": 0,
    "FNC": 0,
    "MSF": 0,
    "MAD": 0,
    "AST": 0,
    "VIT": 0,
    "S04": 0
}

week7d1 = [['S04', 'XL'], ['VIT', 'MSF'], ['MAD', 'AST'], ['G2', 'SK'], ['FNC', 'RGE']]
week7d2 = [['AST', 'S04'], ['XL', 'VIT'], ['RGE', 'MAD'], ['SK', 'FNC'], ['MSF', 'G2']]
week8d1 = [['MSF', 'SK'], ['AST', 'XL'], ['RGE', 'VIT'], ['G2', 'S04'], ['FNC', 'MAD']]
week8d2 = [['VIT', 'S04'], ['SK', 'AST'], ['XL', 'RGE'], ['MAD', 'G2'], ['MSF', 'FNC']]
week8d3 = [['RGE', 'SK'], ['VIT', 'AST'], ['S04', 'FNC'], ['MAD', 'MSF'], ['G2', 'XL']]

games = [*week7d1, *week7d2, *week8d1, *week8d2, *week8d3]

results = list(itertools.product(*games))

cases = [teams.copy() for i in range(len(results))]

for idx,wins in enumerate(results):
    for team in wins:
        cases[idx][team] += 1

max_tiebreakers = 0
tiebreaker_case = []
for idx,case in enumerate(cases):
    case = sorted(case.items(), key=lambda x: x[1], reverse=True)
    if case[5][1] != case[6][1]:
        for team in case[0:6]:
            passes[team[0]] += 1
    else:
        num_tied = 0
        for idx,team in enumerate(case):
            if case[idx][1] == case[5][1]:
                num_tied += 1
                if num_tied>max_tiebreakers:
                    max_tiebreakers = num_tied
                    tiebreaker_case = [case]
        for team in case[5:(5+num_tied)]:
            passes[team[0]] += (1/num_tied)
        for team in case[0:5]:
            passes[team[0]] += 1
total_games = len(results)

for team in passes:
    passes[team] = passes[team]/total_games
print(sorted(passes.items(),key=lambda x: x[1], reverse=True))
print("the most ties is ", max_tiebreakers, " with the season outcome\n", tiebreaker_case)

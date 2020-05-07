import random
import itertools

from cricket_teams.models import cricketTeamsModel
from math import factorial


def nPr(n, r):
    return int(factorial(n)/factorial(n-r))


def create_match_fixtures(num_of_matches):

    all_teams = list(cricketTeamsModel.objects.order_by().values_list('teamName', flat=True).distinct())
    total_permutations = nPr(len(all_teams),2)

    if total_permutations<num_of_matches:
        unique_match_fixtures = list(map(list, itertools.permutations(all_teams,2)))
        count_unique_match_fixtures = len(unique_match_fixtures)
        tmp_match_fixtures = unique_match_fixtures * int(num_of_matches/count_unique_match_fixtures)
        match_fixtures = tmp_match_fixtures + tmp_match_fixtures[:(num_of_matches-len(tmp_match_fixtures))]

    else:
        unique_match_fixtures = list(map(list, itertools.permutations(all_teams,2)))
        print("unique_match_fixtures",unique_match_fixtures)
        match_fixtures = unique_match_fixtures[:num_of_matches]
        print("match_fixtures",match_fixtures)

    return match_fixtures

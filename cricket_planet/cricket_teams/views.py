from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cricket_teams.models import cricketTeamsModel
from . import serializers
import json
from players.models import cricketPlayer


class teamAPIView(APIView):

    def get(self, request, format=None):
        print("Inside get")
        # print(cricketTeamsModel.objects.all())
        all_teams = list(cricketTeamsModel.objects.values())
        print("Result", all_teams)

        return Response({"data": all_teams})

    def post(self, request):
        data = request.data
        team_name = data["teamName"]
        print("team_name",team_name)
        team_details = list(cricketPlayer.objects.filter(
            country=team_name).values('firstName', 'lastName'))
        # list(json.dumps(team_details))
        print("team_details",team_details)
        return Response({"data": team_details})

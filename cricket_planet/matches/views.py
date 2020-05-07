from django.shortcuts import render
from matches.new_match import create_match_fixtures
from rest_framework.views import APIView
from rest_framework.response import Response


class fixturesView(APIView):

    def get(self, request, format=None):
        pass

    def post(self, request):
        number_of_fixtures_needed = request.data['fixturesCount']

        try:
            result_fixtures = create_match_fixtures(
                int(number_of_fixtures_needed))
            return Response({"data": result_fixtures})

        except Exception as E:
            print(E)

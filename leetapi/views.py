from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
# Create your views here.

def idfetch(request, id):
    url = 'https://leetcode.com/graphql/'
    user= id
    details= {}
    temp={}
    ProblemSolvedQuery= """
    query userProblemsSolved($username: String!) {
      matchedUser(username: $username) {
        problemsSolvedBeatsStats {
          difficulty
          percentage
        }
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """

    ContestRatingQuery= """
    query userContestRankingInfo($username: String!) {
      userContestRanking(username: $username) {
        attendedContestsCount
        rating
        globalRanking
        totalParticipants
        topPercentage
        badge {
          name
        }
      }
    }

    """
    status= 404
    try: 
        response = requests.post(url=url, json={"query": ProblemSolvedQuery,"variables": {"username":user}})
        if response.status_code == 200:
            status=200
            details[user]= response.json()

        response = requests.post(url=url, json={"query": ContestRatingQuery,"variables": {"username":user}})
        if response.status_code == 200:
            temp[user]= response.json()
        Leetreturn={
            'status': status,
            'Total': details[user]['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][0]['count'],
            'Easy': details[user]['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][1]['count'],
            'Medium': details[user]['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][2]['count'],
            'Hard': details[user]['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][3]['count'],
            'Rating': round(temp[user]['data']['userContestRanking']['rating'])
        }
              # print(f'{user}: {allvar} {easyvar} {medvar} {hardvar} {rating}')
        return JsonResponse(Leetreturn)
    except TypeError:
      return JsonResponse({'status': 404})


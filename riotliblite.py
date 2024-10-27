import requests
import urllib
import time
import json
from dtos import MatchDto, TimelineDto


api_key = 'RGAPI-272942ca-a0c8-4c80-bac9-3e9b36864e2c'
headers = {"X-Riot-Token": api_key}

def getPuuid(game_name,tag_line):
    tag = urllib.parse.quote(tag_line)
    summoner = urllib.parse.quote(game_name)
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner}/{tag}?api_key={api_key}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        player_info = response.json()
        puuid = player_info['puuid']
    else:
        print(f"Error fetching player data: {response.status_code}")
        return None
    return puuid
def getMatches(puuid,start,count):
    matches_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start={start}&count={count}&api_key={api_key}"
    matches = requests.get(matches_url, headers=headers).json()
    return matches
def getTimelineDto(match_id):
    url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={api_key}'
    response = requests.get(url,headers=headers)
    timeline = response.json()
    status = response.status_code
    return timeline,status
def getMatchDto(match_id):                                         
    url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
    response = requests.get(url,headers=headers)
    match = response.json()
    status = response.status_code
    return match, status
def last_game(puuid):
    return getMatchDto(getMatches(puuid,0,1)[0])

class Game:
    def __init__(self,puuid,match_id) -> None:
        self.puuid = puuid
        self.match_id = match_id
        self.match = MatchDto(getMatchDto(match_id)[0])
        #self.timeline = TimelineDto(self.fetchTimelineDto())
        self.me = Game.getME(self)

    def getME(self):
        parts = self.match.info.participants
        for i in range(0,10):
            if self.puuid == parts[i].puuid:
                return parts[i]
        return None
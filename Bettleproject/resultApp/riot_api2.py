import requests
from urllib import parse


DEVELOPMENTAPIKEY = "RGAPI-97f2ed81-4bee-4975-a55f-74510d188521"
# summonerName = "Hide on Bush"


### /lol/summoner/v4/summoners/by-name/{summonerName}
### {'id': 'e4ZET16WjS-maYdIDLgjuWrPV5CsZDE-VVGSsIcmonuHw3g', 'accountId': '_-NDnoOGlK5aP4aPG1W5JaVcz8TvU8-IYDOzKJqp45kDqtE', 'puuid': 'mOe68-7_EwmpM9HiQST4K5FyqT2_aoul-P6t34YfGGi_UeXzr9HN80tDgakWiUKVkjMuHdEqSSBjlw', 'name': '우 리', 'profileIconId': 907, 'revisionDate': 1653330648000, 'summonerLevel': 317}
### {'status': {'message': 'Data not found - summoner not found', 'status_code': 404}}
def getSummonerInfo(DEVELOPMENTAPIKEY, summonerName):
    encodingSummonerName = parse.quote(summonerName)
    APIURL = (
        "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        + encodingSummonerName
    )
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    }
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data


### /lol/league/v4/entries/by-summoner/{encryptedSummonerId}
def getUserInfo(DEVELOPMENTAPIKEY, summonerName):
    encryptedId = getSummonerInfo(DEVELOPMENTAPIKEY, summonerName)["id"]
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    }
    APIURL = (
        "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedId
    )
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data


### /lol/match/v5/matches/by-puuid/{puuid}/ids
def getMatchsInfo(DEVELOPMENTAPIKEY, summonerName):
    # print('여기', getSummonerInfo(DEVELOPMENTAPIKEY, summonerName))
    puuid = getSummonerInfo(DEVELOPMENTAPIKEY, summonerName)["puuid"]
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    }
    APIURL = (
        "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
        + puuid
        + "/ids?start=0&count=20"
    )
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data


### /lol/match/v5/matches/{matchId}
def getOneMatchInfo(DEVELOPMENTAPIKEY, summonerName, i):
    matchsID = getMatchsInfo(DEVELOPMENTAPIKEY, summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    }
    APIURL = "https://asia.api.riotgames.com/lol/match/v5/matches/" + matchsID[i]
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data


# def getSpectatorInfo(DEVELOPMENTAPIKEY, summonerName, i):
#     encrypt = encrypt(DEVELOPMENTAPIKEY, summonerName)["id"]
#     headers = {
#         "Origin": "https://developer.riotgames.com",
#         "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
#         "X-Riot-Token": DEVELOPMENTAPIKEY,
#         "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
#     }
#     APIURL = "https://asia.api.riotgames.com/lol/match/v5/matches/" + matchsID[i]
#     res = requests.get(APIURL, headers=headers)
#     data = res.json()
#     return data


#
"""
[
    {
        "leagueId": "05fb99f4-e149-3133-a78e-821597582f9d",
        "queueType": "RANKED_SOLO_5x5",
        "tier": "CHALLENGER",
        "rank": "I",
        "summonerId": "4iu04RA8grL6cvdipMpoYOHdv-7YcMb748WfUFZj_qpkQQ",
        "summonerName": "Hide on bush",
        "leaguePoints": 959,
        "wins": 317,
        "losses": 275,
        "veteran": true,
        "inactive": false,
        "freshBlood": false,
        "hotStreak": false
    }
]

"""

# summoner_info = getSummonerInfo(DEVELOPMENTAPIKEY, summonerName)
# user_info = getUserInfo(DEVELOPMENTAPIKEY, summonerName)
# matchs_info = getMatchsInfo(DEVELOPMENTAPIKEY, summonerName)  # 최근 20개 전적 데이터
# one_match_info = getOneMatchInfo(DEVELOPMENTAPIKEY, summonerName, 0)  # 구제척인 게임 정보
# participants = one_match_info["info"]["participants"]
# blue_team = one_match_info["info"]["teams"][0]
# red_team = one_match_info["info"]["teams"][1]


# print(f"{summoner_info}")
# if summoner_info["status"] == True:
#     print("error")

# print()
# print(f"{user_info}")
# print()
# print(f"{matchs_info}")
# print()
# print(f"{one_match_info['metadata']}")
# print(f"{blue_team}")
# print(f"{red_team}")
# print([p[2]["puuid"])

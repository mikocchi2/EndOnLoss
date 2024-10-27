import json
from typing import Dict,List,Any

class TimelineDto:
    class Position:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class ChampionStats:
        def __init__(self, data):
            self.abilityHaste = data["abilityHaste"]
            self.abilityPower = data["abilityPower"]
            self.armor = data["armor"]
            self.armorPen = data["armorPen"]
            self.armorPenPercent = data["armorPenPercent"]
            self.attackDamage = data["attackDamage"]
            self.attackSpeed = data["attackSpeed"]
            self.bonusArmorPenPercent = data["bonusArmorPenPercent"]
            self.bonusMagicPenPercent = data["bonusMagicPenPercent"]
            self.ccReduction = data["ccReduction"]
            self.cooldownReduction = data["cooldownReduction"]
            self.health = data["health"]
            self.healthMax = data["healthMax"]
            self.healthRegen = data["healthRegen"]
            self.lifesteal = data["lifesteal"]
            self.magicPen = data["magicPen"]
            self.magicPenPercent = data["magicPenPercent"]
            self.magicResist = data["magicResist"]
            self.movementSpeed = data["movementSpeed"]
            self.omnivamp = data["omnivamp"]
            self.physicalVamp = data["physicalVamp"]
            self.power = data["power"]
            self.powerMax = data["powerMax"]
            self.powerRegen = data["powerRegen"]
            self.spellVamp = data["spellVamp"]

    class DamageStats:
        def __init__(self, data):
            self.magicDamageDone = data["magicDamageDone"]
            self.magicDamageDoneToChampions = data["magicDamageDoneToChampions"]
            self.magicDamageTaken = data["magicDamageTaken"]
            self.physicalDamageDone = data["physicalDamageDone"]
            self.physicalDamageDoneToChampions = data["physicalDamageDoneToChampions"]
            self.physicalDamageTaken = data["physicalDamageTaken"]
            self.totalDamageDone = data["totalDamageDone"]
            self.totalDamageDoneToChampions = data["totalDamageDoneToChampions"]
            self.totalDamageTaken = data["totalDamageTaken"]
            self.trueDamageDone = data["trueDamageDone"]
            self.trueDamageDoneToChampions = data["trueDamageDoneToChampions"]
            self.trueDamageTaken = data["trueDamageTaken"]

    class ParticipantFrame:
        def __init__(self, data):
            self.participantId = data["participantId"]
            self.championStats = TimelineDto.ChampionStats(data["championStats"])
            self.currentGold = data["currentGold"]
            self.damageStats = TimelineDto.DamageStats(data["damageStats"])
            self.goldPerSecond = data["goldPerSecond"]
            self.jungleMinionsKilled = data["jungleMinionsKilled"]
            self.level = data["level"]
            self.minionsKilled = data["minionsKilled"]
            self.participantId = data["participantId"]
            self.position = TimelineDto.Position(data["position"]["x"], data["position"]["y"]) if data.get("position") else None
            self.timeEnemySpentControlled = data["timeEnemySpentControlled"]
            self.totalGold = data["totalGold"]
            self.xp = data["xp"]

    class Event:
        def __init__(self, data):
            self.type = data["type"]
            self.timestamp = data["timestamp"]
            self.participantId = data.get("participantId")
            self.itemId = data.get("itemId")
            self.skillSlot = data.get("skillSlot")
            self.levelUpType = data.get("levelUpType")
            self.wardType = data.get("wardType")
            self.creatorId = data.get("creatorId")
            self.assistingParticipantIds = data.get("assistingParticipantIds")
            self.bounty = data.get("bounty")
            self.killStreakLength = data.get("killStreakLength")
            self.killerId = data.get("killerId")
            self.position = TimelineDto.Position(data["position"]["x"], data["position"]["y"]) if data.get("position") else None
            self.shutdownBounty = data.get("shutdownBounty")
            self.victimDamageDealt = data.get("victimDamageDealt")
            self.victimDamageReceived = data.get("victimDamageReceived")
            self.victimId = data.get("victimId")
            self.killType = data.get("killType")
            self.multiKillLength = data.get("multiKillLength")

    class Frame:
        def __init__(self, data):
            self.timestamp = data["timestamp"]
            self.events = [TimelineDto.Event(event) for event in data["events"]]
            self.participantFrames = {key: TimelineDto.ParticipantFrame(value) for key, value in data["participantFrames"].items()}

    class Info:
        def __init__(self, data):
            self.endOfGameResult = data.get("endOfGameResult","")
            self.frameInterval = data["frameInterval"]
            self.frames = [TimelineDto.Frame(frame) for frame in data["frames"]]

    class Metadata:
        def __init__(self, data):
            self.dataVersion = data["dataVersion"]
            self.matchId = data["matchId"]
            self.participants = data["participants"]

    def __init__(self, data):
        self.metadata = TimelineDto.Metadata(data["metadata"])
        self.info = TimelineDto.Info(data["info"])

    @staticmethod
    def from_json(data):
        return TimelineDto(data)
class MatchDto:
    class Participant:
        def __init__(self, participant_data: Dict[str, Any]):
            self.all_in_pings = participant_data.get('allInPings', 0)
            self.assist_me_pings = participant_data.get('assistMePings', 0)
            self.assists = participant_data.get('assists', 0)
            self.baron_kills = participant_data.get('baronKills', 0)
            self.basic_pings = participant_data.get('basicPings', 0)
            self.bounty_level = participant_data.get('bountyLevel', 0)
            self.challenges = participant_data.get('challenges', {})
            self.champ_experience = participant_data.get('champExperience', 0)
            self.champ_level = participant_data.get('champLevel', 0)
            self.champion_id = participant_data.get('championId', 0)
            self.champion_name = participant_data.get('championName', "")
            self.command_pings = participant_data.get('commandPings', 0)
            self.consumables_purchased = participant_data.get('consumablesPurchased', 0)
            self.damage_dealt_to_buildings = participant_data.get('damageDealtToBuildings', 0)
            self.damage_dealt_to_objectives = participant_data.get('damageDealtToObjectives', 0)
            self.damage_dealt_to_turrets = participant_data.get('damageDealtToTurrets', 0)
            self.damage_self_mitigated = participant_data.get('damageSelfMitigated', 0)
            self.danger_pings = participant_data.get('dangerPings', 0)
            self.deaths = participant_data.get('deaths', 0)
            self.detector_wards_placed = participant_data.get('detectorWardsPlaced', 0)
            self.double_kills = participant_data.get('doubleKills', 0)
            self.dragon_kills = participant_data.get('dragonKills', 0)
            self.eligible_for_progression = participant_data.get('eligibleForProgression', True)
            self.enemy_missing_pings = participant_data.get('enemyMissingPings', 0)
            self.enemy_vision_pings = participant_data.get('enemyVisionPings', 0)
            self.first_blood_assist = participant_data.get('firstBloodAssist', False)
            self.first_blood_kill = participant_data.get('firstBloodKill', False)
            self.first_tower_assist = participant_data.get('firstTowerAssist', False)
            self.first_tower_kill = participant_data.get('firstTowerKill', False)
            self.game_ended_in_early_surrender = participant_data.get('gameEndedInEarlySurrender', False)
            self.game_ended_in_surrender = participant_data.get('gameEndedInSurrender', False)
            self.gold_earned = participant_data.get('goldEarned', 0)
            self.gold_spent = participant_data.get('goldSpent', 0)
            self.individual_position = participant_data.get('individualPosition', "")
            self.inhibitor_kills = participant_data.get('inhibitorKills', 0)
            self.inhibitor_takedowns = participant_data.get('inhibitorTakedowns', 0)
            self.inhibitors_lost = participant_data.get('inhibitorsLost', 0)
            self.item0 = participant_data.get('item0', 0)
            self.item1 = participant_data.get('item1', 0)
            self.item2 = participant_data.get('item2', 0)
            self.item3 = participant_data.get('item3', 0)
            self.item4 = participant_data.get('item4', 0)
            self.item5 = participant_data.get('item5', 0)
            self.item6 = participant_data.get('item6', 0)
            self.items_purchased = participant_data.get('itemsPurchased', 0)
            self.killing_sprees = participant_data.get('killingSprees', 0)
            self.kills = participant_data.get('kills', 0)
            self.lane = participant_data.get('lane', "")
            self.largest_critical_strike = participant_data.get('largestCriticalStrike', 0)
            self.largest_killing_spree = participant_data.get('largestKillingSpree', 0)
            self.largest_multi_kill = participant_data.get('largestMultiKill', 0)
            self.longest_time_spent_living = participant_data.get('longestTimeSpentLiving', 0)
            self.magic_damage_dealt = participant_data.get('magicDamageDealt', 0)
            self.magic_damage_dealt_to_champions = participant_data.get('magicDamageDealtToChampions', 0)
            self.magic_damage_taken = participant_data.get('magicDamageTaken', 0)
            self.need_vision_pings = participant_data.get('needVisionPings', 0)
            self.neutral_minions_killed = participant_data.get('neutralMinionsKilled', 0)
            self.nexus_kills = participant_data.get('nexusKills', 0)
            self.nexus_lost = participant_data.get('nexusLost', 0)
            self.nexus_takedowns = participant_data.get('nexusTakedowns', 0)
            self.objectives_stolen = participant_data.get('objectivesStolen', 0)
            self.objectives_stolen_assists = participant_data.get('objectivesStolenAssists', 0)
            self.on_my_way_pings = participant_data.get('onMyWayPings', 0)
            self.participant_id = participant_data.get('participantId', 0)
            self.penta_kills = participant_data.get('pentaKills', 0)
            self.physical_damage_dealt = participant_data.get('physicalDamageDealt', 0)
            self.physical_damage_dealt_to_champions = participant_data.get('physicalDamageDealtToChampions', 0)
            self.physical_damage_taken = participant_data.get('physicalDamageTaken', 0)
            self.profile_icon = participant_data.get('profileIcon', 0)
            self.push_pings = participant_data.get('pushPings', 0)
            self.puuid = participant_data.get('puuid', "")
            self.quadra_kills = participant_data.get('quadraKills', 0)
            self.riot_id_name = participant_data.get('riotIdName', "")
            self.riot_id_tagline = participant_data.get('riotIdTagline', "")
            self.role = participant_data.get('role', "")
            self.sight_wards_bought_in_game = participant_data.get('sightWardsBoughtInGame', 0)
            self.spell1_casts = participant_data.get('spell1Casts', 0)
            self.spell2_casts = participant_data.get('spell2Casts', 0)
            self.spell3_casts = participant_data.get('spell3Casts', 0)
            self.spell4_casts = participant_data.get('spell4Casts', 0)
            self.summoner1_casts = participant_data.get('summoner1Casts', 0)
            self.summoner1_id = participant_data.get('summoner1Id', 0)
            self.summoner2_casts = participant_data.get('summoner2Casts', 0)
            self.summoner2_id = participant_data.get('summoner2Id', 0)
            self.summoner_id = participant_data.get('summonerId', "")
            self.summoner_level = participant_data.get('summonerLevel', 0)
            self.summoner_name = participant_data.get('summonerName', "")
            self.team_early_surrendered = participant_data.get('teamEarlySurrendered', False)
            self.team_id = participant_data.get('teamId', 0)
            self.team_position = participant_data.get('teamPosition', "")
            self.time_ccing_others = participant_data.get('timeCCingOthers', 0)
            self.time_played = participant_data.get('timePlayed', 0)
            self.total_damage_dealt = participant_data.get('totalDamageDealt', 0)
            self.total_damage_dealt_to_champions = participant_data.get('totalDamageDealtToChampions', 0)
            self.total_damage_shielded_on_teammates = participant_data.get('totalDamageShieldedOnTeammates', 0)
            self.total_damage_taken = participant_data.get('totalDamageTaken', 0)
            self.total_heal = participant_data.get('totalHeal', 0)
            self.total_heals_on_teammates = participant_data.get('totalHealsOnTeammates', 0)
            self.total_minions_killed = participant_data.get('totalMinionsKilled', 0)
            self.total_time_cc_dealt = participant_data.get('totalTimeCCDealt', 0)
            self.total_time_spent_dead = participant_data.get('totalTimeSpentDead', 0)
            self.total_units_healed = participant_data.get('totalUnitsHealed', 0)
            self.triple_kills = participant_data.get('tripleKills', 0)
            self.true_damage_dealt = participant_data.get('trueDamageDealt', 0)
            self.true_damage_dealt_to_champions = participant_data.get('trueDamageDealtToChampions', 0)
            self.true_damage_taken = participant_data.get('trueDamageTaken', 0)
            self.turret_kills = participant_data.get('turretKills', 0)
            self.turret_takedowns = participant_data.get('turretTakedowns', 0)
            self.turrets_lost = participant_data.get('turretsLost', 0)
            self.unreal_kills = participant_data.get('unrealKills', 0)
            self.vision_cleared_pings = participant_data.get('visionClearedPings', 0)
            self.vision_score = participant_data.get('visionScore', 0)
            self.vision_wards_bought_in_game = participant_data.get('visionWardsBoughtInGame', 0)
            self.wards_killed = participant_data.get('wardsKilled', 0)
            self.wards_placed = participant_data.get('wardsPlaced', 0)
            self.win = participant_data.get('win', None)

    class Team:
        def __init__(self, team_data: Dict[str, Any]):
            self.team_id = team_data.get('teamId', 0)
            self.win = team_data.get('win', False)
            self.bans = team_data.get('bans', [])
            self.objectives = team_data.get('objectives', {})

    class MatchInfo:
        def __init__(self, info_data: Dict[str, Any]):
            self.end_of_game_result = info_data.get('endOfGameResult', "")
            self.game_creation = info_data.get('gameCreation', 0)
            self.game_duration = info_data.get('gameDuration', 0)
            self.game_end_timestamp = info_data.get('gameEndTimestamp', 0)
            self.game_id = info_data.get('gameId', 0)
            self.game_mode = info_data.get('gameMode', "")
            self.game_name = info_data.get('gameName', "")
            self.game_start_timestamp = info_data.get('gameStartTimestamp', 0)
            self.game_type = info_data.get('gameType', "")
            self.game_version = info_data.get('gameVersion', "")
            self.map_id = info_data.get('mapId', 0)
            self.participants = [MatchDto.Participant(participant) for participant in info_data.get('participants', [])]
            self.teams = [MatchDto.Team(team) for team in info_data.get('teams', [])]

        def __repr__(self):
            return f"<MatchInfo ID: {self.game_id}, Mode: {self.game_mode}>"

    class Metadata:
        def __init__(self, metadata_data: Dict[str, Any]):
            self.data_version = metadata_data.get('dataVersion', "")
            self.match_id = metadata_data.get('matchId', "")
            self.participants = metadata_data.get('participants', [])

        def __repr__(self):
            return f"<Metadata Match ID: {self.match_id}>"

    def __init__(self, match_data: Dict[str, Any]):
        self.metadata = MatchDto.Metadata(match_data.get('metadata', {}))
        self.info = MatchDto.MatchInfo(match_data.get('info', {}))

    def __repr__(self):
        return f"<MatchDto {self.metadata.match_id}>"
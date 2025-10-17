import zoneinfo

SERVER_INFO = {
    "NA1": {"name": "North America", "timezone": zoneinfo.ZoneInfo("America/Los_Angeles")},
    "BR1": {"name": "Brazil", "timezone": zoneinfo.ZoneInfo("America/Sao_Paulo")},
    "LA1": {"name": "Latin America North", "timezone": zoneinfo.ZoneInfo("America/Los_Angeles")},
    "LA2": {"name": "Latin America South", "timezone": zoneinfo.ZoneInfo("America/Los_Angeles")},
    "JP1": {"name": "Japan", "timezone": zoneinfo.ZoneInfo("Asia/Tokyo")},
    "KR": {"name": "Korea", "timezone": zoneinfo.ZoneInfo("Asia/Seoul")},
    "SG2": {"name": "South East Asia", "timezone": zoneinfo.ZoneInfo("Asia/Singapore")},
    "TW2": {"name": "Taiwan", "timezone": zoneinfo.ZoneInfo("Asia/Taipei")},
    "VN2": {"name": "Vietnam", "timezone": zoneinfo.ZoneInfo("Asia/Ho_Chi_Minh")},
    "OC1": {"name": "Oceania", "timezone": zoneinfo.ZoneInfo("Australia/Sydney")},
    "ME1": {"name": "Middle East", "timezone": zoneinfo.ZoneInfo("Asia/Riyadh")},
    "EUN1": {"name": "Europe Nordic & East", "timezone": zoneinfo.ZoneInfo("Europe/Amsterdam")},
    "EUW1": {"name": "Europe West", "timezone": zoneinfo.ZoneInfo("Europe/Amsterdam")},
    "TR1": {"name": "Turkey", "timezone": zoneinfo.ZoneInfo("Europe/Istanbul")},
    "RU": {"name": "Russia", "timezone": zoneinfo.ZoneInfo("Europe/Stockholm")},
}

LEVEL_COSTS = [0, 2, 4, 12, 22, 42, 78, 126, 202, 286]

TG_ITEM_HASH = '{218b53a5}'
TAC_ITEM_HASH = '{d304f83b}'
RADIANT_ITEM_HASH = '{6ef5c598}'
ARTIFACT_ITEM_HASH = '{44ace175}'
EMBLEM_ITEM_HASH = '{ebcd1bac}'
CRAFTABLE_ITEM_HASH = '{7ea41d13}'
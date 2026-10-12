from datetime import datetime
from zoneinfo import ZoneInfo
import json
from urllib.request import urlopen

STHLM = ZoneInfo("Europe/Stockholm")

def minutes_diff(expected_iso):
    expected = datetime.fromisoformat(expected_iso).replace(tzinfo=STHLM)
    now = datetime.now(STHLM)
    diff = int((expected - now).total_seconds() // 60)

    return diff

def subway_time_left(site_id, dest_name):
    url = f"https://transport.integration.sl.se/v1/sites/{site_id}/departures"
    with urlopen(url) as response:
        departures = json.load(response)

    time_left_list = []
    for departure in departures["departures"]:
        if dest_name.lower() == departure["destination"].lower():
            time_left = minutes_diff(departure["expected"])
            time_left_list.append(time_left)

    result = [f"Mot {dest_name}", f"{time_left_list[0]} min", f"{time_left_list[1]} min"]

    return result

# test
# site_id = 9305
# dest_name = "Kungsträdgården"

# print(subway_time_left(site_id, dest_name))
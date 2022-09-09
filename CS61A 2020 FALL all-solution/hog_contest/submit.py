import json
import urllib
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen, Request

from ucb import main

URL = "https://hog-contest.cs61a.org"
SUBMISSION_ENDPOINT = "/api/submit_strategy"


def submit(exported_strategy, strategy_name, token, out):
    data = {
        "strat": exported_strategy,
        "name": strategy_name,
        "token": token,
    }
    request = Request(urllib.parse.urljoin(URL, SUBMISSION_ENDPOINT), bytes(urlencode(data), "utf-8"))
    try:
        body = json.loads(urlopen(request).read().decode())
        out("You have submitted in the group: {}".format(body["group"]))
        out("Your strategy has the hash: {}".format(body["hash"]))
        out("Visit {} to see the leaderboard.".format(URL))
        out("Visit {}/log to see the status of your submission as it is processed.".format(URL))
        out("\nGood luck!\n")
    except HTTPError as e:
        message = e.read().decode()
        out("Error: {}".format(message))
        raise Exception(message)

@main
def main():
    print("To submit, please run python3 ok --submit, so your strategy can be validated and backed up!")
import praw
from praw.models import Submission
from typing import List
from PIL import Image
from io import BytesIO
import requests
import os

def getImagefromURL(url: str) -> Image:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def getsubs() -> List[str]:
    
    subs = ["me_irl","prequelmemes","funny"]

    return subs

def getSubmissionPoints(s: Submission) -> int:
    return s.score

reddit = praw.Reddit(client_id='J8_PdiLlLSPTDQ',
                    client_secret='H728p6ZsjIQkTqGvkj5upzAVXbs',
                    user_agent='Memebot by /u/flipnorris')

def getSubmissions() -> List[Submission]:
    submissions = []

    for sub in getsubs():
        print("Fetching submissions from /r/{}".format(sub))
        subr = reddit.subreddits.search_by_name(sub,exact=True)
        if len(subr) == 0:
            print("WARNING: Could not find subreddit /r/{}".format(sub))
        else:
            for subm in subr[0].top("day", limit=10):
                url = subm.url
                if url.endswith(".png") or url.endswith(".jpg"):
                    print(url)
                    submissions.append(subm)

    submissions.sort(reverse=True,key=getSubmissionPoints)

    return submissions

def getSubmissionImage(subm: Submission) -> Image:
    if not os.path.isfile("cache/{}.png".format(subm.id)):
        img = getImagefromURL(subm.url)
        return img
        img.save("cache/{}.png".format(subm.id))
        return img
    return Image.open("cache/{}.png".format(subm.id))
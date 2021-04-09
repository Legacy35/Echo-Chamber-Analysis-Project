import csv

import pandas as pd
import requests
from psaw import PushshiftAPI

def get_comments(subreddit="conservative", limit=100):
    filename= subreddit+".csv"
    api = PushshiftAPI()
    gen = api.search_comments(subreddit=subreddit,
                              filter=["id", "created_utc", "score", "parent_id", "body", "permalink"], limit=limit)
    df = pd.DataFrame(data.d_ for data in gen)
    # Match the other code
    df.rename(columns={"id": "Id",
                       "created_utc": "Date_Created_Utc",
                       "score": "Score",
                       "parent_id": "Parent_id",
                       "body": "Body",
                       "permalink": "Link"}, inplace=True)
    # Add empty rows
    df = pd.concat([df, pd.DataFrame(columns=["Mentioned Nouns",
                                              "Sentiment-Subjectivity", "Sentiment-Polarization",
                                              "Hate Speech Level"])])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    get_comments(subreddit="conservative", limit=100000)

import pandas as pd
from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Processes a file containing tweets and returns the top 10 dates with the top
    user in each date.

    Args:
        file_path (str): The path to the file containing the tweets.

    Returns:
        List[Tuple[datetime.date, str]]: A list of tuples, where each tuple contains a date and the top user for that date.
    """
    # load the entire dataset at once
    df = pd.read_json(file_path, lines=True)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['username'] = df['user'].apply(lambda x: x['username'])

    # group by date and username, count the tweets
    tweet_counts = df.groupby(['date', 'username']).size().reset_index(name='count')

    # sort by date asc and by count desc (top count on top), then remove duplicated non-top rows
    top_users_per_date = tweet_counts.sort_values(['date', 'count'], ascending=[True, False]) \
        .drop_duplicates('date')

    # filter to the top 10 dates with the most tweets
    top_dates = df.groupby('date').size().nlargest(10).index
    top_users = top_users_per_date[top_users_per_date['date'].isin(top_dates)]

    return [(row['date'], row['username']) for _, row in top_users.iterrows()]

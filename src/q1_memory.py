import json
from collections import defaultdict
from typing import List, Tuple
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Processes a file containing tweets and returns the top 10 dates with the top
    user in each date.

    Args:
        file_path (str): The path to the file containing the tweets.

    Returns:
        List[Tuple[datetime.date, str]]: A list of tuples, where each tuple contains a date and the top user for that date.
    """
    date_counts = defaultdict(int)
    user_counts = defaultdict(lambda: defaultdict(int))

    # stream and process the file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            username = tweet['user']['username']
            date_counts[date] += 1
            user_counts[date][username] += 1

    # get top users per date
    top_users = {
        date: max(users, key=users.get) for date, users in user_counts.items()
    }

    # sort and get top 10 dates
    top_10_dates = sorted(date_counts, key=date_counts.get, reverse=True)[:10]

    return [(date, top_users[date]) for date in top_10_dates]

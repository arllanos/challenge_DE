from datetime import date
import pytest
import json
from src.q1_memory import q1_memory

SAMPLE_TWEETS = [
    {"date": "2021-02-01T09:00:00+00:00", "user": {"username": "user1"}, "content": "Tweet content 1"},
    {"date": "2021-02-01T10:00:00+00:00", "user": {"username": "user2"}, "content": "Tweet content 2"},
    {"date": "2021-02-01T11:00:00+00:00", "user": {"username": "user1"}, "content": "Tweet content 3"},
    {"date": "2021-02-02T09:00:00+00:00", "user": {"username": "user3"}, "content": "Tweet content 4"},
    {"date": "2021-02-02T10:00:00+00:00", "user": {"username": "user2"}, "content": "Tweet content 5"},
    {"date": "2021-02-02T10:01:00+00:00", "user": {"username": "user2"}, "content": "Tweet content 6"},
]

@pytest.fixture
def sample_tweets_file(tmp_path):
    file = tmp_path / "sample_tweets.json"
    with file.open('w') as f:
        for tweet in SAMPLE_TWEETS:
            f.write(json.dumps(tweet) + '\n')
    return str(file)

def test_q1_memory(sample_tweets_file):
    expected = [
        (date(2021, 2, 1), "user1"),
        (date(2021, 2, 2), "user2"),  # assuming user2 has more tweets overall if more data is added
    ]
    actual = q1_memory(sample_tweets_file)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_q1_memory_empty_file(tmp_path):
    file = tmp_path / "empty_tweets.json"
    file.touch()
    assert q1_memory(str(file)) == [], "Expected an empty list for an empty file"

import json
import pytest
from src.q3_time import q3_time

# Sample data for testing
SAMPLE_TWEETS = [
    {"mentionedUsers": [{"username": "user1"}]},
    {"mentionedUsers": [{"username": "user2"}, {"username": "user1"}]},
    {"mentionedUsers": [{"username": "user3"}]},
    {"mentionedUsers": [{"username": "user2"}]},
    {"mentionedUsers": [{"username": "user1"}]},
]

@pytest.fixture
def sample_tweets_file(tmp_path):
    file = tmp_path / "sample_tweets.json"
    with file.open('w') as f:
        for tweet in SAMPLE_TWEETS:
            f.write(json.dumps(tweet) + '\n')
    return str(file)

def test_q3_time(sample_tweets_file):
    expected = [
        ("user1", 3),  # assuming user1 is the most mentioned based on the sample
        ("user2", 2),
        ("user3", 1),
    ]
    actual = q3_time(sample_tweets_file)
    
    assert actual == expected, f"Expected {expected}, but got {actual}"

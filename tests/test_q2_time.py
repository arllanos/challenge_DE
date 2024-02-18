import json
import pytest
from src.q2_time import q2_time

SAMPLE_TWEETS = [
    {"content": "Filipenses 4:14 🙏"},
    {"content": "This is so funny 😂"},
    {"content": "Farming is hard work 🚜"},
    {"content": "Wheat fields 🌾"},
    {"content": "Please persist 🙏"},
    {"content": "Hilarious 😂😂"},
    {"content": "Driving my tractor 🚜"},
    {"content": "Harvest season 🌾🚜"},
    {"content": "Grateful 🙏🙏"},
    {"content": "Laughing so much 😂"},
]

@pytest.fixture
def sample_tweets_file(tmp_path):
    file = tmp_path / "sample_tweets.json"
    with file.open('w') as f:
        for tweet in SAMPLE_TWEETS:
            f.write(json.dumps(tweet) + '\n')
    return str(file)

def test_q2_time(sample_tweets_file):
    expected = [
        ("🙏", 4),  # assuming 🙏 appears 4 times
        ("😂", 4),  # assuming 😂 appears 4 times
        ("🚜", 3),  # assuming 🚜 appears 3 times
        ("🌾", 2),  # assuming 🌾 appears 2 times
    ]

    actual = q2_time(sample_tweets_file)
    assert len(actual) == len(expected), f"Expected length {len(expected)}, but got {len(actual)}"
    for exp, act in zip(expected, actual):
        assert exp == act, f"Expected {exp}, but got {act}"

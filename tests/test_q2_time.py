import pytest
from src.q2_time import q2_time

@pytest.fixture
def sample_tweets_file(tmp_path):
    file = tmp_path / "sample_tweets.json"
    with file.open('w') as f:
        f.write('{"content": "I love ❤️ emojis"}\n')
        f.write('{"content": "I love ✈️ emojis"}\n')
        f.write('{"content": "I love 😊 emojis"}\n')
        f.write('{"content": "I love ❤️ emojis"}\n')
        f.write('{"content": "I love ✈️ emojis"}\n')
        f.write('{"content": "I love 😊 emojis"}\n')
    return str(file)

def test_q2_time(sample_tweets_file):
    expected = [
        ("❤️", 2),
        ("✈️", 2),
        ("😊", 2),
    ]
    actual = q2_time(sample_tweets_file)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_q2_time_empty_file(tmp_path):
    file = tmp_path / "empty_tweets.json"
    with file.open('w') as f:
        pass
    expected = []
    actual = q2_time(str(file))
    assert actual == expected, f"Expected {expected}, but got {actual}"

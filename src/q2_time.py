import pandas as pd
import emoji
from typing import List, Tuple
from collections import Counter


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Calculate the top 10 most common emojis from a JSON file containing tweet data.

    Args:
        file_path (str): The path to the JSON file containing tweet data.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains an emoji character and its count.

    Examples:
        >>> q2_time('tweets.json')
        [("✈️", 6856), ("❤️", 5876), ('😊', 100), ...]
    """
    # load the entire dataset at once
    df = pd.read_json(file_path, lines=True)

    emoji_counts = Counter()
    for content in df['content']:
        for emoji_data in emoji.emoji_list(content):
            emoji_char = emoji_data['emoji']
            emoji_counts[emoji_char] += 1

    # using list comprehension
    # emoji_counts = Counter(emoji_char for content in df['content'] for emoji_char in [e['emoji'] for e in emoji.emoji_list(content)])

    return emoji_counts.most_common(10)

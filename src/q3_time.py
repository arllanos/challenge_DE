import pandas as pd
from typing import List, Tuple


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # load the entire dataset at once
    df = pd.read_json(file_path, lines=True)

    if ('mentionedUsers' not in df.columns or df['mentionedUsers'].isnull().all()):
        return []
    
    mentioned_df = df[['mentionedUsers']].explode('mentionedUsers')
    mentioned_df['username'] = mentioned_df['mentionedUsers'].apply(lambda x: x.get('username') if isinstance(x, dict) else None)
    mentioned_df.dropna(subset=['username'], inplace=True)

    # count occurrences of each username
    mentions_count = mentioned_df['username'].value_counts().head(10)

    return list(mentions_count.items())

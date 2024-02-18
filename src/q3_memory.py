import pandas as pd
from typing import List, Tuple


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # read data in chunks to be more memory efficient
    chunk_size = 100  # adjust based on your system's memory
    mention_counts = pd.Series(dtype="int")

    for df_chunk in pd.read_json(file_path, lines=True, chunksize=chunk_size):

        if 'mentionedUsers' in df_chunk.columns and not df_chunk['mentionedUsers'].isnull().all():
            mentioned_df = df_chunk[['mentionedUsers']].explode('mentionedUsers')
            mentioned_df['username'] = mentioned_df['mentionedUsers'].apply(lambda x: x.get('username') if isinstance(x, dict) else None)
            mentioned_df.dropna(subset=['username'], inplace=True)
            
            # update counts by adding to the overall count
            chunk_counts = mentioned_df['username'].value_counts()
            mention_counts = mention_counts.add(chunk_counts, fill_value=0)

    top_10_mentions = mention_counts.nlargest(10).items()
    return list(top_10_mentions)

from src.main import calculate_iqr, save_to_md
from src.lib import get_data
import os

remote_path = 'https://raw.githubusercontent.com/Cavidan-oss/Javidan_Individual_Project_1/refs/heads/main/data/shanghai_ranking_2024.csv'

def test_main():
    df = get_data(remote_path)
    top_50_df = df.iloc[: 50 , :]
    assert int(calculate_iqr(top_50_df, column='Alumni')) == 24

    save_to_md(df)
    assert os.path.exists('summary_statistics.md')

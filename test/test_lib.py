from src.lib import get_data, get_max_val, get_min_val, get_std, get_summary, create_histogram, create_scatter_plot, correlation_matrix
import os
import pandas as pd

remote_path = 'https://raw.githubusercontent.com/Cavidan-oss/Javidan_Individual_Project_1/refs/heads/main/data/shanghai_ranking_2024.csv'

def test_df():
    df = get_data(remote_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 1000
    assert df.shape[1] == 9
    

def test_func():
    df = get_data(remote_path)

    assert get_max_val(df, 'Award') == 100.0
    assert int(get_std(df, 'Award')) == 11
    assert get_min_val(df, "Hici") == 0
    

def test_visualization():
    df = get_data(remote_path)

    create_histogram(df, 'Award', img_save_path='data/test_histogram.png')
    assert os.path.exists('data/test_histogram.png')
    os.remove('data/test_histogram.png')

    create_scatter_plot(df, x_col='Award', y_col='Alumni', img_save_path='data/test_scatter.png')
    assert os.path.exists('data/test_scatter.png')
    os.remove('data/test_scatter.png')

    correlation_matrix(df, img_save_path='data/test_correlation.png')
    assert os.path.exists('data/test_correlation.png')
    os.remove('data/test_correlation.png')





import pandas as pd
from lib import get_data, get_max_val, get_min_val, get_std, get_summary, create_histogram, create_scatter_plot, correlation_matrix


remote_path = 'https://raw.githubusercontent.com/Cavidan-oss/Javidan_Individual_Project_1/refs/heads/main/data/shanghai_ranking_2024.csv'






def save_to_md(data):
    """save summary report to markdown"""
    describe_df = get_summary(data)
    markdown_table1 = describe_df.to_markdown()
    # Write the markdown table to a file
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](data/histogram.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz2](data/scatter_plot.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz3](data/correlation_matrix.png)\n")



if __name__ == '__main__':
    df = pd.read_csv(remote_path)
    

    top_50_df = df.iloc[: 50 , :]
    create_histogram(top_50_df, column='PCP', img_save_path='data/histogram.png')
    create_scatter_plot(top_50_df, x_col='PUB', y_col="Award", img_save_path='data/scatter_plot.png')

    correlation_matrix(top_50_df, img_save_path='data/correlation_matrix.png')

    save_to_md(df)
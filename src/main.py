import pandas as pd

try:
    from src.lib import (
        get_summary,
        create_histogram,
        create_scatter_plot,
        correlation_matrix,
    )
except Exception:
    from lib import (
        get_summary,
        create_histogram,
        create_scatter_plot,
        correlation_matrix,
    )

remote_path = "https://raw.githubusercontent.com/Cavidan-oss/Javidan_Individual_Project_1/refs/heads/main/data/shanghai_ranking_2024.csv"


def calculate_iqr(df, column):
    """
    Calculate the Interquartile Range (IQR) of a given column in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    column (str): The name of the column for which to calculate the IQR.

    Returns:
    float: The calculated IQR of the column.
    """
    # Get the first quartile (25th percentile)
    Q1 = df[column].quantile(0.25)

    # Get the third quartile (75th percentile)
    Q3 = df[column].quantile(0.75)

    # Calculate the IQR
    IQR = Q3 - Q1

    return IQR


def save_to_md(data):
    """save summary report to markdown"""
    describe_df = get_summary(data)
    markdown_table1 = describe_df.to_markdown()
    # Write the markdown table to a file
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![alt_text_hist](data/histogram.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![alt_text_scatter_plot](data/scatter_plot.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![alt_text_correlation_matrix](data/correlation_matrix.png)\n")


if __name__ == "__main__":
    df = pd.read_csv(remote_path)

    top_50_df = df.iloc[:50, :]
    create_histogram(top_50_df, column="PCP", img_save_path="data/histogram.png")
    create_scatter_plot(
        top_50_df, x_col="PUB", y_col="Award", img_save_path="data/scatter_plot.png"
    )

    correlation_matrix(top_50_df, img_save_path="data/correlation_matrix.png")

    save_to_md(df)

    print(calculate_iqr(top_50_df, column="Alumni"))  # 24.500000000000007ßß

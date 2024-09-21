import pandas as pd
import matplotlib.pyplot as plt



def get_data(path):
    """
    Read and return the dataframe from given path
    """
    df = pd.read_csv(path)
    return df

def get_max_val(df, col):
    """
    Get maximum value of the given column
    """
    return df[col].max()

def get_min_val(df, col):
    """
    Get minumum value of the given column
    """
    return df[col].min()

def get_std(df, val):
    """
    Get standard deviation value of the given column
    """
    return df[val].std()

def get_summary(df):

    return df.describe()


def create_histogram( dataframe, column, img_save_path = None ):
    values = dataframe[column].to_numpy()
    # Plotting the histogram using Matplotlib
    plt.hist(values, bins=10, edgecolor='black')
    plt.title('Histogram of Values')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(img_save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

    return plt

def create_scatter_plot(dataframe, x_col, y_col, img_save_path = None ):
    
    x_val = dataframe[x_col].to_numpy()
    y_val = dataframe[y_col].to_numpy()
    plt.scatter(x_val, y_val, color='blue', marker='o')

    # Add titles and labels
    plt.title('Scatter Plot of X vs Y')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.grid(True)
    # Save the scatter plot to a file
    plt.savefig(img_save_path, dpi=300, bbox_inches='tight')  # Save as a PNG file
    plt.show()
    # Optional: Clear the figure after saving
    plt.close()

    return plt




def correlation_matrix(df, img_save_path):
    df = df.select_dtypes(float)
    plt.figure(figsize=(14,10))
    plt.matshow(df.corr(), cmap='coolwarm',)
    plt.title('Correlation Matrix', pad=20)
    plt.colorbar()
    plt.savefig(img_save_path)
    plt.show()


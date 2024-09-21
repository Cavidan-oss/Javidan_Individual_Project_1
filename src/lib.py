import pandas as pd
import matplotlib.pyplot as plt






def correlation_matrix(df):
    df = df.select_dtypes(float)
    plt.figure(figsize=(14,10))
    plt.matshow(df.corr(), cmap='coolwarm',)
    plt.title('Correlation Matrix', pad=20)
    plt.colorbar()
    plt.savefig('correlation_matrix.png')
    plt.show()
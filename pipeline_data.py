import pandas as pd

def compute_median_mean_diff(df):
    mean = df.mean()
    median = df.median()
    diff = mean - median
    result = pd.DataFrame({'Mean': mean, 'Median': median, 'Difference': diff})
    return result
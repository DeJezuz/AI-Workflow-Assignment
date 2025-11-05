"""
Data processing pipeline (example). Replace paths and data loading with your dataset.
"""
import pandas as pd
import numpy as np

def load_data(path):
    # Placeholder loader
    return pd.read_csv(path)

def preprocess(df):
    # Example preprocessing steps
    # 1) Impute numeric columns with median
    num_cols = df.select_dtypes(include=['float64','int64']).columns.tolist()
    for c in num_cols:
        df[c+'_missing'] = df[c].isna().astype(int)
        df[c].fillna(df[c].median(), inplace=True)

    # 2) Simple feature: length of stay (if timestamps available)
    if 'discharge_ts' in df.columns and 'admission_ts' in df.columns:
        df['los_days'] = (pd.to_datetime(df['discharge_ts']) - pd.to_datetime(df['admission_ts'])).dt.total_seconds() / (3600*24)
        df['los_days'].fillna(df['los_days'].median(), inplace=True)

    # 3) Encode categorical with simple mapping (placeholder)
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    for c in cat_cols:
        df[c] = df[c].fillna('unknown')
        df[c+'_enc'] = df[c].astype('category').cat.codes

    return df

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='data/sample.csv')
    parser.add_argument('--output', type=str, default='data/processed.csv')
    args = parser.parse_args()

    if os.path.exists(args.input):
        df = load_data(args.input)
        df2 = preprocess(df)
        df2.to_csv(args.output, index=False)
        print('Processed data saved to', args.output)
    else:
        print('Input file not found; update --input to point to your dataset')

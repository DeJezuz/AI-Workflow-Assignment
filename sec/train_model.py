"""
Train a LightGBM model (example). Ensure data is preprocessed and split appropriately.
"""
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def train(X_train, y_train, X_val, y_val):
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)
    params = {
        'objective': 'binary',
        'metric': 'auc',
        'learning_rate': 0.05,
        'num_leaves': 64,
        'lambda_l2': 1.0,
        'verbose': -1
    }
    bst = lgb.train(params, train_data, num_boost_round=2000, valid_sets=[val_data], early_stopping_rounds=50)
    return bst

if __name__ == '__main__':
    import os
    data_path = 'data/processed.csv'
    if not os.path.exists(data_path):
        print('Processed data not found. Run data_processing first or update paths.')
    else:
        df = pd.read_csv(data_path)
        y = df['readmitted_30d']
        X = df.drop(columns=['readmitted_30d','patient_id','admission_id'], errors='ignore')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, shuffle=False)
        model = train(X_tr, y_tr, X_val, y_val)
        preds = model.predict(X_test)
        print('Test AUROC:', roc_auc_score(y_test, preds))
        model.save_model('model.txt')

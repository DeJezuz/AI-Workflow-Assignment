"""
Evaluation utilities: confusion matrix and metrics
"""
import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, roc_auc_score

def print_confusion(y_true, y_pred_prob, threshold=0.5):
    y_pred = (y_pred_prob >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_pred_prob)
    print(f'TP={tp}, FP={fp}, FN={fn}, TN={tn}')
    print(f'Precision={prec:.3f}, Recall={rec:.3f}, AUROC={auc:.3f}')

if __name__ == '__main__':
    print('Import this module and use print_confusion in your evaluation pipeline')

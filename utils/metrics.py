# -*- coding: utf-8 -*-
import numpy as np
from sklearn import metrics

def calculate_auroc(predictions, labels):
    fpr_list, tpr_list, threshold_list = metrics.roc_curve(y_true=labels, y_score=predictions)
    auroc = metrics.auc(fpr_list, tpr_list)
    return fpr_list, tpr_list, auroc

def calculate_aupr(predictions, labels):
    precision_list, recall_list, threshold_list = metrics.precision_recall_curve(y_true=labels, probas_pred=predictions)
    aupr = metrics.auc(recall_list, precision_list)
    return precision_list, recall_list, aupr
# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt

def plot_loss_curve(train_loss, val_loss, file_path):
    """
    Plot the loss curve to monitor the fitting status.
    :param train_loss: (None)
    :param val_loss: same as train loss.
    :return: None
    """
    plt.figure()
    plt.plot(train_loss, lw=1, label = 'Train Loss')
    plt.plot(val_loss, lw=1, label = 'Valid Loss')
    plt.title("Model Loss")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.legend(loc="upper right")
    plt.savefig(file_path)


def plot_roc_curve(fpr_list, tpr_list, file_path):
    """
    Plot the roc curve of 919 binary classification tasks. (DNase: 125 TFBinding: 690 Histone_Mark: 104)
    :param fpr_list: (919, None)
    :param tpr_list: (919, None)
    :param file_path: destination file path.
    :return: None
    """
    plt.figure()
    for i in range(0, 125):
        plt.plot(fpr_list[i], tpr_list[i], lw=0.2, linestyle='-')
    plt.plot([0, 1], [0, 1], color='navy', lw=0.2, linestyle='-')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(u"DNase I-hypersensitive sites (ROC)")
    plt.savefig(os.path.join(file_path, 'ROC_Curve_DNase.jpg'))

    plt.figure()
    for i in range(125, 815):
        plt.plot(fpr_list[i], tpr_list[i], lw=0.2, linestyle='-')
    plt.plot([0, 1], [0, 1], color='navy', lw=0.2, linestyle='-')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(u"Transcription factors (ROC)")
    plt.savefig(os.path.join(file_path, 'ROC_Curve_TF.jpg'))

    plt.figure()
    for i in range(815, 919):
        plt.plot(fpr_list[i], tpr_list[i], lw=0.2, linestyle='-')
    plt.plot([0, 1], [0, 1], color='navy', lw=0.2, linestyle='-')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(u"Histone marks (ROC)")
    plt.savefig(os.path.join(file_path, 'ROC_Curve_HistoneMark.jpg'))


def plot_pr_curve(precision_list, recall_list, file_path):
    """
    Plot the pr curve of 919 binary classification tasks. (DNase: 125 TFBinding: 690 Histone_Mark: 104)
    :param precision_list: (919, None)
    :param recall_list: (919, None)
    :param file_path: destination file path.
    :return: None.
    """
    plt.figure()
    for i in range(0, 125):
        plt.plot(precision_list[i], recall_list[i], lw=0.2, linestyle='-')
    plt.plot([0, 1], [0, 1], color='navy', lw=0.2, linestyle='-')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(u"DNase I-hypersensitive sites (PR)")
    plt.savefig(os.path.join(file_path, 'PR_Curve_DNase.jpg'))

    plt.figure()
    for i in range(125, 815):
        plt.plot(recall_list[i], precision_list[i], lw=0.2, linestyle='-')
    plt.plot([0, 1], [0, 1], color='navy', lw=0.2, linestyle='-')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(u"Transcription factors (PR)")
    plt.savefig(os.path.join(file_path, 'PR_Curve_TFBinding.jpg'))

    plt.figure()
    for i in range(815, 919):
        plt.plot(precision_list[i], recall_list[i], lw=0.2, linestyle='-')
    plt.plot([0, 1], [0, 1], color='navy', lw=0.2, linestyle='-')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(u"Histone marks (PR)")
    plt.savefig(os.path.join(file_path, 'PR_Curve_HistoneMark.jpg'))
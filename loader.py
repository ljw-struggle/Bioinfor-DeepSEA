# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import scipy.io as sio

def parse_function(example_proto):
    dics = {
        'x': tf.io.FixedLenFeature([1000, 4], tf.int64),
        'y': tf.io.FixedLenFeature([919], tf.int64),
    }
    parsed_example = tf.io.parse_single_example(example_proto, dics)
    x = tf.reshape(parsed_example['x'], [1000, 4])
    y = tf.reshape(parsed_example['y'], [919])
    x = tf.cast(x, tf.float32)
    y = tf.cast(y, tf.int32)
    return (x, y)

def get_train_data(batch_size):
    filenames = ['./data/traindata-00.tfrecord', './data/traindata-01.tfrecord',
                 './data/traindata-02.tfrecord', './data/traindata-03.tfrecord']
    dataset = tf.data.TFRecordDataset(filenames, buffer_size=100000, num_parallel_reads=4)
    dataset = dataset.shuffle(buffer_size=10000)
    dataset = dataset.map(map_func=parse_function, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    dataset = dataset.batch(batch_size, drop_remainder=False)
    dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    dataset = dataset.repeat()
    return dataset # 4400000/64 = 68750

def get_valid_data():
    data = sio.loadmat('./data/valid.mat')
    x = data['validxdata']  # shape = (8000, 4, 1000)
    y = data['validdata']  # shape = (8000, 919)
    x = np.transpose(x, (0, 2, 1)).astype(dtype=np.float32)  # shape = (8000, 1000, 4)
    y = np.transpose(y, (0, 1)).astype(dtype=np.int32)  # shape = (8000, 919)
    return (x, y)

def get_test_data():
    filename = './data/test.mat'
    data = sio.loadmat(filename)
    x = data['testxdata']  # shape = (455024, 4, 1000)
    y = data['testdata']  # shape = (455024, 919)
    x = np.transpose(x, (0, 2, 1)).astype(np.float32)  # shape = (455024, 1000, 4)
    y = np.transpose(y, (0, 1)).astype(np.float32)  # shape = (455024, 919)
    return (x, y)
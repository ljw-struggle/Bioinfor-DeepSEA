# Bioinfor DeepSEA （Implemented by TF-2.0）

This is implemented by tensorflow-2.0 again.


## REQUIREMENT
We run the code on Ubuntu 18.04 LTS with a GTX 1080ti GPU.

### Required
- [Python] (<https://www.python.org>) (3.7.3). 
The easiest way to install Python and all of the necessary dependencies is to download and install [Anaconda] 
(<https://repo.anaconda.com/archive/>)
- [Tensorflow] (<https://tensorflow.google.cn/install>) (2.0.0-beta1).

### Optional
- [CUDA] (<https://developer.nvidia.com/cuda-toolkit-archive>) (10.0)
- [cuDNN] (<https://developer.nvidia.com/cudnn>) (7.4.1)

## USAGE

### Data
You need to first download the training, validation, and testing sets from DeepSEA. You can download the datasets from 
[here] (<http://deepsea.princeton.edu/media/code/deepsea_train_bundle.v0.9.tar.gz>). After you have extracted the 
contents of the tar.gz file, move the 3 .mat files into the data/ folder. 

### Model
The model that trained by myself is available in BAIDU Net Disk [here] (https://pan.baidu.com/s/1tfYvDoO6Xvt7v7y70nDsXg)


### Preprocess
Because of my RAM limited, I firstly transform the train.mat file to .tfrecord files.
```
python preprocess.py
```

### Training

Then you can train the model initially.
```
CUDA_VISIBLE_DEVICES=0 python main.py -e train
```

### Test

When you have trained successfully, you can evaluate the model.
```
CUDA_VISIBLE_DEVICES=0 python main.py -e test
```

## REFERENCE
> [DeepSEA] (<https://www.nature.com/articles/nmeth.3547>)(<https://github.com/jisraeli/DeepSEA>)
import os
import cv2
import random
import numpy as np
import torch
from shutil import copyfile
from src.edge_connect import EdgeConnect
from configure import load_config

def inpainter(mode=2):
    config = load_config(mode)

    # cuda visble devices
    os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(str(e) for e in config.GPU)

    # init device
    if torch.cuda.is_available():
        config.DEVICE = torch.device("cuda")
        torch.backends.cudnn.benchmark = True 
        print('gpu')  # cudnn auto-tuner
    else:
        config.DEVICE = torch.device("cpu")
        print('cpu')

    # set cv2 running threads to 1 (prevents deadlocks with pytorch dataloader)
    cv2.setNumThreads(0)

    # initialize random seed
    torch.manual_seed(config.SEED)
    torch.cuda.manual_seed_all(config.SEED)
    np.random.seed(config.SEED)
    random.seed(config.SEED)

    # build the model and initialize
    model = EdgeConnect(config)
    model.load()

    if config.MODE == 2:
        print('\nstart testing...\n')
        model.test()
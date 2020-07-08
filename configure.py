import os
import cv2
import random
import numpy as np
import torch
import argparse
from src.config import Config

def load_config(mode=2):
    config_path = os.path.join('./psv','config.yml')

    # load config file
    config = Config(config_path)

    # test mode
    if mode == 2:
        config.MODE = 2
        config.MODEL = 3
        config.INPUT_SIZE = 0

        #if args.input is not None:
        config.TEST_FLIST = './Images'

        #if args.mask is not None:
        config.TEST_MASK_FLIST = './Masks'

        #if args.output is not None:
        config.RESULTS = './results'

    return config

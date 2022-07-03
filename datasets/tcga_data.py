import random
import torch
import pandas as pd
from pathlib import Path
import argparse
import openslide
import sys
import os
sys.path.append("D:/Workspace/FanNet/TransMIL-main")
# os.chdir(os.path.dirname(__file__))
# os.chdir('D:/Workspace/FanNet/TransMIL-main')
import torch.utils.data as data
from torch.utils.data import dataloader

# from util.utils import *  # 放到根目录里面才能import


def makeparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage',default='train', type=str, help="stage:train valid test")
    parser.add_argument('--config',default='./Camelyon/FanNet.yaml', type=str)
    parser.add_argument('--csv_dir',default='./dataset_csv/fold0.csv',type=str)
    args = parser.parse_args()
    return args


class TcgaData(data.Dataset):
    def __init__(self, dataset_cfg=None,
                 state=None):
        # Set all input args as attributes
        print(locals())
        self.__dict__.update(locals()) ## self.'key' = dict['key'] 简化传入参数过程
                                       ## locals() 返回当前作用域的全部局部变量的字典
        self.dataset_cfg = dataset_cfg

        #---->data and label
        self.nfolds = self.dataset_cfg.nfold
        self.fold = self.dataset_cfg.fold
        self.feature_dir = self.dataset_cfg.data_dir
        self.csv_dir = self.dataset_cfg.label_dir + f'fold{self.fold}.csv'
        self.slide_data = pd.read_csv(self.csv_dir)
        #---->order
        self.shuffle = self.dataset_cfg.data_shuffle

        #---->split dataset
        if state == 'train':
            self.data = self.slide_data.loc[:, 'pid'].dropna()
            self.label = self.slide_data.loc[:, 'train_label'].dropna()
        # if state == 'val':
        #     self.data = self.slide_data.loc[:, 'val'].dropna()
        #     self.label = self.slide_data.loc[:, 'val_label'].dropna()
        # if state == 'test':
        #     self.data = self.slide_data.loc[:, 'test'].dropna()
        #     self.label = self.slide_data.loc[:, 'test_label'].dropna()


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        slide_name = self.data[idx]
        print(slide_name)
        label = int(self.label[idx])
        # full_path = Path(self.feature_dir) / f'{slide_id}.pt'
        # features = torch.load(full_path)
        slide_path = os.path.join(self.feature_dir,f'{slide_name}')
        slide = openslide.open_slide(slide_path)
        # ----> shuffle
        if self.shuffle == True:
            index = [x for x in range(features.shape[0])]
            random.shuffle(index)
            features = features[index]


        return slide, label

if __name__ == "__main__":
    args = makeparse()
    cfg = read_yaml(args.config)
    dataset_cfg = cfg.Data
    # print(dataset_cfg)
    dataset = TcgaData(dataset_cfg, state=cfg.General.server)
    print(dataset[1])

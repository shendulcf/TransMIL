import os 
import pandas as pd


def calss2_datacsv_gen(path):
 
    name_list = []
    label_list = []

    label = os.listdir(path)
    for i,label in enumerate(label):
        path_label = os.path.join(path, label)
        path_wsi = os.listdir(path_label)
        for j,name in enumerate(path_wsi):
            name_list.append(name)
            label_list.append(label)

    print(name_list)
    print(label_list)

    dataframe = pd.DataFrame({'pid':name_list,'label':label_list})
    dataframe.to_csv('train.csv',index=False,sep=',')

path = r'E:\workspace\Practice\TCGA/'

if __name__ == '__main__':

    calss2_datacsv_gen(path)

from torch.utils.data import DataLoader
from datasets.tcga_data import TcgaData_Patch,args_gen
from PIL import Image
import cv2


# img_path = r'D:\Workspace\Project\TransMIL\data\Patches\BLOCKS\TCGA-A6-2671-11A-01-TS1\TCGA-A6-2671-11A-01-TS1_(2540,9144).jpg'
# img = Image.open(img_path)
# print(img.size)
args = args_gen()
dataset = TcgaData_Patch(args)

dataloader = DataLoader(dataset)


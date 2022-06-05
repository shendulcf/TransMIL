import torch
import torchvision
import torchsummary
import torch.nn as nn
from model import View

resnet50 = torchvision.models.resnet50(pretrained=False)
pth_dir = r'models\resnet50-0676ba61.pth'
resnet50.load_state_dict(torch.load(pth_dir))
# model1 = torch.load(pth_dir)
# print(model1)

modules = list(resnet50.children())[:-3]
print(modules)
model = nn.Sequential(
            *modules,
            nn.AdaptiveAvgPool2d(1),
            View((-1,1024)),
            nn.Linear(1024,512)
        )

torchsummary.summary(model,(3,256,256))

# # pretrained=True就可以使用预训练的模型
# net = models.squeezenet1_1(pretrained=False)
# pthfile = r'E:\anaconda\app\envs\luo\Lib\site-packages\torchvision\models\squeezenet1_1.pth'
# net.load_state_dict(torch.load(pthfile))
# print(net)
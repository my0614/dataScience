import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init

inputs = torch.Tensor(1, 1, 28, 28)
print('텐서의 크기 : {}'.format(inputs.shape))
conv1 = nn.Conv2d(1, 32, 3, padding=1)
print(conv1)
conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
print(conv2)
pool = nn.MaxPool2d(2)
print(pool)
out = conv1(inputs)
print(out.shape)
out = pool(out)
print(out.shape)
out = conv2(out)
print(out.shape)
out = pool(out)
print(out.shape)
# 첫번째 차원인 배치 차원은 그대로 두고 나머지는 펼쳐라
out = out.view(out.size(0), -1) 
print(out.shape)
fc = nn.Linear(3136, 10) # input_dim = 3,136, output_dim = 10
out = fc(out)
print(out.shape)

# -*- coding: utf-8 -*-
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', as_frame=False)

print(mnist.keys()) #data와 target만 사용

x, y = mnist.data, mnist.target
print(x)
print(x.shape) # 28x28개의 픽셀 특징을 가진 이미지 70,000개
print(y)
print(y.shape)

import matplotlib.pyplot as plt

def plot_digit(image_data):
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap="binary")
    plt.axis("off")
    
some_digit = x[0]
plot_digit(some_digit)

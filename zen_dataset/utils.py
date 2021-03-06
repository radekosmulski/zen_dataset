import torch
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import PIL

def paths_to_files_in(dir):
    paths = []
    for path in Path(dir).iterdir():
        if path.is_dir():
            paths += paths_to_files_in(path)
        else:
            paths.append(path)
    return paths

def open_image(path): return PIL.Image.open(path).convert('RGB')

def image2ary(image): return np.asarray(image)

def ary2tensor(ary, dtype=np.float32): return torch.from_numpy(ary.astype(dtype, copy=False))

def image2tensor(image, augment_fn=None):
    ary = image2ary(image)
    if augment_fn: ary = augment_fn(ary)
    ary = ary.transpose(2, 0, 1)
    tensor = ary2tensor(ary)
    return tensor.div_(255)

imagenet_stats = ([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
mean, std = torch.from_numpy(np.array(imagenet_stats).astype(np.float32))

def imagenet_normalize(tensor):
    zero_centered = tensor - mean[:, None, None]
    return zero_centered / std[:, None, None]

def imagenet_denormalize(zero_centered):
    zero_centered = zero_centered * std[:, None, None]
    return zero_centered + mean[:, None, None]

def plot(tensor):
    ary = tensor.numpy()
    plt.imshow(ary.transpose(1,2,0))

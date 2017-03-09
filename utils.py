from matplotlib.pyplot import imshow
from io import BytesIO
from IPython import display 
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np

def plot(img, scale=1, dpi=80):
    plt.figure(figsize=(img.shape[0]*scale/dpi, img.shape[1]*scale/dpi), dpi=dpi)
    imshow(img)
    
# Prepare a tensor to be displayed as image
def normalize(x):
    x = x.copy().astype(float)
    # normalize tensor: center on 0., ensure std is 0.1
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1

    # clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)

    # convert to RGB array
    x *= 255
    return x.astype('uint8')

def show(a, fmt='jpeg'):
    f = BytesIO()
    PIL.Image.fromarray(a.astype('uint8')).save(f, fmt)
    img = display.Image(data=f.getvalue())
    display.display(img)

def resize_array(array, size):
    '''Resizes an image (formatted as np array) to give size.
    Args:
        array: np array representing the image.
        size: The desired size.
    Returns: The resized image as a float np array.
    '''
    image = PIL.Image.fromarray(array.astype('uint8').copy())
    image_resized = image.resize(size, PIL.Image.ANTIALIAS)
    return np.asarray(image_resized).astype(float)    
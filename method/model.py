import json
import os
import cv2 as cv
import numpy as np
from PIL import Image
from google.colab.patches import cv2_imshow
import tensorflow as tf
from google.colab import drive
drive.mount('/content/drive')
from google.colab import files
image = files.upload()
label = files.upload()

from google.colab import drive
drive.mount('/content/drive')

import os
import argparse
import numpy as np
from scipy import misc
import scipy.io as sio
from warpgan import WarpGAN
from PIL import Image
import glob
image_list = []

# Parse aguements
parser = argparse.ArgumentParser()
parser.add_argument("model_dir", help="The path to the pretrained model",
                        type=str)
parser.add_argument("input", help="The path to the aligned image",
                        type=str)
parser.add_argument("output", help="The prefix path to the output file, subfix will be added for different styles.",
                        type=str, default=None)
parser.add_argument("--num_styles", help="The number of images to generate with different styles",
                        type=int, default=1)
parser.add_argument("--scale", help="The path to the input directory",
                        type=float, default=1.0)
parser.add_argument("--aligned", help="Set true if the input face is already normalized",
                        action='store_true')
args = parser.parse_args()


if __name__ == '__main__':

    network = WarpGAN()
    network.load_model(args.model_dir)

    with open("file.txt") as file_in:
      lines = []
      for line in file_in:
          lines.append(line) = f.readlines()


    #imgs = []
    #path = "data/testdata"
    #for im in lines:
    #  imgs.append(Image.open(os.path.join(path,im)))










  n = 0

    for im in lines:
      if n == 20:
        break

      img = misc.imread(im, mode='RGB')
      #img = misc.imread(args.input, mode='RGB')


      if not args.aligned:
          from align.detect_align import detect_align
          img = detect_align(img)

      img = (img - 127.5) / 128.0

      images = np.tile(img[None], [args.num_styles, 1, 1, 1])
      scales = args.scale * np.ones((1))
      #styles = np.random.normal(0., 1., (args.num_styles, network.input_style.shape[1]))

      output = network.generate_BA(images, scales, 16)
      output = 0.5*output + 0.5

      for i in range(args.num_styles):
          print("New image is saved")
          misc.imsave(args.output + '_{}.jpg'.format(i), output[i])



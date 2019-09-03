# Compress images
# https://help.clarifai.com/en/articles/2733027-how-to-compress-image-files-with-python

# start program in console:
# python Image_Compression.py --path=pics --max_size=256

# success:
# 699 pics from 96MB to 27MB (max_size=512) to 9MB (max_size=256)

from PIL import Image
import os, sys
import argparse
from tqdm import tqdm


def resize_image(path, max_size):
  if path[-1] != '/':
    path = path + '/'

  dirs = os.listdir(path)
  for item in tqdm(dirs):
    if os.path.isfile(path+item):
      try:
        im = Image.open(path+item)
        if im.height > max_size or im.width > max_size:
          f,e = os.path.splitext(path+item)

          # if width > height:
          if im.width > im.height:
            desired_width = max_size
            desired_height = im.height / (im.width/max_size)
        
          # if height > width:
          elif im.height > im.width:
            desired_height = max_size
            desired_width = im.width / (im.height/max_size)
        
          else:
            desired_height = max_size
            desired_width = max_size
        
          # convert back to integer
          desired_height = int(desired_height)
          desired_width = int(desired_width)
        
          im_resized = im.resize((desired_width, desired_height))
          # im_resized.save(f + '_resized.jpg', 'JPEG', quality=90) # doesn't overwrite file
          im_resized.save(f + e, 'JPEG', quality=80) # does overwrite file
          # im_resized.save('resized_' + f + '.jpg', 'JPEG', quality=100)

      except:
        continue


def main():
  parser = argparse.ArgumentParser(
    description='given a folder path, resize all images inside')
  parser.add_argument(
    '--path',
    type=str,
    help='full path to the target folder')
  parser.add_argument(
    '--max_size',
    type=float,
    help='the largest size that you want an image to be (in pixels)')

  args = parser.parse_args()

  resize_image(args.path, args.max_size)


if __name__ == '__main__':
  main()
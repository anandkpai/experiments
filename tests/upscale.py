from super_image import ImageLoader, EdsrModel, DrlnModel, MsrnModel
from PIL import Image
from time import time
import os

# time this sucker 
start = time()
BASE_DIR = '/mnt/r/tmp/etc/scalers'
FILE_EXT = 'png'
SCALE=4


# chose model 
# model = MsrnModel.from_pretrained('eugenesiow/msrn', scale=2)
model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=4)
# model = DrlnModel.from_pretrained('eugenesiow/drln-bam', scale=4)


filename_without_extension = '00023-978161562'


image = Image.open(f"{BASE_DIR}/{filename_without_extension}.{FILE_EXT}")
inputs = ImageLoader.load_image(image)
preds = model(inputs)
ImageLoader.save_image(preds, f"{BASE_DIR}/{filename_without_extension}_scaled_{SCALE}x.{FILE_EXT}")
print(f'finished file {filename_without_extension} in {time()-start}')


from super_image import ImageLoader, EdsrModel, DrlnModel, MsrnModel
from PIL import Image
from time import time, sleep
import os

# time this sucker 
start = time()
BASE_DIR = '/mnt/r/tmp/etc/scalers'
FILE_EXT = 'png'
SCALE=2


# chose model 
# model = MsrnModel.from_pretrained('eugenesiow/msrn', scale=SCALE)
# model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=SCALE)
model = DrlnModel.from_pretrained('eugenesiow/drln-bam', scale=SCALE)


def filename_without_extension(x:str) -> str:
    return x.replace(f'.{FILE_EXT}','')


for f in map(filename_without_extension, os.listdir(BASE_DIR)):
    image = Image.open(f"{BASE_DIR}/{f}.{FILE_EXT}")
    inputs = ImageLoader.load_image(image)
    print(f'trying {f}')
    try : 
        preds = model(inputs)
        ImageLoader.save_image(preds, f"{BASE_DIR}/{f}_scaled_{SCALE}x.{FILE_EXT}")
        print(f'finished file {f} in {time()-start}')
        sleep(8)
    except : 
        print(f'{f} did not succeed')
        sleep(20)

    



print(f'finished all in {time()-start}')
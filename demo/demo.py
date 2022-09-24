import rasterio
from random import randint

def distort_image(source_path, target_path):
    with rasterio.open(source_path) as src:
        r = src.read()
        transform = src.transform
        xTranslation = randint(-5000000, 5000000)
        yTranslation = randint(-5000000, 5000000)
        transform2 = rasterio.Affine(transform[0],transform[1], xTranslation, transform[3], transform[4], yTranslation)
        
        new_dataset = rasterio.open(target_path,'w',driver= src.driver, height=src.shape[0],
            width=src.shape[1],
            count=src.count,
            dtype=src.dtypes[0],
            #nodata=255,
            crs=src.crs,
            transform=transform2,)

        new_dataset.write(r)
        new_dataset.close()


distort_image('images/mision79_linea2_1415_180801_151628_rgbnn00l2.img', 'images/newImg.img')
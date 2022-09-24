import rasterio
from rasterio.windows import Window
from random import randint
import pathlib
from osgeo import gdal

def distort_image(source_path:str, target_path: str, x_axis_range: int, y_axis_range: int):
    ''' 
    Este método cambia las coordenadas de la imagen aplicando operaciones de traslación sobre 
    la matriz de transformación de la imagen fuente y guarda la nueva en la ruta objetivo.

            Parámetros:
            ----------
                    source_path (str): ruta a la imagen fuente
                
                    target_path (str): ruta a la imagen destino

                    x_axis_range (int): Entero que representa el rango para generar un númeor aleatorio
                                        para traslación en el eje x
                    
                    y_axis_range (int): Entero que representa el rango para generar un númeor aleatorio
                                        para traslación en el eje y

            Returns:
            --------
                    None (None): None
    
    '''

    # Open source image
    with rasterio.open(source_path) as src:
        # Extract source image's transformation matrix
        sourceTransform = src.transform
        print(src.meta)
        # Create new values for translations in x and y axis
        xTranslation = sourceTransform[2] + randint(-x_axis_range, x_axis_range)
        yTranslation = sourceTransform[5] + randint(-y_axis_range, y_axis_range)

        # Create the new transformation matrix based on the original with the translations applied
        targetTransform = rasterio.Affine(sourceTransform[0],sourceTransform[1], xTranslation, 
                                        sourceTransform[3], sourceTransform[4], yTranslation)
        
        # Open new file based on the target path
        new_dataset = rasterio.open(target_path,'w',driver= src.driver, height=src.shape[0],
            width=src.shape[1],
            count=src.count,
            dtype=src.dtypes[0],
            crs = src.crs,
            transform = targetTransform,)

        # Here we read and save the original file by chunks or blocks, so we define block's width and height 
        # as well as the initial offsets
        DefBlockWidth = 2000
        DefBlockHeight = 2000
        initialwidthBlocks = min(src.shape[1], DefBlockWidth)
        initialheightBlocks = min(src.shape[0], DefBlockHeight)
        
        offsetRow = 0
        heightBlocks = initialheightBlocks
        while(offsetRow < src.shape[0]):
            offsetCol = 0
            widthBlocks = initialwidthBlocks

            while(offsetCol < src.shape[1]):

                r = src.read(window=Window(offsetCol, offsetRow, widthBlocks, heightBlocks))
                new_dataset.write(r, window=Window(offsetCol, offsetRow, widthBlocks, heightBlocks))
                offsetCol += widthBlocks

                if((offsetCol + DefBlockWidth) > src.shape[1]):
                    widthBlocks = min(DefBlockWidth, src.shape[1]-offsetCol)

            offsetRow += heightBlocks

            if(offsetRow + DefBlockHeight > src.shape[0]):
                heightBlocks = min(DefBlockHeight, src.shape[0]-offsetRow)
        
        # Close new file
        new_dataset.close()
    
    

def compress_image_loss(path_in: str, path_out: str):
    '''
    Función que permite comprimir un archivo en formatos loss, esto quiere decir con pérdida de información,
    para formatos TIF e IMG

            Parámetros:
            ----------
                    path_in (str): ruta a la imagen fuente
                
                    path_out (str): rute a la imagen objetivo 

            Retorno:
            --------
                    None (None): None
    '''
    gdal.Translate( path_out, path_in, creationOptions=["COMPRESS=LZW", "TILED=YES", "DISCARD_LSB=10"])  
        
        

    
def compress_image_lossless(path_in: str, path_out: str):
    '''
    Función que permite comprimir un archivo en formatos lossless, esto quiere decir con la menor 
    pérdida de información posible, para formatos TIF e IMG

            Parámetros:
            ----------
                    path_in (str): ruta a la imagen fuente
                
                    path_out (str): rute a la imagen objetivo 

            Retorno:
            --------
                    None (None): None

    '''
    gdal.Translate( path_out, path_in, creationOptions=["COMPRESS=ZSTD", "ZSTD_LEVEL=22"])
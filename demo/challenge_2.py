
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient # también en ASINC

## metodo de compresion para archivos .tif
def compress_tif(path_in, path_out, file_out_name):
    gdal.Translate( path_out, path_in, creationOptions=["COMPRESS=LZW", "TILED=YES", "DISCARD_LSB=10"])
    connection_string = "DefaultEndpointsProtocol=https;AccountName=codefest;AccountKey=eOU8IsIAXLg5QTkE2nuxnF3WqXLCATvn1zrWelBq8KJeiWaAqFtYbgAzXKDfla3YkI/qia3wXwhX+AStAFt2yQ=="
    blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="containercodefest", blob_name =  file_out_name)
    with open(path_out, "rb") as data:
        blob.upload_blob(data)
    
compress_tif('./prueba/recorte_converted.tif','./prueba/recorte_converted_2.0.tif','recorte_converted_2.0.tif')

## metodo de comprension para archivos .img

def compress_img(path_in, path_out, file_out_name):
    gdal.Translate( path_out, path_in, creationOptions=["COMPRESS=ZSTD", "ZSTD_LEVEL=22"])
    connection_string = "DefaultEndpointsProtocol=https;AccountName=codefest;AccountKey=eOU8IsIAXLg5QTkE2nuxnF3WqXLCATvn1zrWelBq8KJeiWaAqFtYbgAzXKDfla3YkI/qia3wXwhX+AStAFt2yQ=="
    blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="containercodefest", blob_name =  file_out_name)
    with open(path_out, "rb") as data:
        blob.upload_blob(data)  
blob2 = BlobClient.from_connection_string(conn_str=connection_string, container_name="containercodefest", blob_name = file_out_name+'ige')
    with open("./prueba/recorte_img_.ige", "rb") as data:
    blob2.upload_blob(data)
    
compress_tif('/dbfs/mnt/blobstorage/type2/img/recorte_mision79_linea2_.img','./prueba/recorte_img_.img','recorte_img_.img')



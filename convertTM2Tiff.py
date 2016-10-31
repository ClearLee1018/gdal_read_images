import os
import numpy as np
import math
from PIL import Image
from osgeo import gdal
import struct
import cv2
import scipy.misc as sm

def convertTM2Tiff(img_name):
    print img_name
    index = img_name.rfind('.')
    save_name = img_name[0:index] + '_change.tif'
    print save_name
    img_dataset = gdal.Open(img_name)
    img_array=img_dataset.ReadAsArray()
    [img_channels,img_height,img_width]=img_array.shape
#    img_height = img_dataset.RasterYSize
#    img_width = img_dataset.RasterXSize
#    img_channels = img_dataset.RasterCount
    print 'img_channels: ', img_channels,'; img_height:',img_height,'; img_width:',img_width    
    savefile_driver = gdal.GetDriverByName('GTiff')
    savedata = savefile_driver.Create(save_name,img_width,img_height,img_channels,gdal.GDT_UInt16)
    for i in range(img_channels):
        savedata.GetRasterBand(i+1).WriteArray(img_array[i,:,:])

if __name__ == "__main__":
    #img_name = '/data/data_cooperation/data_changeDet_forest/7_TM_change/input/2007_part.tif'
    img_name = '/data/data_cooperation/environment_data/licong/train_new/GF1_PMS1_E35.1_N16.3_20150710_L1A0000910283-MSS1_c_sample1/GF1_PMS1_E35.1_N16.3_20150710_L1A0000910283-MSS1.tiff'
    convertTM2Tiff(img_name)

import os
import numpy as np
import math
from PIL import Image
from osgeo import gdal
import struct
import cv2
import scipy.misc as sm

def cropimage(image_name,savepath,crop_size=4000,stride=3800):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    imagename = '/data/data_cooperation/data_GF2road/GF2_PMS1_E113.5_N38.3_20150804_L1A0000959938/fuse/GF2_PMS1_E113.5_N38.3_20150804_L1A0000959938-PAN1_fuse.img'
    index1 = imagename.rfind('/')
    index2 = imagename.rfind('.')
    purename = imagename[index1+1:index2]
    print purename
    
    imgDataset = gdal.Open(imagename)
    img_height = imgDataset.RasterYSize;
    img_width = imgDataset.RasterXSize;
    img_channels = imgDataset.RasterCount
    outimg= np.ones((crop_size,crop_size,3), dtype=np.uint16)
    outimg= outimg * np.iinfo(np.uint16).max
    
    h_num = int(math.ceil(1.0*(img_height-crop_size)/stride) + 1)
    w_num = int(math.ceil(1.0*(img_width-crop_size)/stride) + 1)
    
    for h in range(1,h_num-1):
        h_offset = min(h*crop_size,img_height -crop_size)
        for w in range(1,w_num-1):
            w_offset = min(w* crop_size,img_width - crop_size)
            for i in range(1,img_channels):
                band_data = imgDataset.GetRasterBand(i)
                scanline = band_data.ReadRaster( w_offset,h_offset, crop_size,crop_size,crop_size, crop_size, gdal.GDT_UInt16  )
                data_tmp = struct.unpack('H' * crop_size*crop_size, scanline)
                data_tmp = np.array(data_tmp,dtype=np.uint16)
                data_tmp = data_tmp.reshape(crop_size,crop_size)
                outimg[:,:,i-1] = data_tmp
            savename = savepath + '/' + purename + '_' + str(h+1) + '_' + str(w + 1) + '.jpg'
            print h_offset,w_offset,data_tmp.shape,savename
            sm.imsave(savename,outimg)

if __name__ == "__main__":
    
    image_name = '/data/data_cooperation/data_GF2road/GF2_PMS1_E113.5_N38.3_20150804_L1A0000959938/fuse/GF2_PMS1_E113.5_N38.3_20150804_L1A0000959938-PAN1_fuse.img'
    savepath = '/data/dataprocess_program/dataprocess_gf2_road/crop_image'
    crop_size = 4000 
    stride = 3800
    cropimage(image_name,savepath,crop_size,stride)

import convert2RGB
image_name = '/data/data_cooperation/data_GF2road/GF2_PMS1_E113.5_N38.3_20150804_L1A0000959938/fuse/GF2_PMS1_E113.5_N38.3_20150804_L1A0000959938-PAN1_fuse.img'
savepath = '/data/dataprocess_program/dataprocess_gf2_road/crop_image'
crop_size = 4000 
stride = 3800
convert2RGB.cropimage(image_name,savepath,crop_size,stride)

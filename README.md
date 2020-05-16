# Analyze_Intermediate_Images

## Overview
#### Step1 :
Create ensemble point clouds(.spbr) from one input point cloud
```
./analyzeIntermediateImages [input_file] [output_path]

Input repeat level (the default repeat level is 1) : 10
Num. of input points : 1122011
Repeat level         : 10
Num. of points in each ensemble : 112201

Shuffled.
 ensemble1.spbr done.
 ensemble2.spbr done.
 ensemble3.spbr done.
 ensemble4.spbr done.
 ensemble5.spbr done.
 ensemble6.spbr done.
 ensemble7.spbr done.
 ensemble8.spbr done.
 ensemble9.spbr done.
 ensemble10.spbr done.

File export of all ensembles is complete.
```

#### Step2 :
Automatically, snapshot all intermediate images by using `spbr_auto_snap`
```
python spbr_continuously.py [spbr_file_path] [spbr_header_file] [repeat_level]
```

#### Step3 :
Calculate variance(standard deviation) for each corresponding pixels
```
python calc_variance_for_each_pixel.py [input_images_path] [repeat_level] [image_resolution]
```

<br>

## Result
### Intermediate image (L=100)
|Coords Noise|Color Noise|
|:-:|:-:|
|![](doc/assets/coords_ensemble.bmp)|![](doc/assets/color_ensemble.bmp)|


### Original point cloud (L=1)
|Coords Noise|Color Noise|
|:-:|:-:|
|![](doc/assets/coords_LR1.bmp)|![](doc/assets/color_LR1.bmp)|

### Standard deviation image and histogram
|Coords Noise|Color Noise|
|:-:|:-:|
|![](doc/assets/coords_figure.png)|![](doc/assets/color_figure.png)|

### Transition of standard deviation when increasing repeat level
|Coords Noise|Color Noise|
|:-:|:-:|
|![](doc/assets/coords_SD_mean_max.png)|![](doc/assets/color_SD_mean_max.png)|

***

### 
|M_mean and M_max|M/L|
|:-:|:-:|
|![](doc/assets/M_mean_max.png)|![](doc/assets/ML.png)|
# Analyze_Intermediate_Images

## Overview
#### Step1 :
Create ensemble point clouds(.spbr) from one input point cloud
```
./analyzeIntermediateImages [input_file] [output_path]
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
|![](assets/coords_ensemble.bmp)|![](assets/color_ensemble.bmp)|


### Original point cloud (L=1)
|Coords Noise|Color Noise|
|:-:|:-:|
|![](assets/coords_LR1.bmp)|![](assets/color_LR1.bmp)|

### Standard deviation image and histogram
|Coords Noise|Color Noise|
|:-:|:-:|
|![](assets/coords_figure.png)|![](assets/color_figure.png)|

### Transition of standard deviation when increasing repeat level
|Coords Noise|Color Noise|
|:-:|:-:|
|![](assets/coords_SD_mean_max.png)|![](assets/color_SD_mean_max.png)|

***

### 
|M_mean and M_max|M/L|
|:-:|:-:|
|![](assets/M_mean_max.png)|![](assets/ML.png)|
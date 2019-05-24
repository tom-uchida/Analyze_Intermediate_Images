# Analyze_Intermediate_Images

## Overview
1. Create ensemble point clouds(.spbr) from one input point cloud
2. Snapshot all intermediate images automatically by using spbr_auto_snap
3. Calculate variance(or SD) for each corresponding pixel

### Usage
```
$ ./analyzeIntermediateImages [input_file] [output_path]
```

### Example
```
$ ./analyzeIntermediateImages input.ply OUTPUT_DATA/LR10/
```


## Intermediate image (L=100)
![L100](resources/L100_ensemble.bmp)


## Result
### Standard deviation image
<center>
<img src="resources/sd_image.png" width="500">
</center>

### Standard deviation histogram
<center>
<img src="resources/sd_histogram.png" width="500">
</center>
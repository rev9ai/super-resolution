# Super Resolution

This is the Super-Resolution ESRGAN model. This is the code ported from the following 2 repositories:
1. [ru-dalle by ai-forever](https://github.com/ai-forever/ru-dalle)
2. [rudalle-sr by chenxwh](https://github.com/chenxwh/rudalle-sr)

We have made significant modifications to the code to enhance its capabilities in upscaling images up to 32 times their original resolution of 512x512. Through rigorous testing on a Tesla T4 GPU, we have successfully upscaled an image of size 512x512 to a whopping 16384x16384 resolution using 8x > 2x > 2x models. As such, this version of the code represents a substantial improvement over the original code found in repository 1 of the above list.

TODO: The code is optimized for efficient 32x upscaling on smaller GPUs with limited memory, such as those with 11GB available.

# Project Setup

## Installations
First of all, you need to setup the repo and install dependencies by running following command:
```shell
pip install -r requirements.txt
```
This code is tested on `python=3.8` version. 

To run this model, you first need to download the pre-trained checkpoints from HuggingFace repository by running following command
```shell
python download-weights.py x2
```
This command will download the `x2` Real-ESRGAN model, you can also download the other `x4` and `x8` models as well.

## Inference
Now, run the model for upscalling image by running following command:
```shell
python main.py x2 <PATH_OR_URL_OF_IMAGE>
```
In the above command, we used the `x2` model but we can also use the other models i.e. `x4` and `x8` as well. 
<br/>
`PATH_OR_URL_OF_IMAGE` will be the path to input image. You can use a URL or local image path.
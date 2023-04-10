

import torch
from PIL import Image
from cog import BasePredictor, Input, Path
import sys
import requests
from PIL import Image, ImageFile
import numpy as np
import io
from realesrgan.model import RealESRGAN

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

class Predictor(BasePredictor):

    def setup(self, model='x2'):
        device = torch.device("cuda:0")
        model = RealESRGAN(device, 2)
        model.load_weights(f"checkpoints/RealESRGAN_{model}.pth")
        self.model = model
        print("Model loaded!")

    def predict(
        self,
        input_image: Image,
        scale: int = Input(
            description="Choose up-scaling factor", default=4, choices=[2, 4, 8]
        ),
    ) -> Path:
        # input_image = Image.open(str(image))
        input_image = input_image.convert("RGB")
        with torch.no_grad():
            print("Up-scaling!")
            sr_image = self.model.predict(input_image)
        out_path = "out.png"
        sr_image.save(str(out_path))
        return out_path


def get_img_from_url(url, pil=False):

    try:
        try:
            img_data = requests.get(url).content
            img_data = Image.open(io.BytesIO(img_data))
        except requests.exceptions.MissingSchema:
            img_data = Image.open(url)
        if pil:
            return img_data
        img_arr = np.asarray(img_data)
        return img_arr
    except:
        return None


model = sys.argv[1]
path = sys.argv[2]

predictor = Predictor()
predictor.setup(model=model)
print(predictor.predict(get_img_from_url(path, pil=True), 2))


if __name__ == '__main__':
    pass



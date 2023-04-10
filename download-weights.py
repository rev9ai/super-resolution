import os
import sys
from huggingface_hub import hf_hub_url, cached_download


MODELS = {
    'x2': dict(
        scale=2,
        repo_id='shonenkov/rudalle-utils',
        filename='RealESRGAN_x2.pth',
    ),
    'x4': dict(
        scale=4,
        repo_id='shonenkov/rudalle-utils',
        filename='RealESRGAN_x4.pth',
    ),
    'x8': dict(
        scale=8,
        repo_id='shonenkov/rudalle-utils',
        filename='RealESRGAN_x8.pth',
    ),
}

cache_dir = 'checkpoints'
os.makedirs(cache_dir, exist_ok=True)
config = MODELS[sys.argv[1]]
config_file_url = hf_hub_url(repo_id=config['repo_id'], filename=config['filename'])
cached_download(config_file_url, cache_dir=cache_dir, force_filename=config['filename'])

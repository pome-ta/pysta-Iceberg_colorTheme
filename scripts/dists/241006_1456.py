"""
note: screenshot 画像を合体
ref: [Python, Pillowで画像を縦・横に連結(結合) | note.nkmk.me](https://note.nkmk.me/python-pillow-concat-images/)
"""

from pathlib import Path
from PIL import Image as ImageP


ROOT_PATH = Path(__file__).parent

master_dir = Path(ROOT_PATH, './screenshot')

screenshot_dir = Path(ROOT_PATH, '../prjt4iceberg/screenshot')

w_size = 320

master_images = [ImageP.open(image_path.resolve()) for image_path in master_dir.iterdir() ]


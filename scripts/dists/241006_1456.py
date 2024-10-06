"""
note: screenshot 画像を合体
ref: [Python, Pillowで画像を縦・横に連結(結合) | note.nkmk.me](https://note.nkmk.me/python-pillow-concat-images/)
"""

from pathlib import Path
from PIL import Image as ImageP


def scale_to_width(img, width=320):
  height = round(img.height * width / img.width)
  return img.resize((width, height), ImageP.LANCZOS)


def get_concat_h(im1, im2):
  dst = ImageP.new('RGB', (im1.width + im2.width, im1.height))
  dst.paste(im1, (0, 0))
  dst.paste(im2, (im1.width, 0))
  return dst

ROOT_PATH = Path(__file__).parent

master_dir = Path(ROOT_PATH, './screenshot')

screenshot_dir = Path(ROOT_PATH, '../prjt4iceberg/screenshot')
save_name = 'screenshot.png'

w_size = 320

master_images = [
  ImageP.open(image_path.resolve()) for image_path in master_dir.iterdir()
]

resize_images = [scale_to_width(img, w_size) for img in master_images]


concatenated = get_concat_h(*resize_images)
concatenated.save(Path(screenshot_dir, save_name).resolve())

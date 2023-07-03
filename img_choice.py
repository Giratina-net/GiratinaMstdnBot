import random
import glob

# 画像のランダム選択と画像投稿を関数化
def post_img(img_dir):
    img_list = glob.glob(img_dir)
    img_random = random.choice(img_list)
    return img_random

    
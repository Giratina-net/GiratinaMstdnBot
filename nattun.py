from mastodon import Mastodon
import img_choice
from os import getenv


def run():
    # 初期化
    api = Mastodon(
        api_base_url = "https://mstdn.giratina.net",
        client_id = getenv("NATTUN_CLIENT_KEY"),
        client_secret = getenv("NATTUN_CLIENT_SECRET"),
        access_token = getenv("NATTUN_ACCESS_TOKEN")
    )

    # 画像投稿
    img_random = img_choice.post_img("nattun_img/*")

    img1 = api.media_post(img_random)
    media_files = [img1]

    api.status_post(
        status = "",
        visibility="unlisted",
        media_ids = media_files
        )

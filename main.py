# -*- coding: utf-8 -*-
import qrcode
from PIL import Image


def resize_logo(logo: str):
    Logo = Image.open(logo)
    size = 75, 75
    Logo.thumbnail(size, Image.ANTIALIAS)
    Logo.save('logo-branca.png')

def generate_qrcode(logo: str):
    Logo = Image.open(logo)
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(1234567)
    qr.make()
    img_qr_big = qr.make_image(fill_color="#333333", back_color="white").convert('RGB')

    pos = ((img_qr_big.size[0] - Logo.size[0]) // 2, (img_qr_big.size[1] - Logo.size[1]) // 2)
    img_qr_big.paste(Logo, pos)

    img_qr_big.save('qrcode.png')


if __name__ == '__main__':
    generate_qrcode(logo='logo-branca.png')

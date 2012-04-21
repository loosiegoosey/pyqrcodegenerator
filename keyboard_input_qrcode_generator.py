#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
# Keyboard Input QRCode Generator
# Jonathas Rodrigues <jonathas at archlinux dot us> - 20120420

from pyqrcode import pyqrcode

input = raw_input("Type the text you want for your QRCode: ")

qr_image = pyqrcode.MakeQRImage(input)
qr_image.show()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image

flag = Image.new("RGB", (450, 450))

for i in range(2):
    for j in range(2):
        x = j * 225
        y = i * 225
        pot = "flag-{}.png".format(j + i * 2)
        potImage = Image.open(pot)
        potImage1 = potImage.crop((x, y, x + 225, y + 225))
        flag.paste(potImage1, (x, y))

flag.save('flag.png')

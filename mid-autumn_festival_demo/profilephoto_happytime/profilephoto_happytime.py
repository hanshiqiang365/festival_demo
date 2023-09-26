#author:hanshiqiang365

from PIL import Image
import math

flag_img = Image.open('full_moon.png').convert("RGBA")
photo_img = Image.open('profile_photo.jpg').convert("RGBA")

# 满月图片的宽和高
flag_width, flag_height = flag_img.size
# 截出满月左上角
crop_flag = flag_img.crop((66, 0, flag_height+66, flag_height))

# 渐变处理
for i in range(flag_height):
    for j in range(flag_height):
            color = crop_flag.getpixel((i, j))
            distance = int(math.sqrt(i*i + j*j))
            alpha = 255 - int(distance//3.5)
            new_color = (*color[:-1], alpha if alpha > 0 else 0)
            crop_flag.putpixel((i, j), new_color)
            
# 重置图像尺寸
new_crop_flag = crop_flag.resize(photo_img.size)
photo_img.paste(new_crop_flag, (0, 0), new_crop_flag)

# 保存自己的满月头像
photo_img.save('fullmoon_profilephoto.png')
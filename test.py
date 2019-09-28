from PIL import Image, ImageDraw, ImageFont

width = 500
height = 500          # 设置分辨率
font_size = 120          # 字体大小
font_style  = '‪C:\Windows\Fonts\simhei.ttf'          # 字体格式

bg_1 = (254, 1, 254)
bg_2 = (0, 245, 246)

# 新建一张空白图片
randint = Image.new(mode = 'RGB', size = (width, height), color = bg_1)
draw = ImageDraw.Draw(randint)
# 设置步长
step_r = (bg_2[0] - bg_1[0])  /  height
step_g = (bg_2[1] - bg_1[1])  /  height
step_b = (bg_2[2] - bg_1[2])  /  height
for  y  in  range(0, height):
    bg_r = round(bg_1[0] + step_r  *  y)
    bg_g = round(bg_1[1] + step_g  *  y)
    bg_b = round(bg_1[2] + step_b  *  y)
    for  x  in  range(0, width):
            draw.point((x, y), fill = (bg_r, bg_g, bg_b))

    # 将字体绘制到图片上
    fnt = ImageFont.truetype(font = font_style, size = font_size)
    [fnt_width, fnt_height] = draw.textsize('Randint', font = fnt)
    fnt_x = (width - fnt_width)  /  2
    fnt_y = (height - fnt_height)  /  2
    draw.text((fnt_x, fnt_y), text = 'Randint', font = fnt, fill = 'white')

    randint.show()
    randint.save('randint.png')
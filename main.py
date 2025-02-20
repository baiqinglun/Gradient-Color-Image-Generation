from PIL import Image, ImageDraw, ImageFont
import colorsys
import datetime
import random

def generate_gradient_image(width, height, color1, color2, text, text_size):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    
    # 生成渐变背景
    for y in range(height):
        for x in range(width):
            r = int(color1[0] + (color2[0] - color1[0]) * (x / width))
            g = int(color1[1] + (color2[1] - color1[1]) * (x / width))
            b = int(color1[2] + (color2[2] - color1[2]) * (x / width))
            image.putpixel((x, y), (r, g, b))
    
    # 使用微软雅黑字体
    try:
        font = ImageFont.truetype("msyh.ttc", text_size)
    except IOError:
        font = ImageFont.load_default()
    
    text_box = font.getbbox(text)
    text_x = (width - text_box[2]) / 2
    text_y = (height - text_box[3]) / 2
    
    # 绘制加粗文本
    for offset in range(-1, 2):
        draw.text((text_x + offset, text_y), text, font=font, fill=(255, 255, 255))
        draw.text((text_x, text_y + offset), text, font=font, fill=(255, 255, 255))
    
    return image

def get_random_colors_within_90_degrees():
    h1 = random.random()
    s = 1.0
    v = 1.0
    h2 = (h1 + 0.25) % 1.0  # 90度对应0.25
    color1 = colorsys.hsv_to_rgb(h1, s, v)
    color2 = colorsys.hsv_to_rgb(h2, s, v)
    return (int(color1[0]*255), int(color1[1]*255), int(color1[2]*255)), (int(color2[0]*255), int(color2[1]*255), int(color2[2]*255))

if __name__ == "__main__":
    width, height = 800, 600
    color1, color2 = get_random_colors_within_90_degrees()
    text = "默认文字"
    text_size = 70
    image = generate_gradient_image(width, height, color1, color2, text, text_size)
    
    # 获取当前时间戳并生成文件名
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.png"
    image.save(filename)
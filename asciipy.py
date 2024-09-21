from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def image_to_ascii(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    image = resize_image(image)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_art = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_art += ascii_str[i:i+img_width] + "\n"

    return ascii_art

image_path = input("Wellcome to ASCIIPy\n Created by github.com/TPashaxrd\n   Enter a addres. => ")
ascii_art = image_to_ascii(image_path)
print(ascii_art)

# Created by TPasha
# github.com/TPashaxrd
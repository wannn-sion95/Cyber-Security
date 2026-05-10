from PIL import Image

img = Image.open("input.png")
pixels = list(img.getdata())

message = "This is the message I want to send, but I'm hiding it"
binary = ''.join(format(ord(c), '08b') for c in message) + '1111111111111110'

new_pixels = []
bit_index = 0

for pixel in pixels:
    r, g, b = pixel[:3]

    if bit_index < len(binary):
        r = (r & ~1) | int(binary[bit_index])
        bit_index += 1

    new_pixels.append((r, g, b))

img.putdata(new_pixels)
img.save("output.png")

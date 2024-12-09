from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open("myqr1.png")

cont= decode(img)

print(decode())
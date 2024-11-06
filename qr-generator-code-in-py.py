import pyqrcode
from PIL import Image

link = input("Enter anything to generate QR: ")
qr_code = pyqrcode.create(link)  # Corrected 'pycode' to 'pyqrcode'
qr_code.png("QRCode.png", scale=5)

# Open the generated QR code image
Image.open("QRCode.png").show()  # Corrected 'ORCode.png' to 'QRCode.png'

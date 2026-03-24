import qrcode
from PIL import Image

def generate_qr(link):

    qr = qrcode.make(link)

    qr.save("payment_qr.png")

    print("\n📷 QR Code generated: payment_qr.png")
    print("Scan the QR code to complete payment.")

    # Automatically open QR image
    img = Image.open("payment_qr.png")
    img.show()
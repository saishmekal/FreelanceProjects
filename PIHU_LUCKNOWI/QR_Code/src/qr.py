import qrcode
from PIL import Image

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://pihulucknowi.netlify.app/")
qr.make(fit=True)

# Customize colors
img = qr.make_image(fill_color="white", back_color="#11A690")

# Save image
img.save("my_qr.png")

# Show image
img.show()

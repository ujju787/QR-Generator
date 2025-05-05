import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=7,
        box_size=10,
        border=1
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    img.show()

# Example usage:
link=input("Enter your  link to generate qr : ")
fileName=input("enter filename with extension(for eg. photo.jpg)")
generate_qr_code(link, fileName)

import qrcode
from PIL import _imaging
link = input("plz type your link, we will generate a QRCODE for your link = ")
Fill_color = input("enter a color for QRCODE = ")

QRsize = qrcode.QRCode(version=1,box_size=20,border=4)
QRsize.make(fit=True)
QRsize.add_data(link)
Make_image = QRsize.make_image(fill_color=Fill_color,back_color='white')
Make_image.save('img2.png')
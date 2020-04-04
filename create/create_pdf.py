from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import img2pdf
import datetime
import csv
import os
import qrcode
from django.conf import settings
#STATIC_URL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static\\')
print(settings.STATICFILES_DIRS[0])

class create_pdf:
    roboto_r = os.path.join(settings.STATICFILES_DIRS[0], 'Roboto-Regular.ttf')
    roboto_m = os.path.join(settings.STATICFILES_DIRS[0], 'Roboto-Medium.ttf')

    qrcode_file = os.path.join(settings.STATICFILES_DIRS[0], 'qrcode.png')
    qrcode_small = os.path.join(settings.STATICFILES_DIRS[0], 'qrcode_small.png')


    certificate_meta = [
        {'file': 'kriraathon-part.png', 'xy': (860, 660), 'font': ImageFont.truetype(roboto_r, 40), 'color': (255, 255, 255)},
        {'file': 'rc-certificate.png', 'xy': (1600, 1135), 'font': ImageFont.truetype(roboto_m, 75), 'color': (0, 0, 0)},
        {'file': 'rc-emosync.png', 'xy': (1600, 1135), 'font': ImageFont.truetype(roboto_m, 75), 'color': (0, 0, 0)}
    ]
    
    rollno = ''

    student_name = ''

    choice = int()

    def __init__(self, name, roll_no, choice):
    #def set(name):
        self.rollno = roll_no
        self.student_name = name
        self.choice = int(choice) - 1

    def create_qrcode(self, data):
        qrcode_size = 200, 200

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img_qr = qr.make_image()
        img_qr.save(self.qrcode_file)

        im = Image.open(self.qrcode_file)
        im.thumbnail(qrcode_size, Image.ANTIALIAS)
        im.save(self.qrcode_small)

    def create(self):
        
        self.rollno = self.rollno.replace('/', '')
        
        data = str(self.rollno + ' - ' + self.student_name)
        
        self.create_qrcode(data)

        path = os.path.join(settings.STATICFILES_DIRS[0], self.certificate_meta[self.choice]['file'])

        img = Image.open(path, 'r')
        
        draw = ImageDraw.Draw(img)
            
        #Create Certificates
        draw.text(self.certificate_meta[self.choice]['xy'], self.student_name.upper(), self.certificate_meta[self.choice]['color'], font = self.certificate_meta[self.choice]['font'])
        qr = Image.open(self.qrcode_small, 'r')
        qr_w, qr_h = qr.size
        img_w, img_h = img.size
        offset = ((img_w - qr_w - 75, img_h - qr_h - 75))
        img.paste(qr, offset)

        imgname = pdfname = (self.rollno + ' - ' + self.student_name)
        
        
        #Set image's name
        imgname += '.png'
        imgname = os.path.join(settings.STATICFILES_DIRS[0], os.path.join('Kriraathon Certificates', imgname))
        
        #Set PDF's name
        pdfname += '.pdf'
        pdfname = os.path.join(settings.STATICFILES_DIRS[0], os.path.join('Kriraathon Certificates', pdfname))
        
        #print(imgname, pdfname)
        
        img.save(imgname)
        img.close()
        img = Image.open(imgname)
        pdf = img2pdf.convert(img.filename)
        file = open(pdfname, 'wb')
        file.write(pdf)
        img.close()
        os.remove(imgname)
        #pdfname = pdfname.replace('./create/Kriraathon Certificates/', '')
        return pdfname

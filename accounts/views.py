'''
Created on 2013-4-19

@author: wwjiang
'''

from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random,cStringIO,os


"""
随机数产生函数
"""
def get_random_letter():
    letters = []
    for ascii_num in range(97,123):
        letters.append(chr(ascii_num))
    for ascii_num in range(65,91):
        letters.append(chr(ascii_num))
    #验证码增加数字,容易混淆
#    for number in range(10):
#        letters.append(str(number))
    return random.choice(letters)
"""
随机验证码视图
"""
def captcha(request):
    im = Image.new('RGBA',(100,40),(50,50,50,50))
    draw = ImageDraw.Draw(im)
    rands = ""
    #获得四位随机数
    path = os.path.join(os.path.dirname(__file__),"../templates/fonts/")
    for index in range(4):
        rands = rands + get_random_letter()
    draw.text((2,0),
            rands[0],
            font=ImageFont.truetype(path + "1.ttf",
                random.randrange(20,30)),
            fill='white')
    draw.text((20,0),
            rands[1], 
            font=ImageFont.truetype(path + "2.ttf", 
                random.randrange(24,34)), 
            fill='yellow')
    draw.text((40,0), 
            rands[2], 
            font=ImageFont.truetype(path + "3.ttf", 
                random.randrange(20,30)), 
            fill='blue')
    draw.text((60,0), 
            rands[3], 
            font=ImageFont.truetype(path + "4.ttf", 
                random.randrange(24,34)), 
            fill='green') 
    del draw
    #全部以小写形式存入session
    request.session['captcha'] = rands.lower()
    buf = cStringIO.StringIO()
    im.save(buf, 'gif')
    return HttpResponse(buf.getvalue(),'image/gif')
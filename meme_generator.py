# -*- coding: utf-8 -*-
import urllib2                
from bs4 import BeautifulSoup 
import requests               
import sys                    
import argparse              
import cairo
import pango
import pangocairo
import sys
import argparse
import redis
from random import randint
from common import util
from common import robots_txt

db = redis.Redis()

def draw_background(file_name):
#    file_name = "/duta/server/whatsappchannels/modi_images/{}".format(file_name)
    surf = cairo.ImageSurface.create_from_png(file_name);
    return surf

def find_text_position(position):
    if position == "right" or position == 'right2' or position == 'right3' :
        textPositionX = 70
        textPositionY = 70

    if position == "left" or position == 'left2' or position == 'left3':
        textPositionX = 700
        textPositionY = 70

    if position == "top":
        textPositionX = 500
        textPositionY = 70

    if position == "bottom":
        textPositionX = 200
        textPositionY = 500

    textPosition = (textPositionX, textPositionY)
    return textPosition

def draw_text(surf, position, quote, channel, font_colour, filename):
    context = cairo.Context(surf)
    textPosition = find_text_position(position)
    context.translate(textPosition[0],textPosition[1])
    pangocairo_context = pangocairo.CairoContext(context)
    pangocairo_context.set_antialias(cairo.ANTIALIAS_SUBPIXEL)    
    layout = pangocairo_context.create_layout()
    layout.set_width(700 * pango.SCALE)
    layout.set_wrap(pango.WRAP_WORD)
    fontname = "Rekha"
    font = pango.FontDescription(fontname +  "bold 38")
    layout.set_font_description(font)
    layout.set_text(u"""{}""".format(quote))   
    context.set_source_rgb(font_colour[0], font_colour[1], font_colour[2])
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    num_lines = layout.get_line_count()
#    filename = '/duta/images/modiout{}.png'.format(file_number)
    key = 'independence_test'
    count = int(db.get(key))
    filename = '{}_{}'.format(count, filename)
    db.set(key, str(count + 1))
    with open(filename, "wb") as image_file:
        surf.write_to_png(image_file)

#    util.send_image(db, channel, 'file://{}'.format(filename), quote.encode('utf-8'))

if __name__ == '__main__':
    filename = 'modi_left.png'
    background_image = draw_background(filename)
    font_colour = [128, 0, 0]
    draw_text(background_image, 'bottom', 'You are Gandhiji', 'cricket', font_colour, filename)
#    draw_text(background_image, 'right', 'Hi User', 'cricket', font_colour, filename)

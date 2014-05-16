#!/usr/bin/python
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf, InterpType
import argparse

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def onButtonPressed(self, event, *data):
        print "Button pressed"
    def onKeyPress(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        print "Key %s (%d) was pressed" % (keyname, event.keyval)
    def onCheckResize(self, *data):
        window = builder.get_object("mainWindow")
        newWindowWidth = window.get_size()[0]
        image = builder.get_object("mainImage")
        if (image.get_pixbuf() is None or image.get_pixbuf().get_width() != newWindowWidth):
            image.set_from_pixbuf(imageProcessor.getPixbufScaledByWidth(newWindowWidth))

class ImageProcessor:
    def __init__(self, originalPixbuf):
        self.pixbuf = originalPixbuf

    def getPixbufScaledByWidth(self, widthToScaleInto):
        pixbufRatio = float(self.pixbuf.get_width()) / float(self.pixbuf.get_height())
        newHeight = widthToScaleInto / pixbufRatio
        resizedPixbuf = self.pixbuf.scale_simple( widthToScaleInto, newHeight, InterpType.BILINEAR )
        return resizedPixbuf;

parser = argparse.ArgumentParser(description='Simple image viewer.')
parser.add_argument('imageFileName', help='file name to open')

args = parser.parse_args()

print "Trying to open image %s" % args.imageFileName

builder = Gtk.Builder()
builder.add_from_file("justImage.glade")
builder.connect_signals(Handler())

originalPixbuf = Pixbuf.new_from_file(args.imageFileName)

imageProcessor = ImageProcessor(originalPixbuf)

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()

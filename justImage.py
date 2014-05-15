#!/usr/bin/python
from gi.repository import Gtk, Gdk
import argparse

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def onButtonPressed(self, event, *data):
        print "Button pressed"
    def onKeyPress(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        print "Key %s (%d) was pressed" % (keyname, event.keyval)



parser = argparse.ArgumentParser(description='Simple image viewer.')
parser.add_argument('imageFileName', help='file name to open')

args = parser.parse_args()

print "Trying to open image %s" % args.imageFileName


builder = Gtk.Builder()
builder.add_from_file("justImage.glade")
builder.connect_signals(Handler())

image = builder.get_object("mainImage")
image.set_from_file(args.imageFileName)

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()

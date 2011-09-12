from sphinx.ext.intersphinx import read_inventory_v2
from posixpath import join
url = "https://raw.github.com/xuru/pyvisdk/gh-pages/"
inv = "objects.inv"
f = open(inv, 'rb')
line = f.readline()
invdata = read_inventory_v2(f, url, join)
print invdata.keys()


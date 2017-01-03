#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect("/home/maxs/Escritorio/proy_biblia/biblia/bad.sqlite")
cursor = con.cursor()
print u"la base de datos se ha creado exitosamente"
print cursor
c="3"
v="1"
b="8"


cursor.execute(" select text from verse where chapter=? and verse=? and book_id=? ;" , (c,v,b))
for i in cursor:
        print i[0]

con.close()
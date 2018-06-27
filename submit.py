#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

def go():
    fs = cgi.FieldStorage()
    toWho = fs.getvalue('toWho')
    forWhy = fs.getvalue('whatItSays')
    
    f = open('kudos.txt', 'rU')
    t = f.read()
    f.close()
    
    x = open('kudos.txt', 'w+')
    x.write(t.strip() + '\n' + toWho + ',' + forWhy)
    x.close()
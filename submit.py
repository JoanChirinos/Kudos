#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    for i in fs.keys():
        print i + "<br>"
#    toWho = fs.getvalue('toWho')
#    forWhy = fs.getvalue('whatItSays')
#    
#    f = open('kudos.txt', 'rU')
#    t = f.read()
#    f.close()
#    
#    x = open('kudos.txt', 'w+')
#    x.write(t.strip() + '\n' + toWho.capitalize() + ',' + forWhy.lowercase())
#    x.close()
#    print t.strip() + '\n' + toWho.capitalize() + ',' + forWhy.lowercase()
    
go()
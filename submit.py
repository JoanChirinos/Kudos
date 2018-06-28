#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    if len(fs.keys()) > 1:
        toWho = fs.getvalue('toWho')
        forWhy = fs.getvalue('whatItSays')

        f = open('kudos.txt', 'rU')
        t = f.read()
        f.close()

        x = open('kudos.txt', 'w+')
        x.write(t.strip() + '\n' + toWho.capitalize() + ',' + forWhy.lower())
        x.close()
        print t.strip() + '\n' + toWho.capitalize() + ',' + forWhy.lower()
    else:
        f = open('kudos.txt', 'rU')
        t = f.read()
        f.close()
        
        kl = t.split('\n')
        for i in range(len(kl)):
            kl[i] = kl[i].split(',')
        while kl[0] == [""]:
            kl = kl[1:]
            
        while kl[-1] == [""]:
            kl = kl[:-1]
        
        d = dict()
        
        for i in kl:
            if i[0] in d:
                d[i[0]] += [i[1]]
            else:
                d[i[0]] = [i[1]]
        
        print '<div class="row"><div class="col-3"><div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">'
        
        left = '<a class="nav-link active" id="v-pills-NAME-tab" data-toggle="pill" href="#v-pills-NAME" role="tab" aria-controls="v-pills-NAME" aria-selected="true">NAME</a>'
        right = '<div class="tab-pane fade show active" id="v-pills-NAME" role="tabpanel" aria-labelledby="v-pills-NAME-tab">KUDOS</div>'
        
        toAddLeft = ""
        toAddRight = ""
        
        for i in d.keys():
            print "<!-- " + str(i) + "  |  " + str(d[i]) + " -->"
            toAddLeft += "\n\n" + left.replace('NAME', i)
            temp = toAddRight.replace('NAME', i)
            kudos = ""
            for x in d[i]:
                kudos += '<li>Kudos to ' + i + ' for ' + x
            toReplaceWith = '<ul>' + kudos + '</ul>'
            temp = temp.replace('KUDOS', toReplaceWith)
        
        print toAddLeft
        print '</div></div><div class="col-9"><div class="tab-content" id="v-pills-tabContent">'
        print toAddRight
        print '</div></div></div></div>'
                
    
go()












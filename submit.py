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
        
        if len(t.strip() == 0):
            print '<div class="md-space"></div><div class="row"><div class="col text-center" style="color: red">No Kudos have been submitted yet!</div></div>'
        
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
        
        leftACTIVE = '<a class="nav-link active" id="v-pills-NAME-tab" data-toggle="pill" href="#v-pills-NAME" role="tab" aria-controls="v-pills-NAME" aria-selected="true">NAME</a>'
        rightACTIVE = '<div class="tab-pane fade show active" id="v-pills-NAME" role="tabpanel" aria-labelledby="v-pills-NAME-tab">KUDOS</div>'
        left = '<a class="nav-link" id="v-pills-NAME-tab" data-toggle="pill" href="#v-pills-NAME" role="tab" aria-controls="v-pills-NAME" aria-selected="true">NAME</a>'
        right = '<div class="tab-pane fade show active" id="v-pills-NAME" role="tabpanel" aria-labelledby="v-pills-NAME-tab">KUDOS</div>'
        
        toAddLeft = ""
        toAddRight = ""
        
        hasAddedOne = False
        
        for i in sorted(d.keys()):
            print "\n\n<!-- " + str(i) + "  |  " + str(d[i]) + " -->"
            if not hasAddedOne:
                toAddLeft += "\n" + leftACTIVE.replace('NAME', i)
                temp = rightACTIVE.replace('NAME', i)
                hasAddedOne = True
            else:
                toAddLeft += "\n" + left.replace('NAME', i)
                temp = right.replace('NAME', i)
            kudos = ""
            for x in d[i]:
                kudos += '<li>Kudos to ' + i + ' for ' + x
            toReplaceWith = '<ul>' + kudos + '</ul>'
            temp = temp.replace('KUDOS', toReplaceWith)
            toAddRight += temp
        
        print toAddLeft
        print '\n\n\n</div></div><div class="col-9"><div class="tab-content" id="v-pills-tabContent">'
        print toAddRight
        print '</div></div></div></div>'
                
    
go()












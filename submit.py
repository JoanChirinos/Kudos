#! /usr/bin/python

import cgi, cgitb, time

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
        toWrite = (t.strip(' ') + '\n' + toWho.strip(' ').capitalize() + 'SPLITHERE' + forWhy.strip(' ').lower() + '<span style="color: rgb(100, 100, 100)">' + time.strftime('%B %d %Y @ %I:%M %p') + "</span>").replace(',', ' ').replace('&', 'and')
        x.write(toWrite)
        x.close()
        print t.strip(' ') + '\n' + toWho.strip(' ').capitalize() + 'SPLITHERE' + forWhy.lower() + ' ' + time.strftime('%B %d %Y @ %I:%M %p')
    else:
        f = open('kudos.txt', 'rU')
        t = f.read()
        f.close()
        
        if len(t.strip(' ')) == 0:
            print '</div><div class="row"><div class="col text-center" style="color: red">No Kudos have been submitted yet!</div></div>'
            return
        
        kl = t.split('\n')
        
        for i in range(len(kl)):
            kl[i] = kl[i].split('SPLITHERE')
        while kl[0] == [""]:
            kl = kl[1:]
            
        while kl[-1] == [""]:
            kl = kl[:-1]
        
        d = dict()
        
        for i in kl:
            if i[0].capitalize() in d:
                try:
                    d[i[0].capitalize()] += [i[1]]
                except:
                    continue
            else:
                try:
                    d[i[0].capitalize()] = [i[1]]
                except:
                    continue
        
        print '<div class="row"><div class="col-sm-4"><div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">'
        
        leftACTIVE = '<a class="nav-link active" id="v-pills-NAME-tab" data-toggle="pill" href="#v-pills-NAME" role="tab" aria-controls="v-pills-NAME" aria-selected="true">SANS_FORMAT</a>'
        rightACTIVE = '<div class="tab-pane fade show active" id="v-pills-NAME" role="tabpanel" aria-labelledby="v-pills-NAME-tab">KUDOS</div>'
        left = '<a class="nav-link" id="v-pills-NAME-tab" data-toggle="pill" href="#v-pills-NAME" role="tab" aria-controls="v-pills-NAME" aria-selected="true">SANS_FORMAT</a>'
        right = '<div class="tab-pane fade" id="v-pills-NAME" role="tabpanel" aria-labelledby="v-pills-NAME-tab">KUDOS</div>'
        
        toAddLeft = ''
        toAddRight = ''
        
        hasAddedOne = False
        
        for i in sorted(d.keys()):
            print "\n\n<!-- " + str(i) + "  |  " + str(d[i]) + " -->"
            if not hasAddedOne:
                toAddLeft += "\n" + leftACTIVE.replace('NAME', i.strip(' ').replace(' ', '_')).replace('SANS_FORMAT', i.strip(' '))
                temp = rightACTIVE.replace('NAME', i.strip(' ').replace(' ', '_'))
                hasAddedOne = True
            else:
                toAddLeft += "\n" + left.replace('NAME', i.strip(' ').replace(' ', '_')).replace('SANS_FORMAT', i.strip(' '))
                temp = right.replace('NAME', i.strip(' ').replace(' ', '_'))
            kudos = ""
            for x in d[i]:
                if x.split(' ')[0].lower() == 'for':
                    x = ' '.join(x.split(' ')[1:])
                kudos += '<li>Kudos to ' + i.strip(' ').replace('_', ' ') + ' for ' + x.strip(' ') + '</li>'
            toReplaceWith = '<ul>' + kudos + '</ul>'
            temp = temp.replace('KUDOS', toReplaceWith)
            toAddRight += temp
        
        print toAddLeft
        print '\n\n\n</div></div><div class="col-sm-8"><div class="tab-content" id="v-pills-tabContent">'
        print toAddRight
        print '\n\n\n</div></div></div></div>'
        print '\n<div class="md-space"></div>'
        print '\n\n<!-- this should only show on small screens -->\n\n<div class="row"><div class="col d-sm-block d-md-none d-lg-none d-xl-non"><a href="#" class="btn btn-block btn-info">Back to top</a></div></div>'
        
        print '<br><br><p>Umm this hasn\'t been working very well lately so here\'s all of them without sorting and buttons and stuff. Sorry!</p><ul>\n'
        for i in sorted(d.keys()):
            for x in d[i]:
                print '<li>Kudos to ' + i.strip(' ') + ' for ' + x.strip(' ') + '</li>'
        print '</ul>'
    
go()












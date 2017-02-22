# -*- coding: utf-8 -*-

from grab import Grab
import time

def radio():

    url = 'http://radiovesti.ru/brand/60948/'
    g = Grab()
    g.go(url)
    for elem in g.doc.select("//div[@class='news__content']//h1/a"):
        scr = 'http://radiovesti.ru'+str(elem.attr('href'))
        s = Grab()
        s.go(scr)
        for element in s.doc.select("//a[@class='listen-news']"):
            time.sleep(1)
            scr_audio = ("http://audio.rutv.ru/download?id="+str(element.attr('data-audio-id')))[:-1]
            f = Grab()
            name = s.doc.select("//h1[@class='h1-title']").text()
            name = name.replace(":", "")
            name = name.replace("?", "")
            name = name.replace("!", "")
            print name
            print scr_audio
            f.go(scr_audio, log_file=name+'.mp3')

    print 'Конец'

radio()

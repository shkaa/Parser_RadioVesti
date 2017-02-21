# -*- coding: utf-8 -*-

from grab import Grab


def radio():

    url = 'http://radiovesti.ru/brand/60948/'
    g = Grab()
    g.go(url)
    for elem in g.doc.select("//div[@class='news__content']//h1/a"):
        scr = 'http://radiovesti.ru'+str(elem.attr('href'))
        s = Grab()
        s.go(scr)
        for element in s.doc.select("//a[@class='listen-news']"):
            scr_audio = ("http://audio.rutv.ru/download?id="+str(element.attr('data-audio-id')))[:-1]
            f = Grab()
            name = element.attr('data-audio-title')
            print name
            print scr_audio
            f.go(scr_audio, log_file=name+'..mp3')

    print 'Конец'

radio()

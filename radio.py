# -*- coding: utf-8 -*-

from grab import Grab
from time import sleep
import pytils


def radio():

    print pytils.dt.ru_strftime(u'%d %B %Y', inflected=True)
    url = 'http://radiovesti.ru/brand/60948/'
    g = Grab()
    g.go(url)

    for elem in g.doc.select("//div[@class='news__content']//h1/a"):
        scr = 'http://radiovesti.ru'+str(elem.attr('href'))
        s = Grab()
        s.go(scr)
        i = 0
        if pytils.dt.ru_strftime(u"%d %B %Y", inflected=True) in s.doc.select("//div[@class='news__date'][1]").text():
            for element in s.doc.select("//a[@class='listen-news']"):
                sleep(1)
                scr_audio = ("http://audio.rutv.ru/download?id="+str(element.attr('data-audio-id')))[:-1]
                f = Grab()
                name = s.doc.select("//h1[@class='h1-title']").text()
                name = name.replace(":", "")
                name = name.replace("?", "")
                name = name.replace("!", "")
                print name
                # print scr_audio
                f.go(scr_audio, log_file=name+'.mp3')
                i = + 1

    print '\nКонец, загружено --->',i ,'файлов'

radio()

# -*- coding: utf-8 -*-
'''
Created on 13 april 2013

@author: vl
'''

class CLIView(object):
    '''
    classdocs
    '''

    def __init__(self, analyser):
        '''
        Constructor
        '''
        self.__analyser = analyser
        
    def render(self):
        '''
        Render full statistic to string
        '''
        
        result = ''
        result += "Перелік країн:\n"
        result += "\n".join(self.__analyser.countries())
        result += "\nПерелік ресурсів:\n"
        result += "\n".join(self.__analyser.resources())

        return result
        

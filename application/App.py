'''
Created on 13 april. 2013

@author: vl
'''

from statistic.analyser import Analyser
from statistic.view import CLIView
import os

class App(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        dirname = os.path.dirname(__file__)
        self.__logfile = os.path.join(dirname,'../data/site.log')
    
    def run(self):
        '''
        Run application
        '''
        print self.show_statistic() 
        
    
    def show_statistic(self):
        '''
        Show statistic
        '''
        analyser = Analyser(self.__logfile)
        analyser.load_file()
        view = CLIView(analyser)
        return view.render()
        
    
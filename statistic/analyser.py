# -*- coding: utf8 -*-
'''
Created on 13 april 2013

@author: vl
'''

class Analyser(object):
    '''
    classdocs
    '''
    
    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.__filepath = filepath
        self.__data = []
    
    def load_file(self):
        '''
        Load data from log file
        '''
        log_file = open(self.__filepath,'r')
        data = log_file.readlines()
        log_file.close()
        for line in data:
            self.append_record(line.split())
        return self
    
    def append_record(self, record):
        '''
        Append record
        '''
        self.__data.append(record)
        return self
    
    def get_data(self):
        '''
        Get data
        '''
        return self.__data
    
    def countries(self):
        '''
        Touple of countries
        '''
        countries = []
        # I guess it's better to use numpy for slicing, but this still works
        for ndx, member in enumerate(self.__data):
            if member[2] not in countries:
                countries.append(member[2])
        # TODO: стоврити кортеж країн інформація про які зберігається в лог файлі
        # Список рядків лог файлу доступний в self.__data   
        return tuple(countries)
        
    def resources(self):
        '''
        List of resources
        '''
        resources = []
        # Find shortest resource:
        # I guess, its better to use numpy here and slice numpy array 
        root = []
        for entry in self.__data:
            root.append(entry[1])
        root=min(root, key=len)
        #Same as for countries, but take 2nd column
        for ndx, member in enumerate(self.__data):
            # Build resources list with replacement
            if member[1].replace(root,"/") not in resources:
                resources.append(member[1].replace(root,"/"))

        # TODO: створити кортеж ресурсів сайту. Кожен ресурс предстивити відносно верхнього каталогу
        # Наприклад для запису 'http://google.com/' результат має бути '/'
        # а для запису 'http://google.com/index/?g=1' результат буде '/index/?g=1'
        
        return tuple(resources)

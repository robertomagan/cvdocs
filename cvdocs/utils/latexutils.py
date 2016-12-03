'''
Created on 20 nov. 2016

@author: roberto
'''

def create_chapter(name):
    return '\chapter{' + name + '}'

def create_section(name):
    return '\section{' + name + '}'

def create_subsection(name):
    return '\subsection{' + name + '}'

def insert_pdf_file(name):
    return '\includepdf{' + name + '}'

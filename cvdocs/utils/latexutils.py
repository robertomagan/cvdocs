# -*- coding: utf-8 -*-
"""
    :mod:`latexutils`
    ===========================================================================
    :synopsis: LATEX utilities
    :author: Roberto Magán Carrión
    :contact: robertomagan@gmail.com, rmagan@ugr.es
    :organization: University of Granada
    :project: cvdocs
    :since: 1.0 
"""

def create_chapter(name):
    return '\chapter{' + name + '}'

def create_section(name):
    return '\section{' + name + '}'

def create_subsection(name):
    return '\subsection{' + name + '}'

def insert_pdf_file(name):
    return '\includepdf{' + name + '}'

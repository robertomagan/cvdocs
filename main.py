# -*- coding: utf-8 -*-
"""
    :mod:`main`
    ===========================================================================
    :synopsis: main script
    :author: Roberto Magán Carrión
    :contact: robertomagan@gmail.com, rmagan@ugr.es
    :organization: University of Granada
    :project: cvdocs
    :since: 1.0 
"""
import sys
import yaml
import logging.config
import traceback
import cvdocs.utils.datautils as dutils
import cvdocs.utils.latexutils as lutils
import shutil

from cvdocs.exception.exception import ConfigError
from cvdocs.config.configure import Configure
import os

# character encoding utf-8
reload(sys)
sys.setdefaultencoding('utf8')

CHAPTER = 'chapter'
SECTION = 'section'
SUBSECTION = 'sub' + SECTION
CHAPTER_T = CHAPTER + 'Title'
SECTION_T = SECTION + 'Title'
CHAPTER_P = CHAPTER + 'Path'
SECTION_P = SECTION + 'Path'


def main():
    
    # Get the configuration params and load it into a singleton pattern
    config_params = Configure()
    
    try:
        # Application config params
        config_params.load_config()
        
        # Logging config
        logging.config.dictConfig(yaml.load(open('config/logging.yaml', 'r')))
    except ConfigError as ece:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback ,limit=10, file=sys.stdout)
        ece.print_error()
        exit(1)
    
    # LATEX items list
    latex_body = []
    
    # Get all config items  
    resources = config_params.get_config()['ResourcesTree']
    
    # root document path
    rootPath = resources['rootPath']
    
    # blank PDF path
    blankPDF = config_params.get_config()['GeneralParams']['blankPDFpath']
    
    # Ordering chapter by keys
    od_resources = dutils.sort_dictionary(resources, order_by='key', order='asc')
    
    for c_k,c_v in od_resources.items():
        
        # Chapter
        #print("key_c: " + c_k)
        if c_k.startswith(CHAPTER):
            print("found chapter: " + c_k)                        
            
            # Get title and chapter path
            chapterTitle = od_resources[c_k][CHAPTER_T]
            chapterPath = od_resources[c_k][CHAPTER_P]
            
            # Add a white page before the chapter
            if 'addWhiteBefore' in od_resources[c_k]:
                latex_body.append(lutils.insert_pdf_file(blankPDF))
            
            # Add the chapter to the latex body
            latex_body.append(lutils.create_chapter(chapterTitle))
            
            # Add a white page after the chapter
            if 'addWhiteAfter' in od_resources[c_k]:
                latex_body.append(lutils.insert_pdf_file(blankPDF))
            
            # are there files?
            #chapterFiles = filter(os.path.isfile, os.listdir(rootPath + chapterPath)) 
                    
            # are there files?
            chapterFiles = [i for i in os.listdir(rootPath + chapterPath) 
                            if os.path.isfile(rootPath + chapterPath + i)]
                                        
            # Sort the names as lexicographical order                    
            for f in sorted(chapterFiles):
                        
                if '##' not in f:                         
                    # insert pdf file
                    latex_body.append(lutils.insert_pdf_file(os.path.abspath(rootPath + chapterPath + f)))
                               
                        
            # Ordering section by keys
            od_resources_s = dutils.sort_dictionary(resources[c_k], order_by='key', order='asc')
            
            
            # Get the sections in this chapter
            for s_k,s_v in od_resources_s.items():
                
                #print("key_s -- " + s_k)
                # Section
                if s_k.startswith(SECTION):
                    print("found section -- " + s_k)
                    
                    # Get title and chapter path
                    sectionTitle = od_resources_s[s_k][SECTION_T]
                    sectionPath = od_resources_s[s_k][SECTION_P]
                    
                    # Add a white page
                    if 'addWhiteBefore' in od_resources_s[s_k]:
                        latex_body.append(lutils.insert_pdf_file(blankPDF)) 
            
                    # Add the chapter to the latex body
                    latex_body.append(lutils.create_section(sectionTitle))
                    
                    # Add a white page
                    if 'addWhiteAfter' in od_resources_s[s_k]:
                        latex_body.append(lutils.insert_pdf_file(blankPDF)) 
                    
                    # are there files?
                    #sectionFiles = filter(os.path.isfile, os.listdir(rootPath + chapterPath + sectionPath)) 
                    
                    # are there files?
                    sectionFiles = [i for i in os.listdir(rootPath + chapterPath + sectionPath) 
                                    if os.path.isfile(rootPath + chapterPath + sectionPath + i)]
                                        
                    # Sort the names as lexicographical order                    
                    for f in sorted(sectionFiles):
                        
                        if '##' not in f:                         
                            # insert pdf file
                            latex_body.append(lutils.insert_pdf_file(os.path.abspath(rootPath + chapterPath + sectionPath + f)))
                                               
                    # Ordering sub-section by keys
                    od_resources_sub = dutils.sort_dictionary(resources[c_k][s_k], order_by='key', order='asc')
                    
                    # Get the sub-sections in this section
                    for sub_k,sub_v in od_resources_sub.items():
                         
                        #print("key_sub >> " + sub_k) 
                        # Subsection
                        if sub_k.startswith(SUBSECTION):                            
                            print("found subsection >> " + sub_k)
                            # Get title and chapter path
                            subsectionTitle = od_resources_sub[sub_k][SECTION_T]
                            subsectionPath = od_resources_sub[sub_k][SECTION_P]
                            
                            # Add a white page
                            if 'addWhiteBefore' in od_resources_sub[sub_k]:
                                latex_body.append(lutils.insert_pdf_file(blankPDF))
            
                            # Add the chapter to the latex body
                            latex_body.append(lutils.create_subsection(subsectionTitle))
                            
                            # Add a white page
                            if 'addWhiteAfter' in od_resources_sub[sub_k]:
                                latex_body.append(lutils.insert_pdf_file(blankPDF))
                                
                            # are there files?
                            subsectionFiles = [i for i in os.listdir(rootPath + chapterPath + sectionPath + subsectionPath) 
                                               if os.path.isfile(rootPath + chapterPath + sectionPath + subsectionPath + i)]
                    
                            # Sort the names as lexicographical order                    
                            for f in sorted(subsectionFiles):                                                                            
                        
                                if '##' not in f:
                                    # insert pdf file
                                    latex_body.append(lutils.insert_pdf_file(os.path.abspath(rootPath + chapterPath + sectionPath + subsectionPath + f)))
                                                         
    
    # Write latex body
    with open('body.tex','w') as fl:
        fl.write("\n".join(latex_body))
        
    # Copy body generated file to latex project
    latexTemplatePath = config_params.get_config()['GeneralParams']['latexTemplatePath']
    shutil.copyfile('body.tex',latexTemplatePath + 'body.tex')
    
    
if __name__ == '__main__':
    main()

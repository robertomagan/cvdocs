###
cvdocs
Sumarizing your CV documents quickly and easily!

Pre-requisites
--------------
This software has been developed in python so you can import the following packages to your python 3 (or higher) environment:
- YAML 0.1.6 (pip install pyyaml)

Package structure
-----------------
- config/ --> configuration files 
- examples/documents/ --> contains folders and documents that will be added to the output LATEX CV document
- examples/templates/ --> contains the LATEX template used 

How to
------
1. Set up the configuration file _config.yaml_ located in _config_ folder. The structure and params to be configured are self-explained and described in _config.yaml_.
2. Run python3 main.py This generates the body latex file (body.tex) built and copied to the corresponding latex template. See the attached example.
3. Compile the complete LATEX document
4. See the results and enjoy!

Notes
-----
Some useful notes:
- The script searchs for PDF documents in the folder hierarchy configured in _config.yaml_.
- The files found in a specific folder are lexicographycally ordered.
- Double slash ## found in the file name means that this file is excluded.
- You can add blank PDF files either before a section/subsection/chapter or after them by using the corresponding configuration param in the _config.yaml_ (See the examples)

Future work
-----------
Comments and contributions will be very appreciated ;)







# **CVdocs v1.0**
Building and compiling all your CV documents easy and quickly!

Pre-requisites
--------------
This software has been developed in python so you must be sure that the following packages are previously added to your python 3 (or higher) environment:
- YAML 0.1.6 (pip install pyyaml)

Package structure
-----------------
- **config/** --> _configuration files_
- **examples/documents/** --> _contains folders and documents that will be added to the output LATEX CV document_
-**examples/templates/** --> _contains the LATEX template used_
- **log/** --> _script log folder (see config/logging.yaml config file)_ 

How to
------
1. Set up the configuration file _config.yaml_ located in _config_ folder. The structure and params to be configured are self-explained and described in _config.yaml_.
2. Run **python3 main.py** This generates the body latex file (body.tex). After that it is copied to the corresponding latex template location. See the attached example.
3. Compile the complete LATEX document (i.e, the project.tex document located in the latex folder)
4. See the results and enjoy!

Notes
-----
Some useful notes:
- The script searchs for PDF documents through the folder hierarchy previously configured in _config.yaml_.
- The files found in these folders are lexicographycally ordered to be inserted in the output latex file.
- Double slash ## found in the file name means that it will be excluded from the compilation. In others word, it will not be  appear en the final latex document.
- You can add blank PDF files either before a section/subsection/chapter or after them by using the corresponding configuration param in the _config.yaml_ (See the examples)

LATEX
-----
The script and LATEX files use the following LATEX package:
- **\usepackage{pdfpages}**

The user can set up the way of the PDF are inserted and compiled in LATEX, just modifying the next package directive (see project.tex for more information):
- **\includepdfset{**pages=-, pagecommand=\thispagestyle{plain}, openright=false, linktodoc=true**}**

Issues & questions
------------------
Comments and contributions will be very appreciated ;)








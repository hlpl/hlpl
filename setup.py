#! /usr/bin/python
from setuptools  import setup
import os
import sys
import platform
import configparser

from io import open
# to install type:
# python setup.py install --root=/
LONG_DESCRIPTION=open('README.md','r',encoding='utf8').read()        
        
if sys.version_info[0] < 3:
    raise Exception(
        'You are tying to install ChatterBot on Python version {}.\n'
        'Please install ChatterBot in Python 3 instead.'.format(
            platform.python_version()
        )
    )
    
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'hlpl/setup.cfg')
config.read(config_file_path)

VERSION = config['hlpl']['version']
AUTHOR = config['hlpl']['author']
AUTHOR_EMAIL = config['hlpl']['email']
URL = config['hlpl']['url']


projects_urls={}
for i in range(4,len(list(config['hlpl'].keys()))):
    x=list(config['hlpl'].keys())[i]
    y=x
    y=y[0:len(y)-4]
    projects_urls[y]=config['hlpl'][x]
    

setup (name='hlpl', version=VERSION,
      description='A Programming Language for Human Life ',
      long_description_content_type='text/markdown',  
      long_description = LONG_DESCRIPTION,       
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=URL+'/download/',
      project_urls=projects_urls,      
      python_requires='>=3, <=3.9',
      license='MIT',
      platform="OS independent",
      keywords=['hlpl', 'hlpl docs', 'hlpl composer', 'hlpl templater', 'hlpl transcriber', 'hlpl press', 'hlpl character', 'hlpl photographer', 'hlpl graphis', 'human life programming language'],
      package_dir={'hlpl': 'hlpl',},
      packages=['hlpl',],
      install_requires=[ 'hlpl_graphics','hlpl_photographer','hlpl_character','hlpl_press','hlpl_transcriber','hlpl_templater','hlpl_composer',
      ],         
      include_package_data=True,
      entry_points ={
        'console_scripts': [
                'hlpl = hlpl.__main__:main',
            ]},   
      classifiers=[
          'Framework :: Robot Framework',
          'Framework :: Robot Framework :: Library',
          'Framework :: Robot Framework :: Tool',
          'Natural Language :: Arabic',
          'Natural Language :: English',
          ],
                  
    );

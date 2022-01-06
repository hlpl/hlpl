import configparser
import sys
import os
import hlpl_graphics,hlpl_photographer,hlpl_character,hlpl_press,hlpl_transcriber,hlpl_templater,hlpl_composer

def get_hlpl_version(case):
    config = configparser.ConfigParser()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, 'setup.cfg')
    config.read(config_file_path)
    if case=='version':
       return config['hlpl']['version']
    if case=='hlpl':
       st='version: '+config['hlpl']['version']+'\n'+'site: '+config['hlpl']['url']+'\n'+'email: '+config['hlpl']['email']+'\n'+'author: '+config['hlpl']['author']+'\n'
       return st
    if case=='version':
       return 'hlpl version: '+config['hlpl']['version']   
    
def main():
    if 'version' in sys.argv:
        print('\n'+get_hlpl_version('version'))
    elif 'composer' in sys.argv:
        print('\n'+'hlpl composer under developement, it will be released next HLPL vesrions')
    elif 'templater' in sys.argv:
        print('\n'+'hlpl templater under developement, it will be released next HLPL vesrions')
    elif 'transcriber' in sys.argv:
        print('\n'+'hlpl transcriber under developement, it will be released next HLPL vesrions')
    elif 'press' in sys.argv:
        print('\n'+'hlpl pressunder developement, it will be released next HLPL vesrions')
    elif 'character' in sys.argv:
        print('\n'+'hlpl character under developement, it will be released next HLPL vesrions')
    elif 'photographer' in sys.argv:
        print('\n'+'hlpl photographer under developement, it will be released next HLPL vesrions')
    elif 'graphics' in sys.argv:
        print('\n'+'hlpl graphicsunder developement, it will be released next HLPL vesrions')
    else:
        print('\n'+get_hlpl_version('hlpl'))
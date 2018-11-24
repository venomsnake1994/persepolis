#!/usr/bin/env python3
# coding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import os
import warnings
import sys
import shutil
import platform


# lists of the os platforms    the program supporting 
os_lists = ['Linux', 'FreeBSD', 'OpenBSD']

py_dependencies = ['PyQt5', 'requests ', 'setproctitle',
               'psutil', 'youtube_dl', 'sys']

dependencies = ['aria2c', 'paplay', 'notify-send']


not_installed = []

setuptools_available = False

os_type = platform.system()


def os_checker(os_type):
    if os_type in os_lists:
        from setuptools import setup, Command, find_packages
        setuptools_available = True
    else:
        print('<!> Incompatible os Platform for running "setup.py"  script')
        sys.exit()

def seperator(sep='-'):
    """simple function for make output nicer """
    print(sep * 60)

#function for  preventing the code  repetion
def py_dependencie_checker(dependencies):
    """ check requirement modules for import """
    for index, module in enumerate(dependencies):
        try:
            exec('import {}'.format(module))
            seperator()
            print("Requirement already satisfied  {}".format(module))
        except:
            not_installed.append(module)
            seperator()
            print('Error : {} is not installed!'.format(module))
        
    
def dependencie_checker(dependencies):
    
    for index, name in enumerate(dependencies):
        answer = os.system('{} --version 1>/dev/null'.format(dependencies))
        if answer != 0:
            #print('Error: {} is Not installed!'.format(dependencies))
            seperator()
            not_installed.append(dependencies)
        else:
            print('{} is found!'.format(dependencies))         
            seperator()


os_checker(os_type)

py_dependencies(py_dependencies)

dependencie_checker(dependencies)



# sound-theme-freedesktop
if os_type == 'Linux':
    notifications_path = '/usr/share/sounds/freedesktop/stereo/'
elif os_type == 'FreeBSD' or os_type == 'OpenBSD':
    notifications_path = '/usr/local/share/sounds/freedesktop/stereo/'

if os.path.isdir(notifications_path):
    print('sound-theme-freedesktop is found!')
else:
    print('Warning: sound-theme-freedesktop is not installed! you need this package for sound notifications!')
    not_installed = not_installed + 'sound-theme-freedesktop'

# show warning , if dependencies not installed!
if not_installed != '':
    print('########################')
    print('####### WARNING ########')
    print('########################')
    print('Some dependencies are not installed .It causes some problems for persepolis! : \n')
    print(not_installed )
    print('Read this link for more information: \n')
    print('https://github.com/persepolisdm/persepolis/wiki/git-installation-instruction\n\n')
    answer = input('Do you want to continue?(y/n)')
    if answer.upper().startswith('N'):
        sys.exit(1)

#if sys.argv[1] == "test":
 #   print('Unittest is not avaiable')  
  #  sys.exit()

DESCRIPTION = 'Persepolis Download Manager'

if os_type == 'Linux':
    DATA_FILES = [
        ('/usr/share/man/man1/', ['man/persepolis.1.gz']),
        ('/usr/share/applications/', ['xdg/com.github.persepolisdm.persepolis.desktop']),
        ('/usr/share/metainfo/', ['xdg/com.github.persepolisdm.persepolis.appdata.xml']),
        ('/usr/share/pixmaps/', ['resources/persepolis.svg']),
        ('/usr/share/pixmaps/', ['resources/persepolis-tray.svg'])
        ]
elif os_type == 'FreeBSD' or os_type == 'OpenBSD':
    DATA_FILES = [
        ('/usr/local/share/man/man1/', ['man/persepolis.1.gz']),
        ('/usr/local/share/applications/', ['xdg/com.github.persepolisdm.persepolis.desktop']),
        ('/usr/local/share/metainfo/', ['xdg/com.github.persepolisdm.persepolis.appdata.xml']),
        ('/usr/local/share/pixmaps/', ['resources/persepolis.svg']),
        ('/usr/local/share/pixmaps/', ['resources/persepolis-tray.svg'])
        ]



# finding current directory
cwd = os.path.abspath(__file__)
setup_dir = os.path.dirname(cwd)

#clearing __pycache__
src_pycache = os.path.join(setup_dir, 'persepolis', '__pycache__')
gui_pycache = os.path.join(setup_dir, 'persepolis', 'gui', '__pycache__')
scripts_pycache = os.path.join(setup_dir, 'persepolis', 'scripts', '__pycache__')

for folder in [src_pycache, gui_pycache, scripts_pycache]:
    if os.path.isdir(folder):
        shutil.rmtree(folder)
        print(str(folder)
            + ' is removed!')



# Creating man page file
persepolis_man_page = os.path.join(setup_dir, 'man', 'persepolis.1')
os.system('gzip -f -k -9 "'
        + persepolis_man_page
        + '"')
print('man page file is generated!')


setup(
    name = 'persepolis',
    version = '3.1.0',
    license = 'GPL3',
    description = DESCRIPTION,
    long_description = DESCRIPTION,
    include_package_data = True,
    url = 'https://github.com/persepolisdm/persepolis',
    author = 'AliReza AmirSamimi',
    author_email = 'alireza.amirsamimi@gmail.com',
    maintainer = 'AliReza AmirSamimi',
    maintainer_email = 'alireza.amirsamimi@gmail.com',
    packages = (
        'persepolis',
        'persepolis.scripts', 'persepolis.gui',
        ),
    data_files = DATA_FILES,
    entry_points={
        'console_scripts': [
              'persepolis = persepolis.__main__'
        ]
    }
)


#!C:/Users/tmoodey/Desktop/AI_U-nets\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==38.5.1','console_scripts','easy_install-3.5'
__requires__ = 'setuptools==38.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==38.5.1', 'console_scripts', 'easy_install-3.5')()
    )

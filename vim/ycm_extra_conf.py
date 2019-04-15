import os
import ycm_core

flags = [
'-std=c++11',
'-I./include',
'-I../include',
'-I../lib/include',
'-I../../lib/include'
]

def FlagsForFile( filename, **kwargs ):
    return { 'flags': flags }


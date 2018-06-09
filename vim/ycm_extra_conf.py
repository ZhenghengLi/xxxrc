import os
import ycm_core

flags = [
'-std=c++11',
'-I./include',
'-I../include',
'-I../lib/include',
'-I../../lib/include',
'-I/usr/include',
'-I/usr/include/c++/5',
'-I/opt/mark/ROOT/ROOT_6.12.06/include',
'-I/opt/mark/GEANT4/GEANT4_10.04.p01/include/Geant4'
]

def FlagsForFile( filename, **kwargs ):
    return { 'flags': flags }


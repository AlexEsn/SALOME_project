#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/sasch/OneDrive/Рабочий стол')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("Number_Boxs", 20)
notebook.set("Length_Box1", 1000)
notebook.set("Widht_Box1", 1000)
notebook.set("Height_Box1", 100)
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(10, 10, 10)
Multi_Translation_1 = geompy.MakeMultiTranslation1D(Box_1, OX, 15, "Number_Boxs")
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Multi_Translation_1, 'Multi-Translation_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()

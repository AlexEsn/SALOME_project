#!/usr/bin/env python

#####################################
import sys
import salome
salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/sasch/OneDrive/Рабочий стол')
import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
geompy = geomBuilder.New()
######################################
####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("Number_Boxs", 50)
notebook.set("Length_Box1", 1000)
notebook.set("Widht_Box1", 1000)
notebook.set("Height_Box1", 100)
Number_Boxs = notebook.get("Number_Boxs")
Length_Box1 = notebook.get("Length_Box1")
Widht_Box1 = notebook.get("Widht_Box1")
Height_Box1 = notebook.get("Height_Box1")
####################################################
##        End of NoteBook variables section       ##
####################################################
Height_Boxs = Height_Box1 * 5
Length_Boxs = Length_Box1/Number_Boxs/2
Widht_Box1 = Widht_Box1
Boxs = []
Translations = []
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
#######################################

Box_1 = geompy.MakeBoxDXDYDZ(Length_Box1, Widht_Box1, Height_Box1)
Box_1 = geompy.addToStudy( Box_1, 'Box_1' )

i = Number_Boxs
while i >= 0:
  Boxs.append(geompy.MakeBoxDXDYDZ(Length_Boxs, Widht_Box1, Height_Boxs))
  i = i - 1

i = Number_Boxs
j = 0
while i >= 0:
  Translations.append(geompy.MakeTranslation(Boxs[i], j, 0, 0))
  j = j + (Length_Boxs * 2)
  i = i - 1

i = Number_Boxs
while i >= 0:
  geompy.addToStudy( Translations[i], 'Translations' )
  i = i - 1

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
  

gg = salome.ImportComponentGUI("GEOM")
gg.createAndDisplayGO(Box_1)
gg.setDisplayMode(Box_1,1)
gg.setVectorsMode(Box_1, 1)
gg.setVerticesMode(Box_1, 1)
gg.setNameMode(Box_1, 1)
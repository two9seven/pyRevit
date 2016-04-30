'''
Copyright (c) 2014-2016 Ehsan Iran-Nejad
Python scripts for Autodesk Revit

This file is part of pyRevit repository at https://github.com/eirannejad/pyRevit

pyRevit is a free set of scripts for Autodesk Revit: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See this link for a copy of the GNU General Public License protecting this package.
https://github.com/eirannejad/pyRevit/blob/master/LICENSE
'''

__window__.Close()
from Autodesk.Revit.UI.Selection import ISelectionFilter
from System.Collections.Generic import List
from Autodesk.Revit.DB import ElementId

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


class pickByCategorySelectionFilter(ISelectionFilter):
    def __init__(self, catName):
        self.category = catName

    def AllowElement(self, element):
        if self.category in element.Category.Name:
            return True
        else:
            return False

    def AllowReference(self, refer, point):
        return false


def pickByCategory(catName):
    sel = pickByCategorySelectionFilter(catName)
    list = uidoc.Selection.PickElementsByRectangle(sel)
    set = []
    for el in list:
        set.append(el.Id)
    uidoc.Selection.SetElementIds(List[ElementId](set))


pickByCategory("Column")

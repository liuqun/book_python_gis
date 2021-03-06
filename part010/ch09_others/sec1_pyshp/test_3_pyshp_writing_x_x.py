#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import shapefile
w = shapefile.Writer('xx_pyshp_1')
###############################################################################
w.close()
###############################################################################
import shapefile
with shapefile.Writer('xx_pyshp_2') as w:
    pass
###############################################################################
from io import BytesIO
shp = BytesIO(); shx = BytesIO(); dbf = BytesIO()
w = shapefile.Writer(shp=shp, shx=shx, dbf=dbf)
###############################################################################
w = shapefile.Writer('xx_pyshp_3', shapeType=1)
w.shapeType
###############################################################################
w.shapeType = 3
w.shapeType
###############################################################################
w.autoBalance = 1
###############################################################################
w.balance()
###############################################################################
w = shapefile.Writer('xx_pyshp_4')
w.field('FIRST_FLD')
w.field('SECOND_FLD','C','40')
###############################################################################
w.record('First','Point')
w.record('Second','Point')
###############################################################################
w.balance()
w.close()
###############################################################################
w = shapefile.Writer('xx_pyshp_5')
w.field('NAME')
w.point( 91  , 29.6)
w.point(125.35 , 43.88333)
w.record('LaSa')
w.record('ChangChun')
w.close()
###############################################################################
w = shapefile.Writer('xx_pyshp_6', shapefile.POLYLINE)
w.line([[[1,3],[5,3]]])
###############################################################################
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.field('FIRST_FLD','C','40')
w.record('First')
w.record('Second')
w.close()
###############################################################################
w = shapefile.Writer('xx_pyshp_7')
w.field('name', 'C')
w.poly([
    [[4,4], [4,8], [8,8], [8,4]],
    [[6,7], [7,5], [5,5]],
    [[9,4], [9,6], [10,4]]
    ])
w.record('polygon1')
w.close()
###############################################################################
w = shapefile.Writer('xx_pyshp_8', shapeType=1)
w.field('NAME')
w.null()
###############################################################################
w.record('null')
w.close()

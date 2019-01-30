# Copyright (c) 2014-2018, Manfred Moitzi
# License: MIT License
# Just one header var definition for all DXF version needed, because AutoCAD ignores unknown header vars
from functools import partial

from ezdxf.lldxf.hdrvars import SingleValue, Point2D, Point3D

VARMAP = {
    '$ACADVER': partial(SingleValue, code=1),
    '$ANGBASE': partial(SingleValue, code=50),
    '$ANGDIR': partial(SingleValue, code=70),
    '$ATTDIA': partial(SingleValue, code=70),
    '$ATTMODE': partial(SingleValue, code=70),
    '$ATTREQ': partial(SingleValue, code=70),
    '$AUNITS': partial(SingleValue, code=70),  # 0: decimal degrees; 1: deg/min/sec; 2: grad; 3: radians; 4: surveyor's units
    '$AUPREC': partial(SingleValue, code=70),
    '$BLIPMODE': partial(SingleValue, code=70),
    '$CECOLOR': partial(SingleValue, code=62),
    '$CELTYPE': partial(SingleValue, code=6),
    '$CHAMFERA': partial(SingleValue, code=40),
    '$CHAMFERB': partial(SingleValue, code=40),
    '$CLAYER': partial(SingleValue, code=8),
    '$COORDS': partial(SingleValue, code=70),
    '$DIMALT': partial(SingleValue, code=70),
    '$DIMALTD': partial(SingleValue, code=70),
    '$DIMALTF': partial(SingleValue, code=40),
    '$DIMAPOST': partial(SingleValue, code=1),
    '$DIMASO': partial(SingleValue, code=70),
    '$DIMASZ': partial(SingleValue, code=40),
    '$DIMBLK': partial(SingleValue, code=1),
    '$DIMBLK1': partial(SingleValue, code=1),
    '$DIMBLK2': partial(SingleValue, code=1),
    '$DIMCEN': partial(SingleValue, code=40),
    '$DIMCLRD': partial(SingleValue, code=70),
    '$DIMCLRE': partial(SingleValue, code=70),
    '$DIMCLRT': partial(SingleValue, code=70),
    '$DIMDLE': partial(SingleValue, code=40),
    '$DIMDLI': partial(SingleValue, code=40),
    '$DIMEXE': partial(SingleValue, code=40),
    '$DIMEXO': partial(SingleValue, code=40),
    '$DIMGAP': partial(SingleValue, code=40),
    '$DIMLFAC': partial(SingleValue, code=40),
    '$DIMLIM': partial(SingleValue, code=70),
    '$DIMPOST': partial(SingleValue, code=1),
    '$DIMRND': partial(SingleValue, code=40),
    '$DIMSAH': partial(SingleValue, code=70),
    '$DIMSCALE': partial(SingleValue, code=40),
    '$DIMSE1': partial(SingleValue, code=70),
    '$DIMSE2': partial(SingleValue, code=70),
    '$DIMSHO': partial(SingleValue, code=70),
    '$DIMSOXD': partial(SingleValue, code=70),
    '$DIMSTYLE': partial(SingleValue, code=2),
    '$DIMTAD': partial(SingleValue, code=70),
    '$DIMTFAC': partial(SingleValue, code=40),
    '$DIMTIH': partial(SingleValue, code=70),
    '$DIMTIX': partial(SingleValue, code=70),
    '$DIMTM': partial(SingleValue, code=40),
    '$DIMTOFL': partial(SingleValue, code=70),
    '$DIMTOH': partial(SingleValue, code=70),
    '$DIMTOL': partial(SingleValue, code=70),
    '$DIMTP': partial(SingleValue, code=40),
    '$DIMTSZ': partial(SingleValue, code=40),
    '$DIMTVP': partial(SingleValue, code=40),
    '$DIMTXT': partial(SingleValue, code=40),
    '$DIMZIN': partial(SingleValue, code=70),
    '$DWGCODEPAGE': partial(SingleValue, code=3),
    '$DRAGMODE': partial(SingleValue, code=70),
    '$ELEVATION': partial(SingleValue, code=40),
    '$EXTMAX': Point3D,
    '$EXTMIN': Point3D,
    '$FILLETRAD': partial(SingleValue, code=40),
    '$FILLMODE': partial(SingleValue, code=70),
    '$HANDLING': partial(SingleValue, code=70),
    '$HANDSEED': partial(SingleValue, code=5),
    '$INSBASE': Point3D,
    '$LIMCHECK': partial(SingleValue, code=70),
    '$LIMMAX': Point2D,
    '$LIMMIN': Point2D,
    '$LTSCALE': partial(SingleValue, code=40),
    '$LUNITS': partial(SingleValue, code=70),
    '$LUPREC': partial(SingleValue, code=70),
    '$MAXACTVP': partial(SingleValue, code=70),
    '$MENU': partial(SingleValue, code=1),
    '$MIRRTEXT': partial(SingleValue, code=70),
    '$ORTHOMODE': partial(SingleValue, code=70),
    '$OSMODE': partial(SingleValue, code=70),
    '$PDMODE': partial(SingleValue, code=70),
    '$PDSIZE': partial(SingleValue, code=40),
    '$PELEVATION': partial(SingleValue, code=40),
    '$PEXTMAX': Point3D,
    '$PEXTMIN': Point3D,
    '$PLIMCHECK': partial(SingleValue, code=70),
    '$PLIMMAX': Point2D,
    '$PLIMMIN': Point2D,
    '$PLINEGEN': partial(SingleValue, code=70),
    '$PLINEWID': partial(SingleValue, code=40),
    '$PSLTSCALE': partial(SingleValue, code=70),
    '$PUCSNAME': partial(SingleValue, code=2),
    '$PUCSORG': Point3D,
    '$PUCSXDIR': Point3D,
    '$PUCSYDIR': Point3D,
    '$QTEXTMODE': partial(SingleValue, code=70),
    '$REGENMODE': partial(SingleValue, code=70),
    '$SHADEDGE': partial(SingleValue, code=70),
    '$SHADEDIF': partial(SingleValue, code=70),
    '$SKETCHINC': partial(SingleValue, code=40),
    '$SKPOLY': partial(SingleValue, code=70),
    '$SPLFRAME': partial(SingleValue, code=70),
    '$SPLINESEGS': partial(SingleValue, code=70),
    '$SPLINETYPE': partial(SingleValue, code=70),
    '$SURFTAB1': partial(SingleValue, code=70),
    '$SURFTAB2': partial(SingleValue, code=70),
    '$SURFTYPE': partial(SingleValue, code=70),
    '$SURFU': partial(SingleValue, code=70),
    '$SURFV': partial(SingleValue, code=70),
    '$TDCREATE': partial(SingleValue, code=40),
    '$TDINDWG': partial(SingleValue, code=40),
    '$TDUPDATE': partial(SingleValue, code=40),
    '$TDUSRTIMER': partial(SingleValue, code=40),
    '$TEXTSIZE': partial(SingleValue, code=40),
    '$TEXTSTYLE': partial(SingleValue, code=7),
    '$THICKNESS': partial(SingleValue, code=40),
    '$TILEMODE': partial(SingleValue, code=70),
    '$TRACEWID': partial(SingleValue, code=40),
    '$UCSNAME': partial(SingleValue, code=2),
    '$UCSORG': Point3D,
    '$UCSXDIR': Point3D,
    '$UCSYDIR': Point3D,
    '$UNITMODE': partial(SingleValue, code=70),
    '$USERI1': partial(SingleValue, code=70),
    '$USERI2': partial(SingleValue, code=70),
    '$USERI3': partial(SingleValue, code=70),
    '$USERI4': partial(SingleValue, code=70),
    '$USERI5': partial(SingleValue, code=70),
    '$USERR1': partial(SingleValue, code=40),
    '$USERR2': partial(SingleValue, code=40),
    '$USERR3': partial(SingleValue, code=40),
    '$USERR4': partial(SingleValue, code=40),
    '$USERR5': partial(SingleValue, code=40),
    '$USRTIMER': partial(SingleValue, code=70),
    '$VISRETAIN': partial(SingleValue, code=70),
    '$WORLDVIEW': partial(SingleValue, code=70),
}

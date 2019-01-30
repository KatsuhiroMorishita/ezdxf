# Purpose: using DIMENSION horizontal, vertical and rotated
# Created: 29.12.2018
# Copyright (c) 2018-2019, Manfred Moitzi
# License: MIT License
import ezdxf

import pathlib
OUTDIR = pathlib.Path(r'C:\Users\manfred\Desktop\Outbox')


def linear_tutorial_R12():
    dwg = ezdxf.new('R12', setup=True)
    msp = dwg.modelspace()

    msp.add_line((0, 0), (3, 0))

    # horizontal DIMENSION
    # Default DimStyle EZDXF: 1 drawing unit == 1m; scale 1: 100; length_factor=100 -> measurement in cm
    #
    # base: defines the dimension line, ezdxf accepts any point on the dimension line
    # ext1: defines the start point of the first extension line, which also defines the first point to measure
    # ext2: defines the start point of the second extension line, which also defines the second point to measure
    dim = msp.add_linear_dim(base=(3, 2), ext1=(0, 0), ext2=(3, 0), dimstyle='EZDXF')
    # necessary second step, to create the BLOCK entity with the DIMENSION geometry.
    # ezdxf supports DXF R2000 attributes for DXF R12 rendering, but they have to be applied by the DIMSTYLE override
    # feature, this additional attributes are not stored in the DIMSTYLE entity, they are just used to render the DIMENSION
    # entity.
    msp.render_dimension(dim, override=dim.dimstyle_override({'dimtxsty': 'OpenSans'}))

    # rotated DIMENSION without `override` uses DEFAULT_DIM_TEXT_STYLE="OPEN_SANS_CONDENSED_LIGHT"
    # angle: defines the angle of the dimension line, measurement is the distance between first and second measurement point
    # in direction of `angle`
    dim2 = msp.add_linear_dim(base=(10, 2), ext1=(7, 0), ext2=(10, 0), angle=-30, dimstyle='EZDXF')
    style = dim2.dimstyle_override(dxfattribs={
        'dimdle': 0.,
    })
    # some variables have setter methods for convenience.
    style.set_arrows(blk=ezdxf.ARROWS.closed_filled, size=.25)
    style.set_align(halign='right')
    msp.render_dimension(dim2, override=style)
    dwg.saveas(OUTDIR / 'dim_linear_R12_tutorial.dxf')


def linear_tutorial_R2007():
    dwg = ezdxf.new('R2007', setup=True)
    msp = dwg.modelspace()

    msp.add_line((0, 0), (10, 0))

    # horizontal DIMENSION
    # Default DimStyle EZDXF: 1 drawing unit == 1m; scale 1: 100; length_factor=100 -> measurement in cm
    #
    # base: defines the dimension line, ezdxf accepts any point on the dimension line
    # ext1: defines the start point of the first extension line, which also defines the first point to measure
    # ext2: defines the start point of the second extension line, which also defines the second point to measure
    dim = msp.add_linear_dim(base=(3, 2), ext1=(0, 0), ext2=(10, 0), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs={
        'dimdle': 0.,
        'dimexe': .5,  # length of extension line above dimension line
        'dimexfix': 1,  # fix length extension line
        'dimexlen': .5,  # length of extension line below dimension line
    })
    style.set_align(valign='center')
    style.set_arrows(size=.25)
    msp.render_dimension(dim, override=style)

    # text and arrows outside
    attribs = {
        'dimdle': 0.,
        'dimexe': .5,  # length of extension line above dimension line
        'dimexfix': 1,  # fix length extension line
        'dimexlen': .5,  # length of extension line below dimension line
    }
    x, y = 15, 0
    dim = msp.add_linear_dim(base=(x, y+2), ext1=(x, y), ext2=(x+.3, y), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs=attribs)
    style.set_arrows(blk=ezdxf.ARROWS.closed_filled, size=.25)
    style.set_align(valign='center')
    msp.render_dimension(dim, override=style)

    # text and arrows outside
    x, y = 15, 5
    dim = msp.add_linear_dim(base=(x, y + 2), ext1=(x, y), ext2=(x + .3, y), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs=attribs)
    style.set_arrows(blk=ezdxf.ARROWS.closed_filled, size=.25)
    style.set_align(valign='above')
    msp.render_dimension(dim, override=style)

    # text and arrows outside
    x, y = 15, 10
    dim = msp.add_linear_dim(base=(x, y + 2), ext1=(x, y), ext2=(x + .3, y), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs=attribs)
    style.set_arrows(blk=ezdxf.ARROWS.closed_filled, size=.25)
    style.set_align(valign='below')
    msp.render_dimension(dim, override=style)

    # text outside with ticks
    x, y = 20, 0
    dim = msp.add_linear_dim(base=(x, y+2), ext1=(x, y), ext2=(x+.3, y), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs=attribs)
    style.set_tick(size=.25)
    style.set_align(valign='center')
    msp.render_dimension(dim, override=style)

    # text outside with ticks
    x, y = 20, 5
    dim = msp.add_linear_dim(base=(x, y + 2), ext1=(x, y), ext2=(x + .3, y), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs=attribs)
    style.set_tick(size=.25)
    style.set_align(valign='above')
    msp.render_dimension(dim, override=style)

    # text outside with ticks
    x, y = 20, 10
    dim = msp.add_linear_dim(base=(x, y + 2), ext1=(x, y), ext2=(x + .3, y), dimstyle='EZDXF')
    style = dim.dimstyle_override(dxfattribs=attribs)
    style.set_tick(size=.25)
    style.set_align(valign='below')
    msp.render_dimension(dim, override=style)

    dwg.saveas(OUTDIR / 'dim_linear_R2007_tutorial.dxf')


def linear_all_arrow_style(version='R12', dimltype=None, dimltex1=None, dimltex2=None, filename=""):
    dwg = ezdxf.new(version, setup=True)
    msp = dwg.modelspace()
    ezdxf_dimstyle = dwg.dimstyles.get('EZDXF')
    ezdxf_dimstyle.copy_to_header(dwg)

    for index, name in enumerate(sorted(ezdxf.ARROWS.__all_arrows__)):
        y = index * 4

        dim = msp.add_linear_dim(base=(3, y+2), ext1=(0, y), ext2=(3, y), dimstyle='EZDXF')

        attributes = {
            'dimtxsty': 'LiberationMono',
            'dimdle': 0.5,
        }

        if dimltype:
            attributes['dimltype'] = dimltype
        if dimltex1:
            attributes['dimltex1'] = dimltex1
        if dimltex2:
            attributes['dimltex2'] = dimltex2

        style = dim.dimstyle_override(attributes)
        style.set_arrows(blk=name, size=.25)
        msp.render_dimension(dim, override=style)
    if not filename:
        filename = 'all_arrow_styles_dim_{}.dxf'.format(version)

    dwg.saveas(OUTDIR / filename)


def linear_tutorial_ext_lines():
    dwg = ezdxf.new('R12', setup=True)
    msp = dwg.modelspace()

    msp.add_line((0, 0), (3, 0))

    dim = msp.add_linear_dim(base=(3, 2), ext1=(0, 0), ext2=(3, 0), dimstyle='EZDXF')
    attributes = {
        'dimexo': 0.5,
        'dimexe': 0.5,
        'dimdle': 0.5,
        'dimblk': ezdxf.ARROWS.none,
        'dimclrt': 3,
    }
    style = dim.dimstyle_override(attributes)
    msp.render_dimension(dim, override=style)

    attributes = {
        'dimtad': 4,
        'dimclrd': 2,
        'dimclrt': 4,
    }
    dim = msp.add_linear_dim(base=(10, 2), ext1=(7, 0), ext2=(10, 0), angle=-30, dimstyle='EZDXF')
    msp.render_dimension(dim, override=dim.dimstyle_override(attributes))

    dim = msp.add_linear_dim(base=(3, 5), ext1=(0, 10), ext2=(3, 10), dimstyle='EZDXF')
    msp.render_dimension(dim, override=dim.dimstyle_override(attributes))

    dwg.saveas(OUTDIR / 'dim_linear_R12_ext_lines.dxf')


def linear_EZ_M(fmt):
    dwg = ezdxf.new('R12', setup=True)
    msp = dwg.modelspace()
    ezdxf.setup_dimstyle(dwg, fmt)

    msp.add_line((0, 0), (1, 0))
    dim = msp.add_linear_dim(base=(0, .1), ext1=(0, 0), ext2=(1, 0), dimstyle=fmt)
    msp.render_dimension(dim)
    dwg.saveas(OUTDIR / f'dim_linear_R12_{fmt}.dxf')


def linear_EZ_CM(fmt):
    dwg = ezdxf.new('R12', setup=True)
    msp = dwg.modelspace()
    ezdxf.setup_dimstyle(dwg, fmt)

    msp.add_line((0, 0), (100, 0))
    dim = msp.add_linear_dim(base=(0, 10), ext1=(0, 0), ext2=(100, 0), dimstyle=fmt)
    msp.render_dimension(dim)
    dwg.saveas(OUTDIR / f'dim_linear_R12_{fmt}.dxf')


def linear_EZ_MM(fmt):
    dwg = ezdxf.new('R12', setup=True)
    msp = dwg.modelspace()
    ezdxf.setup_dimstyle(dwg, fmt)

    msp.add_line((0, 0), (1000, 0))
    dim = msp.add_linear_dim(base=(0, 100), ext1=(0, 0), ext2=(1000, 0), dimstyle=fmt)
    msp.render_dimension(dim)
    dwg.saveas(OUTDIR / f'dim_linear_R12_{fmt}.dxf')


ALL = False


if __name__ == '__main__':
    #linear_tutorial_R12()
    linear_tutorial_R2007()
    linear_all_arrow_style('R12')
    linear_all_arrow_style('R12', dimltex1='DOT2', dimltex2='DOT2', filename='dotted_extension_lines_R12.dxf')
    linear_all_arrow_style('R2000')
    linear_all_arrow_style('R2007', dimltex1='DOT2', dimltex2='DOT2', filename='dotted_extension_lines_R2007.dxf')
    if ALL:
        linear_tutorial_ext_lines()

        linear_EZ_M('EZ_M_100_H25_CM')
        linear_EZ_M('EZ_M_1_H25_CM')

        linear_EZ_CM('EZ_CM_100_H25_CM')
        linear_EZ_CM('EZ_CM_1_H25_CM')

        linear_EZ_MM('EZ_MM_100_H25_MM')
        linear_EZ_MM('EZ_MM_1_H25_MM')


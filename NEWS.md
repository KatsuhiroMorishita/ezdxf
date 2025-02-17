
News
====

Version 0.11a0 - dev
--------------------

- NEW: `Dimension.get_measurement()` supports angular, angular3p and ordinate dimensions
- NEW: `Drawing.set_modelspace_vport()` set initial view/zoom location for the modelspace
- NEW: `Layout.add_radius_dim()` implemented
- NEW: shortcut calls `Layout.add_radius_dim_2p()` and `Layout.add_radius_dim_cra()`
- NEW: `Circle.vertices(angles)`  yields vertices for iterable angles in WCS
- NEW: `Ellipse.vertices(params)`  yields vertices for iterable params in WCS
- NEW: Arc properties `start_point` and `end_point` returns start- and end point of arc in WCS
- NEW: Ellipse properties `start_point` and `end_point` returns start- and end point of ellipse in WCS
- NEW: `Drawing.set_modelspace_vport(height, center)` set initial view/zoom location for the modelspace
- NEW: 2d construction function `ezdxf.math.offset_vertices_2d()`
- NEW: `Drawing.output_encoding`  returns required output encoding
- NEW: `UCS.rotate(axis, angle)` returns a new rotated UCS
- BUGFIX: fixed base point calculation of aligned dimensions
- BUGFIX: fixed length extension line support

Version 0.10.2 - 2019-10-05
---------------------------

- NEW: `Dimension.get_measurement()` returns the actual dimension measurement in WCS units, no scaling applied; angular 
  and ordinate dimension are not supported yet. 
- BUGFIX: ordinate dimension exports wrong feature location
- BUGFIX: `Hatch.set_pattern_fill()` did not set pattern scale, angle and double values

Version 0.10.1 - 2019-09-07
---------------------------

- BUGFIX: group code for header var $ACADMAINTVER is 90 for DXF R2018+ and 70 for previous DXF versions. This is a 
  critical bug because AutoCAD 2012/2013 (and possibly earlier versions) will not open DXF files with the new group 
  code 90 for header variable $ACADMAINTVER.
 
Version 0.10 - 2019-09-01
-------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-10.html
- unified entity system for all DXF versions
- saving as later DXF version than the source DXF version is possible, but maybe data loss if saving as an older DXF 
  version than source DXF version (_ezdxf_ is not a DXF converter)
- templates no more needed and removed from package
- CHANGE: `DXFEntity`
    - renamed `DXFEntity.drawing` to `DXFEntity.doc`
    - `DXFEntity.get_xdata()` keyword `xdata_tag` renamed to `tags`
    - `DXFEntity.set_xdata()` keyword `xdata_tag` renamed to `tags`
    - renamed `DXFEntity.remove_reactor_handle()` renamed to `DXFEntity.discard_reactor_handle()`
    - `DXFEntity.get_extension_dict()` returns `ExtensionDict` object instead of the raw DICTIONARY object
    - renamed `DXFEntity.supports_dxf_attrib()` to `DXFEntity.is_supported_dxf_attrib()`
    - renamed `DXFEntity.dxf_attrib_exists()` to `DXFEntity.has_dxf_attrib()`
- CHANGE: `Layer` entity
    - removed `Layer.dxf.line_weight` as synonym for `Layer.dxf.lineweight`
    - renamed `Layer.dxf.plot_style_name` to `Layer.dxf.plotstyle_handle` 
    - renamed `Layer.dxf.material` to `Layer.dxf.material_handle` 
- CHANGE: same treatment of `Viewport` entity for all DXF versions
- CHANGE: `Polyline.vertices()` is now an attribute `Polyline.vertices`, implemented as regular Python list.
- CHANGE: `Insert.attribs()` is now an attribute `Insert.attribs`, implemented as regular Python list.
- CHANGE: renamed `Viewport.dxf.center_point` to `Viewport.dxf.center` 
- CHANGE: renamed `Viewport.dxf.target_point` to `Viewport.dxf.target`
- CHANGE: direct access to hatch paths (`Hatch.paths`), pattern (`Hatch.pattern`) and gradient (`Hatch.gradient`), 
          context manager to edit this data is not needed anymore, but still available for backward compatibility  
- CHANGE: Options
    - removed `template_dir`, no more needed
    - new `log_unprocessed_tags` to log unprocessed (unknown) DXF tags 
- CHANGE: `Dimension()` removes associated anonymous dimension block at deletion
- CHANGE: safe block deletion protects not explicit referenced blocks like anonymous dimension blocks and arrow blocks
- CHANGE: `Importer` add-on rewritten, API incompatible to previous ezdxf versions, but previous implementation was 
          already broken 
- CHANGE: moved `add_attdef()` to generic layout interface, adding ATTDEF to model- and paperspace is possible
- CHANGE: entity query - exclude DXF types from `'*'` search, by appending type name with a preceding '!' e.g. query for 
  all entities except LINE = `"* !LINE"`
- CHANGE: entity query - removed regular expression support for type name match
- CHANGE: integration of `MTextData` methods into `MText`
- CHANGE: removed  `edit_data`, `get_text`, `set_text` methods from `MText`
- restructured package, module and test file organization
- NEW: support for `Layer.dxf.true_color` and `Layer.dxf.transparency` attributes (DXF R2004+, undocumented)
- NEW: `Layer.rgb`, `Layer.color`, `Layer.description` and `Layer.transparency` properties
- NEW: renaming a `Layer` also renames references to this layer, but use with care
- NEW: support for adding LEADER entities
- NEW: `Dimension.get_geometry_block()`, returns the associated anonymous dimension block or `None`
- NEW: `EntityQuery()` got `first` and `last` properties, to get first or last entity or `None` if query result is empty
- NEW: added `ngon()`, `star()` and `gear()` to `ezdxf.render.forms`
- NEW: Source code generator to create Python source code from DXF entities, to recreate this entities by `ezdxf`. 
  This tool creates only simple structures as a useful starting point for parametric DXF entity creation from existing 
  DXF files. Not all DXF entities are supported!
- NEW: support for named plot style files (STB)
- NEW: can open converted Gerber DXF files tagged as "Version 1.0, Gerber Technology."
- BUGFIX: fixed MTEXT and GEODATA text splitting errors (do not split at '^')
- BUGFIX: fixed some subclass errors, mostly DXF reference errors
- BUGFIX: VERTEX entity inherit `owner` and `linetype` attribute from POLYLINE entity
- BUGFIX: MTEXT - replacement of `\n` by `\P` at DXF export to avoid invalid DXF files.
- tested with CPython 3.8
- removed batch files (.bat) for testing, use `tox` command instead

Version 0.9 - 2019-02-24
------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-9.html
- IMPORTANT: Python 2 support REMOVED, if Python 2 support needed: add `ezdxf<0.9` to your `requirements.txt` 
- NEW: testing on Manjaro Linux in a VM by tox
- CHANGE: converted NEWS.rst to NEWS.md and README.rst to README.md  
- CHANGE: moved `Importer()` from `ezdxf.tools` to `ezdxf.addons` - internal structures of modern DXF files are too complex
  and too undocumented to support importing data in a reliable way - using `Importer()` may corrupt your DXF files or just 
  don't work!
- NEW: type annotations to core package and add-ons.
- NEW: argument `setup` in `ezdxf.new('R12', setup=True)` to setup default line types, text styles and dimension styles, 
  this feature is disabled by default.
- NEW: Duplicate table entries: `dwg.styles.duplicate_entry('OpenSans', new_name='OpenSansNew')`, this works for 
  all tables, but is intended to duplicate STYLES and DIMSTYLES.
- CHANGED: replaced proprietary fonts in style declarations by open source fonts
- NEW: open source fonts to download https://github.com/mozman/ezdxf/tree/master/fonts
- __OpenSansCondensed-Light__ font used for default dimension styles
- NEW: subpackage `ezdxf.render`, because of DIMENSION rendering
- NEW: support for AutoCAD standard arrows
- NEW: support for creating linear DIMENSION entities
- NEW: background color support for MTEXT
- CHANGE: DXF template cleanup, removed non standard text styles, dimension styles, layers and blocks
- CHANGE: text style STANDARD uses `txt` font 
- CHANGE: renamed subpackage `ezdxf.algebra` to `ezdxf.math`
- CHANGE: moved `addons.curves` to `render.curves`
- CHANGE: moved `addons.mesh` to `render.mesh`
- CHANGE: moved `addons.r12spline` to `render.r12spline`
- CHANGE: moved `addons.forms` to `render.forms`
- CHANGE: renamed construction helper classes into Construction...()
  - `Ray2D()` renamed to `ConstructionRay()`
  - `Circle()` renamed to `ConstructionCircle()`
  - `Arc()` renamed to `ConstructionArc()`
- NEW: construction tools `ConstructionLine()` and `ConstructionBox()`
- REMOVED: `almost_equal` use `math.isclose`
- REMOVED: `almost_equal_points` use `ezdxf.math.is_close_points`
- BUGFIX: closed LWPOLYLINE did not work in AutoCAD (tag order matters), introduced with v0.8.9 packed data structure
- BUGFIX: `UCS.to_ocs_angle_deg()` corrected

Version 0.8.9 - 2018-11-28
--------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-8-9.html
- IMPORTANT: Python 2 support will be dropped in ezdxf v0.9.0, because Python 2 support get more and more annoying.
- CHANGE: refactoring of internal tag representation for a smaller memory footprint, but with some speed penalty
- NEW: packed data for LWPOLYLINE points, faster `__getitem__`;  added `__setitem__`, `__delitem__`, `insert()` and 
  `append()` methods; renamed `discard_points()` in `clear()`; removed `get_rstrip_points()` and ctx manager 
  `rstrip_points()`; user defined point format;
- NEW: packed data for SPLINE, knots, weights, fit- and control points are stored as `array.array()`;
  `Spline.get_knot_values()`, `Spline.get_weights()`, `Spline.get_control_points()` and `Spline.get_fit_points()` are 
  deprecated, direct access to this attributes by `Spline.knot_values`, `Spline.weights`, `Spline.control_points` and 
  `Spline.fit_points`, all attributes with a list-like interface. Knot, control point and fit point counter updated 
  automatically, therefore counters are read only now.
- NEW: packed data for MESH, vertices, faces, edges and edge crease values stored as `array.array()`, high level interface unchanged
- NEW: `Drawing.layouts_and_blocks()`, iterate over all layouts (mode space and paper space) and all block definitions.
- NEW: `Drawing.chain_layouts_and_blocks()`, chain entity spaces of all layouts and blocks. Yields an iterator for all
  entities in all layouts and blocks
- NEW: `Drawing.query()`, entity query over all layouts and blocks
- NEW: `Drawing.groupby()`, groups DXF entities of all layouts and blocks by an DXF attribute or a key function
- NEW: `Layout.set_redraw_order()` and `Layout.get_redraw_order()`, to change redraw order of entities in model space and
  paper space layouts
- NEW: `BlockLayout.is_layout_block`, `True` if block is a model space or paper space block definition
- NEW: `ezdxf.algebra.Arc` helper class to create arcs from 2 points and an angle or radius, or from 3 points
- NEW: `ezdxf.algebra.Arc.add_to_layout()` with UCS support to create 3D arcs
- NEW: rename paper space layouts by `Drawing.layouts.rename(old_name, new_name)`
- NEW: Basic support for embedded objects (new in AutoCAD 2018), ezdxf reads and writes the embedded data as it is,
  no interpretation no modification, just enough to not break DXF files with embedded objects at saving.
- CHANGE: `Drawing.blocks.delete_block(name, safe=True)`, new parameter save, check if block is still referenced
  (raises `DXFValueError`)
- CHANGE: `Drawing.blocks.delete_all_blocks(safe=True)`, if parameter safe is `True`, do not delete blocks that are still referenced
- BUGFIX: invalid CLASS definition for DXF version R2000 (AC1015) fixed, bug was only triggered at upgrading from R13/R14 to R2000
- BUGFIX: fixed broken `Viewport.AcDbViewport` property
- __BASIC__ read support for many missing DXF entities/objects

    - ACAD_PROXY_GRAPHIC
    - HELIX
    - LEADER
    - LIGHT
    - MLEADER (incomplete)
    - MLINE (incomplete)
    - OLEFRAME
    - OLE2FRAME
    - SECTION
    - TABLE (incomplete)
    - TOLERANCE
    - WIPEOUT
    - ACAD_PROXY_OBJECT
    - DATATABLE
    - DICTIONARYVAR
    - DIMASSOC
    - FIELD (incomplete)
    - FIELDLIST (not documented by Autodesk)
    - IDBUFFER
    - LAYER_FILTER
    - MATERIAL
    - MLEADERSTYLE
    - MLINESTYLE
    - SORTENTSTABLE
    - SUN
    - SUNSTUDY (incomplete) (no real world DXF files with SUNSTUDY for testing available)
    - TABLESTYLE (incomplete)
    - VBA_PROJECT (no real world DXF files with embedded VBA for testing available)
    - VISUALSTYLE
    - WIPEOUTVARIABLES
    - for all unsupported entities/objects exist only raw DXF tag support

Version 0.8.8 - 2018-04-02
--------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-8-8.html
- NEW: read/write support for GEODATA entity
- NEW: read/(limited)write support for SURFACE, EXTRUDEDSURFACE, REVOLVEDSURFACE, LOFTEDSURFACE and SWEPTSURFACE entity
- NEW: support for extension dictionaries
- NEW: `add_spline_control_frame()`, create and add B-spline control frame from fit points
- NEW: `add_spline_approx()`, approximate B-spline by a reduced count of control points
- NEW: `ezdxf.setup_linetypes(dwg)`, setup standard line types
- NEW: `ezdxf.setup_styles(dwg)`, setup standard text styles
- NEW: `LWPolyline.vertices()` yields all points as `(x, y)` tuples in OCS, `LWPolyline.dxf.elevation` is the z-axis value
- NEW: `LWPolyline.vertices_in_wcs()` yields all points as `(x, y, z)` tuples in WCS
- NEW: basic `__str__()`  and `__repr__()` support for DXF entities, returns just DXF type and handle
- NEW: bulge related function in module `ezdxf.algebra.bulge`
- NEW: Object Coordinate System support by `DXFEntity.ocs()` and `OCS()` class in module ezdxf.algebra
- NEW: User Coordinate System support by `UCS()` class in module `ezdxf.algebra`
- CHANGE: `DXFEntity.set_app_data()` and `Entity.set_xdata` accept also list of tuples as tags, `DXFTag()` is not required
- BUGFIX: entity structure validator excepts group code >= 1000 before XDATA section (used in AutoCAD Civil 3D and AutoCAD Map 3D)

Version 0.8.7 - 2018-03-04
--------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-8-7.html
- NEW: entity.get_layout() returns layout in which entity resides or None if unassigned
- NEW: copy any DXF entity by entity.copy() without associated layout, add copy to any layout you want, by
  layout.add_entity().
- NEW: copy entity to another layout by entity.copy_to_layout(layout)
- NEW: move entity from actual layout to another layout by entity.move_to_layout(layout)
- NEW: support for splines by control points: add_open_spline(), add_closed_spline(), add_rational_spline(),
  add_closed_rational_spline()
- NEW: bspline_control_frame() calculates B-spline control points from fit points, but not the same as AutoCAD
- NEW: R12Spline add-on, 2d B-spline with control frame support by AutoCAD, but curve is just an approximated POLYLINE
- NEW: added entity.get_flag_state() and entity.set_flag_state() for easy access to binary coded flags
- NEW: set new $FINGERPRINTGUID for new drawings
- NEW: set new $VERSIONGUID on saving a drawing
- NEW: improved IMAGE support, by adding RASTERVARIABLES entity, use Drawing.set_raster_variables(frame, quality, units)
- BUGFIX: closing user defined image boundary path automatically, else AutoCAD crashes

Version 0.8.6 - 2018-02-17
--------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-8-6.html
- NEW: ezdxf project website: https://ezdxf.mozman.at/
- CHANGE: create all missing tables of the TABLES sections for DXF R12
- BUGFIX: entities on new layouts will be saved
- NEW: Layout.page_setup() and correct 'main' viewport for DXF R2000+; For DXF R12 page_setup() exists, but does not
  provide useful results. Page setup for DXF R12 is still a mystery to me.
- NEW: Table(), MText(), Ellipse(), Spline(), Bezier(), Clothoid(), LinearDimension(), RadialDimension(),
  ArcDimension() and AngularDimension() composite objects from dxfwrite as add-ons, these add-ons support DXF R12
- NEW: geometry builder as add-ons: MeshBuilder(), MeshVertexMerger(), MengerSponge(), SierpinskyPyramid(), these
  add-ons require DXF R2000+ (MESH entity)
- BUGFIX: fixed invalid implementation of context manager for r12writer

Version 0.8.5 - 2018-01-28
--------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-8-5.html
- CHANGE: block names are case insensitive 'TEST' == 'Test' (like AutoCAD)
- CHANGE: table entry (layer, linetype, style, dimstyle, ...) names are case insensitive 'TEST' == 'Test' (like AutoCAD)
- CHANGE: raises DXFInvalidLayerName() for invalid characters in layer names: <>/\":;?*|=`
- CHANGE: audit process rewritten
- CHANGE: skip all comments, group code 999
- CHANGE: removed compression for unused sections (THUMBNAILSECTION, ACDSDATA)
- NEW: write DXF R12 files without handles: set dwg.header['$HANDLING']=0, default value is 1
- added subclass marker filter for R12 and prior files in legacy_mode=True (required for malformed DXF files)
- removed special check for Leica Disto Unit files, use readfile(filename, legacy_mode=True) (malformed DXF R12 file,
  see previous point)

Version 0.8.4 - 2018-01-14
--------------------------

- Release notes: https://ezdxf.mozman.at/release-v0-8-4.html
- NEW: Support for complex line types with text or shapes
- NEW: DXF file structure validator at SECTION level, tags outside of sections will be removed
- NEW: Basic read support for DIMENSION
- CHANGE: improved exception management, in the future ezdxf should only raise exceptions inherited from DXFError for
  DXF related errors, previous exception classes still work

    - DXFValueError(DXFError, ValueError)
    - DXFKeyError(DXFError, KeyError)
    - DXFAttributeError(DXFError, AttributeError)
    - DXFIndexError(DXFError, IndexError)
    - DXFTableEntryError(DXFValueError)

- speedup low level tag reader around 5%, and speedup tag compiler around 5%

Version 0.8.3 - 2018-01-02
--------------------------

- CHANGE: Lwpolyline - suppress yielding z coordinates if they exists (DXFStructureError: z coordinates are not defined in the DXF standard)
- NEW: setup creates a script called 'dxfpp' (DXF Pretty Printer) in the Python script folder
- NEW: basic support for DXF format AC1032 introduced by AutoCAD 2018
- NEW: ezdxf use logging and writes all logs to a logger called 'ezdxf'. Logging setup is the domain of the application!
- NEW: warns about multiple block definitions with the same name in a DXF file. (DXFStructureError)
- NEW: legacy_mode parameter in ezdxf.read() and ezdxf.readfile(): tries do fix coordinate order in LINE
  entities (10, 11, 20, 21) by the cost of around 5% overall speed penalty at DXF file loading

Version 0.8.2 - 2017-05-01
--------------------------

- NEW: Insert.delete_attrib(tag) - delete ATTRIB entities from the INSERT entity
- NEW: Insert.delete_all_attribs() - delete all ATTRIB entities from the INSERT entity
- BUGFIX: setting attribs_follow=1 at INSERT entity before adding an attribute entity works

Version 0.8.1 - 2017-04-06
--------------------------

- NEW: added support for constant ATTRIB/ATTDEF to the INSERT (block reference) entity
- NEW: added ATTDEF management methods to BlockLayout (has_attdef, get_attdef, get_attdef_text)
- NEW: added (read/write) properties to ATTDEF/ATTRIB for setting flags (is_const, is_invisible, is_verify, is_preset)

Version 0.8.0 - 2017-03-28
--------------------------

- added groupby(dxfattrib='', key=None) entity query function, it is supported by all layouts and the query result
  container: Returns a dict, where entities are grouped by a dxfattrib or the result of a key function.
- added ezdxf.audit() for DXF error checking for drawings created by ezdxf - but not very capable yet
- dxfattribs in factory functions like add_line(dxfattribs=...), now are copied internally and stay unchanged, so they
  can be reused multiple times without getting modified by ezdxf.
- removed deprecated Drawing.create_layout() -> Drawing.new_layout()
- removed deprecated Layouts.create() -> Layout.new()
- removed deprecated Table.create() -> Table.new()
- removed deprecated DXFGroupTable.add() -> DXFGroupTable.new()
- BUFIX in EntityQuery.extend()

Version 0.7.9 - 2017-01-31
--------------------------

- BUGFIX: lost data if model space and active layout are called \*MODEL_SPACE and \*PAPER_SPACE

Version 0.7.8 - 2017-01-22
--------------------------

- BUGFIX: HATCH accepts SplineEdges without defined fit points
- BUGFIX: fixed universal line ending problem in ZipReader()
- Moved repository to GitHub: https://github.com/mozman/ezdxf.git

Version 0.7.7 - 2016-10-22
--------------------------

- NEW: repairs malformed Leica Disto DXF R12 files, ezdxf saves a valid DXF R12 file.
- NEW: added Layout.unlink(entity) method: unlinks an entity from layout but does not delete entity from the drawing database.
- NEW: added Drawing.add_xref_def(filename, name) for adding external reference definitions
- CHANGE: renamed parameters for EdgePath.add_ellipse() - major_axis_vector -> major_axis; minor_axis_length -> ratio
  to be consistent to the ELLIPSE entity
- UPDATE: Entity.tags.new_xdata() and Entity.tags.set_xdata() accept tuples as tags, no import of DXFTag required
- UPDATE: EntityQuery to support both 'single' and "double" quoted strings - Harrison Katz <harrison@neadwerx.com>
- improved DXF R13/R14 compatibility

Version 0.7.6 - 2016-04-16
--------------------------

* NEW: r12writer.py - a fast and simple DXF R12 file/stream writer. Supports only LINE, CIRCLE, ARC, TEXT, POINT,
  SOLID, 3DFACE and POLYLINE. The module can be used without ezdxf.
* NEW: Get/Set extended data on DXF entity level, add and retrieve your own data to DXF entities
* NEW: Get/Set app data on DXF entity level (not important for high level users)
* NEW: Get/Set/Append/Remove reactors on DXF entity level (not important for high level users)
* CHANGE: using reactors in PdfDefinition for well defined UNDERLAY entities
* CHANGE: using reactors and IMAGEDEF_REACTOR for well defined IMAGE entities
* BUGFIX: default name=None in add_image_def()

Version 0.7.5 - 2016-04-03
--------------------------

* NEW: Drawing.acad_release property - AutoCAD release number for the drawing DXF version like 'R12' or 'R2000'
* NEW: support for PDFUNDERLAY, DWFUNDERLAY and DGNUNDERLAY entities
* BUGFIX: fixed broken layout setup in repair routine
* BUGFIX: support for utf-8 encoding on saving, DXF R2007 and later is saved with UTF-8 encoding
* CHANGE: Drawing.add_image_def(filename, size_in_pixel, name=None), renamed key to name and set name=None for auto-generated internal image name
* CHANGE: argument order of Layout.add_image(image_def, insert, size_in_units, rotation=0., dxfattribs=None)

Version 0.7.4 - 2016-03-13
--------------------------

* NEW: support for DXF entity IMAGE (work in progress)
* NEW: preserve leading file comments (tag code 999)
* NEW: writes saving and upgrading comments when saving DXF files; avoid this behavior by setting options.store_comments = False
* NEW: ezdxf.new() accepts the AutoCAD release name as DXF version string e.g. ezdxf.new('R12') or R2000, R2004, R2007, ...
* NEW: integrated acadctb.py module from my dxfwrite package to read/write AutoCAD .ctb config files; no docs so far
* CHANGE: renamed Drawing.groups.add() to new() for consistent name schema for adding new items to tables (public interface)
* CHANGE: renamed Drawing.<tablename>.create() to new() for consistent name schema for adding new items to tables,
  this applies to all tables: layers, styles, dimstyles, appids, views, viewports, ucs, block_records. (public interface)
* CHANGE: renamed Layouts.create() to new() for consistent name schema for adding new items to tables (internal interface)
* CHANGE: renamed Drawing.create_layout() to new_layout() for consistent name schema for adding new items (public interface)
* CHANGE: renamed factory method <layout>.add_3Dface() to add_3dface()
* REMOVED: logging and debugging options
* BUGFIX: fixed attribute definition for align_point in DXF entity ATTRIB (AC1015 and newer)
* Cleanup DXF template files AC1015 - AC1027, file size goes down from >60kb to ~20kb

Version 0.7.3 - 2016-03-06
--------------------------

* Quick bugfix release, because ezdxf 0.7.2 can damage DXF R12 files when saving!!!
* NEW: improved DXF R13/R14 compatibility
* BUGFIX: create CLASSES section only for DXF versions newer than R12 (AC1009)
* TEST: converted a bunch of R8 (AC1003) files to R12 (AC1009), AutoCAD didn't complain
* TEST: converted a bunch of R13 (AC1012) files to R2000 (AC1015), AutoCAD did not complain
* TEST: converted a bunch of R14 (AC1014) files to R2000 (AC1015), AutoCAD did not complain

Version 0.7.2 - 2016-03-05
--------------------------

* NEW: reads DXF R13/R14 and saves content as R2000 (AC1015) - experimental feature, because of the lack of test data
* NEW: added support for common DXF attribute line weight
* NEW: POLYLINE, POLYMESH - added properties is_closed, is_m_closed, is_n_closed
* BUGFIX: MeshData.optimize() - corrected wrong vertex optimization
* BUGFIX: can open DXF files without existing layout management table
* BUGFIX: restore module structure ezdxf.const

Version 0.7.1 - 2016-02-21
--------------------------

* Supported/Tested Python versions: CPython 2.7, 3.4, 3.5, pypy 4.0.1 and pypy3 2.4.0
* NEW: read legacy DXF versions older than AC1009 (DXF R12) and saves it as DXF version AC1009.
* NEW: added methods is_frozen(), freeze(), thaw() to class Layer()
* NEW: full support for DXF entity ELLIPSE (added add_ellipse() method)
* NEW: MESH data editor - implemented add_face(vertices), add_edge(vertices), optimize(precision=6) methods
* BUGFIX: creating entities on layouts works
* BUGFIX: entity ATTRIB - fixed halign attribute definition
* CHANGE: POLYLINE (POLYFACE, POLYMESH) - on layer change also change layer of associated VERTEX entities

Version 0.7.0 - 2015-11-26
--------------------------

* Supported Python versions: CPython 2.7, 3.4, pypy 2.6.1 and pypy3 2.4.0
* NEW: support for DXF entity HATCH (solid fill, gradient fill and pattern fill), pattern fill with background color supported
* NEW: support for DXF entity GROUP
* NEW: VIEWPORT entity, but creating new viewports does not work as expected - just for reading purpose.
* NEW: support for new common DXF attributes in AC1018 (AutoCAD 2004): true_color, color_name, transparency
* NEW: support for new common DXF attributes in AC1021 (AutoCAD 2007): shadow_mode
* NEW: extended custom vars interface
* NEW: dxf2html - added support for custom properties in the header section
* NEW: query() supports case insensitive attribute queries by appending an 'i' to the query string, e.g. '\*[layer=="construction"]i'
* NEW: Drawing.cleanup() - call before saving the drawing but only if necessary, the process could take a while.
* BUGFIX: query parser couldn't handle attribute names containing '_'
* CHANGE: renamed dxf2html to pp (pretty printer), usage: py -m ezdxf.pp yourfile.dxf (generates yourfile.html in the same folder)
* CHANGE: cleanup file structure

Version 0.6.5 - 2015-02-27
--------------------------

* BUGFIX: custom properties in header section written after $LASTSAVEDBY tag - the only way AutoCAD accepts custom tags

Version 0.6.4 - 2015-02-27
--------------------------

* NEW: Support for custom properties in the header section - Drawing.header.custom_vars - but so far AutoCAD ignores
  new created custom properties by ezdxf- I don't know why.
* BUGFIX: wrong DXF subclass for Arc.extrusion (error in DXF Standard)
* BUGFIX: added missing support files for dxf2html

Version 0.6.3 - 2014-09-10
--------------------------

* Beta status
* BUGFIX: Text.get_pos() - dxf attribute error "alignpoint"

Version 0.6.2 - 2014-05-09
--------------------------

* Beta status
* NEW: set ``ezdxf.options.compress_default_chunks = True`` to compress unnecessary Sections (like THUMBNAILIMAGE) in
  memory with zlib
* NEW: Drawing.compress_binary_data() - compresses binary data (mostly code 310) in memory with zlib or set
  ``ezdxf.options.compress_binary_data = True`` to compress binary data of every drawing you open.
* NEW: support for MESH entity
* NEW: support for BODY, 3DSOLID and REGION entity, you get the ACIS data
* CHANGE: Spline() - removed context managers fit_points(), control_points(), knot_values() and weights() and added a
  general context_manager edit_data(), similar to Mesh.edit_data() - unified API
* CHANGE: MText.buffer() -> MText.edit_data() - unified API (MText.buffer() still exists as alias)
* CHANGE: refactored internal structure - only two DXF factories remaining:
    - LegacyDXFFactory() for AC1009 (DXF12) drawings
    - ModernDXFFactory() for newer DXF versions except DXF13/14.
* BUGFIX: LWPolyline.get_rstrip_point() removed also x- and y-coords if zero
* BUGFIX: opens DXF12 files without handles again
* BUGFIX: opens DXF12 files with HEADER section but without $ACADVER set

Version 0.6.1 - 2014-05-02
--------------------------

* Beta status
* NEW: create new layouts - Drawing.create_layout(name, dxfattribs=None)
* NEW: delete layouts - Drawing.delete_layout(name)
* NEW: delete blocks - Drawing.blocks.delete_block(name)
* NEW: read DXF files from zip archives (its slow).
* CHANGE: LWPolyline returns always 5-tuples (x, y, start_width, end_width, bulge). start_width, end_width and bulge
  is 0 if not present.
* NEW: LWPolyline.get_rstrip_points() -> generates points without appending zeros.
* NEW: LWPolyline.rstrip_points() -> context manager for points without appending zeros.
* BUGFIX: fixed handle creation bug for DXF12 files without handles, a code 5/105 issue
* BUGFIX: accept floats as int (thanks to ProE)
* BUGFIX: accept entities without owner tag (thanks to ProE)
* improved dxf2html; creates a more readable HTML file; usage: python -m ezdxf.dxf2html filename.dxf

Version 0.6.0 - 2014-04-25
--------------------------

* Beta status
* Supported Python versions: CPython 2.7, 3.4 and pypy 2.2.1
* Refactoring of internal structures
* CHANGE: appended entities like VERTEX for POLYLINE and ATTRIB for INSERT are linked to the main entity and do
  not appear in layouts, model space or blocks (modelspace.query('VERTEX') is always an empty list).
* CHANGE: refactoring of the internal 2D/3D point representation for reduced memory footprint
* faster unittests
* BUGFIX: opens minimalistic DXF12 files
* BUGFIX: support for POLYLINE new (but undocumented) subclass names: AcDbPolyFaceMesh, AcDbPolygonMesh
* BUGFIX: support for VERTEX new (but undocumented) subclass names: AcDbFaceRecord, AcDbPolyFaceMeshVertex,
  AcDbPolygonMeshVertex, AcDb3dPolylineVertex
* CHANGE: Polyline.get_mode() returns new names: AcDb2dPolyline, AcDb3dPolyline, AcDbPolyFaceMesh, AcDbPolygonMesh
* CHANGE: separated layout spaces - each layout has its own entity space

Version 0.5.2 - 2014-04-15
--------------------------

* Beta status
* Supported Python versions: CPython 2.7, 3.3, 3.4 and pypy 2.2.1
* BUGFIX: ATTRIB definition error for AC1015 and later (error in DXF specs)
* BUGFIX: entity.dxf_attrib_exists() returned True for unset attribs with defined DXF default values
* BUGFIX: layout.delete_entity() didn't delete following data entities for INSERT (ATTRIB) & POLYLINE (VERTEX)
* NEW: delete all entities from layout/block/entities section
* cleanup DXF template files

Version 0.5.1 - 2014-04-14
--------------------------

* Beta status
* Supported Python versions: CPython 2.7, 3.3, 3.4 and pypy 2.2.1
* BUGFIX: restore Python 2 compatibility (has no list.clear() method); test launcher did not run tests in subfolders,
  because of missing __init__.py files

Version 0.5.0 - 2014-04-13
--------------------------

* Beta status
* BUGFIX: Drawing.get_layout_setter() - did not work with entities without DXF attribute *paperspace*
* NEW: default values for DXF attributes as defined in the DXF standard, this allows usage of optional DXF attributes
  (with defined default values) without check of presence, like *entity.dxf.paperspace*.
* NEW: DXF entities SHAPE, RAY, XLINE, SPLINE
* NEW: delete entities from layout/block
* CHANGE: entity 3DFACE requires 3D coordinates (created by add_3Dface())
* CHANGE: LWPolyline all methods return points as (x, y, [start_width, [end_width, [bulge]]]) tuples
* updated docs

Version 0.4.2 - 2014-04-02
--------------------------

* Beta status
* Supported Python versions: CPython 2.7, 3.3, 3.4 and pypy 2.1
* NEW: DXF entities LWPOLYLINE, MTEXT
* NEW: convenience methods place(), grid(), get_attrib_text() and has_attrib() for the Insert entity
* CHANGE: pyparsing as external dependency
* BUGFIX: iteration over drawing.entities yields full functional entities (correct layout attribute)
* BUGFIX: install error with pip and missing DXF template files of versions 0.4.0 & 0.4.1

Version 0.3.0 - 2013-07-20
--------------------------

* Alpha status
* Supported Python versions: CPython 2.7, 3.3 and pypy 2.0
* NEW: Entity Query Language
* NEW: Import data from other DXF files
* CHANGE: License changed to MIT License

Version 0.1.0 - 2010-03-14
--------------------------

* Alpha status
* Initial release

from waterobjects import *
from modelexport.export_functions import *

class Exceptions(Exception):
    pass

class MODELOBJECTS:
    '''
    This object provides structure to SWMM model parameters. Types of water
    objects (i.e. SUBCATCHMENTS) are stored into lookup tables and thier
    respective values have callable attributes.

    The Eval functions instantiate a 'section' of the model (i.e. HYDROLOGY or
    NODES).  Once the section object is create, water objects can be added,
    removed*, or updated*.

    Adding Features can be done by calling add_XXXXXXX function within each
    section object while passing the required parameters.  Several default
    parameters are provided for the tool but should be 


    *Future Version
    
    '''
    def __init__(self):
        self.Exceptions = Exceptions()
        
    def Eval_Options(self):
        '''
        Instantiate Options Object
        '''
        self.Options = OPTIONSset()
        
    def Eval_Nodes(self):
        '''
        Instantiates Nodes Object
        '''
        self.Nodes = NODES(self)

    def Eval_Links(self):
        '''
        Instantites Links Object
        '''
        self.Links = LINKS(self)
        
    def Eval_Hydrology(self):
        '''
        Instantiates Hydrology Object(s)
        '''
        self.Hydrology = HYDROLOGY(self)

    def Eval_GroundwaterFlow(self):
        '''
        Instantiates Groundwater Object(s)

        Prereq = Eval_Nodes needs to be run first        
        '''
        if hasattr(self, 'Nodes'):
            self.GroundwaterFlow = GROUNDWATERFLOW(self)
        else:
            pass
        
    def Eval_RemainingObjects(self):
        '''
        Instantiates Nodes Object
        '''
        self.Remaining = REMAINING(self)
            


class GROUNDWATERFLOW:
    def __init__(sub, self):
        sub.self = self
        
        sub.groundwater = {}
        sub.aquifers = {}
        
    def add_GWFLOW(sub, AQNAME,SUBCNAME,LOADINGNODE,SURFACEEL=0,BOTTOMELEVATION=0,\
                   WATERTABLEELEVATION=0, POROSITY=0.41, WILTINGPOINT=0.035, \
                   FIELDCAPACITY=0.92,CONDUCTIVITY=3.26, CONDUCTIVITYSLOPE=2,\
                   TENSIONSLOPE=35.2,UPPEREVAPFRACTION=99, LOWEREVAPFRACTION=8,\
                   LOWERGWLOSS=1.5,UNSATZONEMOISTURE=0.092,UPPEREVAPPATTERN = '',\
                   A1=0.4,B1=1,A2=0,B2=0,A3=0,TW=0,GWTHEIGHT=0):
        
        assert LOADINGNODE in self.Nodes.nodetypedict.keys()

        sub._add_groundwater(SUBCNAME,AQNAME,LOADINGNODE,SURFACEEL,\
                             A1,B1,A2,B2,A3,TW,GWTHEIGHT)        
        sub._add_aquifer(AQNAME,POROSITY,WILTINGPOINT,FIELDCAPACITY,\
                         CONDUCTIVITY, CONDUCTIVITYSLOPE,TENSIONSLOPE,\
                         UPPEREVAPFRACTION, LOWEREVAPFRACTION, LOWERGWLOSS,\
                         BOTTOMELEVATION, WATERTABLEELEVATION, UNSATZONEMOISTURE,\
                         UPPEREVAPPATTERN)
        
    def _add_groundwater(sub,SUBCNAME,AQNAME,LOADINGNODE,SURFACEEL,\
                         A1,B1,A2,B2,A3,TW,GWTHEIGHT):
        
        sub.groundwater[SUBCNAME] = GROUNDWATER()
        sub.groundwater[SUBCNAME].SUBCNAME = SUBCNAME
        sub.groundwater[SUBCNAME].AQNAME = AQNAME
        sub.groundwater[SUBCNAME].LOADINGNODE = LOADINGNODE
        sub.groundwater[SUBCNAME].SURFACEEL = SURFACEEL
        sub.groundwater[SUBCNAME].A1 = A1
        sub.groundwater[SUBCNAME].B1 = B1
        sub.groundwater[SUBCNAME].A2 = A2
        sub.groundwater[SUBCNAME].B2 = B2
        sub.groundwater[SUBCNAME].A3 = A3
        sub.groundwater[SUBCNAME].TW = TW
        sub.groundwater[SUBCNAME].GWTHEIGHT = GWTHEIGHT

    def _add_aquifer(sub,AQNAME,POROSITY,WILTINGPOINT,FIELDCAPACITY,\
                     CONDUCTIVITY, CONDUCTIVITYSLOPE,TENSIONSLOPE,\
                     UPPEREVAPFRACTION, LOWEREVAPFRACTION, LOWERGWLOSS,\
                     BOTTOMELEVATION, WATERTABLEELEVATION, UNSATZONEMOISTURE,\
                     UPPEREVAPPATTERN):
        
        sub.aquifers[AQNAME] = AQUIFERS()
        sub.aquifers[AQNAME].AQNAME = AQNAME
        sub.aquifers[AQNAME].POROSITY = POROSITY
        sub.aquifers[AQNAME].WILTINGPOINT = WILTINGPOINT
        sub.aquifers[AQNAME].FIELDCAPACITY = FIELDCAPACITY
        sub.aquifers[AQNAME].CONDUCTIVITY = CONDUCTIVITY
        sub.aquifers[AQNAME].CONDUCTIVITYSLOPE = CONDUCTIVITYSLOPE
        sub.aquifers[AQNAME].TENSIONSLOPE = TENSIONSLOPE
        sub.aquifers[AQNAME].UPPEREVAPFRACTION = UPPEREVAPFRACTION
        sub.aquifers[AQNAME].LOWEREVAPFRACTION = LOWEREVAPFRACTION
        sub.aquifers[AQNAME].LOWERGWLOSS = LOWERGWLOSS
        sub.aquifers[AQNAME].BOTTOMELEVATION = BOTTOMELEVATION
        sub.aquifers[AQNAME].WATERTABLEELEVATION = WATERTABLEELEVATION
        sub.aquifers[AQNAME].UNSATZONEMOISTURE = UNSATZONEMOISTURE
        sub.aquifers[AQNAME].UPPEREVAPPATTERN = UPPEREVAPPATTERN


class LINKS:
    '''
    Currently setup for conduits, only (BM 1/24/2015). 
    '''
    def __init__(sub, self):

        sub.linktypedict = {}
        
        sub.conduits = {}
        sub.weirs = {}
        sub.orifices = {}
        sub.outlets = {}

        sub.xsections = {}
        sub.losses = {}
        sub.transects = {}
        
    def add_LINK(sub, LINKNAME, INLETNODE, OUTLETNODE, LENGTH, MANNINGN, INLETOFFSET, OUTLETOFFSET, INITIALFLOW,\
                 MAXFLOW, SHAPE='CIRCULAR', GEOM1=0, GEOM2=0, GEOM3=0, GEOM4=0, BARRELS=1, CLASS = 'CONDUIT'):
        if CLASS == 'CONDUIT': sub._add_conduit(LINKNAME, INLETNODE, OUTLETNODE,\
                                                LENGTH, MANNINGN, INLETOFFSET, OUTLETOFFSET, INITIALFLOW, MAXFLOW,\
                                                SHAPE, GEOM1, GEOM2, GEOM3, GEOM4, BARRELS)
##        if CLASS == 'WEIR': sub._add_weir(NODENAME, ELEVATION,\
##                                                XCOORD, YCOORD, TYPE,\
##                                                TSERIES, GATE)
##        if CLASS == 'ORIFICE': sub._add_orifice(NODENAME, ELEVATION, XCOORD, YCOORD, YMAX, Y0, PONDINGAREA,\
##                                                FEVAP, TABULAR, ACURVE, FUNCTIONAL, SH, HC, IMD)
##        if CLASS == 'OUTLET': sub._add_outlet(NODENAME, ELEVATION, XCOORD, YCOORD, YMAX,\
##                                                  Y0, YSURCHARGE, PONDINGAREA)
    def add_TRANSECT(sub, TRANSNAME,LOBStation,ROBStation,LOBN,ROBN,CHANNELN,\
                     LeftEncrStation=0,RightEncrStation=0,STATIONS=0,ELEVATIONS=0,MEANDER=0,\
                     ZCOORD = [], XCOORD=[], Area = [],Hrad = [],Width = []):
        sub.transects[TRANSNAME] = TRANSECTS()
        sub.transects[TRANSNAME].TRANSNAME = TRANSNAME
        sub.transects[TRANSNAME].LOBStation = float(LOBStation)
        sub.transects[TRANSNAME].ROBStation = float(ROBStation)
        sub.transects[TRANSNAME].LOBN = float(LOBN)
        sub.transects[TRANSNAME].ROBN = float(ROBN)
        sub.transects[TRANSNAME].CHANNELN = float(CHANNELN)
        sub.transects[TRANSNAME].LeftEncrStation = float(LeftEncrStation)
        sub.transects[TRANSNAME].RightEncrStation = float(RightEncrStation)
        sub.transects[TRANSNAME].STATIONS = float(STATIONS)
        sub.transects[TRANSNAME].ELEVATIONS = float(ELEVATIONS)
        sub.transects[TRANSNAME].MEANDER = float(MEANDER)
        sub.transects[TRANSNAME].ZCOORD = [float(val) for val in ZCOORD]
        sub.transects[TRANSNAME].XCOORD = [float(val) for val in XCOORD]
        sub.transects[TRANSNAME].Area = [float(val) for val in Area]
        sub.transects[TRANSNAME].Hrad = [float(val) for val in Hrad]
        sub.transects[TRANSNAME].Width = [float(val) for val in Width]
                     
    def remove_LINK(sub,LINKNAME):
        sub.conduits.pop(LINKNAME,None)
        sub.weirs.pop(LINKNAME,None)
        sub.orifices.pop(LINKNAME,None)
        sub.outlets.pop(LINKNAME,None)
        sub.linktypedict.pop(LINKNAME,None)
        sub.xsections.pop(LINKNAME,None)
        sub.losses.pop(LINKNAME,None)

    def _add_conduit(sub, LINKNAME, INLETNODE, OUTLETNODE, LENGTH, MANNINGN, \
                     INLETOFFSET, OUTLETOFFSET,INITIALFLOW, MAXFLOW,\
                     SHAPE, GEOM1, GEOM2, GEOM3, GEOM4, BARRELS):
        assert LINKNAME not in sub.linktypedict.keys()
        #udpate link type dict
        sub.linktypedict[LINKNAME] = 'CONDUIT'
        #assign link params
        
        sub.conduits[LINKNAME] = CONDUITS()
        sub.conduits[LINKNAME].LINKNAME = LINKNAME
        sub.conduits[LINKNAME].INLETNODE = INLETNODE
        sub.conduits[LINKNAME].OUTLETNODE = OUTLETNODE
        sub.conduits[LINKNAME].LENGTH = float(LENGTH)
        sub.conduits[LINKNAME].MANNINGN = float(MANNINGN)
        sub.conduits[LINKNAME].INLETOFFSET = float(INLETOFFSET)
        sub.conduits[LINKNAME].OUTLETOFFSET = float(OUTLETOFFSET)
        sub.conduits[LINKNAME].INITIALFLOW = float(INITIALFLOW)
        sub.conduits[LINKNAME].MAXFLOW = float(MAXFLOW)

        sub.xsections[LINKNAME] = XSECTIONS()
        sub.xsections[LINKNAME].LINKNAME = LINKNAME
        sub.xsections[LINKNAME].SHAPE = SHAPE
        try:
            GEOM1 = float(GEOM1)
        except:
            pass        
        sub.xsections[LINKNAME].GEOM1 = GEOM1
        sub.xsections[LINKNAME].GEOM2 = float(GEOM2)
        sub.xsections[LINKNAME].GEOM3 = float(GEOM3)
        sub.xsections[LINKNAME].GEOM4 = float(GEOM4)
        sub.xsections[LINKNAME].BARRELS = int(BARRELS)

    def UpdateXSection(sub, LINKNAME, SHAPE, GEOM1, GEOM2, GEOM3, GEOM4, BARRELS):
        sub.xsections[LINKNAME].LINKNAME = LINKNAME
        sub.xsections[LINKNAME].SHAPE = SHAPE
        try:
            GEOM1 = float(GEOM1)
        except:
            pass
        sub.xsections[LINKNAME].GEOM1 = GEOM1
        sub.xsections[LINKNAME].GEOM2 = float(GEOM2)
        sub.xsections[LINKNAME].GEOM3 = float(GEOM3)
        sub.xsections[LINKNAME].GEOM4 = float(GEOM4)
        sub.xsections[LINKNAME].BARRELS = int(BARRELS)
        
class REMAINING:
    def __init__(sub, self):
        return


class NODES:
    '''
    Currently setup for junctions, only (BM 6/3/2015). 
    '''
    def __init__(sub, self):

        sub.nodetypedict = {}
        sub.coordinates = {}
        
        sub.junctions = {}
        sub.outfalls = {}
        sub.storages = {}
        sub.dividers = {}
        
    def add_NODE(sub, NODENAME, ELEVATION, XCOORD, YCOORD, YMAX = 0, Y0 = 0,\
                 YSURCHARGE = 0, PONDINGAREA = 0, CLASS = 'JUNCTION',TYPE = 'FREE',\
                 TSERIES = '', GATE = False, FEVAP=0, TABULAR='', ACURVE='',\
                 FUNCTIONAL='', SH='', HC='', IMD=''):
        if CLASS == 'JUNCTION': sub._add_junction(NODENAME, ELEVATION, XCOORD, YCOORD, YMAX,\
                                                  Y0, YSURCHARGE, PONDINGAREA)
        if CLASS == 'OUTFALL': sub._add_outfall(NODENAME, ELEVATION,\
                                                XCOORD, YCOORD, TYPE,\
                                                TSERIES, GATE)
        if CLASS == 'STORAGE': sub._add_storage(NODENAME, ELEVATION, XCOORD, YCOORD, YMAX, Y0, PONDINGAREA,\
                                                FEVAP, TABULAR, ACURVE, FUNCTIONAL, SH, HC, IMD)
##        if CLASS == 'DIVIDER': sub._add_divider(NODENAME, ELEVATION, XCOORD, YCOORD, YMAX,\
##                                                  Y0, YSURCHARGE, PONDINGAREA)        
    def remove_NODE(sub,NODENAME):
        sub.junctions.pop(NODENAME,None)
        sub.coordinates.pop(NODENAME,None)
        sub.nodetypedict.pop(NODENAME,None)

    def update_NODE():
        pass

    def convert_NODE():
        pass
    
    def _add_junction(sub, NODENAME, ELEVATION, XCOORD, YCOORD, YMAX, Y0, YSURCHARGE, PONDINGAREA):
        assert NODENAME not in sub.nodetypedict.keys()
        #udpate node type dict
        sub.nodetypedict[NODENAME] = 'JUNCTION'
        sub._assignNodeCoordinates(NODENAME, XCOORD, YCOORD)
        
        #assign junction params
        sub.junctions[NODENAME] = JUNCTIONS()
        sub.junctions[NODENAME].NODENAME = NODENAME
        sub.junctions[NODENAME].ELEVATION = ELEVATION
        sub.junctions[NODENAME].YMAX = YMAX
        sub.junctions[NODENAME].Y0 = Y0
        sub.junctions[NODENAME].YSURCHARGE = YSURCHARGE
        sub.junctions[NODENAME].PONDINGAREA = PONDINGAREA

    def _add_outfall(sub, NODENAME, ELEVATION, XCOORD, YCOORD, TYPE,TSERIES, GATE):
        assert NODENAME not in sub.nodetypedict.keys()
        #udpate node type dict
        sub.nodetypedict[NODENAME] = 'OUTFALL'
        sub._assignNodeCoordinates(NODENAME, XCOORD, YCOORD)

        sub.outfalls[NODENAME] = OUTFALLS()
        sub.outfalls[NODENAME].NODENAME = NODENAME
        sub.outfalls[NODENAME].ELEVATION = ELEVATION
        sub.outfalls[NODENAME].TYPE = TYPE
        sub.outfalls[NODENAME].TSERIES = TSERIES
        sub.outfalls[NODENAME].GATE = GATE
        
    def _add_storage(sub, NODENAME, ELEVATION, XCOORD, YCOORD, YMAX, Y0, PONDINGAREA,\
                     FEVAP, TABULAR, ACURVE, FUNCTIONAL, SH, HC, IMD):
        assert NODENAME not in sub.nodetypedict.keys()
        #udpate node type dict
        sub.nodetypedict[NODENAME] = 'STORAGE'
        sub._assignNodeCoordinates(NODENAME, XCOORD, YCOORD)

        sub.storages[NODENAME] = STORAGE()
        sub.storages[NODENAME].NODENAME = NODENAME
        sub.storages[NODENAME].ELEVATION = ELEVATION
        sub.storages[NODENAME].YMAX = YMAX
        sub.storages[NODENAME].Y0 = Y0
        sub.storages[NODENAME].APOND = PONDINGAREA
        sub.storages[NODENAME].FEVAP = FEVAP
        sub.storages[NODENAME].TABULAR = TABULAR
        sub.storages[NODENAME].ACURVE = ACURVE
        sub.storages[NODENAME].FUNCTIONAL = FUNCTIONAL
        sub.storages[NODENAME].SH = SH
        sub.storages[NODENAME].HC = HC
        sub.storages[NODENAME].IMD = IMD        
      
    def _assignNodeCoordinates(sub, NODENAME, XCOORD, YCOORD):
        #assign coordinates
        sub.coordinates[NODENAME] = COORDINATES()
        sub.coordinates[NODENAME].NODENAME = NODENAME
        sub.coordinates[NODENAME].xcoord = XCOORD
        sub.coordinates[NODENAME].ycoord = YCOORD

        
class HYDROLOGY:
    '''
    Currently setup for Green-Ampt Infiltration, only (BM 6/3/2015).

    PolygonGrid assigns a grid position for a polygon based on
    the position of the loading manhole. by using gridpos, the
    location of the polygon will be assigned based on the x and y
    offsets, polygon width and height, and x and y separation. 

    PolygonGrid
     --- --- --- ---
    | 1 | 2 | 3 | 4 |
     --- --- --- ---
    | 5 | 6 | 7 | 8 |
     --- --- --- ---
    | 9 | 10| 11| 12|
     --- --- --- ---
     
    1 -,2 -,3 -,4 -,5 -,6 -,7 -,8 -,9 -,10-,11-, 12-
    
    '''
    def __init__(sub, self):

        sub.self = self
    
        sub.subcatchments = {}
        sub.subareas = {}
        sub.infiltration = {}
        sub.polygons = {}

        sub.xOffset_all = 10
        sub.yOffset_all = 10
        sub.polywidth = 10
        sub.polyheight = 10
        sub.xsep = 15
        sub.ysep = 15
        
        sub.updatePolyGrid()
        
    def updatePolyGrid(sub):
        #Polygon grid spacing
        sub.gridx = {1:0*sub.xsep, 2:1*sub.xsep, 3:2*sub.xsep, 4:3*sub.xsep,\
                     5:0*sub.xsep, 6:1*sub.xsep, 7:2*sub.xsep, 8:3*sub.xsep,\
                     9:0*sub.xsep, 10:1*sub.xsep,11:2*sub.xsep,12:3*sub.xsep}
        sub.gridy = {1:2*sub.ysep, 2:2*sub.ysep, 3:2*sub.ysep, 4:2*sub.ysep,\
                     5:1*sub.ysep, 6:1*sub.ysep, 7:1*sub.ysep, 8:1*sub.ysep,\
                     9:0*sub.ysep, 10:0*sub.ysep,11:0*sub.ysep,12:0*sub.ysep}

    def updatePolyCirc(sub, radius = 40):
        from math import pi, sin, cos
        import numpy as np

        sub.radius = radius        
        Positions = np.linspace(0, 2*pi, 13)
        sub.gridx = {}
        sub.gridy = {}
        for i in range(1,13):
            sub.gridx[i] = sin(Positions[i-1])*sub.radius
            sub.gridy[i] = cos(Positions[i-1])*sub.radius
            
        
        
        
    def add_HYDROLOGY(sub, SUBCNAME, RGAGE, OUTID, CLAJunction, AREA, PERCENT_IMPERV,\
                      WIDTH, ROUTETO = 'Outlet', SLOPE = 0.1, CLENGTH = 0, SNOWPACK = 0,\
                      NIMP = 0.015, NPERV = 0.015, SIMP = 0.01, SPERV = 0.01,\
                      PERCENT_ZERO = 0, PERCENT_ROUTED = 100,\
                      SUCTION = 11, CONDUCT=0.12, INITDEF = 0.1, \
                      gridpos = 9):
        
        sub._add_subcatchment(SUBCNAME, RGAGE, OUTID, AREA, PERCENT_IMPERV,\
                              WIDTH, SLOPE, CLENGTH, SNOWPACK)
        sub._add_subarea(SUBCNAME, NIMP, NPERV, SIMP, SPERV,\
                         PERCENT_ZERO, ROUTETO, PERCENT_ROUTED)
        sub._add_infiltration(SUBCNAME, SUCTION, CONDUCT, INITDEF)

        sub._add_polygon(SUBCNAME, CLAJunction, gridpos) 

    def remove_HYDROLOGY(sub, SUBCNAME):
        sub.subcatchments[SUBCNAME].pop(SUBCNAME,None)
        sub.subareas[SUBCNAME].pop(SUBCNAME,None)
        sub.infiltration[SUBCNAME].pop(SUBCNAME,None)
        sub.polygons[SUBCNAME].pop(SUBCNAME,None)
        if hasattr(sub.self,'GroundwaterFlow'):
            sub.self.GroundwaterFlow.groundwater.pop(SUBCATCH,None)
            sub.self.GroundwaterFlow.aquifers.pop(SUBCATCH,None)

    def update_HYDROLOGY():
        pass

    def _add_subcatchment(sub, SUBCNAME, RGAGE, OUTID, AREA, PERCENT_IMPERV,\
                          WIDTH, SLOPE, CLENGTH, SNOWPACK):
        
        sub.subcatchments[SUBCNAME] = SUBCATCHMENTS()
        sub.subcatchments[SUBCNAME].SUBCNAME = SUBCNAME
        sub.subcatchments[SUBCNAME].RGAGE = RGAGE
        sub.subcatchments[SUBCNAME].OUTID = OUTID
        sub.subcatchments[SUBCNAME].AREA = AREA
        sub.subcatchments[SUBCNAME].PERCENT_IMPERV = PERCENT_IMPERV
        sub.subcatchments[SUBCNAME].WIDTH = WIDTH
        sub.subcatchments[SUBCNAME].SLOPE = SLOPE
        sub.subcatchments[SUBCNAME].CLENGTH = CLENGTH
        sub.subcatchments[SUBCNAME].SNOWPACK = SNOWPACK
            
    def _add_subarea(sub, SUBCNAME, NIMP, NPERV, SIMP, SPERV,\
                     PERCENT_ZERO, ROUTETO, PERCENT_ROUTED):
        
        sub.subareas[SUBCNAME] = SUBAREAS()
        sub.subareas[SUBCNAME].SUBCNAME = SUBCNAME
        sub.subareas[SUBCNAME].NIMP = NIMP
        sub.subareas[SUBCNAME].NPERV = NPERV
        sub.subareas[SUBCNAME].SIMP = SIMP
        sub.subareas[SUBCNAME].SPERV = SPERV
        sub.subareas[SUBCNAME].PERCENT_ZERO = PERCENT_ZERO
        sub.subareas[SUBCNAME].ROUTETO = ROUTETO
        sub.subareas[SUBCNAME].PERCENT_ROUTED = PERCENT_ROUTED

    def _add_infiltration(sub, SUBCNAME, SUCTION, CONDUCT, INITDEF):
        
        sub.infiltration[SUBCNAME] = INFILTRATION()
        sub.infiltration[SUBCNAME].SUBCNAME = SUBCNAME
        sub.infiltration[SUBCNAME].SUCTION = SUCTION
        sub.infiltration[SUBCNAME].CONDUCT = CONDUCT
        sub.infiltration[SUBCNAME].INITDEF = INITDEF

    def _add_polygon(sub, SUBCNAME, CLAJunction, gridpos):
        if str(CLAJunction) in sub.self.Nodes.nodetypedict.keys():
            sub.polygons[SUBCNAME] = POLYGONS()
            sub.polygons[SUBCNAME].SUBCNAME = SUBCNAME
            NodeXcoord = int(sub.self.Nodes.coordinates[str(CLAJunction)].xcoord)
            NodeYcoord = int(sub.self.Nodes.coordinates[str(CLAJunction)].ycoord)
            #NW
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] - 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] + 0.5* sub.polyheight ])
            #NE
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] + 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] + 0.5* sub.polyheight ])
            #SE
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] + 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] - 0.5* sub.polyheight ])
            #SW
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] - 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] - 0.5* sub.polyheight ])        

    def _add_polygonUL(sub, SUBCNAME, CLAJunction, gridpos):
        if str(CLAJunction) in sub.self.Nodes.nodetypedict.keys():
            sub.polygons[SUBCNAME] = POLYGONS()
            sub.polygons[SUBCNAME].SUBCNAME = SUBCNAME
            NodeXcoord = int(sub.self.Nodes.coordinates[str(CLAJunction)].xcoord)
            NodeYcoord = int(sub.self.Nodes.coordinates[str(CLAJunction)].ycoord)
            #NW
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] - 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] + 0.5* sub.polyheight ])
            #NE
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] + 0.45* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] + 0.5* sub.polyheight ])
            #SW
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] - 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] - 0.45* sub.polyheight ])
            
    def _add_polygonLR(sub, SUBCNAME, CLAJunction, gridpos):
        if str(CLAJunction) in sub.self.Nodes.nodetypedict.keys():
            sub.polygons[SUBCNAME] = POLYGONS()
            sub.polygons[SUBCNAME].SUBCNAME = SUBCNAME
            NodeXcoord = int(sub.self.Nodes.coordinates[str(CLAJunction)].xcoord)
            NodeYcoord = int(sub.self.Nodes.coordinates[str(CLAJunction)].ycoord)
            #NE
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] + 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] + 0.45* sub.polyheight ])
            #SE
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] + 0.5* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] - 0.5* sub.polyheight ])
            #SW
            sub.polygons[SUBCNAME].PolyCoord.append([NodeXcoord + sub.xOffset_all + sub.gridx[gridpos] - 0.45* sub.polywidth ,\
                                                     NodeYcoord + sub.yOffset_all + sub.gridy[gridpos] - 0.5* sub.polyheight ]) 



class OPTIONSset:
    def __init__(self):
        self.Options = OPTIONS()
        
    def add_OPTIONS(self,\
                    FLOW_UNITS = 'MGD',\
                    INFILTRATION = 'GREEN_AMPT',\
                    FLOW_ROUTING = 'KINWAVE',\
                    LINK_OFFSETS = 'DEPTH',\
                    FORCE_MAIN_EQUATION = 'H-W',\
                    IGNORE_RAINFALL = 'NO',\
                    IGNORE_SNOWMELT = 'NO',\
                    IGNORE_GROUNDWATER = 'NO',\
                    IGNORE_ROUTING = 'NO',\
                    IGNORE_QUALITY = 'NO',\
                    ALLOW_PONDING = 'NO',\
                    SKIP_STEADY_STATE = 'NO',\
                    START_DATE = '01/01/2015',\
                    START_TIME = '00:00',\
                    END_DATE = '01/01/2015',\
                    END_TIME = '00:00',\
                    REPORT_START_DATE = '01/02/2015',\
                    REPORT_START_TIME = '00:00',\
                    SWEEP_START = '01/01',\
                    SWEEP_END = '12/31',\
                    DRY_DAYS = '0',\
                    REPORT_STEP = '0:15:00',\
                    WET_STEP = '0:05:00',\
                    DRY_STEP = '1:00:00',\
                    ROUTING_STEP = '30',\
                    LENGTHENING_STEP = '0',\
                    VARIABLE_STEP = '0',\
                    INERTIAL_DAMPENING = 'NONE',\
                    NORMAL_FLOW_LIMITED = 'BOTH',\
                    MIN_SURFAREA = '12.566',\
                    MIN_SLOPE = '0.001',\
                    TEMPDIR = ''):
        
        self.Options.FLOW_UNITS = FLOW_UNITS
        self.Options.INFILTRATION = INFILTRATION
        self.Options.FLOW_ROUTING = FLOW_ROUTING
        self.Options.LINK_OFFSETS = LINK_OFFSETS
        self.Options.FORCE_MAIN_EQUATION = FORCE_MAIN_EQUATION
        self.Options.IGNORE_RAINFALL = IGNORE_RAINFALL
        self.Options.IGNORE_SNOWMELT = IGNORE_SNOWMELT
        self.Options.IGNORE_GROUNDWATER = IGNORE_GROUNDWATER
        self.Options.IGNORE_ROUTING = IGNORE_ROUTING
        self.Options.IGNORE_QUALITY = IGNORE_QUALITY
        self.Options.ALLOW_PONDING = ALLOW_PONDING
        self.Options.SKIP_STEADY_STATE = SKIP_STEADY_STATE
        self.Options.START_DATE = START_DATE
        self.Options.START_TIME = START_TIME
        self.Options.END_DATE = END_DATE
        self.Options.END_TIME = END_TIME
        self.Options.REPORT_START_DATE = REPORT_START_DATE
        self.Options.REPORT_START_TIME = REPORT_START_TIME
        self.Options.SWEEP_START = SWEEP_START
        self.Options.SWEEP_END = SWEEP_END
        self.Options.DRY_DAYS = DRY_DAYS
        self.Options.REPORT_STEP = REPORT_STEP
        self.Options.WET_STEP = WET_STEP
        self.Options.DRY_STEP = DRY_STEP
        self.Options.ROUTING_STEP = ROUTING_STEP
        self.Options.LENGTHENING_STEP = LENGTHENING_STEP
        self.Options.VARIABLE_STEP = VARIABLE_STEP
        self.Options.INERTIAL_DAMPENING = INERTIAL_DAMPENING
        self.Options.NORMAL_FLOW_LIMITED = NORMAL_FLOW_LIMITED
        self.Options.MIN_SURFAREA = MIN_SURFAREA
        self.Options.MIN_SLOPE = MIN_SLOPE
        self.Options.TEMPDIR = TEMPDIR        

if __name__ in '__main__':
    self = MODELOBJECTS()

    self.Eval_Options()
    self.Options.add_OPTIONS()
    
    self.Eval_Nodes()
    self.Nodes.add_NODE('Node1',122,0,0)
    self.Nodes.add_NODE('Node2',500,200,200)
    self.Nodes.add_NODE('Node4',500,200,200, CLASS = 'OUTFALL')
    self.Nodes.add_NODE('Node6',500,200,200, CLASS = 'STORAGE')
    
    self.Eval_Hydrology()
    self.Hydrology.add_HYDROLOGY('A','Node1',222,'Node1',4000,50,200, gridpos=5)
    self.Hydrology.add_HYDROLOGY('B','Node2',44,'Node2',40100,520,2003)

    self.Eval_GroundwaterFlow()
    self.GroundwaterFlow.add_GWFLOW('Aa_A','A', 'Node6')

    print_Model(self)

'''

'''

class OPTIONS:
    def __init__(self):
        self.FLOW_UNITS = ''
        self.INFILTRATION = ''
        self.FLOW_ROUTING = ''
        self.LINK_OFFSETS = ''
        self.FORCE_MAIN_EQUATION = ''
        self.IGNORE_RAINFALL = ''
        self.IGNORE_SNOWMELT = ''
        self.IGNORE_GROUNDWATER = ''
        self.IGNORE_ROUTING = ''
        self.IGNORE_QUALITY = ''
        self.ALLOW_PONDING = ''
        self.SKIP_STEADY_STATE = ''
        self.START_DATE = ''
        self.START_TIME = ''
        self.END_DATE = ''
        self.END_TIME = ''
        self.REPORT_START_DATE = ''
        self.REPORT_START_TIME = ''
        self.SWEEP_START = ''
        self.SWEEP_END = ''
        self.DRY_DAYS = ''
        self.REPORT_STEP = ''
        self.WET_STEP = ''
        self.DRY_STEP = ''
        self.ROUTING_STEP = ''
        self.LENGTHENING_STEP = ''
        self.VARIABLE_STEP = ''
        self.INERTIAL_DAMPENING = ''
        self.NORMAL_FLOW_LIMITED = ''
        self.MIN_SURFAREA = ''
        self.MIN_SLOPE = ''
        self.TEMPDIR = ''

class REPORT:
    def __init__(self):
        self.INPUT = 'YES'
        self.CONTINUITY = 'YES'
        self.FLOWSTATS = 'YES'
        self.CONTROLS = 'YES'
        self.SUBCATCHMENTS = 'ALL'
        self.NODES = 'ALL'
        self.LINKS = 'ALL'

class FILES:
    def __init__(self):
        self.RAINFALL = ''
        self.RUNOFF = ''
        self.HOTSTART = ''
        self.RDII = ''
        self.INFLOWS = ''
        self.OUTFLOWS = ''

class RAINGAGES:
    def __init__(self):
        self.NAME = ''
        self.FORM = ''
        self.INTERVAL = ''
        self.SCF = ''
        
        #Type (TIMESERIES)
        self.TIMESERIES = None
        self.Tseries = None
        #Type (FILE)        
        self.FILE = None
        self.FNAME = None
        self.Station = None
        self.Units = None

class EVAPORATION:
    def __init__(self):
        self.CONSTANT = ''
        self.MONTHLY = [None]*12
        self.TIMESERIES = ''
        self.TEMPERATURE_FILE = ['']*12
        self.RECOVERY = ''
        self.DRY_ONLY = 'NO'

class TEMPERATURE:
    def __init__(self):
        self.TIMESERIES = ''
        self.FILE = ''
        self.FILE_START = ''
        self.WINDSPEED = [None]*12
        self.WINDSPEED_FILE = ''
##        self.SNOWMELT_STEMP = ''
##        self.SNOWMELT_ATIWT = ''
##        self.SNOWMELT_RNM = ''
##        self.SNOWMELT_ELEV = ''
##        self.SNOWMELT_LAT = ''
##        self.SNOWMELT_DTLONG = ''
##        self.ADC_

class SUBCATCHMENTS:
    def __init__(self):
        self.SUBCNAME = ''
        self.RGAGE = ''
        self.OUTID = ''
        self.AREA = ''
        self.PERCENT_IMPERV = ''
        self.WIDTH = ''
        self.SLOPE = ''
        self.CLENGTH = ''
        self.SNOWPACK = ''

class SUBAREAS:
    def __init__(self):
        self.SUBCNAME = ''
        self.NIMP = ''
        self.NPERV = ''
        self.SIMP = ''
        self.SPERV = ''
        self.PERCENT_ZERO = ''
        self.ROUTETO = ''
        self.PERCENT_ROUTED = ''

class INFILTRATION:
    def __init__(self):
        self.SUBCNAME = ''
        #HORTON
        self.MAXRATE = None
        self.MINRATE = None
        
        self.DRYTIME = None
        self.MAXINF = None
        #GREEN-AMPT
        self.SUCTION = None
        self.INITDEF = None
        #CURVE-NUMBER
        self.CURVENO = None        
        #GA and CN
        self.CONDUCT = ''
        #Hort and CN
        self.DECAY = ''

class AQUIFERS:
    def __init__(self):
        self.AQNAME = ''
        self.POROSITY = ''
        self.WILTINGPOINT = ''
        self.FIELDCAPACITY = ''
        self.CONDUCTIVITY = ''
        self.CONDUCTIVITYSLOPE = ''
        self.TENSIONSLOPE = ''
        self.UPPEREVAPFRACTION = ''
        self.LOWEREVAPFRACTION = ''
        self.LOWERGWLOSS = ''
        self.BOTTOMELEVATION = ''
        self.WATERTABLEELEVATION = ''
        self.UNSATZONEMOISTURE = ''
        self.UPPEREVAPPATTERN = ''

class GROUNDWATER:
    def __init__(self):
        self.SUBCNAME = ''
        self.AQNAME = ''
        self.LOADINGNODE = ''
        self.SURFACEEL = ''
        self.A1 = ''
        self.B1 = ''
        self.A2 = ''
        self.B2 = ''
        self.A3 = ''
        self.TW = ''
        self.GWTHEIGHT = ''

class JUNCTIONS:
    def __init__(self):
        self.NODENAME = ''
        self.ELEVATION = ''
        self.YMAX = ''
        self.Y0 = ''
        self.YSURCHARGE = ''
        self.PONDINGAREA = ''

class OUTFALLS:
    def __init__(self):
        self.NODENAME = ''
        self.ELEVATION = ''
        self.TYPE = ''
        self.TSERIES = ''
        self.GATE = False

##class DIVIDERS:
##    def __init__(self):
##        self.NODENAME = ''
##        self.ELEVATION = ''

class STORAGE:
    def __init__(self):
        self.NODENAME = ''
        self.ELEVATION = ''
        self.YMAX = ''
        self.Y0 = ''
        self.APOND = ''
        self.FEVAP = ''
        self.TABULAR = False
        self.ACURVE = ''
        self.FUNCTIONAL = True
        self.SH = ''
        self.HC = ''
        self.IMD = ''
        
        

class POLYGONS:
    def __init__(self):
        self.SUBCNAME = ''
        self.PolyCoord = []

class COORDINATES:
    def __init__(self):
        self.NODENAME = ''
        self.xcoord = ''
        self.ycoord = ''

'''
This script includes the object export functions used for printing to screen

Author: B.E. McDonnell
Date: 6/4/2015

'''


def print_Model(self):
    
    if hasattr(self, 'Nodes'):
        print '[JUNCTIONS]'
        for junc in self.Nodes.junctions.keys():
            Node = self.Nodes.junctions[junc]
            print '\t'.join([Node.NODENAME, str(Node.ELEVATION), str(Node.YMAX), str(Node.Y0), str(Node.YSURCHARGE), str(Node.PONDINGAREA)])

    if hasattr(self.Nodes, 'coordinates'):
        print '\n[COORDINATES]'
        for node in self.Nodes.coordinates.keys():
            Node = self.Nodes.coordinates[node]
            print '\t'.join([Node.NODENAME, str(Node.xcoord), str(Node.ycoord)])

    if hasattr(self,'Hydrology'):
        print '\n[SUBCATCHMENTS]'
        for scatch in self.Hydrology.subcatchments.keys():
            SC = self.Hydrology.subcatchments[scatch]
            print '\t'.join([str(SC.SUBCNAME),str(SC.RGAGE),str(SC.OUTID),str(SC.AREA),str(SC.PERCENT_IMPERV),\
                             str(SC.WIDTH),str(SC.SLOPE),str(SC.CLENGTH),str(SC.SNOWPACK)])

        print '\n[SUBAREAS]'
        for scatch in self.Hydrology.subareas.keys():
            SA = self.Hydrology.subareas[scatch]
            print '\t'.join([str(SA.SUBCNAME),str(SA.NIMP),str(SA.NPERV),str(SA.SIMP),\
                             str(SA.SPERV),str(SA.PERCENT_ZERO),str(SA.ROUTETO),str(SA.PERCENT_ROUTED)])                

        print '\n[INFILTRATION]'
        for scatch in self.Hydrology.infiltration.keys():
            SC = self.Hydrology.infiltration[scatch]
            print '\t'.join([str(SC.SUBCNAME),str(SC.SUCTION),str(SC.CONDUCT),str(SC.INITDEF)])

    if hasattr(self.Hydrology, 'polygons'):
        print '\n[POLYGONS]'
        for scatch in self.Hydrology.polygons.keys():
            SC = self.Hydrology.polygons[scatch]
            for coord in SC.PolyCoord:
                print '\t'.join([str(SC.SUBCNAME), str(coord[0]), str(coord[1])])

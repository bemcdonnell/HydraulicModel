'''
This script includes the object export functions used for printing to screen

Author: B.E. McDonnell
Date: 6/4/2015

'''


def print_Model(self):
    
    if hasattr(self, 'Nodes'):
        if hasattr(self.Nodes, 'junctions'):
            print '\n[JUNCTIONS]'
            for junc in self.Nodes.junctions.keys():
                Node = self.Nodes.junctions[junc]
                print '\t'.join([Node.NODENAME, str(Node.ELEVATION), str(Node.YMAX), str(Node.Y0), str(Node.YSURCHARGE), str(Node.PONDINGAREA)])
        if hasattr(self.Nodes, 'outfalls'):
            print '\n[OUTFALLS]'
            for junc in self.Nodes.outfalls.keys():
                Node = self.Nodes.outfalls[junc]
                print '\t'.join([Node.NODENAME, str(Node.ELEVATION), str(Node.TYPE), str(Node.TSERIES), str(Node.GATE)])
        if hasattr(self.Nodes, 'storages'):
            print '\n[STORAGE]'
            for junc in self.Nodes.storages.keys():
                Node = self.Nodes.storages[junc]
                print '\t'.join([Node.NODENAME, str(Node.ELEVATION), str(Node.YMAX), str(Node.Y0), str(Node.APOND), str(Node.FEVAP), str(Node.TABULAR), str(Node.ACURVE), str(Node.FUNCTIONAL), str(Node.SH), str(Node.HC), str(Node.IMD)])


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
                             str(SC.WIDTH),str(SC.SLOPE),str(SC.CLENGTH)])#,str(SC.SNOWPACK)]) #< - For now ignoreing snow pack

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


    if hasattr(self, 'GroundwaterFlow'):
        if hasattr(self.GroundwaterFlow, 'groundwater'):
            print '\n[GROUNDWATER]'
            for GW in self.GroundwaterFlow.groundwater.keys():
                SC = self.GroundwaterFlow.groundwater[GW]
                print '\t'.join([str(SC.SUBCNAME),str(SC.AQNAME),\
                                 str(SC.LOADINGNODE),str(SC.SURFACEEL),\
                                 str(SC.A1),str(SC.B1),str(SC.A2),str(SC.B2),\
                                 str(SC.A3),str(SC.TW),str(SC.GWTHEIGHT)])
        if hasattr(self.GroundwaterFlow, 'aquifers'):
            print '\n[AQUIFERS]'
            for GW in self.GroundwaterFlow.aquifers.keys():
                SC = self.GroundwaterFlow.aquifers[GW]
                print '\t'.join([str(SC.AQNAME),str(SC.POROSITY),\
                                 str(SC.WILTINGPOINT),str(SC.FIELDCAPACITY),\
                                 str(SC.CONDUCTIVITY),str(SC.CONDUCTIVITYSLOPE),\
                                 str(SC.TENSIONSLOPE),str(SC.UPPEREVAPFRACTION),\
                                 str(SC.LOWEREVAPFRACTION),str(SC.LOWERGWLOSS),\
                                 str(SC.BOTTOMELEVATION),str(SC.WATERTABLEELEVATION),\
                                 str(SC.UNSATZONEMOISTURE),str(SC.UPPEREVAPPATTERN)])
                                
def export_Model(self, ModelFile = 'Testing.inp'):
    with open(ModelFile, 'w') as f:
##        f.write('testing\n')
        if hasattr(self, 'Options') and True == False:
            f.write('[OPTIONS]'+'\n')
            f.write('FLOW_UNITS '+ self.Options.FLOW_UNITS+'\n')
            f.write('INFILTRATION ' + self.Options.INFILTRATION+'\n') 
            f.write('FLOW_ROUTING ' +self.Options.FLOW_ROUTING+'\n')  
            f.write('LINK_OFFSETS ' +self.Options.LINK_OFFSETS+'\n')  
            f.write('FORCE_MAIN_EQUATION ' +self.Options.FORCE_MAIN_EQUATION+'\n')
            f.write('IGNORE_RAINFALL ' +self.Options.IGNORE_RAINFALL+'\n') 
            f.write('IGNORE_SNOWMELT ' +self.Options.IGNORE_SNOWMELT+'\n')  
            f.write('IGNORE_GROUNDWATER '+ self.Options.IGNORE_GROUNDWATER+'\n') 
            f.write('IGNORE_ROUTING '+ self.Options.IGNORE_ROUTING+'\n')
            f.write('IGNORE_QUALITY '+ self.Options.IGNORE_QUALITY+'\n') 
            f.write('ALLOW_PONDING '+ self.Options.ALLOW_PONDING+'\n')  
            f.write('SKIP_STEADY_STATE '+ self.Options.SKIP_STEADY_STATE+'\n')
            f.write('START_DATE '+ self.Options.START_DATE+'\n')
            f.write('START_TIME '+ self.Options.START_TIME+'\n') 
            f.write('END_DATE '+ self.Options.END_DATE+'\n')
            f.write('END_TIME '+ self.Options.END_TIME+'\n') 
            f.write('REPORT_START_DATE '+ self.Options.REPORT_START_DATE+'\n')
            f.write('REPORT_START_TIME '+ self.Options.REPORT_START_TIME+'\n') 
            f.write('SWEEP_START '+ self.Options.SWEEP_START+'\n')
            f.write('SWEEP_END '+ self.Options.SWEEP_END+'\n')
            f.write('DRY_DAYS '+ self.Options.DRY_DAYS+'\n') 
            f.write('REPORT_STEP '+ self.Options.REPORT_STEP+'\n')
            f.write('WET_STEP '+ self.Options.WET_STEP+'\n')
            f.write('DRY_STEP '+ self.Options.DRY_STEP+'\n') 
            f.write('ROUTING_STEP '+ self.Options.ROUTING_STEP+'\n')
            f.write('LENGTHENING_STEP '+ self.Options.LENGTHENING_STEP+'\n')
            f.write('VARIABLE_STEP '+ self.Options.VARIABLE_STEP+'\n')
            f.write('INERTIAL_DAMPENING '+ self.Options.INERTIAL_DAMPENING+'\n') 
            f.write('NORMAL_FLOW_LIMITED '+ self.Options.NORMAL_FLOW_LIMITED+'\n')
            f.write('MIN_SURFAREA '+ self.Options.MIN_SURFAREA+'\n')
            f.write('MIN_SLOPE '+ self.Options.MIN_SLOPE+'\n')
            f.write('TEMPDIR '+ self.Options.TEMPDIR+'\n')            
        if hasattr(self, 'Nodes'):
            f.write('[JUNCTIONS]'+'\n')
            for junc in self.Nodes.junctions.keys():
                Node = self.Nodes.junctions[junc]
                f.write('\t'.join([Node.NODENAME, str(Node.ELEVATION), str(Node.YMAX), str(Node.Y0), str(Node.YSURCHARGE), str(Node.PONDINGAREA)])+'\n')

        if hasattr(self.Nodes, 'coordinates'):
            f.write('\n[COORDINATES]'+'\n')
            for node in self.Nodes.coordinates.keys():
                Node = self.Nodes.coordinates[node]
                f.write('\t'.join([Node.NODENAME, str(Node.xcoord), str(Node.ycoord)])+'\n')

        if hasattr(self,'Hydrology'):
            f.write('\n[SUBCATCHMENTS]'+'\n')
            for scatch in self.Hydrology.subcatchments.keys():
                SC = self.Hydrology.subcatchments[scatch]
                f.write('\t'.join([str(SC.SUBCNAME),str(SC.RGAGE),str(SC.OUTID),str(SC.AREA),str(SC.PERCENT_IMPERV),\
                                 str(SC.WIDTH),str(SC.SLOPE),str(SC.CLENGTH)])+'\n') #,str(SC.SNOWPACK) removed snow back for time being

            f.write('\n[SUBAREAS]'+'\n')
            for scatch in self.Hydrology.subareas.keys():
                SA = self.Hydrology.subareas[scatch]
                f.write('\t'.join([str(SA.SUBCNAME),str(SA.NIMP),str(SA.NPERV),str(SA.SIMP),\
                                 str(SA.SPERV),str(SA.PERCENT_ZERO),str(SA.ROUTETO),str(SA.PERCENT_ROUTED)])+'\n')               

            f.write('\n[INFILTRATION]'+'\n')
            for scatch in self.Hydrology.infiltration.keys():
                SC = self.Hydrology.infiltration[scatch]
                f.write('\t'.join([str(SC.SUBCNAME),str(SC.SUCTION),str(SC.CONDUCT),str(SC.INITDEF)])+'\n')

            if hasattr(self.Hydrology, 'polygons'):
                f.write('\n[POLYGONS]'+'\n')
                for scatch in self.Hydrology.polygons.keys():
                    SC = self.Hydrology.polygons[scatch]
                    for coord in SC.PolyCoord:
                        f.write('\t'.join([str(SC.SUBCNAME), str(coord[0]), str(coord[1])])+'\n')
    f.close()

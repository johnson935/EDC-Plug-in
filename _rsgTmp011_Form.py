from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class _rsgTmp011_Form(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='fEDC',
            objectName='EDC2', registerQuery=False)
        pickedDefault = ''
        self.modelKw = AFXStringKeyword(self.cmd, 'model', True)
        self.partKw = AFXStringKeyword(self.cmd, 'part', True)
        if not self.radioButtonGroups.has_key('cusMat'):
            self.cusMatKw1 = AFXIntKeyword(None, 'cusMatDummy', True)
            self.cusMatKw2 = AFXStringKeyword(self.cmd, 'cusMat', True)
            self.radioButtonGroups['cusMat'] = (self.cusMatKw1, self.cusMatKw2, {})
        self.radioButtonGroups['cusMat'][2][59] = 'Default Material'
        self.cusMatKw1.setValue(59)
        self.matKw = AFXStringKeyword(self.cmd, 'mat', True, 'T800s/M21')
        if not self.radioButtonGroups.has_key('cusMat'):
            self.cusMatKw1 = AFXIntKeyword(None, 'cusMatDummy', True)
            self.cusMatKw2 = AFXStringKeyword(self.cmd, 'cusMat', True)
            self.radioButtonGroups['cusMat'] = (self.cusMatKw1, self.cusMatKw2, {})
        self.radioButtonGroups['cusMat'][2][60] = 'Custom Material'
        self.g0Kw = AFXIntKeyword(self.cmd, 'g0', True, 0)
        self.g90Kw = AFXStringKeyword(self.cmd, 'g90', True, '0')
        self.unitKw = AFXStringKeyword(self.cmd, 'unit', True, 'm/N')
        self.singlePlaneKw = AFXBoolKeyword(self.cmd, 'singlePlane', AFXBoolKeyword.TRUE_FALSE, True, False)
        if not self.radioButtonGroups.has_key('selectPsingle'):
            self.selectPsingleKw1 = AFXIntKeyword(None, 'selectPsingleDummy', True)
            self.selectPsingleKw2 = AFXStringKeyword(self.cmd, 'selectPsingle', True)
            self.radioButtonGroups['selectPsingle'] = (self.selectPsingleKw1, self.selectPsingleKw2, {})
        self.radioButtonGroups['selectPsingle'][2][61] = 'Select Three Points (Nodes In Mesh) On Fracture Plane:'
        self.selectPsingleKw1.setValue(61)
        self.coord1Kw = AFXObjectKeyword(self.cmd, 'coord1', TRUE, pickedDefault)
        self.coord2Kw = AFXObjectKeyword(self.cmd, 'coord2', TRUE, pickedDefault)
        self.coord3Kw = AFXObjectKeyword(self.cmd, 'coord3', TRUE, pickedDefault)
        if not self.radioButtonGroups.has_key('selectPsingle'):
            self.selectPsingleKw1 = AFXIntKeyword(None, 'selectPsingleDummy', True)
            self.selectPsingleKw2 = AFXStringKeyword(self.cmd, 'selectPsingle', True)
            self.radioButtonGroups['selectPsingle'] = (self.selectPsingleKw1, self.selectPsingleKw2, {})
        self.radioButtonGroups['selectPsingle'][2][62] = 'Or Define Points Manually:'
        self.enterCoord1Kw = AFXTableKeyword(self.cmd, 'enterCoord1', True)
        self.enterCoord1Kw.setColumnType(-1, AFXTABLE_TYPE_FLOAT)
        self.enterCoord1Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.enterCoord1Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.enterCoord2Kw = AFXTableKeyword(self.cmd, 'enterCoord2', True)
        self.enterCoord2Kw.setColumnType(-1, AFXTABLE_TYPE_FLOAT)
        self.enterCoord2Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.enterCoord2Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.enterCoord3Kw = AFXTableKeyword(self.cmd, 'enterCoord3', True)
        self.enterCoord3Kw.setColumnType(-1, AFXTABLE_TYPE_FLOAT)
        self.enterCoord3Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.enterCoord3Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.multiPlaneKw = AFXBoolKeyword(self.cmd, 'multiPlane', AFXBoolKeyword.TRUE_FALSE, True, False)
        if not self.radioButtonGroups.has_key('selectAxis'):
            self.selectAxisKw1 = AFXIntKeyword(None, 'selectAxisDummy', True)
            self.selectAxisKw2 = AFXStringKeyword(self.cmd, 'selectAxis', True)
            self.radioButtonGroups['selectAxis'] = (self.selectAxisKw1, self.selectAxisKw2, {})
        self.radioButtonGroups['selectAxis'][2][63] = 'Select Direction Of Global Axis Perpendicular To Desired Fracture Planes'
        self.selectAxisKw1.setValue(63)
        if not self.radioButtonGroups.has_key('axisGlobal'):
            self.axisGlobalKw1 = AFXIntKeyword(None, 'axisGlobalDummy', True)
            self.axisGlobalKw2 = AFXStringKeyword(self.cmd, 'axisGlobal', True)
            self.radioButtonGroups['axisGlobal'] = (self.axisGlobalKw1, self.axisGlobalKw2, {})
        self.radioButtonGroups['axisGlobal'][2][64] = 'X'
        self.axisGlobalKw1.setValue(64)
        if not self.radioButtonGroups.has_key('axisGlobal'):
            self.axisGlobalKw1 = AFXIntKeyword(None, 'axisGlobalDummy', True)
            self.axisGlobalKw2 = AFXStringKeyword(self.cmd, 'axisGlobal', True)
            self.radioButtonGroups['axisGlobal'] = (self.axisGlobalKw1, self.axisGlobalKw2, {})
        self.radioButtonGroups['axisGlobal'][2][65] = 'Y'
        if not self.radioButtonGroups.has_key('axisGlobal'):
            self.axisGlobalKw1 = AFXIntKeyword(None, 'axisGlobalDummy', True)
            self.axisGlobalKw2 = AFXStringKeyword(self.cmd, 'axisGlobal', True)
            self.radioButtonGroups['axisGlobal'] = (self.axisGlobalKw1, self.axisGlobalKw2, {})
        self.radioButtonGroups['axisGlobal'][2][66] = 'Z'
        if not self.radioButtonGroups.has_key('selectAxis'):
            self.selectAxisKw1 = AFXIntKeyword(None, 'selectAxisDummy', True)
            self.selectAxisKw2 = AFXStringKeyword(self.cmd, 'selectAxis', True)
            self.radioButtonGroups['selectAxis'] = (self.selectAxisKw1, self.selectAxisKw2, {})
        self.radioButtonGroups['selectAxis'][2][67] = 'Or Create Own Desired Axis'
        if not self.radioButtonGroups.has_key('axisPoints'):
            self.axisPointsKw1 = AFXIntKeyword(None, 'axisPointsDummy', True)
            self.axisPointsKw2 = AFXStringKeyword(self.cmd, 'axisPoints', True)
            self.radioButtonGroups['axisPoints'] = (self.axisPointsKw1, self.axisPointsKw2, {})
        self.radioButtonGroups['axisPoints'][2][68] = 'Select 2 Points (Nodes In Mesh) To Create Axis'
        self.axisPointsKw1.setValue(68)
        self.axisPointStartKw = AFXObjectKeyword(self.cmd, 'axisPointStart', TRUE, pickedDefault)
        self.axisPointEndKw = AFXObjectKeyword(self.cmd, 'axisPointEnd', TRUE, pickedDefault)
        if not self.radioButtonGroups.has_key('axisPoints'):
            self.axisPointsKw1 = AFXIntKeyword(None, 'axisPointsDummy', True)
            self.axisPointsKw2 = AFXStringKeyword(self.cmd, 'axisPoints', True)
            self.radioButtonGroups['axisPoints'] = (self.axisPointsKw1, self.axisPointsKw2, {})
        self.radioButtonGroups['axisPoints'][2][69] = 'Or Enter Points Manually'
        self.coordAxisStartKw = AFXTableKeyword(self.cmd, 'coordAxisStart', True)
        self.coordAxisStartKw.setColumnType(-1, AFXTABLE_TYPE_FLOAT)
        self.coordAxisStartKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.coordAxisStartKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.CoordAxisEndKw = AFXTableKeyword(self.cmd, 'CoordAxisEnd', True)
        self.CoordAxisEndKw.setColumnType(-1, AFXTABLE_TYPE_FLOAT)
        self.CoordAxisEndKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.CoordAxisEndKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.NKw = AFXIntKeyword(self.cmd, 'N', True, 10)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _rsgTmp011_DB
        return _rsgTmp011_DB._rsgTmp011_DB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def deactivate(self):
    
        try:
            osutils.remove(os.path.join('c:\\Users\\user\\abaqus_plugins\\plugin3', '_rsgTmp011_DB.py'), force=True )
            osutils.remove(os.path.join('c:\\Users\\user\\abaqus_plugins\\plugin3', '_rsgTmp011_DB.pyc'), force=True )
        except:
            pass
        try:
            osutils.remove(os.path.join('c:\\Users\\user\\abaqus_plugins\\plugin3', '_rsgTmp011_Form.py'), force=True )
            osutils.remove(os.path.join('c:\\Users\\user\\abaqus_plugins\\plugin3', '_rsgTmp011_Form.pyc'), force=True )
        except:
            pass
        AFXForm.deactivate(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getCommandString(self):

        cmds = 'import EDC2\n'
        cmds += AFXForm.getCommandString(self)
        return cmds

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

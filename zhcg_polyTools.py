import maya.cmds as mc
import maya.mel as mm

if not mc.optionVar(ex='zhcg_polyTools_averageLine_stepMode'):
    mc.optionVar(iv=['zhcg_polyTools_averageLine_stepMode', 0])
if not mc.optionVar(ex='zhcg_polyTools_flatten_axis'):
    mc.optionVar(sv=['zhcg_polyTools_flatten_axis', 'view plane'])
    mc.symmetricModelling(e=True, t=0.01, st=0.01)
if not mc.optionVar(ex='zhcg_polyTools_flatten_space'):
    mc.optionVar(sv=['zhcg_polyTools_flatten_space', 'os'])
if not mc.optionVar(ex='zhcg_polyTools_flatten_align'):
    mc.optionVar(sv=['zhcg_polyTools_flatten_align', 'mean'])
if not mc.optionVar(ex='zhcg_polyTools_relax_keepBorder'):
    mc.optionVar(iv=['zhcg_polyTools_relax_keepBorder', 1])
if not mc.optionVar(ex='zhcg_polyTools_relax_keepShape'):
    mc.optionVar(iv=['zhcg_polyTools_relax_keepShape', 0])
if not mc.optionVar(ex='zhcg_polyTools_relax_step'):
    mc.optionVar(iv=['zhcg_polyTools_relax_step', 1])
if not mc.optionVar(ex='zhcg_polyTools_randomize_space'):
    mc.optionVar(iv=['zhcg_polyTools_randomize_space', 1])
if not mc.optionVar(ex='zhcg_polyTools_randomize_axis_x'):
    mc.optionVar(iv=['zhcg_polyTools_randomize_axis_x', 0])
if not mc.optionVar(ex='zhcg_polyTools_randomize_axis_y'):
    mc.optionVar(iv=['zhcg_polyTools_randomize_axis_y', 0])
if not mc.optionVar(ex='zhcg_polyTools_randomize_axis_z'):
    mc.optionVar(iv=['zhcg_polyTools_randomize_axis_z', 1])
if not mc.optionVar(ex='zhcg_polyTools_randomize_shift'):
    mc.optionVar(fv=['zhcg_polyTools_randomize_shift', 0.1])
if not mc.optionVar(ex='zhcg_polyTools_randomize_keepBorder'):
    mc.optionVar(iv=['zhcg_polyTools_randomize_keepBorder', 1])
if not mc.optionVar(ex='zhcg_polyTools_averageLine_even'):
    mc.optionVar(iv=['zhcg_polyTools_averageLine_even', 0])
if not mc.optionVar(ex='zhcg_polyTools_averageLine_keepShape'):
    mc.optionVar(iv=['zhcg_polyTools_averageLine_keepShape', 0])
if not mc.optionVar(ex='zhcg_polyTools_averageLine_smooth'):
    mc.optionVar(iv=['zhcg_polyTools_averageLine_smooth', 0])
if not mc.optionVar(ex='zhcg_polyTools_averageLine_align'):
    mc.optionVar(iv=['zhcg_polyTools_averageLine_align', 1])
if not mc.optionVar(ex='zhcg_polyTools_averageLine_step'):
    mc.optionVar(iv=['zhcg_polyTools_averageLine_step', 1])
if not mc.optionVar(ex='zhcg_polyTools_circlelizeLine_even'):
    mc.optionVar(iv=['zhcg_polyTools_circlelizeLine_even', 0])
if not mc.optionVar(ex='zhcg_polyTools_circlelizeLine_align'):
    mc.optionVar(iv=['zhcg_polyTools_circlelizeLine_align', 1])
if not mc.optionVar(ex='zhcg_polyTools_circlelizeLine_radius'):
    mc.optionVar(iv=['zhcg_polyTools_circlelizeLine_radius', 1])
if not mc.optionVar(ex='zhcg_polyTools_circlelizeLine_customRadius'):
    mc.optionVar(fv=['zhcg_polyTools_circlelizeLine_customRadius', 1])
if not mc.optionVar(ex='zhcg_polyTools_straightenLine_even'):
    mc.optionVar(iv=['zhcg_polyTools_straightenLine_even', 0])
if not mc.optionVar(ex='zhcg_polyTools_shapeLine_even'):
    mc.optionVar(iv=['zhcg_polyTools_shapeLine_even', 0])
if not mc.optionVar(ex='zhcg_polyTools_mirror_mode'):
    mc.optionVar(iv=['zhcg_polyTools_mirror_mode', 1])
if not mc.optionVar(ex='zhcg_polyTools_duplicateEdges_degree'):
    mc.optionVar(iv=['zhcg_polyTools_duplicateEdges_degree', 1])
if not mc.optionVar(ex='zhcg_polyTools_connect_div'):
    mc.optionVar(iv=['zhcg_polyTools_connect_div', 1])
if not mc.optionVar(ex='zhcg_polyTools_insertEdgeLoop_div'):
    mc.optionVar(iv=['zhcg_polyTools_insertEdgeLoop_div', 1])
if not mc.optionVar(ex='zhcg_polyTools_subdivEdges_div'):
    mc.optionVar(iv=['zhcg_polyTools_subdivEdges_div', 1])
if not mc.optionVar(ex='zhcg_polyTools_mergeFacet_cleanVtxs'):
    mc.optionVar(iv=['zhcg_polyTools_mergeFacet_cleanVtxs', 0])
if not mc.optionVar(ex='zhcg_polyTools_selToPattern_reverse'):
    mc.optionVar(iv=['zhcg_polyTools_selToPattern_reverse', 0])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardFaces_3side'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardFaces_3side', 1])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardFaces_5side'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardFaces_5side', 1])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardFaces_6side'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardFaces_6side', 1])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardStars_2star'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_2star', 0])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardStars_3star'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_3star', 0])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardStars_5star'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_5star', 0])
if not mc.optionVar(ex='zhcg_polyTools_selNonQuardStars_6star'):
    mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_6star', 1])
if not mc.optionVar(ex='zhcg_polyTools_selCenterVtxsThreshold'):
    mc.optionVar(fv=['zhcg_polyTools_selCenterVtxsThreshold', 0.1])

import re, copy, os, glob
from random import uniform, randint, choice

mm.eval('source "dagMenuProc"')
mc.scriptJob(e=['Undo', '%s.pf_68()' % __name__])
commandDict = {'DeleteMeshHistory': '%s.delMeshHistory()' % __name__,
 'EditComponents_EditFacet': '%s.editFacet()' % __name__,
 'EditComponents_SpinDialog': '%s.spin(dialog=True)' % __name__,
 'EditComponents_SpinForward': '%s.spin()' % __name__,
 'EditComponents_SpinBackward': '%s.spin(reverse=True)' % __name__,
 'EditComponents_Connect': '%s.connect()' % __name__,
 'EditComponents_ConnectOptionBox': '%s.connectUI()' % __name__,
 'EditComponents_InsertEdgeLoop': '%s.insertEdgeLoop()' % __name__,
 'EditComponents_InsertEdgeLoopOptionBox': '%s.insertEdgeLoopUI()' % __name__,
 'EditComponents_SubdivideEdges': '%s.subdivEdges()' % __name__,
 'EditComponents_SubdivideEdgesOptionBox': '%s.subdivEdgesUI()' % __name__,
 'EditComponents_MergeFaces': '%s.mergeFacet()' % __name__,
 'EditComponents_MergeFacesOptionBox': '%s.mergeFacetUI()' % __name__,
 'EditComponents_AddNewFaces': '%s.addNewFaces()' % __name__,
 'MirrorPoly_CreateMirror': '%s.createMirror()' % __name__,
 'MirrorPoly_CreateMirrorOptionBox': '%s.mirrorPolyUI()' % __name__,
 'MirrorPoly_DeleteMirror': '%s.delMirror()' % __name__,
 'MirrorPoly_TakeHalf': '%s.takeHalf()' % __name__,
 'MirrorPoly_UpdateMirror': '%s.updateMirror()' % __name__,
 'MirrorPoly_ToggleMirror': '%s.toggleMirror()' % __name__,
 'MirrorPoly_SelectCenterVtxs': '%s.getCenterVtxs()' % __name__,
 'MirrorPoly_SelectCenterVtxsOptionBox': '%s.getCenterVtxsUI()' % __name__,
 'MirrorPoly_MoveToCenter': '%s.getCenterVtxsUI()' % __name__,
 'SplitMesh_Split': '%s.splitMesh()' % __name__,
 'SplitMesh_Merge': '%s.mergeMesh()' % __name__,
 'SplitMesh_Isolate': '%s.isolateSelFaces()' % __name__,
 'SplitMesh_Unisolate': '%s.unIsolateMesh()' % __name__,
 'SplitMesh_Duplicate': '%s.dupSelFaces()' % __name__,
 'Regularize_Flatten': '%s.flatten()' % __name__,
 'Regularize_FlattenOptionBox': '%s.flattenUI()' % __name__,
 'Regularize_Relax': '%s.relax()' % __name__,
 'Regularize_RelaxOptionBox': '%s.relaxUI()' % __name__,
 'Regularize_Randomize': '%s.randomize()' % __name__,
 'Regularize_RandomizeOptionBox': '%s.randomizeUI()' % __name__,
 'Regularize_AverageLine': '%s.averageLine()' % __name__,
 'Regularize_AverageLineOptionBox': '%s.averageLineUI()' % __name__,
 'Regularize_StraightenLine': '%s.straightenLine()' % __name__,
 'Regularize_StraightenLineOptionBox': '%s.straightenLineUI()' % __name__,
 'Regularize_CirclelizeLine': '%s.circlelizeLine()' % __name__,
 'Regularize_CirclelizeLineOptionBox': '%s.circlelizeLineUI()' % __name__,
 'Regularize_DuplicateEdges': '%s.duplicateEdges()' % __name__,
 'Regularize_DuplicateEdgesOptionBox': '%s.duplicateEdgesUI()' % __name__,
 'Regularize_ShapeLine': '%s.shapeLineUI()' % __name__,
 'Regularize_ShrinkWrap': '%s.shrinkWrapUI()' % __name__,
 'Select_QuickSel': '%s.quickSel()' % __name__,
 'Select_SelectNonQuardFaces': '%s.selNonQuardFaces()' % __name__,
 'Select_SelectNonQuardFacesOptionBox': '%s.selNonQuardFacesUI()' % __name__,
 'Select_SelectNonQuardStars': '%s.selNonQuardStars()' % __name__,
 'Select_SelectNonQuardStarsOptionBox': '%s.selNonQuardStarsUI()' % __name__,
 'Select_SelectOpenEdges': '%s.selBorder()' % __name__,
 'Select_ToPattern': '%s.selToPattern()' % __name__,
 'Select_ToPatternOptionBox': '%s.selToPatternUI()' % __name__,
 'Select_ToBorder': "%s.selToBorder(mode='border')" % __name__,
 'Select_ToInteral': "%s.selToBorder(mode='inside')" % __name__,
 'Display_ToggleShader': '%s.toggleShader()' % __name__,
 'Display_ToggleTransparency': '%s.toggleShaderTransparency()' % __name__,
 'Display_DisplayHardEdgesOnly': 'mc.polyOptions(ao=True,he=True)',
 'Display_DisplayAllEdges': 'mc.polyOptions(ao=True,ae=True)',
 'Display_HardenEdges': '%s.hardenEdge()' % __name__,
 'Display_SoftenEdges': '%s.softenEdge()' % __name__,
 'ZhCG_PolyTools_info': '%s.info()' % __name__,
 'ZhCG_PolyTools_register': '%s.register()' % __name__}

def setCmd():
    for namedCommand, command in commandDict.items():
        try:
            mc.runTimeCommand(namedCommand, c=command, cat='ZhCG_PolyTools', cl='python')
        except:
            pass
def delCmd():
    for namedCommand in commandDict:
        try:
            mc.runTimeCommand(namedCommand, edit=True, delete=True)
        except:
            pass
def prtCmd():
    print ('\n\n\n\n\n' + ver + ' nameCommands:\n')
    for i in sorted(commandDict.keys()):
        print (i)
setCmd()
mc.optionVar(iv=['zhcg_polyTools_setNamedCommand', 1])
mc.optionVar(iv=['zhcg_polyTools_setNamedCommand2', 1])

def create_menu():
    menus = mc.lsUI(menus=True)
    for eachMenu in menus:
        if 'ZhCG_PolyTools' in mc.menu(eachMenu, q=True, l=True):
            mc.deleteUI(eachMenu)
            break

    melMenuCmds1 = '\n    menu -l "ZhCG_PolyTools" -tearOff 1 -allowOptionBoxes 1 -p "MayaWindow";\n    menuItem -l "Delete Mesh History" -c "DeleteMeshHistory";\n    menuItem -d 1;\n\n    menuItem -l "Edit Components" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n    menuItem -l "Edit Facet" -c "EditComponents_EditFacet";\n    menuItem -l "Spin" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n    menuItem -l "Spin Dialog" -c "EditComponents_SpinDialog";\n    menuItem -l "-->" -c "EditComponents_SpinForward";\n    menuItem -l "<--" -c "EditComponents_SpinBackward";\n    setParent -menu ..;\n\n    menuItem -d 1;\n    menuItem -l "Connect" -c "EditComponents_Connect";\n    menuItem -optionBox 1 -c "EditComponents_ConnectOptionBox";\n    menuItem -l "Insert Edge Loop" -c "EditComponents_InsertEdgeLoop";\n    menuItem -optionBox 1 -c "EditComponents_InsertEdgeLoopOptionBox";\n    menuItem -l "Subdivide Edges" -c "EditComponents_SubdivideEdges";\n    menuItem -optionBox 1 -c "EditComponents_SubdivideEdgesOptionBox";\n    menuItem -l "Merge Faces" -c "EditComponents_MergeFaces";\n    menuItem -optionBox 1 -c "EditComponents_MergeFacesOptionBox";\n    menuItem -l "Add New Faces" -c "EditComponents_AddNewFaces";\n\n    setParent -menu ..;\n    menuItem -l "MirrorPoly" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n    menuItem -l "Create Mirror" -c "MirrorPoly_CreateMirror";\n    menuItem -optionBox 1 -c "MirrorPoly_CreateMirrorOptionBox";\n    menuItem -l "Delete Mirror" -c "MirrorPoly_DeleteMirror";\n    menuItem -l "Take Half" -c "MirrorPoly_TakeHalf";\n    menuItem -d 1;\n    menuItem -l "Update Mirror" -c "MirrorPoly_UpdateMirror";\n    menuItem -l "Toggle Mirror" -c "MirrorPoly_ToggleMirror";\n    menuItem -d 1;\n    menuItem -l "Sel Center Vtxs" -c "MirrorPoly_SelectCenterVtxs";\n    menuItem -optionBox 1 -c "MirrorPoly_SelectCenterVtxsOptionBox";\n    menuItem -l "Move to Center" -c "MirrorPoly_MoveToCenter";\n\n    setParent -menu ..;\n    setParent -menu ..;\n    menuItem -l "Split Mesh" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n    menuItem -l "Split" -c "SplitMesh_Split";\n    menuItem -l "Merge" -c "SplitMesh_Merge";\n    menuItem -d 1;\n    menuItem -l "Isolate" -c "SplitMesh_Isolate";\n    menuItem -l "Unisolate" -c "SplitMesh_Unisolate";\n    menuItem -d 1;\n    menuItem -l "Duplicate" -c "SplitMesh_Duplicate";\n\n    setParent -menu ..;\n    menuItem -l "Regularize" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n\n    menuItem -l "Flatten" -c "Regularize_Flatten";\n    menuItem -optionBox 1 -c "Regularize_FlattenOptionBox";\n\n    menuItem -l "Relax" -c "Regularize_Relax";\n    menuItem -optionBox 1 -c "Regularize_RelaxOptionBox";\n\n    menuItem -l "Randomize" -c "Regularize_Randomize";\n    menuItem -optionBox 1 -c "Regularize_RandomizeOptionBox";\n\n    menuItem -l "Average Line" -c "Regularize_AverageLine";\n    menuItem -optionBox 1 -c "Regularize_AverageLineOptionBox";\n\n    menuItem -l "Straighten Line" -c "Regularize_StraightenLine";\n    menuItem -optionBox 1 -c "Regularize_StraightenLineOptionBox";\n\n    menuItem -l "Circlelize Line" -c "Regularize_CirclelizeLine";\n    menuItem -optionBox 1 -c "Regularize_CirclelizeLineOptionBox";\n\n    menuItem -l "Duplicate Edges" -c "Regularize_DuplicateEdges";\n    menuItem -optionBox 1 -c "Regularize_DuplicateEdgesOptionBox";\n\n    menuItem -l "Shape Line..." -c "Regularize_ShapeLine";\n\n    menuItem -l "ShrinkWrap..." -c "Regularize_ShrinkWrap";\n\n    setParent -menu ..;\n    menuItem -l "Select" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n    menuItem -l "Quick Sel" -c "Select_QuickSel";\n    menuItem -d 1;\n    menuItem -l "Select NonQuard Faces" -c "Select_SelectNonQuardFaces";\n    menuItem -optionBox 1 -c "Select_SelectNonQuardFacesOptionBox";\n    menuItem -l "Select NonQuard Stars" -c "Select_SelectNonQuardStars";\n    menuItem -optionBox 1 -c "Select_SelectNonQuardStarsOptionBox";\n    menuItem -l "Select Open Edges" -c "Select_SelectOpenEdges";\n    menuItem -d 1;\n    menuItem -l "To Pattern" -c "Select_ToPattern";\n    menuItem -optionBox 1 -c "Select_ToPatternOptionBox";\n    menuItem -l "To Border" -c "Select_ToBorder";\n    menuItem -l "To Interal" -c "Select_ToInteral";\n\n    setParent -menu ..;\n    menuItem -l "Display" -subMenu 1 -tearOff 1 -allowOptionBoxes 1;\n    menuItem -l "Toggle Shader" -c "Display_ToggleShader";\n    menuItem -l "Toggle Transparency" -c "Display_ToggleTransparency";\n    menuItem -d 1;\n    menuItem -l "Display Hard Edges Only" -c "Display_DisplayHardEdgesOnly";\n    menuItem -l "Display All Edges" -c "Display_DisplayAllEdges";\n    menuItem -d 1;\n    menuItem -l "Harden Edges" -c "Display_HardenEdges";\n    menuItem -l "Soften Edges" -c "Display_SoftenEdges";\n\n    setParent -menu ..;\n    menuItem -d 1;\n    menuItem -l "v1.62" -en 0;\n    '
    melMenuCmds = melMenuCmds1
    mm.eval(melMenuCmds)
create_menu()



def flattenUI():
    global flatten_RB_1
    global RBG_axis_flatten
    global flatten_RB_3
    global flatten_RB_4
    global flatten_RB_5
    global RCL_axis_flatten
    global flatten_RB_2
    global RBG_flatten_space
    global RBG_flatten_align
    pf_61()
    if pf_73('zhcg_polyTools_flattenUI'):
        pf_71('Flatten Window Exists!')
    else:
        mc.window('zhcg_polyTools_flattenUI', t='Flatten - ZhCG_PolyTools', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        RCL_axis_flatten = mc.rowColumnLayout(nc=6, cw=zip(range(1, 7), [50,
         35,
         35,
         35,
         80,
         100]), cal=zip(range(1, 7), ['left'] * 6))
        RBG_axis_flatten = mc.radioCollection()
        mc.text(l=' Axis:', al='left')
        flatten_RB_1 = mc.radioButton(l='X', sl=mc.optionVar(q='zhcg_polyTools_flatten_axis') == 'x', onc="mc.radioButtonGrp(%s.RBG_flatten_space,e=True,en=True);mc.optionVar(sv=['zhcg_polyTools_flatten_axis','x'])" % __name__)
        flatten_RB_2 = mc.radioButton(l='Y', sl=mc.optionVar(q='zhcg_polyTools_flatten_axis') == 'y', onc="mc.radioButtonGrp(%s.RBG_flatten_space,e=True,en=True);mc.optionVar(sv=['zhcg_polyTools_flatten_axis','y'])" % __name__)
        flatten_RB_3 = mc.radioButton(l='Z', sl=mc.optionVar(q='zhcg_polyTools_flatten_axis') == 'z', onc="mc.radioButtonGrp(%s.RBG_flatten_space,e=True,en=True);mc.optionVar(sv=['zhcg_polyTools_flatten_axis','z'])" % __name__)
        flatten_RB_4 = mc.radioButton(l='View Plane', sl=mc.optionVar(q='zhcg_polyTools_flatten_axis') == 'view plane', onc="mc.radioButtonGrp(%s.RBG_flatten_space,e=True,en=False);mc.optionVar(sv=['zhcg_polyTools_flatten_axis','view plane'])" % __name__)
        flatten_RB_5 = mc.radioButton(l='Average Normal', sl=mc.optionVar(q='zhcg_polyTools_flatten_axis') == 'average normal', onc="mc.radioButtonGrp(%s.RBG_flatten_space,e=True,en=False);mc.optionVar(sv=['zhcg_polyTools_flatten_axis','average normal'])" % __name__)
        mc.setParent('..')
        RBG_flatten_space = mc.radioButtonGrp(l=' Space:', nrb=2, la2=['World Space', 'Object Space'], cw3=[50, 110, 120], cl3=['left'] * 3, sl=1 if mc.optionVar(q='zhcg_polyTools_flatten_space') == 'ws' else 2, en=mc.optionVar(q='zhcg_polyTools_flatten_axis') in ('x', 'y', 'z'), on1="mc.optionVar(sv=['zhcg_polyTools_flatten_space','ws'])", on2="mc.optionVar(sv=['zhcg_polyTools_flatten_space','os'])")
        RBG_flatten_align = mc.radioButtonGrp(l=' Align:', nrb=3, la3=['Mean', 'Max', 'Min'], cw4=[50,
         80,
         70,
         70], cl4=['left'] * 4, sl=1 if mc.optionVar(q='zhcg_polyTools_flatten_align') == 'mean' else (2 if mc.optionVar(q='zhcg_polyTools_flatten_align') == 'min' else 3), on1="mc.optionVar(sv=['zhcg_polyTools_flatten_align','mean'])", on2="mc.optionVar(sv=['zhcg_polyTools_flatten_align','min'])", on3="mc.optionVar(sv=['zhcg_polyTools_flatten_align','max'])")
        mc.button(l='Flatten', c='%s.flatten()' % __name__)
        mc.showWindow('zhcg_polyTools_flattenUI')


def relaxUI():
    global CB_relax_keepBorder
    global CB_relax_keepShape
    global ISG_relax_step
    pf_61()
    if pf_73('zhcg_polyTools_relaxUI'):
        pf_71('Relax Window Exists!')
    else:
        mc.window('zhcg_polyTools_relaxUI', t='Relax', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        mc.rowColumnLayout(nc=2, cw=[(1, 110), (2, 100)])
        CB_relax_keepBorder = mc.checkBox(l=' Keep Border', al='left', v=mc.optionVar(q='zhcg_polyTools_relax_keepBorder'), cc="mc.optionVar(iv=['zhcg_polyTools_relax_keepBorder',mc.checkBox(%s.CB_relax_keepBorder,q=True,v=True)])" % __name__)
        CB_relax_keepShape = mc.checkBox(l=' Keep Shape', al='left', v=mc.optionVar(q='zhcg_polyTools_relax_keepShape'), cc="mc.optionVar(iv=['zhcg_polyTools_relax_keepShape',mc.checkBox(%s.CB_relax_keepShape,q=True,v=True)])" % __name__)
        mc.setParent('..')
        ISG_relax_step = mc.intSliderGrp(l=' Step:', f=True, min=1, max=10, cw=[(1, 40), (2, 40)], cal=[(1, 'left')], rat=[1, 'top', 3], v=mc.optionVar(q='zhcg_polyTools_relax_step'), cc="mc.optionVar(iv=['zhcg_polyTools_relax_step',mc.intSliderGrp(%s.ISG_relax_step,q=True,v=True)])" % __name__)
        mc.button(l='Relax', c='%s.relax()' % __name__)
        mc.showWindow('zhcg_polyTools_relaxUI')


def averageLineUI():
    global CB_averageLine_even
    global CB_averageLine_keepShape
    global CB_averageLine_smooth
    global ISG_averageLine_step
    global RBG_averageLine_align
    pf_61()
    if pf_73('zhcg_polyTools_averageLineUI'):
        pf_71('Average Line Window Exists!')
    else:
        mc.window('zhcg_polyTools_averageLineUI', t='Average Line', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        mc.rowColumnLayout(nc=3, cw=[(1, 80), (2, 120), (3, 80)])
        CB_averageLine_even = mc.checkBox(l=' Even', al='left', v=mc.optionVar(q='zhcg_polyTools_averageLine_even'), cc="mc.optionVar(iv=['zhcg_polyTools_averageLine_even',mc.checkBox(%s.CB_averageLine_even,q=True,v=True)]);mc.intSliderGrp(%s.ISG_averageLine_step,e=True,en=not mc.optionVar(q='zhcg_polyTools_averageLine_even'))" % (__name__, __name__))
        CB_averageLine_keepShape = mc.checkBox(l=' Keep Shape', al='left', v=mc.optionVar(q='zhcg_polyTools_averageLine_keepShape'), cc="mc.optionVar(iv=['zhcg_polyTools_averageLine_keepShape',mc.checkBox(%s.CB_averageLine_keepShape,q=True,v=True)])" % __name__)
        CB_averageLine_smooth = mc.checkBox(l=' smooth', al='left', v=mc.optionVar(q='zhcg_polyTools_averageLine_smooth'), cc="mc.optionVar(iv=['zhcg_polyTools_averageLine_smooth',mc.checkBox(%s.CB_averageLine_smooth,q=True,v=True)])" % __name__)
        mc.setParent('..')
        RBG_averageLine_align = mc.radioButtonGrp(l=' Align:', nrb=4, la4=['YZ',
         'XZ',
         'XY',
         'Auto'], cw5=[55,
         40,
         40,
         40,
         40], cl5=['left'] * 5, sl=mc.optionVar(q='zhcg_polyTools_averageLine_align'), cc="mc.optionVar(iv=['zhcg_polyTools_averageLine_align',mc.radioButtonGrp(%s.RBG_averageLine_align,q=True,sl=True)])" % __name__)
        ISG_averageLine_step = mc.intSliderGrp(l=' Step:', f=True, min=1, max=10, cw=[(1, 55), (2, 40)], cal=[(1, 'left')], rat=[1, 'top', 3], en=not mc.optionVar(q='zhcg_polyTools_averageLine_even'), v=mc.optionVar(q='zhcg_polyTools_averageLine_step'), cc="mc.optionVar(iv=['zhcg_polyTools_averageLine_step',mc.intSliderGrp(%s.ISG_averageLine_step,q=True,v=True)])" % __name__)
        mc.button(l='Average Line', c='%s.averageLine()' % __name__)
        mc.showWindow('zhcg_polyTools_averageLineUI')


def straightenLineUI():
    global CB_averageLine_even
    pf_61()
    if pf_73('zhcg_polyTools_straightenLineUI'):
        pf_71('straighten Line Window Exists!')
    else:
        mc.window('zhcg_polyTools_straightenLineUI', t='Straighten Line', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CB_averageLine_even = mc.checkBox(l=' Even', al='left', v=mc.optionVar(q='zhcg_polyTools_straightenLine_even'), cc="mc.optionVar(iv=['zhcg_polyTools_straightenLine_even',mc.checkBox(%s.CB_averageLine_even,q=True,v=True)])" % __name__)
        mc.button(l='Straighten Line', w=230, c='%s.straightenLine()' % __name__)
        mc.showWindow('zhcg_polyTools_straightenLineUI')


def circlelizeLineUI():
    global RBG_circlelizeLine_align
    global RBG_circlelizeLine_radius
    global CB_circlelizeLine_even
    global FF_circlelizeLine_customRadius
    pf_61()
    if pf_73('zhcg_polyTools_circlelizeLineUI'):
        pf_71('Circlelize Line Window Exists!')
    else:
        mc.window('zhcg_polyTools_circlelizeLineUI', t='Circlelize Line', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CB_circlelizeLine_even = mc.checkBox(l=' Even', al='left', v=mc.optionVar(q='zhcg_polyTools_circlelizeLine_even'), cc="mc.optionVar(iv=['zhcg_polyTools_circlelizeLine_even',mc.checkBox(%s.CB_circlelizeLine_even,q=True,v=True)])" % __name__)
        mc.setParent('..')
        mc.columnLayout(rs=3, adj=True)
        RBG_circlelizeLine_align = mc.radioButtonGrp(l=' Align:', nrb=4, la4=['YZ',
         'XZ',
         'XY',
         'Auto'], cw5=[55,
         55,
         55,
         55,
         55], cl5=['left'] * 5, sl=mc.optionVar(q='zhcg_polyTools_circlelizeLine_align'), cc="mc.optionVar(iv=['zhcg_polyTools_circlelizeLine_align',mc.radioButtonGrp(%s.RBG_circlelizeLine_align,q=True,sl=True)])" % __name__)
        mc.rowColumnLayout(nc=2, cw=[(1, 270), (2, 60)], rat=[1, 'bottom', 3])
        RBG_circlelizeLine_radius = mc.radioButtonGrp(l=' Radius:', nrb=4, la4=['Mean',
         'Max',
         'Min',
         'Custom:'], cw5=[55,
         55,
         50,
         45,
         60], cl5=['left'] * 5, sl=mc.optionVar(q='zhcg_polyTools_circlelizeLine_radius'), cc="mc.optionVar(iv=['zhcg_polyTools_circlelizeLine_radius',mc.radioButtonGrp(%s.RBG_circlelizeLine_radius,q=True,sl=True)]);mc.floatField(%s.FF_circlelizeLine_customRadius,e=True,en=(mc.optionVar(q='zhcg_polyTools_circlelizeLine_radius')==4))" % (__name__, __name__))
        FF_circlelizeLine_customRadius = mc.floatField(min=0.001, max=100, pre=2, en=mc.optionVar(q='zhcg_polyTools_circlelizeLine_radius') == 4, v=mc.optionVar(q='zhcg_polyTools_circlelizeLine_customRadius'), cc="mc.optionVar(fv=['zhcg_polyTools_circlelizeLine_customRadius',mc.floatField(%s.FF_circlelizeLine_customRadius,q=True,v=True)])" % __name__)
        mc.setParent('..')
        mc.button(l='Circlelize Line', c='%s.circlelizeLine()' % __name__)
        mc.showWindow('zhcg_polyTools_circlelizeLineUI')


def shapeLineUI():
    global TFBG_shapeLine
    global BT_shapeLine
    global CB_shapeLine_even
    pf_61()
    if pf_73('zhcg_polyTools_shapeLineUI'):
        pf_71('AverageLine Window Exists!')
    else:
        mc.window('zhcg_polyTools_shapeLineUI', t='Shape Line', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CB_shapeLine_even = mc.checkBox(l=' Even', al='left', v=mc.optionVar(q='zhcg_polyTools_shapeLine_even'), cc="mc.optionVar(iv=['zhcg_polyTools_shapeLine_even',mc.checkBox(%s.CB_shapeLine_even,q=True,v=True)])" % __name__)
        TFBG_shapeLine = mc.textFieldButtonGrp(eb=True, bl=' Add Curve ', ed=False, cw=[1, 180], bc='%s.addShapeCurve()' % __name__)
        BT_shapeLine = mc.button(l='Shape Line', en=False, c='%s.shapeLine()' % __name__)
        mc.showWindow('zhcg_polyTools_shapeLineUI')


def randomizeUI():
    global FSG_shift_randomize
    global RBG_space_randomize
    global CBG_axis_randomize
    global CB_protectBorder_randomize
    pf_61()
    if pf_73('zhcg_polyTools_randomizeUI'):
        pf_71('Randomize Window Exists!')
    else:
        mc.window('zhcg_polyTools_randomizeUI', t='Randomize', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        RBG_space_randomize = mc.radioButtonGrp(l=' Space:', nrb=3, la3=['Normal', 'Object', 'World'], cw4=[50,
         60,
         60,
         60], cl4=['left'] * 4, sl=mc.optionVar(q='zhcg_polyTools_randomize_space'), cc="mc.optionVar(iv=['zhcg_polyTools_randomize_space',mc.radioButtonGrp(%s.RBG_space_randomize,q=True,sl=True)])" % __name__)
        CBG_axis_randomize = mc.checkBoxGrp(l=' Axis:', ncb=3, la3=['X', 'Y', 'Z'], cw4=[50,
         60,
         60,
         60], cl4=['left'] * 4, v1=mc.optionVar(q='zhcg_polyTools_randomize_axis_x'), v2=mc.optionVar(q='zhcg_polyTools_randomize_axis_y'), v3=mc.optionVar(q='zhcg_polyTools_randomize_axis_z'), cc1="mc.optionVar(iv=['zhcg_polyTools_randomize_axis_x',mc.checkBoxGrp(%s.CBG_axis_randomize,q=True,v1=True)])" % __name__, cc2="mc.optionVar(iv=['zhcg_polyTools_randomize_axis_y',mc.checkBoxGrp(%s.CBG_axis_randomize,q=True,v2=True)])" % __name__, cc3="mc.optionVar(iv=['zhcg_polyTools_randomize_axis_z',mc.checkBoxGrp(%s.CBG_axis_randomize,q=True,v3=True)])" % __name__)
        FSG_shift_randomize = mc.floatSliderGrp(l=' Shift:', f=True, v=mc.optionVar(q='zhcg_polyTools_randomize_shift'), step=0.001, min=0.001, max=1, cw=[(1, 50), (2, 38)], cal=[(1, 'left')], cc="mc.optionVar(fv=['zhcg_polyTools_randomize_shift',mc.floatSliderGrp(%s.FSG_shift_randomize,q=True,v=True)])" % __name__)
        CB_protectBorder_randomize = mc.checkBox(l='Keep Border', v=mc.optionVar(q='zhcg_polyTools_randomize_keepBorder'), al='left', cc="mc.optionVar(iv=['zhcg_polyTools_randomize_keepBorder',mc.checkBox(%s.CB_protectBorder_randomize,q=True,v=True)])" % __name__)
        mc.button(l='Randomize', c='%s.randomize()' % __name__)
        mc.showWindow('zhcg_polyTools_randomizeUI')


def shrinkWrapUI():
    global CB_border_shrinkWrap
    global RBG_mode_shrinkWrap
    global BT_shrinkWrap
    global TFBG_shrinkWrap
    pf_61()
    if pf_73('zhcg_polyTools_shrinkWrapUI'):
        pf_71('ShrinkWrap Window Exists!')
    else:
        mc.window('zhcg_polyTools_shrinkWrapUI', t='ShrinkWrap', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        TFBG_shrinkWrap = mc.textFieldButtonGrp(eb=True, bl=' Add Target ', ed=False, cw=[1, 150], bc='%s.addWrapTarget()' % __name__)
        mc.rowColumnLayout(nc=2, cw=[(1, 150), (2, 60)], cat=[2, 'left', 12])
        RBG_mode_shrinkWrap = mc.radioButtonGrp(nrb=2, l=' Mode:', la2=['Vertex', 'Facet'], sl=1, cw3=[45, 60, 45], cal=[1, 'left'], on1='mc.checkBox(%s.CB_border_shrinkWrap,e=True,en=False)' % __name__, on2='mc.checkBox(%s.CB_border_shrinkWrap,e=True,en=True)' % __name__)
        CB_border_shrinkWrap = mc.checkBox(l='Border', v=True, en=False)
        mc.setParent('..')
        BT_shrinkWrap = mc.button(l='ShrinkWrap', en=False, c='%s.shrinkWrap()' % __name__)
        mc.showWindow('zhcg_polyTools_shrinkWrapUI')


def shrinkWrapUI_popupMenu():
    if pf_73('shrinkWrapUI_popupMenu'):
        mc.deleteUI('shrinkWrapUI_popupMenu')
    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
    if target and mc.objExists(target):
        mc.popupMenu('shrinkWrapUI_popupMenu', p=TFBG_shrinkWrap)
        mc.menuItem(l='Enable', cb=True, c='%s.enableShrinkWrap()' % __name__)
        mc.menuItem(d=True)
        mc.menuItem(l='Select Target', c='%s.selWrapTarget()' % __name__)
        mc.menuItem(l='Remove Target', c='%s.removeWrapTarget()' % __name__)
        mc.menuItem(d=True)
        mc.menuItem(l='Make Target Live', c="mc.makeLive('%s')" % mc.listRelatives(target, s=True)[0])
        mc.menuItem(l='Turn Off Live', c='mc.makeLive(n=True)')
        mc.menuItem(d=True)
        mc.menuItem(l='Target Visibility', cb=mc.getAttr(target + '.v'), c='%s.toggleWrapTargetVis()' % __name__)
        targetShape = mc.listRelatives(target, s=True)[0]
        curShaderGrp = mc.listConnections(targetShape, t='shadingEngine')
        if curShaderGrp:
            curShader = mc.listConnections(curShaderGrp[0], t='lambert')
            if curShader:
                curShader = curShader[0]
                transparency = any(mc.getAttr(curShader + '.transparency')[0])
        mc.menuItem(l='Target Transparency', cb=transparency, c='%s.toggleWrapTargetTranspency()' % __name__)
        mc.radioMenuItemCollection(p='shrinkWrapUI_popupMenu')
        mc.menuItem(l='Normal', rb=True if not mc.getAttr(target + '.overrideEnabled') or mc.getAttr('%s.overrideDisplayType' % target) == 0 else False, c='%s.toggleWrapTargetOverride(mode=0)' % __name__)
        mc.menuItem(l='Template', rb=True if mc.getAttr('%s.overrideDisplayType' % target) == 1 and mc.getAttr(target + '.overrideEnabled') else False, c='%s.toggleWrapTargetOverride(mode=1)' % __name__)
        mc.menuItem(l='Reference', rb=True if mc.getAttr('%s.overrideDisplayType' % target) == 2 and mc.getAttr(target + '.overrideEnabled') else False, c='%s.toggleWrapTargetOverride(mode=2)' % __name__)


def relax():
    pf_61()
    selComps = pf_06()
    if selComps:
        selComps, selVtxs = selComps[:2]
        keepBorder = mc.optionVar(q='zhcg_polyTools_relax_keepBorder')
        keepShape = mc.optionVar(q='zhcg_polyTools_relax_keepShape')
        step = mc.optionVar(q='zhcg_polyTools_relax_step')
        if keepBorder:
            selVtxs = [ vtx for vtx in selVtxs if not pf_08(vtx) ]
        if keepShape:
            mesh = pf_29()
            target = None
            if pf_73('zhcg_polyTools_shrinkWrapUI') and mc.button(BT_shrinkWrap, q=True, en=True):
                target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
                if target:
                    if mc.objExists(target):
                        targetMesh = target
                    else:
                        target = None
            if not target:
                targetMesh = mc.duplicate(mesh)[0]
                mc.setAttr(targetMesh + '.v', False)
        if selVtxs:
            gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
            mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='relaxing...', maxValue=step * 5 + 5)
            for i in range(step):
                if mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                    break
                mc.progressBar(gMainProgressBar, edit=True, step=1)
                mc.polyAverageVertex(selVtxs)
                delMeshHistory()
                mc.progressBar(gMainProgressBar, edit=True, step=4)

            if keepShape:
                pf_48(targetMesh, mesh, len(selVtxs), [ pf_32(vtx) for vtx in selVtxs ])
            if keepShape and not target:
                mc.delete(targetMesh)
            mc.progressBar(gMainProgressBar, edit=True, step=2)
            mc.select(selComps)
            pf_68()
            mc.progressBar(gMainProgressBar, edit=True, step=3)
            delMeshHistory()
            pf_22()
            mc.progressBar(gMainProgressBar, edit=True, endProgress=True)


def flatten():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    selMode = pf_06('vtx')
    if selMode and selMode[1]:
        selComps, vtxs = selMode[0], selMode[1]
        vtxNum = len(vtxs)
        mesh = pf_29()
        axis = mc.optionVar(q='zhcg_polyTools_flatten_axis')
        space = mc.optionVar(q='zhcg_polyTools_flatten_space')
        align = mc.optionVar(q='zhcg_polyTools_flatten_align')
        if axis in ('average normal', 'view plane'):
            if axis == 'average normal':
                if selFaces:
                    normal = pf_37(selFaces).toTuple()
                else:
                    pf_71('No faces selectd!')
                    return False
            elif axis == 'view plane':
                modelPanel = mc.getPanel(wf=1)
                camera = mc.modelPanel(modelPanel, q=True, camera=True)
                targetNull = mc.group(em=True)
                baseNull = mc.group(em=True)
                mc.move(0, 0, 1, targetNull)
                mc.parent(targetNull, baseNull)
                mc.delete(mc.orientConstraint(camera, baseNull))
                normal = mc.xform(targetNull, q=True, ws=True, rp=True)
                mc.delete(baseNull)
            centerPos = mc.xform(mesh, q=True, ws=True, rp=True)
            parentNull = mc.group(em=True)
            mc.xform(parentNull, ws=True, t=centerPos)
            mc.parent(mesh, parentNull)
            loc = mc.spaceLocator()
            mc.xform(loc, ws=True, t=centerPos)
            mc.xform(loc, ws=True, r=True, t=(0, 1, 0))
            mc.delete(mc.aimConstraint(loc, parentNull, aim=normal), loc)
            space = 'ws'
            axis2 = 'y'
        else:
            axis2 = axis
        funcDict = {'mean': 'sum',
         'max': 'max',
         'min': 'min'}
        vtxPosGroup = pf_69.vectorList(eval('mc.xform(vtxs,q=True,%s=True,t=True)' % space))
        num = vtxNum if align == 'mean' else 1
        val = eval('%s([pos.%s for pos in vtxPosGroup])/%s' % (funcDict[align], axis2, num))
        eval('mc.move(val,vtxs,%s=True,%s=True)' % (space, axis2))
        if axis in ('average normal', 'view plane'):
            mc.setAttr(parentNull + '.r', 0, 0, 0)
            mc.ungroup(parentNull)
        mm.eval('doMenuComponentSelection("%s", "facet")' % mesh)
        mc.select(selComps)
        pf_70()


def randomize():
    pf_61()
    selComps = pf_06('vtx')
    if selComps:
        comps, vtxs, selMode = selComps
        if mc.optionVar(q='zhcg_polyTools_randomize_keepBorder'):
            vtxs = [ vtx for vtx in vtxs if not pf_08(vtx) ]
        if vtxs:
            gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
            mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='Randomizing...', maxValue=len(vtxs) * 1.1)
            space = mc.optionVar(q='zhcg_polyTools_randomize_space')
            shift = mc.optionVar(q='zhcg_polyTools_randomize_shift')
            axis_x = mc.optionVar(q='zhcg_polyTools_randomize_axis_x')
            axis_y = mc.optionVar(q='zhcg_polyTools_randomize_axis_y')
            axis_z = mc.optionVar(q='zhcg_polyTools_randomize_axis_z')
            cmd = 'mc.polyMoveVertex(vtx,'
            if space == 3:
                cmd += 'ws=True,'
            if axis_x:
                if space == 1:
                    cmd += 'ltx=uniform(%f,%f),' % (-shift, shift)
                else:
                    cmd += 'tx=uniform(%f,%f),' % (-shift, shift)
            if axis_y:
                if space == 1:
                    cmd += 'lty=uniform(%f,%f),' % (-shift, shift)
                else:
                    cmd += 'ty=uniform(%f,%f),' % (-shift, shift)
            if axis_z:
                if space == 1:
                    cmd += 'ltz=uniform(%f,%f),' % (-shift, shift)
                else:
                    cmd += 'tz=uniform(%f,%f),' % (-shift, shift)
            cmd = cmd[:-1]
            cmd += ')'
            for vtx in vtxs:
                if mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                    break
                eval(cmd)
                delMeshHistory()
                mc.progressBar(gMainProgressBar, edit=True, step=1)

            mc.select(comps)
            mc.progressBar(gMainProgressBar, edit=True, endProgress=True)
            pf_22()


def straightenLine():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    selVtxs = mc.filterExpand(sm=31)
    if selEdges and len(selEdges) > 1:
        vtxGrps = pf_03(selEdges, breakVtxs=selVtxs)
        if vtxGrps:
            openVtxGrps = vtxGrps[0]
            if openVtxGrps:
                grpsNum = len(openVtxGrps)
                mesh = pf_29()
                even = mc.optionVar(q='zhcg_polyTools_straightenLine_even')
                gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
                mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='straightening...', maxValue=grpsNum)
                for vtxGrp in openVtxGrps:
                    if mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                        break
                    pf_43(vtxGrp, even)
                    mc.progressBar(gMainProgressBar, edit=True, step=1)

                mm.eval('doMenuComponentSelection("%s", "edge")' % mesh)
                mc.select(selEdges)
                if selVtxs:
                    mc.select(selVtxs, add=True)
                mc.progressBar(gMainProgressBar, edit=True, endProgress=True)
                delMeshHistory()
                pf_22()


def circlelizeLine():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    if selEdges and len(selEdges) > 1:
        vtxGrps = pf_03(selEdges)
        if vtxGrps:
            closeVtxGrps = vtxGrps[1]
            if closeVtxGrps:
                even = mc.optionVar(q='zhcg_polyTools_circlelizeLine_even')
                grpsNum = len(closeVtxGrps)
                mesh = pf_29()
                alignDict = {1: 'YZ',
                 2: 'XZ',
                 3: 'XY',
                 4: 'Auto'}
                align = alignDict[mc.optionVar(q='zhcg_polyTools_circlelizeLine_align')]
                radiusDict = {1: 'Mean',
                 2: 'Max',
                 3: 'Min',
                 4: 'Custom'}
                radius = radiusDict[mc.optionVar(q='zhcg_polyTools_circlelizeLine_radius')]
                radiusValue = mc.optionVar(q='zhcg_polyTools_circlelizeLine_customRadius')
                gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
                mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='circlelizing...', maxValue=grpsNum)
                for vtxGrp in closeVtxGrps:
                    if mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                        break
                    pf_42(vtxGrp, even, radius, radiusValue, align, mesh)
                    mc.progressBar(gMainProgressBar, edit=True, step=1)

                mm.eval('doMenuComponentSelection("%s", "edge")' % mesh)
                mc.select(selEdges)
                mc.progressBar(gMainProgressBar, edit=True, endProgress=True)
                delMeshHistory()
                pf_22()


def averageLine():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    selVtxs = mc.filterExpand(sm=31)
    if selEdges and len(selEdges) > 1:
        vtxGrps = pf_03(selEdges, breakVtxs=selVtxs)
        if vtxGrps:
            even = mc.optionVar(q='zhcg_polyTools_averageLine_even')
            keepShape = mc.optionVar(q='zhcg_polyTools_averageLine_keepShape')
            openVtxGrps, closeVtxGrps = vtxGrps
            allVtxGrps = openVtxGrps + closeVtxGrps
            grpsNum = len(allVtxGrps)
            mesh = pf_29()
            if keepShape:
                target = None
                if pf_73('zhcg_polyTools_shrinkWrapUI') and mc.button(BT_shrinkWrap, q=True, en=True):
                    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
                    if target:
                        if mc.objExists(target):
                            targetMesh = target
                        else:
                            target = None
                if not target:
                    targetMesh = mc.duplicate(mesh)[0]
                    mc.setAttr(targetMesh + '.v', False)
            smooth = mc.optionVar(q='zhcg_polyTools_averageLine_smooth')
            alignDict = {1: 'YZ',
             2: 'XZ',
             3: 'XY',
             4: 'Auto'}
            align = alignDict[mc.optionVar(q='zhcg_polyTools_averageLine_align')]
            step = mc.optionVar(q='zhcg_polyTools_averageLine_step')
            gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
            mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='averaging...', maxValue=grpsNum)
            for vtxGrp in allVtxGrps:
                if mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                    break
                pf_44(vtxGrp, vtxGrp in closeVtxGrps, mesh, even, smooth, step, align)
                if keepShape:
                    pf_48(targetMesh, mesh, len(vtxGrp), [ pf_32(vtx) for vtx in vtxGrp ])
                mc.progressBar(gMainProgressBar, edit=True, step=1)

            if keepShape and not target:
                mc.delete(targetMesh)
            mm.eval('doMenuComponentSelection("%s", "edge")' % mesh)
            mc.select(selEdges)
            if selVtxs:
                mc.select(selVtxs, add=True)
            mc.progressBar(gMainProgressBar, edit=True, endProgress=True)
            delMeshHistory()
            pf_22()


def pf_45(vtxGrp, close, mesh, even):
    refreshShapeCurve()
    shapeCurve = mc.textFieldButtonGrp(TFBG_shapeLine, q=True, tx=True)
    if shapeCurve and mc.objExists(shapeCurve):
        vtxNum = len(vtxGrp)
        if even:
            dupCurve = mc.duplicate(shapeCurve)[0]
            dupCurve = mc.rebuildCurve(dupCurve, s=vtxNum if close else vtxNum - 1, d=3 if close else 1, ch=False)[0]
            curveStartPos = pf_69(mc.xform('%s.ep[%s]' % (dupCurve, 0), q=True, ws=True, t=True))
            if close:
                firstVtxId = 0
                firstVtxPos = pf_69(mc.xform(vtxGrp[0], q=True, ws=True, t=True))
                firstVtxDist = curveStartPos.distance(firstVtxPos)
                for i in range(1, vtxNum):
                    vtxPos = pf_69(mc.xform(vtxGrp[i], q=True, ws=True, t=True))
                    dist = curveStartPos.distance(vtxPos)
                    if dist < firstVtxDist:
                        firstVtxDist = dist
                        firstVtxId = i

                vtxGrp = vtxGrp[firstVtxId:] + vtxGrp[:firstVtxId]
                curveEp2Pos = pf_69(mc.xform('%s.ep[%s]' % (dupCurve, 1), q=True, ws=True, t=True))
                vtx2Pos = pf_69(mc.xform(vtxGrp[1], q=True, ws=True, t=True))
                vtx_last_Pos = pf_69(mc.xform(vtxGrp[-1], q=True, ws=True, t=True))
                if curveEp2Pos.distance(vtx2Pos) > curveEp2Pos.distance(vtx_last_Pos):
                    vtxGrp.reverse()
                    vtxGrp = vtxGrp[-1:] + vtxGrp[:-1]
            else:
                firstVtxPos = pf_69(mc.xform(vtxGrp[0], q=True, ws=True, t=True))
                lastVtxPos = pf_69(mc.xform(vtxGrp[-1], q=True, ws=True, t=True))
                firstDist = curveStartPos.distance(firstVtxPos)
                lastDist = curveStartPos.distance(lastVtxPos)
                if firstDist > lastDist:
                    vtxGrp.reverse()
            for i in range(vtxNum):
                mc.xform(vtxGrp[i], ws=True, t=mc.xform('%s.ep[%s]' % (dupCurve, i), q=True, ws=True, t=True))

            mc.delete(dupCurve)
            pf_48(shapeCurve, mesh, vtxNum, [ pf_32(vtx) for vtx in vtxGrp ])
        else:
            pf_48(shapeCurve, mesh, vtxNum, [ pf_32(vtx) for vtx in vtxGrp ])


def shapeLine():
    pf_61()
    if pf_73('zhcg_polyTools_shapeLineUI'):
        selEdges = mc.filterExpand(sm=32)
        if selEdges:
            continua = pf_17(selEdges, returnMode='comps')
            if continua:
                close = True if continua[0] == 'close' else False
                vtxGrp = continua[1]
                mesh = pf_29()
                even = mc.optionVar(q='zhcg_polyTools_shapeLine_even')
                pf_45(vtxGrp, close, mesh, even)
                mc.select(selEdges)
                mm.eval('doMenuComponentSelection("%s", "edge")' % mesh)


def shrinkWrap():
    pf_61()
    if pf_73('zhcg_polyTools_shrinkWrapUI'):
        refreshWrapTarget()
        target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
        if target and mc.objExists(target):
            mesh = pf_29()
            if mesh and mesh != target:
                delMeshHistory()
                pf_22()
                shrinkMode = mc.radioButtonGrp(RBG_mode_shrinkWrap, q=True, sl=True)
                selComps = pf_06('selModeOnly')
                if selComps:
                    if shrinkMode == 1:
                        selComps, selVtxs, selMode = pf_06('vtx')
                        vtxNum = len(selVtxs)
                        allVtxIds = [ pf_32(vtx) for vtx in selVtxs ]
                    elif shrinkMode == 2:
                        selComps, selFaces, selMode = pf_06('face')
                        faceNum = len(selFaces)
                        allFaceIdsSet_1 = set([ pf_32(face) for face in selFaces ])
                else:
                    msg = mc.confirmDialog(t='Warnning!', m='Will ShrinkWrap the whole Mesh, are you sure?', b=['OK', 'Cancel'], db='OK', ds='Cancel', cb='Cancel')
                    if msg == 'OK':
                        if shrinkMode == 1:
                            selComps, selMode = (None, 'mesh')
                            vtxNum = mc.polyEvaluate(mesh, v=True)
                            allVtxIds = range(vtxNum)
                        elif shrinkMode == 2:
                            selComps, selMode = (None, 'mesh')
                            faceNum = mc.polyEvaluate(mesh, f=True)
                            allFaceIdsSet_1 = set(range(faceNum))
                    else:
                        return False
                targetFaceNum = mc.polyEvaluate(target, f=True)
                disableUndo = False
                if targetFaceNum > 5000 and (shrinkMode == 1 and vtxNum > 500 or shrinkMode == 2 and faceNum > 500):
                    disableUndo = True
                    mc.undoInfo(swf=False)
                if shrinkMode == 1:
                    pf_48(target, mesh, vtxNum, allVtxIds, progressBar=True)
                elif shrinkMode == 2:
                    pf_46(target, mesh, faceNum, allFaceIdsSet_1, progressBar=True)
                    fixBorder = mc.checkBox(CB_border_shrinkWrap, q=True, v=True)
                    if fixBorder:
                        if selComps:
                            selEdges = pf_06('edge')[1]
                            selBorderEdges = [ edge for edge in selEdges if pf_07(edge) ]
                        else:
                            selBorderEdges = pf_23(mesh)
                        if selBorderEdges:
                            pf_47(target, mesh, selBorderEdges, progressBar=True)
                if selMode == 'mesh':
                    mc.select(mesh)
                else:
                    mm.eval('doMenuComponentSelection("%s", "%s")' % (mesh, selMode))
                    mc.select(selComps)
                if disableUndo:
                    mc.undoInfo(swf=True)


def enableShrinkWrap():
    state = mc.button(BT_shrinkWrap, q=True, en=True)
    mc.button(BT_shrinkWrap, e=True, en=not state)


def refreshWrapTarget():
    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
    if not mc.objExists(target):
        removeWrapTarget()
        pf_71('%s not exists!' % target)


def selWrapTarget():
    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
    if mc.objExists(target):
        mc.select(target)
    refreshWrapTarget()


def removeWrapTarget():
    mc.textFieldButtonGrp(TFBG_shrinkWrap, e=True, tx='')
    mc.button(BT_shrinkWrap, e=True, en=False)
    shrinkWrapUI_popupMenu()


def toggleWrapTargetVis():
    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
    if mc.objExists(target):
        state = mc.getAttr(target + '.v')
        mc.setAttr(target + '.v', not state)
    refreshWrapTarget()


def toggleWrapTargetTranspency():
    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
    if mc.objExists(target):
        targetShape = mc.listRelatives(target, s=True)[0]
        curShaderGrp = mc.listConnections(targetShape, t='shadingEngine')
        if curShaderGrp:
            curShader = mc.listConnections(curShaderGrp[0], t='lambert')
            if curShader:
                curShader = curShader[0]
                transparency = any(mc.getAttr(curShader + '.transparency')[0])
                if transparency:
                    mc.setAttr(curShader + '.transparency', 0, 0, 0)
                else:
                    mc.setAttr(curShader + '.transparency', 0.3, 0.3, 0.3)
    refreshWrapTarget()


def toggleWrapTargetOverride(mode = 0):
    target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
    if mc.objExists(target):
        state = mc.getAttr(target + '.overrideEnabled')
        if not state:
            mc.setAttr(target + '.overrideEnabled', not state)
        mc.setAttr(target + '.overrideDisplayType', mode)
    refreshWrapTarget()


def addWrapTarget():
    sel = mc.ls(sl=True)
    target = None
    if sel:
        if mc.nodeType(sel[0]) == 'transform':
            shape = mc.listRelatives(sel[0], s=True)[0]
            if mc.objectType(shape, isa='geometryShape'):
                target = sel[0]
            else:
                target = None
        elif mc.objectType(sel[0], isa='geometryShape') and '.' not in sel[0]:
            transform = mc.listRelatives(sel[0], p=True)[0]
            target = transform
    if target:
        mc.textFieldButtonGrp(TFBG_shrinkWrap, e=True, tx=target)
        mc.button(BT_shrinkWrap, e=True, en=True)
    else:
        mc.textFieldButtonGrp(TFBG_shrinkWrap, e=True, tx='')
        mc.button(BT_shrinkWrap, e=True, en=False)
    mc.refresh()
    shrinkWrapUI_popupMenu()


def addShapeCurve():
    sel = mc.ls(sl=True)
    target = None
    if sel:
        if mc.nodeType(sel[0]) == 'transform':
            shape = mc.listRelatives(sel[0], s=True)[0]
            if mc.nodeType(shape) == 'nurbsCurve':
                target = sel[0]
            else:
                target = None
        elif mc.nodeType(sel[0]) == 'nurbsCurve':
            transform = mc.listRelatives(sel[0], p=True)[0]
            target = transform
    if target:
        mc.textFieldButtonGrp(TFBG_shapeLine, e=True, tx=target)
        mc.button(BT_shapeLine, e=True, en=True)
    else:
        mc.textFieldButtonGrp(TFBG_shapeLine, e=True, tx='')
        mc.button(BT_shapeLine, e=True, en=False)
    mc.refresh()
    addShapeCurve_popupMenu()


def addShapeCurve_popupMenu():
    if pf_73('addShapeCurve_popupMenu'):
        mc.deleteUI('addShapeCurve_popupMenu')
    target = mc.textFieldButtonGrp(TFBG_shapeLine, q=True, tx=True)
    if target and mc.objExists(target):
        mc.popupMenu('addShapeCurve_popupMenu', p=TFBG_shapeLine)
        mc.menuItem(l='Select Curve', c='%s.selShapeCurve()' % __name__)
        mc.menuItem(l='Remove Curve', c='%s.removeShapeCurve()' % __name__)
        mc.menuItem(d=True)
        mc.menuItem(l='Curve Visibility', cb=mc.getAttr(target + '.v'), c='%s.toggleShapeCurveVis()' % __name__)
        mc.radioMenuItemCollection(p='addShapeCurve_popupMenu')
        mc.menuItem(l='Normal', rb=True if not mc.getAttr(target + '.overrideEnabled') or mc.getAttr('%s.overrideDisplayType' % target) == 0 else False, c='%s.toggleShapeCurveOverride(mode=0)' % __name__)
        mc.menuItem(l='Template', rb=True if mc.getAttr('%s.overrideDisplayType' % target) == 1 and mc.getAttr(target + '.overrideEnabled') else False, c='%s.toggleShapeCurveOverride(mode=1)' % __name__)
        mc.menuItem(l='Reference', rb=True if mc.getAttr('%s.overrideDisplayType' % target) == 2 and mc.getAttr(target + '.overrideEnabled') else False, c='%s.toggleShapeCurveOverride(mode=2)' % __name__)


def refreshShapeCurve():
    target = mc.textFieldButtonGrp(TFBG_shapeLine, q=True, tx=True)
    if not mc.objExists(target):
        removeShapeCurve()
        pf_71('%s not exists!' % target)


def selShapeCurve():
    target = mc.textFieldButtonGrp(TFBG_shapeLine, q=True, tx=True)
    if mc.objExists(target):
        mc.select(target)
    refreshShapeCurve()


def removeShapeCurve():
    mc.textFieldButtonGrp(TFBG_shapeLine, e=True, tx='')
    mc.button(BT_shapeLine, e=True, en=False)
    addShapeCurve_popupMenu()


def toggleShapeCurveVis():
    target = mc.textFieldButtonGrp(TFBG_shapeLine, q=True, tx=True)
    if mc.objExists(target):
        state = mc.getAttr(target + '.v')
        mc.setAttr(target + '.v', not state)
    refreshShapeCurve()


def toggleShapeCurveOverride(mode = 0):
    target = mc.textFieldButtonGrp(TFBG_shapeLine, q=True, tx=True)
    if mc.objExists(target):
        state = mc.getAttr(target + '.overrideEnabled')
        if not state:
            mc.setAttr(target + '.overrideEnabled', not state)
        mc.setAttr(target + '.overrideDisplayType', mode)
    refreshShapeCurve()


def spin(spinType = None, dialog = False, reverse = False):
    global firstID
    pf_61()
    comps = pf_06('face')
    if comps:
        selComps, selFaces, selMode = comps
    else:
        return False
    if not spinType:
        continua = pf_18(selFaces)
        if continua:
            outlineEdgesNum = pf_09(selFaces, num=True)
            if outlineEdgesNum % 2 == 0 and outlineEdgesNum >= 4:
                if pf_12(selFaces):
                    spinType = 'pf_52'
                elif len(selFaces) == 2 and len(pf_64(selFaces)) == 1:
                    spinType = 'pf_49'
                elif pf_11(selFaces):
                    spinType = 'pf_51'
                elif pf_13(selFaces):
                    spinType = 'pf_54'
                elif pf_14(selFaces):
                    spinType = 'pf_53'
                elif pf_15(selFaces, selMode):
                    spinType = 'pf_50'
            elif len(selFaces) == 2 and len(pf_64(selFaces)) == 1:
                spinType = 'pf_49'
    if spinType:
        delMeshHistory()
        messageDict = {'pf_50': 'Spin %s-loop:' % len(selFaces),
         'pf_52': 'Spin %s-ribbon:' % len(selFaces),
         'pf_51': 'Spin %s-star:' % len(selFaces),
         'pf_53': 'Spin %s-grid:' % pf_14(selFaces),
         'pf_49': 'Spin edge:',
         'pf_54': 'Spin H-shape:'}
        if spinType == 'pf_50':
            sortedVtxs_A, sortedVtxs_B = pf_05(selFaces, selMode)
            vtxNum = len(selFaces)
        if spinType in ('pf_53', 'pf_54'):
            mesh = pf_29()
            target = None
            if pf_73('zhcg_polyTools_shrinkWrapUI') and mc.button(BT_shrinkWrap, q=True, en=True):
                target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
                if target:
                    if mc.objExists(target):
                        targetMesh = target
                    else:
                        target = None
            if not target:
                targetMesh = mc.duplicate(mesh)[0]
                mc.setAttr(targetMesh + '.v', False)
            if spinType == 'pf_53':
                gridType = pf_14(selFaces)
        if not dialog:
            pf_22()
            if spinType == 'pf_51':
                pf_51(selMode)
            elif spinType == 'pf_52':
                pf_52(selMode, reverse, 1)
            elif spinType == 'pf_49':
                pf_49(selMode, reverse, 1)
            elif spinType == 'pf_54':
                pf_54(selMode, reverse, mesh, targetMesh)
                if not target:
                    mc.delete(targetMesh)
            elif spinType == 'pf_53':
                pf_53(selMode, reverse, 1, gridType, mesh, targetMesh)
                if not target:
                    mc.delete(targetMesh)
            elif spinType == 'pf_50':
                pf_50(selMode, vtxNum, sortedVtxs_A, sortedVtxs_B, -1 if reverse else 1)
            pf_22()
            return 1
        firstID = 0
        opNum = 0
        if spinType in ('pf_49', 'pf_54'):
            bts = ['<--',
             'OK',
             'Cancel',
             '-->']
        elif spinType == 'pf_51':
            bts = ['OK', 'Cancel', '-->']
        elif spinType == 'pf_52' and len(selFaces) == 2:
            bts = ['<--',
             'OK',
             'Cancel',
             '-->']
        elif spinType == 'pf_53' and len(selFaces) == 6 or spinType == 'pf_50':
            bts = ['<<--',
             '<--',
             'OK',
             'Cancel',
             '-->',
             '-->>']
        else:
            bts = ['<<--',
             '<--',
             'OK',
             'Cancel',
             '-->',
             '-->>',
             '90 Degree']
        mc.undoInfo(ock=True)
        while True:
            msg = mc.confirmDialog(t='Spin - ZhCG_PolyTools', m=messageDict[spinType], b=bts, db='OK', ds='Cancel', cb='Cancel')
            pf_22()
            if msg == 'OK':
                if spinType in ('pf_53', 'pf_54') and not target and mc.objExists(targetMesh):
                    mc.delete(targetMesh)
                mc.undoInfo(cck=True)
                pf_22()
                delMeshHistory()
                return opNum
            if msg == 'Cancel':
                mc.undoInfo(cck=True)
                pf_22()
                if opNum:
                    pf_35()
                    if spinType in ('pf_53', 'pf_54') and not target and mc.objExists(targetMesh):
                        mc.delete(targetMesh)
                return 0
            if spinType == 'pf_50':
                if msg == '<<--':
                    for i in range(2):
                        firstID -= 1
                        pf_50(selMode, vtxNum, sortedVtxs_A, sortedVtxs_B, firstID)

                elif msg == '<--':
                    firstID -= 1
                    pf_50(selMode, vtxNum, sortedVtxs_A, sortedVtxs_B, firstID)
                elif msg == '-->':
                    firstID += 1
                    pf_50(selMode, vtxNum, sortedVtxs_A, sortedVtxs_B, firstID)
                elif msg == '-->>':
                    for i in range(2):
                        firstID += 1
                        pf_50(selMode, vtxNum, sortedVtxs_A, sortedVtxs_B, firstID)

            elif spinType == 'pf_51':
                if msg == '-->':
                    pf_51(selMode)
            elif spinType == 'pf_52':
                if msg == '<<--':
                    pf_52(selMode, True, 2)
                elif msg == '<--':
                    pf_52(selMode, True, 1)
                elif msg == '-->':
                    pf_52(selMode, False, 1)
                elif msg == '-->>':
                    pf_52(selMode, False, 2)
                elif msg == '90 Degree':
                    pf_52(selMode, False, 3)
            elif spinType == 'pf_54':
                if msg == '<--':
                    pf_54(selMode, True, mesh, targetMesh)
                elif msg == '-->':
                    pf_54(selMode, False, mesh, targetMesh)
            elif spinType == 'pf_53':
                if msg == '<<--':
                    pf_53(selMode, True, 2, gridType, mesh, targetMesh)
                elif msg == '<--':
                    pf_53(selMode, True, 1, gridType, mesh, targetMesh)
                elif msg == '-->':
                    pf_53(selMode, False, 1, gridType, mesh, targetMesh)
                elif msg == '-->>':
                    pf_53(selMode, False, 2, gridType, mesh, targetMesh)
                elif msg == '90 Degree':
                    pf_53(selMode, False, 3, gridType, mesh, targetMesh)
            elif spinType == 'pf_49':
                if msg == '<<--':
                    pf_49(selMode, True, 2)
                elif msg == '<--':
                    pf_49(selMode, True, 1)
                elif msg == '-->':
                    pf_49(selMode, False, 1)
                elif msg == '-->>':
                    pf_49(selMode, False, 2)
                elif msg == '90 Degree':
                    pf_49(selMode, False, 3)
            mc.refresh()
            opNum += 1


def editFacet():
    pf_61()
    delMeshHistory()
    opNum = 0
    mc.undoInfo(ock=True)
    mesh = pf_29()
    while True:
        pf_22()
        selFaces = mc.filterExpand(sm=34)
        if not selFaces:
            pf_71('No faces selected!')
            break
        else:
            outlineEdgesNum = pf_09(selFaces, num=True)
            interEdges = pf_64(selFaces)
            if outlineEdgesNum % 2:
                (interEdges and not len(interEdges) == 1 or outlineEdgesNum < 4) and pf_71('Number of outlineEdges is %d.' % outlineEdgesNum)
                break
            else:
                continua = pf_18(selFaces, True)
                if not continua:
                    pf_71('Selected Faces is not Continual!')
                    break
                elif continua not in ['0 hole', '1 hole', False]:
                    if 'hole' in continua:
                        pf_71("Selected Faces has %s, can't convert!" % continua)
                    else:
                        pf_71("Selected Faces is %s, can't convert!" % continua)
                    break
                else:
                    faceNum = len(selFaces)
                    curType = None
                    message = '%s faces. %s outline edges. ' % (faceNum, outlineEdgesNum)
                    if continua == '1 hole':
                        outlineEdges = pf_09(selFaces)
                        closeEdgesGrp = pf_03(outlineEdges, mesh=None, returnMode='vtx')[1]
                        if len(closeEdgesGrp[0]) != len(closeEdgesGrp[1]):
                            pf_71("2 border edges num is not the same, can't convert!")
                            break
                        elif pf_15(selFaces):
                            curType = 'loop'
                            message += "It's %s-loop. " % faceNum
                            availableTypes = []
                        else:
                            availableTypes = ['loop']
                    elif continua == '0 hole':
                        if pf_12(selFaces):
                            curType = 'ribbon'
                            message += "It's %s-ribbon. " % faceNum
                        elif pf_13(selFaces):
                            curType = 'H-shape'
                            message += "It's H-shape. "
                        elif pf_11(selFaces):
                            curType = 'star'
                            message += "It's %s-star. " % (outlineEdgesNum / 2)
                        elif pf_14(selFaces):
                            curType = pf_14(selFaces)
                            message += "It's %s-grid. " % curType
                        elif len(selFaces) == 2:
                            curType = '2faces'
                        availableTypes = []
                        if outlineEdgesNum % 2 == 0:
                            availableTypes = ['ribbon', 'star'] if outlineEdgesNum > 4 else (['Quad Face', 'star'] if faceNum > 1 else ['star'])
                            if outlineEdgesNum == 6:
                                availableTypes.append('H-shape')
                            availableGridTypes = gridDict1.get(outlineEdgesNum)
                            if availableGridTypes:
                                availableTypes += availableGridTypes
                            availableTypes = [ eachType for eachType in availableTypes if eachType != curType ]
                    for i in range(len(availableTypes)):
                        if 'x' in availableTypes[i]:
                            availableTypes[i] += ' grid'
                        elif availableTypes[i] == 'ribbon':
                            if outlineEdgesNum == 4:
                                availableTypes[i] = 'Quad Face'
                            else:
                                availableTypes[i] = '%s-%s' % ((outlineEdgesNum - 2) / 2, availableTypes[i])
                        elif availableTypes[i] == 'star':
                            availableTypes[i] = '%s-%s' % (outlineEdgesNum / 2, availableTypes[i])
                        elif availableTypes[i] == 'loop':
                            availableTypes[i] = '%s-%s' % (outlineEdgesNum / 2, availableTypes[i])

                    buttons = availableTypes
                    if curType == 'loop' or curType == '2faces' and outlineEdgesNum % 2:
                        message += 'You can spin it: '
                        buttons.insert(0, 'Spin')
                    elif curType:
                        message += 'You can spin it or convert it to: '
                        buttons.insert(0, 'Spin')
                    else:
                        message += 'You can convert it to: '
                    if opNum:
                        buttons.append('OK')
                    if not buttons:
                        break
                    else:
                        buttons.append('Cancel')
                        msg = mc.confirmDialog(t='Edit Facet - ZhCG_PolyTools', m=message, b=buttons, db='OK' if opNum else availableTypes[0], ds='Cancel', cb='Cancel')
                        if msg == 'Cancel':
                            mc.undoInfo(cck=True)
                            if opNum:
                                pf_35()
                            break
                        elif msg == 'OK':
                            mc.undoInfo(cck=True)
                            break
                        else:
                            if msg == 'Spin':
                                if 'x' in curType:
                                    spinType = 'pf_53'
                                else:
                                    spinDict = {'loop': 'pf_50',
                                     'star': 'pf_51',
                                     'ribbon': 'pf_52',
                                     '2faces': 'pf_49',
                                     'H-shape': 'pf_54'}
                                    spinType = spinDict[curType]
                                if spin(spinType, True):
                                    opNum += 1
                            else:
                                if 'ribbon' in msg:
                                    pf_57(mesh)
                                elif msg == 'Quad Face':
                                    pf_57(mesh)
                                elif 'star' in msg:
                                    pf_58(mesh)
                                elif 'loop' in msg:
                                    pf_56(mesh)
                                elif msg == 'H-shape':
                                    pf_59(mesh)
                                else:
                                    gridType = msg.split(' ')[0]
                                    pf_55(gridType, mesh)
                                opNum += 1
                            mc.refresh()

    delMeshHistory()
    pf_22()


def isolateSelFaces():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        mesh = pf_29()
        attrVals = None
        if pf_74(mesh, 'mirrorMode'):
            if mc.getAttr(mesh + '.mirrorMode') == 'mirror':
                pf_71("Can't isolate! You can 'Delete Mirror' or 'Take Half' first, then try again.")
                return False
            attrVals = [ mc.getAttr(mesh + '.' + attr) for attr in mirrorAttrs ]
        meshFaceNum = mc.polyEvaluate(mesh, f=True)
        if len(selFaces) < meshFaceNum:
            mc.undoInfo(ock=True)
            mc.polyChipOff(selFaces, kft=True, dup=False)
            newMeshs = mc.polySeparate(mesh, ch=False)
            isoMeshs = [ eachMesh for eachMesh in newMeshs if mc.polyEvaluate(eachMesh, f=True) == len(selFaces) ]
            if not isoMeshs:
                mc.undoInfo(cck=True)
                pf_35()
                pf_70("Can't isolate!")
            else:
                otherMeshs = [ eachMesh for eachMesh in newMeshs if eachMesh != isoMeshs[0] ]
                isoMesh = mc.rename(isoMeshs[0], mesh + '_iso')
                if attrVals:
                    pf_34(isoMesh, attrVals)
                for eachMesh in otherMeshs:
                    mc.setAttr(eachMesh + '.v', False)

                mm.eval('doMenuComponentSelection("%s", "facet")' % isoMesh)
                mc.undoInfo(cck=True)
                pf_70('')


def unIsolateMesh():
    pf_61()
    mesh = pf_29()
    if mesh and '_iso' in mesh:
        attrVals = None
        if pf_74(mesh, 'mirrorMode'):
            if mc.getAttr(mesh + '.mirrorMode') == 'mirror':
                mc.setAttr(mesh + '.mirrorMode', 'instance', type='string')
                pf_39(mesh)
            attrVals = [ mc.getAttr(mesh + '.' + attr) for attr in mirrorAttrs ]
        parentGrp = mc.listRelatives(mesh, p=True, type='transform')
        if parentGrp:
            parentGrp = parentGrp[0]
            allMeshs = mc.listRelatives(parentGrp, c=True)
            if allMeshs:
                for eachMesh in allMeshs:
                    if attrVals and not pf_74(eachMesh, 'mirrorMode'):
                        pf_39(eachMesh)

                newMesh = mc.rename(mc.polyUnite(allMeshs, ch=False)[0], parentGrp)
                mc.polyMergeVertex(newMesh, d=0.001, ch=False)
                mc.polyMergeUV(newMesh, d=0.001, ch=False)
                if attrVals:
                    pf_34(newMesh, attrVals)
                mc.select(newMesh)


def dupSelFaces():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        mesh = pf_29()
        meshFaceNum = mc.polyEvaluate(mesh, f=True)
        if len(selFaces) < meshFaceNum:
            attrVals = None
            if pf_74(mesh, 'mirrorMode'):
                attrVals = [ mc.getAttr(mesh + '.' + attr) for attr in mirrorAttrs ]
            mc.polyChipOff(selFaces, kft=True, dup=True, ch=False)
            newMeshs = mc.polySeparate(mesh, ch=False)
            oldMesh = [ eachMesh for eachMesh in newMeshs if mc.polyEvaluate(eachMesh, f=True) == meshFaceNum ][0]
            dupMeshs = [ eachMesh for eachMesh in newMeshs if eachMesh != oldMesh ]
            mc.ungroup(mesh)
            oldMesh = mc.rename(oldMesh, mesh)
            if len(dupMeshs) == 1:
                dupMesh = dupMeshs[0]
            else:
                dupMesh = mc.polyUnite(dupMeshs, ch=False)[0]
            dupMesh = mc.rename(dupMesh, pf_75(mesh + '_dup'))
            if attrVals:
                pf_34(oldMesh, attrVals)
                pf_34(dupMesh, attrVals)
            mc.select(dupMesh)
            pf_70('')
            return dupMesh


def splitMesh():
    pf_61()
    mesh = pf_29()
    if mesh:
        mc.delete(mesh, ch=True)
        attrVals = None
        if pf_74(mesh, 'mirrorMode'):
            attrVals = [ mc.getAttr(mesh + '.' + attr) for attr in mirrorAttrs ]
        selEdges = mc.filterExpand(sm=32)
        if not selEdges:
            selFaces = mc.filterExpand(sm=34)
            if selFaces:
                selEdges = pf_09(selFaces)
        newMeshs = None
        if selEdges:
            toVtxs = mc.filterExpand(mc.polyListComponentConversion(selEdges, fe=True, tv=True), sm=31)
            faceNum = mc.polyEvaluate(mesh, f=True)
            try:
                mc.undoInfo(ock=True)
                mc.polySplitVertex(toVtxs)
                mc.delete(mesh, ch=True)
                newMeshs = mc.polySeparate(mesh, ch=False)
                fixMeshs = [ i for i in newMeshs if mc.polyEvaluate(i, f=True) == 1 ]
                if fixMeshs and len(fixMeshs) > 1 and len(fixMeshs) < faceNum:
                    fixedMesh = mc.polyUnite(fixMeshs, ch=False)[0]
                    newMeshs = [ i for i in newMeshs if i not in fixMeshs ]
                    newMeshs.append(fixedMesh)
                mc.undoInfo(cck=True)
            except:
                mc.undoInfo(cck=True)
                pf_35()
                pf_71("Can't split!")

        else:
            try:
                newMeshs = mc.polySeparate(mesh, ch=False)
            except:
                pf_71("Can't split!")

        if newMeshs:
            for part in newMeshs:
                mc.polyMergeVertex(part, d=0, ch=False)
                mc.polyMergeUV(part, d=0.001, ch=False)
                mc.polySoftEdge(part, a=0, ch=False)
                if attrVals:
                    pf_34(part, attrVals)

            mc.ungroup(mesh)
            mc.select(newMeshs)
            for part in newMeshs:
                if re.search('_part\\d+\\b', mesh):
                    mc.rename(part, pf_75('%s' % mesh))
                else:
                    mc.rename(part, pf_75('%s_part' % mesh))

            pf_70()
            pf_22()


def mergeMesh():
    pf_61()
    meshs = pf_30()
    if meshs and len(meshs) > 1:
        attrVals = None
        for mesh in meshs:
            if pf_74(mesh, 'mirrorMode'):
                attrVals = [ mc.getAttr(mesh + '.' + attr) for attr in mirrorAttrs ]
                break

        newMesh = mc.polyUnite(meshs, ch=False)[0]
        mc.polyMergeVertex(newMesh, d=0.001, ch=False)
        mc.polyMergeUV(newMesh, d=0.001, ch=False)
        mc.polySoftEdge(newMesh, a=0, ch=False)
        mc.select(newMesh)
        if attrVals:
            pf_34(newMesh, attrVals)
        nameString = None
        for mesh in meshs:
            m = re.match('(\\w+)_(part|dup)\\d+\\b', mesh)
            if m:
                nameString = m.group(1)
                break

        if nameString:
            mc.rename(newMesh, nameString)
    pf_22()


def selNonQuardFacesUI():
    global CBG_selNonQuardFaces
    pf_61()
    if pf_73('zhcg_polyTools_selNonQuardFacesUI'):
        pf_71('Select NonQuard Faces Window Exists!')
    else:
        mc.window('zhcg_polyTools_selNonQuardFacesUI', t='Select NonQuard Faces', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CBG_selNonQuardFaces = mc.checkBoxGrp(ncb=3, la3=['3 Side', '5 Side', '6+ Side'], cw3=[80, 80, 80], cl3=['left'] * 3, v1=mc.optionVar(q='zhcg_polyTools_selNonQuardFaces_3side'), v2=mc.optionVar(q='zhcg_polyTools_selNonQuardFaces_5side'), v3=mc.optionVar(q='zhcg_polyTools_selNonQuardFaces_6side'), cc1="mc.optionVar(iv=['zhcg_polyTools_selNonQuardFaces_3side',mc.checkBoxGrp(%s.CBG_selNonQuardFaces,q=True,v1=True)])" % __name__, cc2="mc.optionVar(iv=['zhcg_polyTools_selNonQuardFaces_5side',mc.checkBoxGrp(%s.CBG_selNonQuardFaces,q=True,v2=True)])" % __name__, cc3="mc.optionVar(iv=['zhcg_polyTools_selNonQuardFaces_6side',mc.checkBoxGrp(%s.CBG_selNonQuardFaces,q=True,v3=True)])" % __name__)
        mc.button(l='Select NonQuard Faces', w=260, c='%s.selNonQuardFaces()' % __name__)
        mc.showWindow('zhcg_polyTools_selNonQuardFacesUI')


def selNonQuardFaces():
    pf_61()
    mesh = pf_29()
    if mesh:
        sel3side = mc.optionVar(q='zhcg_polyTools_selNonQuardFaces_3side')
        sel5side = mc.optionVar(q='zhcg_polyTools_selNonQuardFaces_5side')
        sel6side = mc.optionVar(q='zhcg_polyTools_selNonQuardFaces_6side')
        if any([sel3side, sel5side, sel6side]):
            selectFacesIds = []
            msgs = ''
            side_3_ids = []
            side_5_ids = []
            side_6plus_ids = []
            faceNum = mc.polyEvaluate(mesh, f=True)
            infos = iter(mc.polyInfo('%s.f[0:%s]' % (mesh, faceNum - 1), fv=True))
            for info in infos:
                nums = re.findall('\\d+', info)
                if len(nums) != 5:
                    if len(nums) == 4:
                        side_3_ids.append(nums[0])
                    elif len(nums) == 6:
                        side_5_ids.append(nums[0])
                    elif len(nums) > 6:
                        side_6plus_ids.append(nums[0])

            if sel3side:
                if side_3_ids:
                    selectFacesIds.extend(side_3_ids)
                    msgs += '%s  3Side face. ' % len(side_3_ids)
                else:
                    msgs += 'No 3Side face found. '
            if sel5side:
                if side_5_ids:
                    selectFacesIds.extend(side_5_ids)
                    msgs += '%s  5Side face. ' % len(side_5_ids)
                else:
                    msgs += 'No 5Side face found. '
            if sel6side:
                if side_6plus_ids:
                    selectFacesIds.extend(side_6plus_ids)
                    msgs += '%s  6+Side face. ' % len(side_6plus_ids)
                else:
                    msgs += 'No 6+Side face found. '
            if selectFacesIds:
                selectFaces = [ '%s.f[%s]' % (mesh, faceId) for faceId in selectFacesIds ]
                mc.select(selectFaces)
                mm.eval('doMenuComponentSelection("%s", "face")' % mesh)
            pf_70(msgs)
        else:
            pf_71('No item specified!')


def selNonQuardStarsUI():
    global CBG_selNonQuardStars
    pf_61()
    if pf_73('zhcg_polyTools_selNonQuardStarsUI'):
        pf_71('Select NonQuard Stars Window Exists!')
    else:
        mc.window('zhcg_polyTools_selNonQuardStarsUI', t='Select NonQuard Stars', s=False, mxb=False, w=320)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CBG_selNonQuardStars = mc.checkBoxGrp(ncb=4, la4=['2Star',
         '3Star',
         '5Star',
         '6+Star'], cw4=[80,
         80,
         80,
         80], cl4=['left'] * 4, v1=mc.optionVar(q='zhcg_polyTools_selNonQuardStars_2star'), v2=mc.optionVar(q='zhcg_polyTools_selNonQuardStars_3star'), v3=mc.optionVar(q='zhcg_polyTools_selNonQuardStars_5star'), v4=mc.optionVar(q='zhcg_polyTools_selNonQuardStars_6star'), cc1="mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_2star',mc.checkBoxGrp(%s.CBG_selNonQuardStars,q=True,v1=True)])" % __name__, cc2="mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_3star',mc.checkBoxGrp(%s.CBG_selNonQuardStars,q=True,v2=True)])" % __name__, cc3="mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_5star',mc.checkBoxGrp(%s.CBG_selNonQuardStars,q=True,v3=True)])" % __name__, cc4="mc.optionVar(iv=['zhcg_polyTools_selNonQuardStars_6star',mc.checkBoxGrp(%s.CBG_selNonQuardStars,q=True,v4=True)])" % __name__)
        mc.button(l='Select NonQuard Stars', c='%s.selNonQuardStars()' % __name__)
        mc.showWindow('zhcg_polyTools_selNonQuardStarsUI')


def selNonQuardStars():
    pf_61()
    mesh = pf_29()
    if mesh:
        sel2star = mc.optionVar(q='zhcg_polyTools_selNonQuardStars_2star')
        sel3star = mc.optionVar(q='zhcg_polyTools_selNonQuardStars_3star')
        sel5star = mc.optionVar(q='zhcg_polyTools_selNonQuardStars_5star')
        sel6star = mc.optionVar(q='zhcg_polyTools_selNonQuardStars_6star')
        if any([sel2star,
         sel3star,
         sel5star,
         sel6star]):
            selectVtxIds = []
            msgs = ''
            star_2_ids = []
            star_3_ids = []
            star_5_ids = []
            star_6plus_ids = []
            vtxNum = mc.polyEvaluate(mesh, v=True)
            infos = iter(mc.polyInfo('%s.vtx[0:%s]' % (mesh, vtxNum - 1), ve=True))
            for info in infos:
                nums = re.findall('\\d+', info)
                if len(nums) != 5:
                    if len(nums) == 3:
                        star_2_ids.append(nums[0])
                    elif len(nums) == 4:
                        star_3_ids.append(nums[0])
                    elif len(nums) == 6:
                        star_5_ids.append(nums[0])
                    elif len(nums) > 6:
                        star_6plus_ids.append(nums[0])

            if sel2star:
                if star_2_ids:
                    selectVtxIds.extend(star_2_ids)
                    msgs += '%s  2Star. ' % len(star_2_ids)
                else:
                    msgs += 'No 2Star found. '
            if sel3star:
                if star_3_ids:
                    selectVtxIds.extend(star_3_ids)
                    msgs += '%s  3Star. ' % len(star_3_ids)
                else:
                    msgs += 'No 3Star found. '
            if sel5star:
                if star_5_ids:
                    selectVtxIds.extend(star_5_ids)
                    msgs += '%s  5Star. ' % len(star_5_ids)
                else:
                    msgs += 'No 5Star found. '
            if sel6star:
                if star_6plus_ids:
                    selectVtxIds.extend(star_6plus_ids)
                    msgs += '%s  6+Star. ' % len(star_6plus_ids)
                else:
                    msgs += 'No 6+Star found. '
            if selectVtxIds:
                selectVtx = [ '%s.vtx[%s]' % (mesh, vtxId) for vtxId in selectVtxIds ]
                mc.select(selectVtx)
                mm.eval('doMenuComponentSelection("%s", "vertex")' % mesh)
            pf_70(msgs)
        else:
            pf_71('No item specified!')


def selBorder():
    pf_61()
    mesh = pf_29()
    if mesh:
        borderEdges = pf_23(mesh)
        mc.select(borderEdges)
        mm.eval('doMenuComponentSelection("%s", "edge")' % mesh)
        if borderEdges:
            pf_71('%s open edges.' % len(borderEdges))
        else:
            pf_70('No open edges found.')


def softenEdge():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    if selEdges:
        mc.polySoftEdge(selEdges, a=180)
        delMeshHistory()
    else:
        meshs = pf_30()
        if meshs:
            hil = mc.ls(hl=True)
            for mesh in meshs:
                mc.polySoftEdge(mesh, a=180)

            delMeshHistory()
            if hil:
                mc.select(cl=True)
            else:
                mc.select(meshs)


def hardenEdge():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    if selEdges:
        mc.polySoftEdge(selEdges, a=0)
        delMeshHistory()
    else:
        meshs = pf_30()
        if meshs:
            hil = mc.ls(hl=True)
            for mesh in meshs:
                mc.polySoftEdge(mesh, a=0)

            delMeshHistory()
            if hil:
                mc.select(cl=True)
            else:
                mc.select(meshs)


def toggleShader():
    pf_61()
    hil = mc.ls(hl=True)
    mesh = pf_29()
    meshShape = pf_31()
    if meshShape:
        if not mc.objExists('modeling_Blinn'):
            mc.shadingNode('blinn', asShader=True, n='modeling_Blinn')
        if not mc.objExists('modeling_Lambert'):
            mc.shadingNode('lambert', asShader=True, n='modeling_Lambert')
        curShaderGrp = mc.listConnections(meshShape, t='shadingEngine')
        if curShaderGrp:
            melCmds = 'defaultNavigation -source %s -destination %s.instObjGroups[0] -connectToExisting;                        connectNodeToAttrOverride("%s", "%s.instObjGroups[0]");                        sets -edit -forceElement %s %s;'
            curShader = mc.listConnections(curShaderGrp[0], t='lambert')
            if curShader:
                curShaderType = mc.nodeType(curShader[0])
                if curShaderType == 'blinn':
                    mm.eval(melCmds % (('modeling_Lambert', meshShape) * 2 + ('modeling_LambertSG', meshShape)))
                else:
                    mm.eval(melCmds % (('modeling_Blinn', meshShape) * 2 + ('modeling_BlinnSG', meshShape)))
            else:
                mm.eval(melCmds % (('modeling_Blinn', meshShape) * 2 + ('modeling_BlinnSG', meshShape)))
            if not hil:
                mc.select(mesh)
            if pf_74(mesh, 'mirrorMode') and mc.getAttr(mesh + '.mirrorMode') == 'instance' and ('_instance' in mesh and mc.objExists(mesh.replace('_instance', '')) or '_instance' not in mesh and mc.objExists(mesh + '_instance')):
                updateMirror()
            pf_70()


def toggleShaderTransparency():
    pf_61()
    meshShape = pf_31()
    if meshShape:
        curShaderGrp = mc.listConnections(meshShape, t='shadingEngine')
        if curShaderGrp:
            curShader = mc.listConnections(curShaderGrp[0], t='lambert')
            if curShader:
                curShader = curShader[0]
                transparency = mc.getAttr(curShader + '.transparency')[0]
                if any(transparency):
                    mc.setAttr(curShader + '.transparency', 0, 0, 0)
                else:
                    mc.setAttr(curShader + '.transparency', 0.5, 0.5, 0.5)


def selToBorder(mode = 'border'):
    pf_61()
    if mode == 'border':
        where = 1
    else:
        where = 2
    selMode = pf_06('selModeOnly')
    if selMode and selMode in ('vertex', 'puv', 'edge', 'facet'):
        mesh = pf_29()
        typeDict = {'vertex': 1,
         'edge': 32768,
         'puv': 16,
         'facet': 8}
        mc.polySelectConstraint(t=typeDict[selMode], w=where, m=2)
        mc.polySelectConstraint(t=typeDict[selMode], w=0, m=0)


def selToEdge():
    pf_61()
    mesh = pf_29()
    mm.eval('ConvertSelectionToEdges;')
    mm.eval('doMenuComponentSelection("%s", "edge")' % mesh)


def selToOutlineEdge():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        outlineEdges = pf_09(selFaces)
        if outlineEdges:
            mm.eval('doMenuComponentSelection("%s", "edge")' % pf_29())
            mc.select(outlineEdges)


def selToOutlineVtx():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        outlineEdges = pf_63(selFaces)
        if outlineEdges:
            mm.eval('doMenuComponentSelection("%s", "vertex")' % pf_29())
            mc.select(outlineEdges)


def selToVtx():
    pf_61()
    mesh = pf_29()
    mm.eval('ConvertSelectionToVertices;')
    mm.eval('doMenuComponentSelection("%s", "vertex")' % mesh)


def selToInterVtx():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    selFaces = mc.filterExpand(sm=34)
    interVtxs = None
    if selEdges:
        interVtxs = pf_66(selEdges)
    elif selFaces:
        interVtxs = pf_65(selFaces)
    if interVtxs:
        mm.eval('doMenuComponentSelection("%s", "vertex")' % pf_29())
        mc.select(interVtxs)


def selToInterEdge():
    pf_61()
    selVtxs = mc.filterExpand(sm=31)
    selFaces = mc.filterExpand(sm=34)
    interEdges = None
    if selVtxs:
        interEdges = pf_67(selVtxs)
    elif selFaces:
        interEdges = pf_64(selFaces)
    if interEdges:
        mm.eval('doMenuComponentSelection("%s", "edge")' % pf_29())
        mc.select(interEdges)


def selToFacet():
    pf_61()
    mesh = pf_29()
    mm.eval('ConvertSelectionToFaces;')
    mm.eval('doMenuComponentSelection("%s", "facet")' % mesh)


def selToInterFace():
    pf_61()
    selVtxs = mc.filterExpand(sm=31)
    selEdges = mc.filterExpand(sm=32)
    interFace = None
    if selVtxs:
        interFace = mc.polyListComponentConversion(selVtxs, fv=True, tf=True, internal=True)
    elif selEdges:
        interFace = mc.polyListComponentConversion(selEdges, fe=True, tf=True, internal=True)
    if interFace:
        mm.eval('doMenuComponentSelection("%s", "facet")' % pf_29())
        mc.select(interFace)


def selToPatternUI():
    global CB_selToPattern_reverse
    pf_61()
    if pf_73('selToPatternUI'):
        pf_71('To Pattern Window Exists!')
    else:
        mc.window('selToPatternUI', t='To Pattern', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CB_selToPattern_reverse = mc.checkBox(l=' Reverse', al='left', v=mc.optionVar(q='zhcg_polyTools_selToPattern_reverse'), cc="mc.optionVar(iv=['zhcg_polyTools_selToPattern_reverse',mc.checkBox(%s.CB_selToPattern_reverse,q=True,v=True)])" % __name__)
        mc.button(l='To Pattern', w=200, c='%s.selToPattern()' % __name__)
        mc.showWindow('selToPatternUI')


def selToPattern():
    pf_61()
    reverse = mc.optionVar(q='zhcg_polyTools_selToPattern_reverse')
    selVtxs = mc.filterExpand(sm=31)
    if selVtxs:
        selVtxToPattern(selVtxs, reverse=reverse)
    else:
        selEdges = mc.filterExpand(sm=32)
        if selEdges:
            selEdgeToPattern(selEdges, reverse=reverse)
        else:
            selFaces = mc.filterExpand(sm=34)
            if selFaces:
                selFaceToPattern(selFaces, reverse=reverse)


def selEdgeToPattern(selEdges, reverse = False):
    if len(selEdges) == 2:
        mesh = pf_29()
        ringPt = mc.polySelect(rpt=[pf_32(selEdges[0]), pf_32(selEdges[1])])
        if ringPt and reverse:
            ring = mc.polySelect(mesh, er=pf_32(selEdges[0]))
            if ring[0] == ring[-1]:
                ring = ring[:-1]
                selIds = [ ring.index(num) for num in [ pf_32(edge) for edge in selEdges ] ]
                selIds.sort()
                firstId, secondId = selIds
                step = secondId - firstId
                if step > len(ring) / 2:
                    step = len(ring) - step
                    firstId, secondId = secondId, firstId
                ring = ring[firstId:] + ring[:firstId]
                rintPt = ring[::step]
                patternEdgeRing = [ pf_33(mesh, 'edge', num) for num in rintPt ]
                mc.select(patternEdgeRing)
            else:
                mc.select([ pf_33(mesh, 'edge', num) for num in ringPt ])
        if not ringPt:
            if pf_07(selEdges[0]):
                loopPt = mc.polySelect(mesh, lbp=[pf_32(selEdges[0]), pf_32(selEdges[1])])
                if loopPt and reverse:
                    loop = mc.polySelect(mesh, elb=pf_32(selEdges[0]))
                    if loop[0] == loop[-1]:
                        loop = loop[:-1]
                        selIds = [ loop.index(num) for num in [ pf_32(edge) for edge in selEdges ] ]
                        selIds.sort()
                        firstId, secondId = selIds
                        step = secondId - firstId
                        if step > len(loop) / 2:
                            step = len(loop) - step
                            firstId, secondId = secondId, firstId
                        loop = loop[firstId:] + loop[:firstId]
                        loopPtIds = loop[::step]
                        patternEdgeLoop = [ pf_33(mesh, 'edge', num) for num in loopPtIds ]
                        mc.select(patternEdgeLoop)
                    else:
                        mc.select([ pf_33(mesh, 'edge', num) for num in loopPt ])
            else:
                loopPt = mc.polySelect(mesh, lpt=[pf_32(selEdges[0]), pf_32(selEdges[1])])
                if loopPt and reverse:
                    loop = mc.polySelect(mesh, el=pf_32(selEdges[0]))
                    if loop[0] == loop[-1]:
                        loop = loop[:-1]
                        selIds = [ loop.index(num) for num in [ pf_32(edge) for edge in selEdges ] ]
                        selIds.sort()
                        firstId, secondId = selIds
                        step = secondId - firstId
                        if step > len(loop) / 2:
                            step = len(loop) - step
                            firstId, secondId = secondId, firstId
                        loop = loop[firstId:] + loop[:firstId]
                        loopPtIds = loop[::step]
                        patternEdgeLoop = [ pf_33(mesh, 'edge', num) for num in loopPtIds ]
                        mc.select(patternEdgeLoop)
                    else:
                        mc.select([ pf_33(mesh, 'edge', num) for num in loopPt ])
            if not loopPt:
                mc.select(selEdges)


def selVtxToPattern(selVtxs, reverse = False):
    if len(selVtxs) == 2:
        mm.eval('SelectEdgeLoopSp')
        loopVtxs = mc.filterExpand(sm=31)
        if loopVtxs:
            mm.eval('SelectEdgeLoopSp')
            loopVtxs = mc.filterExpand(sm=31)
            loopVtxs2Edges = mc.polyListComponentConversion(loopVtxs, fv=True, te=True, internal=True)
            state, sortedVtxs = pf_17(loopVtxs2Edges, returnMode='comps')[:2]
            selIds = [ sortedVtxs.index(vtx) for vtx in selVtxs ]
            selIds.sort()
            firstId, secondId = selIds
            step = secondId - firstId
            if state == 'open':
                if step > 1:
                    patternVtxs = sortedVtxs[firstId::step] + sortedVtxs[firstId::-step]
                    mc.select(patternVtxs)
            elif state == 'close':
                if step > len(sortedVtxs) / 2:
                    step = len(sortedVtxs) - step
                    firstId, secondId = secondId, firstId
                if step > 1:
                    sortedVtxs = sortedVtxs[firstId:] + sortedVtxs[:firstId]
                    if reverse:
                        sortedVtxs.reverse()
                        firstId = len(sortedVtxs) - step - 1
                        sortedVtxs = sortedVtxs[firstId:] + sortedVtxs[:firstId]
                    patternVtxs = sortedVtxs[::step]
                    mc.select(patternVtxs)
        else:
            mc.select(selVtxs)


def selFaceToPattern(selFaces, reverse = False):
    if len(selFaces) == 2:
        mm.eval('SelectEdgeLoopSp')
        loopFaces = mc.filterExpand(sm=34)
        if loopFaces:
            mm.eval('SelectEdgeLoopSp')
            loopFaces = mc.filterExpand(sm=34)
            loopFaces = [ face for face in loopFaces if pf_19(face) ]
            state, sortedFaces = pf_01(loopFaces)
            selIds = [ sortedFaces.index(face) for face in selFaces ]
            selIds.sort()
            firstId, secondId = selIds
            step = secondId - firstId
            if state == 'open':
                if step > 1:
                    patternFaces = sortedFaces[firstId::step] + sortedFaces[firstId::-step]
                    mc.select(patternFaces)
                else:
                    mc.select(loopFaces)
            elif state == 'close':
                if step > len(sortedFaces) / 2:
                    step = len(sortedFaces) - step
                    firstId, secondId = secondId, firstId
                if step > 1:
                    sortedFaces = sortedFaces[firstId:] + sortedFaces[:firstId]
                    if reverse:
                        sortedFaces.reverse()
                        firstId = len(sortedFaces) - step - 1
                        sortedFaces = sortedFaces[firstId:] + sortedFaces[:firstId]
                    patternFaces = sortedFaces[::step]
                    mc.select(patternFaces)
                else:
                    mc.select(loopFaces)
        else:
            mc.select(selFaces)


def shortestEdgePath():
    pf_61()
    selVtxs = mc.filterExpand(sm=31)
    if selVtxs and len(selVtxs) == 2:
        mc.polySelect(sep=[pf_32(selVtxs[0]), pf_32(selVtxs[1])])


def mirrorPolyUI():
    global FSG_threshold
    global RBG_mode
    global CB_center
    pf_61()
    if pf_73('zhcg_polyTools_mirrorPolyUI'):
        pf_71('MirrorPoly Window Exists!')
    else:
        mc.window('zhcg_polyTools_mirrorPolyUI', t='Create Mirror - ZhCG_PolyTools', s=False, mxb=False)
        mc.columnLayout(co=('both', 5), rs=3, adj=True)
        mc.rowColumnLayout(nc=2, cw=[(1, 210), (2, 110)], cat=[2, 'left', 10])
        RBG_mode = mc.radioButtonGrp(nrb=2, l=' Mode:', la2=['Instance', 'Mirror'], cw3=[60, 80, 70], cal=[1, 'left'], sl=mc.optionVar(q='zhcg_polyTools_mirror_mode'), cc="mc.optionVar(iv=['zhcg_polyTools_mirror_mode',mc.radioButtonGrp(%s.RBG_mode,q=True,sl=True)])" % __name__)
        CB_center = mc.checkBox(l='Have Center Line', v=1, cc='mc.radioButtonGrp(%s.RBG_mode,e=True,en=mc.checkBox(%s.CB_center,q=True,v=True))' % (__name__, __name__))
        mc.setParent('..')
        mc.symmetricModelling(e=True, st=mc.symmetricModelling(q=True, t=True), ax='x', about='object')
        FSG_threshold = mc.floatSliderGrp(l=' Threshold:', f=True, step=0.001, min=0.001, max=0.2, fmx=100, cw=[(1, 62), (2, 38)], cal=[(1, 'left')], v=mc.symmetricModelling(q=True, t=True), cc='mc.symmetricModelling(e=True,t=%(1)s,st=%(1)s)', dc='mc.symmetricModelling(e=True,t=%(1)s,st=%(1)s)')
        mc.rowColumnLayout(nc=3, cw=[(1, 110), (2, 110), (3, 110)])
        mc.button(l='Delete Mirror', c='%s.delMirror()' % __name__)
        mc.button(l='Take Half', c='%s.takeHalf()' % __name__)
        mc.button(l='Create Mirror', c='%s.createMirror()' % __name__)
        mc.showWindow('zhcg_polyTools_mirrorPolyUI')

# TODO: BROKEN. fix it
def createMirror():
    pf_61()
    meshs = pf_30()
    if meshs:        
        msgs = ''
        for mesh in meshs:
            if not pf_74(mesh, 'mirrorMode'):                
                mc.undoInfo(ock=True)
                mc.addAttr(mesh, ln='mirrorMode', dt='string', h=True)
                mc.addAttr(mesh, ln='centerLine', at='enum', en='False:True:', h=True)
                mc.addAttr(mesh, ln='threshold', at='float', h=True)
                if pf_73('zhcg_polyTools_mirrorPolyUI'):
                    print('pf_73 active')
                    mc.setAttr(mesh + '.centerLine', mc.checkBox(CB_center, q=True, v=True))
                    mc.setAttr(mesh + '.threshold', mc.floatSliderGrp(FSG_threshold, q=True, v=True))
                else:
                    print('no 73')
                    mc.setAttr(mesh + '.centerLine', True)
                    mc.setAttr(mesh + '.threshold', mc.symmetricModelling(q=True, t=True))
                if mc.optionVar(q='zhcg_polyTools_mirror_mode') == 1:
                    pf_39(mesh)
                    pf_41(mesh)
                else:
                    pf_39(mesh)
                    pf_40(mesh)
                if pf_06():
                    mc.select(cl=True)
                msgs += mesh + ' Done! '
                mc.undoInfo(cck=True)
            else:
                msgs += mesh + ' have been mirrored before! '

        pf_70(msgs)
    pf_22()


def toggleMirror():
    pf_61()
    hil = mc.ls(hl=True)
    meshs = pf_30()
    if meshs:
        for mesh in meshs:
            if pf_74(mesh, 'mirrorMode'):
                if '_instance' in mesh and mc.objExists(mesh.replace('_instance', '')):
                    mesh = mesh.replace('_instance', '')
                    mc.select(mesh)
                mirrorMode = mc.getAttr(mesh + '.mirrorMode')
                centerLine = mc.getAttr(mesh + '.centerLine')
                if mirrorMode == 'instance':
                    if mc.objExists(mesh + '_instance'):
                        mc.delete(mesh + '_instance')
                    pf_40(mesh)
                else:
                    pf_39(mesh)
                    pf_41(mesh)

        if hil:
            mc.select(cl=True)
        else:
            mc.select(meshs)
        pf_70()
    pf_22()


def takeHalf():    
    pf_61()
    meshs = pf_30()
    if meshs:
        for mesh in meshs:
            if pf_74(mesh, 'mirrorMode'):
                if mc.getAttr(mesh + '.mirrorMode') == 'instance':
                    if '_instance' in mesh and mc.objExists(mesh.replace('_instance', '')):
                        mc.delete(mesh)
                        mc.select(mesh.replace('_instance', ''))
                    elif '_instance' not in mesh and mc.objExists(mesh + '_instance'):
                        mc.delete(mesh + '_instance')
                else:
                    if pf_73('zhcg_polyTools_mirrorPolyUI'):
                        mc.setAttr(mesh + '.threshold', mc.floatSliderGrp(FSG_threshold, q=True, v=True))
                    mc.setAttr(mesh + '.mirrorMode', 'instance', type='string')
                    pf_39(mesh)
            else:
                mc.addAttr(mesh, ln='mirrorMode', dt='string', h=True)
                mc.addAttr(mesh, ln='centerLine', at='enum', en='False:True:', h=True)
                mc.addAttr(mesh, ln='threshold', at='float', h=True)
                mc.setAttr(mesh + '.mirrorMode', 'instance', type='string')
                if pf_73('zhcg_polyTools_mirrorPolyUI'):
                    mc.setAttr(mesh + '.centerLine', mc.checkBox(CB_center, q=True, v=True))
                    mc.setAttr(mesh + '.threshold', mc.floatSliderGrp(FSG_threshold, q=True, v=True))
                else:
                    mc.setAttr(mesh + '.centerLine', True)
                    mc.setAttr(mesh + '.threshold', 0.001)
                pf_39(mesh)

        pf_70()
    pf_22()


def updateMirror():
    pf_61()
    sel = mc.ls(sl=True)
    hil = mc.ls(hl=True)
    meshs = pf_30()
    if meshs:
        for mesh in meshs:
            if pf_74(mesh, 'mirrorMode'):
                reverse = False
                if mc.getAttr(mesh + '.mirrorMode') == 'mirror':
                    pf_39(mesh)
                    pf_40(mesh)
                    if hil:
                        mc.select(cl=True)
                    elif sel:
                        try:
                            mc.select(sel)
                        except:
                            pass

                    else:
                        mc.select(cl=True)
                elif mc.getAttr(mesh + '.centerLine'):
                    if mc.objExists(mesh + '_instance'):
                        mc.delete(mesh + '_instance')
                    pf_41(mesh)

        pf_70()
    pf_22()


def moveToCenter():
    pf_61()
    selComps = pf_06('vtx')
    if selComps:
        vtxs = selComps[1]
        mesh = pf_29()
        worldRotatePivot = mc.xform(mesh, ws=True, q=True, rp=True)
        translate = mc.getAttr(mesh + '.t')[0]
        localRotatepivot = (pf_69(worldRotatePivot) - pf_69(translate)).toTuple()
        mc.move(localRotatepivot[0], vtxs, os=True, x=True)
        pf_22()


def getCenterVtxsUI():
    global FSG_selCenterVtxs
    pf_61()
    if pf_73('zhcg_polyTools_getCenterVtxsUI'):
        pf_71('Select Center Vtxs Window Exists!')
    else:
        mc.window('zhcg_polyTools_getCenterVtxsUI', t='Select Center Vtxs', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        FSG_selCenterVtxs = mc.floatSliderGrp(l=' Threshold:', f=True, min=0, max=0.1, fmn=0, fmx=100, pre=3, s=0.001, cw=[(1, 60), (2, 40)], cal=[(1, 'left')], rat=[1, 'top', 3], v=mc.optionVar(q='zhcg_polyTools_selCenterVtxsThreshold'), cc="mc.optionVar(fv=['zhcg_polyTools_selCenterVtxsThreshold',mc.floatSliderGrp(%s.FSG_selCenterVtxs,q=True,v=True)])" % __name__)
        mc.rowColumnLayout(nc=2)
        mc.button(l='Select Center Vtxs', c='%s.getCenterVtxs()' % __name__)
        mc.button(l='Move to Center', c='%s.moveToCenter()' % __name__)
        mc.showWindow('zhcg_polyTools_getCenterVtxsUI')


def getCenterVtxs():
    pf_61()
    mesh = pf_29()
    if mesh:
        threshold = mc.optionVar(q='zhcg_polyTools_selCenterVtxsThreshold')
        vtxsNum = mc.polyEvaluate(mesh, v=True)
        centerVtxs = []
        vtxPosGrp = mc.xform('%s.vtx[0:%s]' % (mesh, vtxsNum - 1), q=True, os=True, t=True)
        for i in range(0, vtxsNum * 3, 3):
            if abs(vtxPosGrp[i]) <= threshold:
                centerVtxs.append(pf_33(mesh, 'vtx', i / 3))

        if centerVtxs:
            mm.eval('doMenuComponentSelection("%s", "vertex")' % mesh)
            mc.select(centerVtxs)
            pf_71('%s center vertices selected.' % len(centerVtxs))
        else:
            pf_71('No center vertices found.')


def delMirror():
    pf_61()
    meshs = pf_30()
    if meshs:
        msgs = ''
        for mesh in meshs:
            if pf_74(mesh, 'mirrorMode'):
                mirrorMode = mc.getAttr(mesh + '.mirrorMode')
                if mirrorMode == 'instance':
                    if '_instance' in mesh and mc.objExists(mesh.replace('_instance', '')):
                        mc.delete(mesh)
                        mesh = mesh.replace('_instance', '')
                        mc.select(mesh)
                    elif '_instance' not in mesh and mc.objExists(mesh + '_instance'):
                        mc.delete(mesh + '_instance')
                for attr in ['mirrorMode', 'centerLine', 'threshold']:
                    if pf_74(mesh, attr):
                        mc.deleteAttr(mesh, at=attr)

                msgs += mesh + ' Done! '

        if msgs:
            pf_70(msgs)
        else:
            pf_70('No mirrored mesh found!')


def mergeFacetUI():
    global CB_mergeFacet_clearVtxs
    pf_61()
    if pf_73('mergeFacetUI'):
        pf_71('Merge Faces Window Exists!')
    else:
        mc.window('mergeFacetUI', t='Merge Faces', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CB_mergeFacet_clearVtxs = mc.checkBox(l=' Clean Vertices', al='left', v=mc.optionVar(q='zhcg_polyTools_mergeFacet_cleanVtxs'), cc="mc.optionVar(iv=['zhcg_polyTools_mergeFacet_cleanVtxs',mc.checkBox(%s.CB_mergeFacet_clearVtxs,q=True,v=True)])" % __name__)
        mc.button(l='Merge Faces', w=200, c='%s.mergeFacet()' % __name__)
        mc.showWindow('mergeFacetUI')


def mergeFacet():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces and len(selFaces) > 1:
        cleanVertices = mc.optionVar(q='zhcg_polyTools_mergeFacet_cleanVtxs')
        continua = pf_18(selFaces, True)
        if continua and continua == '0 hole':
            interEdges = pf_64(selFaces)
            outlineVtxs = pf_63(selFaces)
            outlineEdgesNum = len(outlineVtxs)
            outlineVtxPosGroup = pf_69.vectorList(mc.xform(outlineVtxs, q=True, os=True, t=True))
            mc.polyDelEdge(interEdges, cleanVertices=cleanVertices)
            for vtx in outlineVtxs:
                if pf_69(mc.xform(vtx, q=True, os=True, t=True)) in outlineVtxPosGroup:
                    curVtx = vtx
                    break
            else:
                curVtx = None

            if curVtx:
                curVtx2faces = mc.filterExpand(mc.polyListComponentConversion(curVtx, fv=True, tf=True), sm=34)
                polyFaces = []
                for face in curVtx2faces:
                    faceEdgeNum = len(re.findall('\\d+', mc.polyInfo(face, fe=True)[0])) - 1
                    if faceEdgeNum == outlineEdgesNum:
                        polyFaces.append(face)

                if polyFaces:
                    if len(polyFaces) > 1:
                        centerPos = pf_69.center(*outlineVtxPosGroup)
                        for face in polyFaces:
                            if pf_69.center(*pf_69.vectorList(mc.xform(face, q=True, os=True, t=True))) == centerPos:
                                newFace = face
                                break
                        else:
                            newFace = None

                    else:
                        newFace = polyFaces[0]
                    if newFace:
                        mc.select(newFace)
    pf_22()


def freezeTransformations():
    pf_61()
    meshs = pf_30()
    if meshs:
        if pf_73('zhcg_polyTools_freezeTransformationsUI'):
            v1 = mc.checkBoxGrp(CB_freezeTransformationsUI, q=True, v1=True)
            v2 = mc.checkBoxGrp(CB_freezeTransformationsUI, q=True, v2=True)
            v3 = mc.checkBoxGrp(CB_freezeTransformationsUI, q=True, v3=True)
            if any([v1, v2, v3]):
                cmd = 'mc.makeIdentity("%s",a=True'
                if v1:
                    cmd += ',t=True'
                if v2:
                    cmd += ',r=True'
                if v3:
                    cmd += ',s=True'
                cmd += ')'
                for mesh in meshs:
                    eval(cmd % mesh)

        else:
            mc.makeIdentity(meshs, a=True, t=True, r=True, s=True)


def freezeTransformationsUI():
    global CB_freezeTransformationsUI
    pf_61()
    if pf_73('zhcg_polyTools_freezeTransformationsUI'):
        pf_71('Freeze Transformations Window Exists!')
    else:
        mc.window('zhcg_polyTools_freezeTransformationsUI', t='Freeze Transformations', s=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        CB_freezeTransformationsUI = mc.checkBoxGrp(ncb=3, l=' Freeze:', la3=['Translate', 'Rotate', 'Scale'], cw4=[50,
         80,
         65,
         60], cl4=['left'] * 4, va3=[True] * 3)
        mc.button(l='Freeze Transformations', c='%s.freezeTransformations()' % __name__, bgc=(0.95, 0.62, 0.46))
        mc.showWindow('zhcg_polyTools_freezeTransformationsUI')


def zeroTransformation():
    pf_61()
    meshs = pf_30()
    if meshs:
        for mesh in meshs:
            mc.setAttr('%s.t' % mesh, 0, 0, 0)
            mc.setAttr('%s.r' % mesh, 0, 0, 0)
            mc.setAttr('%s.s' % mesh, 1, 1, 1)
            if pf_74(mesh, 'mirrorMode'):
                if mc.getAttr('%s.mirrorMode' % mesh) == 'instance' and '_instance' in mesh:
                    mc.setAttr('%s.sx' % mesh, -1)


def extrudeFaces():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        mc.polyExtrudeFacet(selFaces, ltz=0.001)
        delMeshHistory()
        mm.eval('performPolyMove "" 0;')


def extrudeEdges():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    if selEdges:
        mc.polyExtrudeEdge(selEdges, ltz=0.001)
        delMeshHistory()
        mm.eval('performPolyMove "" 0;')


def addNewFaces():
    pf_61()
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        if pf_18(selFaces):
            mc.polyExtrudeFacet(selFaces)
            mc.polyMoveFacet(ls=[0.33, 0.33, 1])
            delMeshHistory()
            mm.eval('performPolyMove "" 0;')
            pf_22()
    else:
        selEdges = mc.filterExpand(sm=32)
        if selEdges and len(selEdges) >= 3 and pf_10(selEdges):
            continua = pf_17(selEdges, returnMode='comps')
            if continua:
                if continua[0] == 'open':
                    sideEdges = list(set(mc.filterExpand(mc.polyListComponentConversion(continua[1][1:-1], fv=True, te=True), sm=32)) - set(continua[2][1:-1]))
                    mc.polySplitRing(sideEdges)
                    newEndVtxs = list(set(mc.filterExpand(mc.polyListComponentConversion(continua[2][0], continua[2][-1], fe=True, tv=True), sm=31)) - set(continua[1]))
                    if len(selEdges) == 3:
                        end_edges_del = list(set(mc.filterExpand(mc.polyListComponentConversion(continua[1][1], continua[1][-2], newEndVtxs, fv=True, te=True, internal=True), sm=32)) - set(mc.filterExpand(mc.polyListComponentConversion(continua[1][1], continua[1][-2], fv=True, te=True, internal=True), sm=32)))
                    else:
                        end_edges_del = mc.filterExpand(mc.polyListComponentConversion(continua[1][1], continua[1][-2], newEndVtxs, fv=True, te=True, internal=True), sm=32)
                    mc.select(end_edges_del)
                    mm.eval('SelectEdgeLoopSp')
                    toVtxs = mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tv=True)
                    mc.delete(end_edges_del)
                    toEdges = mc.polyListComponentConversion(toVtxs, fv=True, te=True, internal=True)
                    mc.select(toEdges)
                    end_edges_col = mc.polyListComponentConversion(continua[1][0], continua[1][-1], newEndVtxs, fv=True, te=True, internal=True)
                    for edge in end_edges_col:
                        vtxs = mc.filterExpand(mc.polyListComponentConversion(edge, fe=True, tv=True), sm=31)
                        newVtx = [ vtx for vtx in vtxs if vtx in newEndVtxs ][0]
                        oldVtx = [ vtx for vtx in vtxs if vtx not in newEndVtxs ][0]
                        mc.xform(newVtx, os=True, t=mc.xform(oldVtx, q=True, os=True, t=True))

                    mc.polyMergeVertex(newEndVtxs, continua[1][0], continua[1][-1], d=0.001)
                    mc.select(cl=True)
                    delMeshHistory()
                    pf_22()


def insertEdgeLoopUI():
    global ISG_insertEdgeLoop_div
    pf_61()
    if pf_73('insertEdgeLoopUI'):
        pf_71('Insert EdgeLoop Window Exists!')
    else:
        mc.window('insertEdgeLoopUI', t='Insert EdgeLoop', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        ISG_insertEdgeLoop_div = mc.intSliderGrp(l=' Divisions:', f=True, min=1, max=max(10, mc.optionVar(q='zhcg_polyTools_connect_div')), fmn=1, fmx=100, cw=[(1, 60), (2, 40)], cal=[(1, 'left')], rat=[1, 'top', 3], v=mc.optionVar(q='zhcg_polyTools_insertEdgeLoop_div'), cc="mc.optionVar(iv=['zhcg_polyTools_insertEdgeLoop_div',mc.intSliderGrp(%s.ISG_insertEdgeLoop_div,q=True,v=True)])" % __name__)
        mc.button(l='Insert EdgeLoop', c='%s.insertEdgeLoop()' % __name__)
        mc.showWindow('insertEdgeLoopUI')


def insertEdgeLoop():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    if selEdges:
        delMeshHistory()
        div = mc.optionVar(q='zhcg_polyTools_insertEdgeLoop_div')
        gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
        mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=False, status='Inserting Edge Loops...', maxValue=len(selEdges))
        newEdges = []
        allEdgeRings = []
        refreshCount = 0
        for edge in selEdges:
            edgeIndex = pf_32(edge)
            if edgeIndex not in allEdgeRings:
                newEdgeRings = mc.polySelect(er=edgeIndex)
                allEdgeRings.extend(newEdgeRings)
                if newEdgeRings and len(newEdgeRings) > 1:
                    mc.polySplitRing(div=div, stp=2)
                    newEdges += mc.filterExpand(sm=32)
                    delMeshHistory()
                    mc.progressBar(gMainProgressBar, edit=True, step=1)
                    refreshCount += 1

        if newEdges:
            mc.select(newEdges)
        else:
            mc.select(selEdges)
        mc.progressBar(gMainProgressBar, edit=True, endProgress=True)
    pf_22()


def subdivEdges(option = False):
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    if selEdges:
        div = mc.optionVar(q='zhcg_polyTools_subdivEdges_div')
        mc.polySubdivideEdge(dv=div)
        delMeshHistory()


def subdivEdgesUI():
    global ISG_subdivEdges_div
    pf_61()
    if pf_73('zhcg_polyTools_subdivEdgesUI'):
        pf_71('Subdiv Edges Window Exists!')
    else:
        mc.window('zhcg_polyTools_subdivEdgesUI', t='Subdiv Edges', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        ISG_subdivEdges_div = mc.intSliderGrp(l=' Divisions:', f=True, min=1, max=max(10, mc.optionVar(q='zhcg_polyTools_subdivEdges_div')), fmn=1, fmx=100, cw=[(1, 60), (2, 40)], cal=[(1, 'left')], rat=[1, 'top', 3], v=mc.optionVar(q='zhcg_polyTools_subdivEdges_div'), cc="mc.optionVar(iv=['zhcg_polyTools_subdivEdges_div',mc.intSliderGrp(%s.ISG_subdivEdges_div,q=True,v=True)])" % __name__)
        mc.button(l='Subdiv Edges', c='%s.subdivEdges()' % __name__)
        mc.showWindow('zhcg_polyTools_subdivEdgesUI')


def connectUI():
    global ISG_connect_div
    pf_61()
    if pf_73('zhcg_polyTools_connectUI'):
        pf_71('Connect Window Exists!')
    else:
        mc.window('zhcg_polyTools_connectUI', t='Connect', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        ISG_connect_div = mc.intSliderGrp(l=' Divisions( if ONLY select edges ):', f=True, min=1, max=max(10, mc.optionVar(q='zhcg_polyTools_connect_div')), fmn=1, fmx=100, cw=[(1, 170), (2, 40)], cal=[(1, 'left')], rat=[1, 'top', 3], v=mc.optionVar(q='zhcg_polyTools_connect_div'), cc="mc.optionVar(iv=['zhcg_polyTools_connect_div',mc.intSliderGrp(%s.ISG_connect_div,q=True,v=True)])" % __name__)
        mc.button(l='Connect', c='%s.connect()' % __name__)
        mc.showWindow('zhcg_polyTools_connectUI')


def connect(option = False):
    pf_61()
    mesh = pf_29()
    selVtxs = mc.filterExpand(sm=31)
    selEdges = mc.filterExpand(sm=32)
    if selVtxs or selEdges:
        if not selVtxs and selEdges and len(selEdges) > 1:
            div = mc.optionVar(q='zhcg_polyTools_connect_div')
            mc.polySplitRing(div=div, stp=2)
        else:
            mc.polyConnectComponents()
            mc.select(cl=True)
        delMeshHistory()
        pf_70()
        pf_22()


def duplicateEdges():
    pf_61()
    selEdges = mc.filterExpand(sm=32)
    selVtxs = mc.filterExpand(sm=31)
    if selEdges:
        degree = mc.optionVar(q='zhcg_polyTools_duplicateEdges_degree')
        vtxGrps = pf_03(selEdges, breakVtxs=selVtxs)
        if vtxGrps:
            openVtxGrps, closeVtxGrps = vtxGrps
            curves = []
            for openVtxGrp in openVtxGrps:
                vtxPosTupleGroup = [ pf_69(mc.xform(vtx, q=True, ws=True, t=True)).toTuple() for vtx in openVtxGrp ]
                openCurve = mc.curve(n='dupEdge_open1', ep=vtxPosTupleGroup, d=1 if degree == 1 else 3)
                curves.append(openCurve)

            for closeVtxGrp in closeVtxGrps:
                vtxPosTupleGroup = [ pf_69(mc.xform(vtx, q=True, ws=True, t=True)).toTuple() for vtx in closeVtxGrp ]
                vtxNum = len(closeVtxGrp)
                closeCurve = mc.circle(n='dupEdge_close1', s=vtxNum, c=(0, 0, 0), d=1 if degree == 1 else 3)[0]
                curves.append(closeCurve)
                for i in range(vtxNum):
                    mc.xform(closeCurve + '.ep[%d]' % i, ws=True, t=vtxPosTupleGroup[i])

                if degree == 1:
                    mc.xform(closeCurve + '.ep[%d]' % vtxNum, ws=True, t=vtxPosTupleGroup[0])

            if curves:
                mc.select(curves)


def duplicateEdgesUI():
    global RBG_duplicateEdges_degree
    pf_61()
    if pf_73('zhcg_polyTools_duplicateEdgesUI'):
        pf_71('Duplicate Edges Window Exists!')
    else:
        mc.window('zhcg_polyTools_duplicateEdgesUI', t='Duplicate Edges', s=False, mxb=False)
        mc.columnLayout(co=['both', 5], rs=3, adj=True)
        RBG_duplicateEdges_degree = mc.radioButtonGrp(l=' Curve Degree:', nrb=2, la2=['1', '3'], cw3=[100, 50, 50], cl3=['left'] * 3, sl=mc.optionVar(q='zhcg_polyTools_duplicateEdges_degree'), on1="mc.optionVar(iv=['zhcg_polyTools_duplicateEdges_degree',1])", on2="mc.optionVar(iv=['zhcg_polyTools_duplicateEdges_degree',2])")
        mc.button(l='Duplicate Edges', w=240, c='%s.duplicateEdges()' % __name__)
        mc.showWindow('zhcg_polyTools_duplicateEdgesUI')


def quickSel(mode = 'create'):
    pf_61()
    sel = mc.ls(sl=True)
    if sel:
        createSelBox(sel)
    else:
        pf_71('Nothing selected!')


def createSelBox(sel):
    if not pf_73('quickSelUI'):
        mc.window('quickSelUI', t=' Quick Sel', s=False, tlb=True, tb=True)
        mc.columnLayout('mainCL_quickSel')
        height = mc.window('quickSelUI', q=True, h=True)
        mc.window('quickSelUI', e=True, wh=[120, 1])
        if height % 22 != 1:
            mc.window('quickSelUI', e=True, te=mc.window('quickSelUI', q=True, te=True) + 21, le=mc.window('quickSelUI', q=True, le=True) + 3)
        mc.showWindow('quickSelUI')
    oldBoxes = mc.columnLayout('mainCL_quickSel', q=True, childArray=True)
    if not oldBoxes or len(oldBoxes) < 20:
        ann = ', '.join(sel)
        if len(ann) > 100:
            ann = ann[:100] + '......'
        if len(sel) == 1 and '.' not in sel[0]:
            label = sel[0].split('|')[-1]
            if len(label) > 18:
                label = label[:13] + '......'
        elif not oldBoxes:
            label = 'QuickSel 1'
        else:
            oldBoxesLabelGrp = [ mc.button(box, q=True, label=True) for box in oldBoxes ]
            for i in range(1, 21):
                if 'QuickSel %d' % i not in oldBoxesLabelGrp:
                    label = 'QuickSel %d' % i
                    break
        bt = mc.button(p='mainCL_quickSel', l=label, w=120, bgc=(0.95, 0.62, 0.46))
        mc.button(bt, e=True, ann=ann, c="%s.selectSelBox(%s,'%s')" % (__name__, sel, bt))
        quickSelBox_popupMenu(bt, sel)
        bt_H = mc.button(bt, q=True, h=True)
        oldUI_H = mc.window('quickSelUI', q=True, h=True)
        newUI_H = oldUI_H + bt_H
        mc.window('quickSelUI', e=True, h=newUI_H)
    else:
        pf_71('Max SelBox number is 20.')

def selectSelBox(sel, box):
    try:
        mc.select(sel)
    except:
        mc.select(cl=True)
        for each in sel:
            try:
                mc.select(each, add=True)
            except:
                pass

    newSel = mc.ls(sl=True)
    if newSel:
        ann = ', '.join(newSel)
        if len(ann) > 100:
            ann = ann[:100] + '......'
        mc.button(box, e=True, ann=ann, c="%s.selectSelBox(%s,'%s')" % (__name__, newSel, box))
        pf_68()
    else:
        pf_71('%s not exists!' % mc.button(box, q=True, ann=True))
        delSelBox(box)


def quickSelBox_popupMenu(box, sel):
    mc.popupMenu(p=box)
    mc.menuItem(l='Add to', c="%s.updateSelBox('add','%s')" % (__name__, box))
    mc.menuItem(l='Remove from', c="%s.updateSelBox('deselect','%s')" % (__name__, box))
    mc.menuItem(l='Update', c="%s.updateSelBox('replace','%s')" % (__name__, box))
    mc.menuItem(d=True)
    mc.menuItem(l='Rename', c="%s.renameSelBox('%s')" % (__name__, box))
    mc.menuItem(l='Delete', c="%s.delSelBox('%s')" % (__name__, box))
    mc.menuItem(l='Delete Others', c="%s.delOtherSelBox('%s')" % (__name__, box))


def delOtherSelBox(box):
    mc.select( cl=True )
    allBoxes = mc.columnLayout('mainCL_quickSel', q=True, childArray=True)
    if len(allBoxes) >= 2:
        for eachBox in allBoxes:
            if eachBox.split('|')[-1] != box.split('|')[-1]:
                mc.deleteUI(eachBox)


def delSelBox(box):
    mc.select( cl=True )
    mc.deleteUI(box)


def renameSelBox(box):
    contents = mc.button(box, q=True, ann=True).split(', ')
    oldName = contents[0] if len(contents) == 1 and mc.objExists(contents[0]) else mc.button(box, q=True, l=True)
    if mc.promptDialog(m='Enter new name:', tx=oldName, b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel') == 'OK':
        tx = mc.promptDialog(q=True, tx=True).strip()
        if tx:
            newName = tx
            if len(newName) > 18:
                newName = newName[:13] + '......'
            mc.button(box, e=True, l=newName, w=120)


def updateSelBox(mode, box):
    sel = mc.ls(sl=True)
    if sel:
        command = mc.button(box, q=True, c=True).replace('%s.' % __name__, '')
        eval(command)
        eval('mc.select(%s,%s=True)' % (sel, mode))
        newSel = mc.ls(sl=True)
        ann = ', '.join(newSel)
        if len(ann) > 100:
            ann = ann[:100] + '......'
        mc.button(box, e=True, ann=ann, c="%s.selectSelBox(%s,'%s')" % (__name__, newSel, box))
        pf_68()
    else:
        pf_71('Nothing selected!')


def pf_74(node, attr):
    import maya.cmds as mc
    attrs = mc.listAttr(node)
    if attrs == None:
        return False
    elif attr in attrs:
        return True
    else:
        return False


def pf_75(nameString):
    import maya.cmds as mc
    import re
    m = re.match('(\\w+?)(\\d+\\b)', nameString)
    if m:
        nameString = m.group(1)
    num = 1
    while mc.objExists('%s%d' % (nameString, num)):
        num += 1

    return '%s%d' % (nameString, num)


def pf_73(ui):
    import maya.cmds as mc
    if ui in mc.lsUI(p=True, ed=True, wnd=True, ctl=True, cl=True, col=True, rmc=True, m=True, mi=True, ctx=True, ct=True):
        return True
    else:
        return False


def pf_70(message = 'Done!'):
    import maya.mel as mm
    mm.eval('print("%s\\n")' % message)


def pf_71(warningString = 'warningString'):
    import maya.mel as mm
    try:
        mm.eval('warning "%s"' % warningString)
    except:
        pass


def pf_72(errorString = 'errorString'):
    import maya.mel as mm
    try:
        mm.eval('error "%s"' % errorString)
    except:
        pass


class pf_69(object):

    def __init__(self, *nums):
        if len(nums) == 1 and isinstance(nums[0], (list, tuple)) and len(nums[0]) == 3 and all((isinstance(i, (float, int)) for i in nums[0])):
            self.x = nums[0][0]
            self.y = nums[0][1]
            self.z = nums[0][2]
        elif len(nums) == 3 and all((isinstance(i, (float, int)) for i in nums)):
            self.x = nums[0]
            self.y = nums[1]
            self.z = nums[2]
        elif len(nums) == 0:
            self.x = 0
            self.y = 0
            self.z = 0         

    def __str__(self):
        return '<<%s,%s,%s>>' % (self.x, self.y, self.z)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, (tuple, list)) and len(other) == 3 and all((isinstance(i, (int, float)) for i in other)):
            return self.__class__(self.x + other[0], self.y + other[1], self.z + other[2])
        raise TypeError('Illegal argument type!')

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        if isinstance(other, (tuple, list)) and len(other) == 3 and all((isinstance(i, (int, float)) for i in other)):
            self.x += other[0]
            self.y += other[1]
            self.z += other[2]
            return self
        raise TypeError('Illegal argument type!')

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, (tuple, list)) and len(other) == 3 and all((isinstance(i, (int, float)) for i in other)):
            return self.__class__(self.x - other[0], self.y - other[1], self.z - other[2])
        raise TypeError('Illegal argument type!')

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        if isinstance(other, (tuple, list)) and len(other) == 3 and all((isinstance(i, (int, float)) for i in other)):
            self.x -= other[0]
            self.y -= other[1]
            self.z -= other[2]
            return self
        raise TypeError('Illegal argument type!')

    __rsub__ = __sub__

    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return self.__class__(self.x * num, self.y * num, self.z * num)
        raise TypeError('Illegal argument type!')

    def __imul__(self, num):
        if isinstance(num, (int, float)):
            self.x *= num
            self.y *= num3
            self.z *= num
            return self
        raise TypeError('Illegal argument type!')

    __rmul__ = __mul__

    def __div__(self, num):
        if isinstance(num, (int, float)):
            return self.__class__(self.x / float(num), self.y / float(num), self.z// float(num))
        raise TypeError('Illegal argument type!')
    
    # Added for python 3    
    def __truediv__(self, num):
        if isinstance(num, pf_69):
            self.x / num
            self.y / num
            self.z / num
            return self
        elif isinstance(num, int):
            self.x / num
            self.y / num
            self.z / num
            return self
        else:
            raise TypeError("Unsupported operand type for division.")
    

    def __idiv__(self, num):
        if isinstance(num, (int, float)):
            self.x /= float(num)
            self.y /= float(num)
            self.z /= float(num)
            return self
        raise TypeError('Illegal argument type!')

    def __nonzero__(self):
        return self.x or self.y or self.z

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __neg__(self):
        return self * -1

    def module(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def distance(self, *nums):
        if len(nums) == 1 and isinstance(nums[0], (list, tuple)) and len(nums[0]) == 3 and all((isinstance(i, (int, float)) for i in nums[0])):
            return ((self.x - nums[0][0]) ** 2 + (self.y - nums[0][2]) ** 2 + (self.z - nums[0][2]) ** 2) ** 0.5
        if len(nums) == 1 and isinstance(nums[0], self.__class__):
            return ((self.x - nums[0].x) ** 2 + (self.y - nums[0].y) ** 2 + (self.z - nums[0].z) ** 2) ** 0.5
        if len(nums) == 3 and all((isinstance(i, (int, float)) for i in nums)):
            return ((self.x - nums[0]) ** 2 + (self.y - nums[1]) ** 2 + (self.z - nums[2]) ** 2) ** 0.5
        raise TypeError('Illegal argument type!')

    def toList(self):
        return [self.x, self.y, self.z]

    def toTuple(self):
        return (self.x, self.y, self.z)

    def normalize(self):
        m = self.module()
        self.x /= m
        self.y /= m
        self.z /= m
        return self

    @staticmethod
    def center(*vectors):
        if vectors:
            sum = (0, 0, 0)            
            for i in vectors:
                sum += i                                    
            return sum / len(vectors)

    @staticmethod
    def vectorList(seq = []):
        if seq and len(seq) % 3 == 0:
            return [ pf_69(seq[i:i + 3]) for i in range(0, len(seq), 3) ]


def pf_09(faces, num = False):
    allEdges = mc.filterExpand(mc.polyListComponentConversion(faces, ff=True, te=True), sm=32)
    outlineEdges = mc.polyListComponentConversion(faces, ff=True, te=True, border=True)
    if outlineEdges:
        outlineEdges = mc.filterExpand(outlineEdges, sm=32)
    borderEdges = [ edge for edge in allEdges if pf_07(edge) ]
    outlineEdges += borderEdges
    if num:
        return len(outlineEdges)
    else:
        return outlineEdges


def pf_63(faces):
    return mc.filterExpand(mc.polyListComponentConversion(pf_09(faces), fe=True, tv=True), sm=31)


def pf_64(faces):
    edges = mc.polyListComponentConversion(faces, ff=True, te=True, internal=True)
    if edges:
        edges = mc.filterExpand(edges, sm=32)
        interEdges = [ edge for edge in edges if not pf_07(edge) ]
        return interEdges


def pf_65(faces):
    vtxs = mc.polyListComponentConversion(faces, ff=True, tv=True, internal=True)
    if vtxs:
        vtxs = mc.filterExpand(vtxs, sm=31)
        interVtxs = [ vtx for vtx in vtxs if not pf_08(vtx) ]
        return interVtxs


def pf_66(edges):
    vtxs = mc.polyListComponentConversion(edges, fe=True, tv=True, internal=True)
    if vtxs:
        interVtxs = [ vtx for vtx in mc.filterExpand(vtxs, sm=31) if not pf_08(vtx) ]
        return interVtxs


def pf_67(vtxs):
    edges = mc.polyListComponentConversion(vtxs, fv=True, te=True, internal=True)
    if edges:
        return edges


def pf_01(loopFaces):
    mesh = pf_29()
    f2eInfos = mc.polyInfo(loopFaces, fe=True)
    edgeIds = []
    for info in f2eInfos:
        edgeIds.extend(re.findall('\\d+', info)[1:])

    for edgeId in edgeIds:
        if edgeIds.count(edgeId) == 2:
            edgeRingIds = mc.polySelect(er=int(edgeId))
            break

    edgeRings = [ pf_33(mesh, 'edge', index) for index in edgeRingIds ]
    sortedFaces = []
    for i in range(len(edgeRings) - 1):
        e2v = mc.polyListComponentConversion(edgeRings[i], edgeRings[i + 1], fe=True, tv=True)
        v2f = mc.polyListComponentConversion(e2v, fv=True, tf=True, internal=True)
        sortedFaces.extend(v2f)

    mc.select(cl=True)
    if edgeRingIds[0] == edgeRingIds[-1]:
        return ('close', sortedFaces)
    else:
        return ('open', sortedFaces)


def pf_02(faces):
    outlineEdges = pf_09(faces)
    continua = pf_17(outlineEdges, returnMode='comps')
    if continua:
        return continua[1]


def pf_03(selEdges, mesh = None, returnMode = 'vtx', breakVtxs = None):
    if breakVtxs:
        breakVtxs = [ pf_32(vtx) for vtx in breakVtxs ]
    if selEdges and len(selEdges) > 1:
        if not mesh:
            mesh = pf_29()
        e2vInfos = mc.polyInfo(selEdges, ev=True)
        e2vDict = {}
        for info in e2vInfos:
            evList = [ int(i) for i in re.findall('\\d+', info) ]
            e2vDict.update(dict([(evList[0], evList[1:])]))

        openEdgesGrps = []
        closeEdgesGrps = []
        openVtxsGrps = []
        closeVtxsGrps = []
        while True:
            try:
                startEdge, startVtxs = e2vDict.popitem()
            except:
                break

            edgesGrp = [startEdge]
            vtxsGrp = []
            num = 0
            for vtx in startVtxs:
                curVtx = vtx
                while True:
                    if num == 0:
                        vtxsGrp.append(curVtx)
                    else:
                        vtxsGrp.insert(0, curVtx)
                    if breakVtxs and curVtx in breakVtxs:
                        break
                    nextEdges = []
                    for k in e2vDict:
                        if curVtx in e2vDict[k]:
                            nextEdges.append(k)

                    if nextEdges:
                        if len(nextEdges) == 1:
                            if num == 0:
                                edgesGrp.append(nextEdges[0])
                            else:
                                edgesGrp.insert(0, nextEdges[0])
                            nextVtxs = e2vDict[nextEdges[0]]
                            curVtx = [ vtx for vtx in nextVtxs if vtx != curVtx ][0]
                            e2vDict.pop(nextEdges[0])
                        else:
                            return False
                    else:
                        break

                num += 1

            if len(vtxsGrp) >= 3:
                edgesGrp = [ pf_33(mesh, 'edge', num) for num in edgesGrp ]
                vtxsGrp = [ pf_33(mesh, 'vtx', num) for num in vtxsGrp ]
                if vtxsGrp[0] == vtxsGrp[-1]:
                    closeEdgesGrps.append(edgesGrp)
                    closeVtxsGrps.append(vtxsGrp[:-1])
                else:
                    openEdgesGrps.append(edgesGrp)
                    openVtxsGrps.append(vtxsGrp)

        if returnMode == 'vtx':
            return (openVtxsGrps, closeVtxsGrps)
        if returnMode == 'edge':
            return (openEdgesGrps, closeEdgesGrps)
        if returnMode == 'vtx_edge':
            return (openVtxsGrps,
             closeVtxsGrps,
             openEdgesGrps,
             closeEdgesGrps)


def pf_04(centerVtx):
    v2einfo = mc.polyInfo(centerVtx, ve=True)[0]
    sortedEdgeIds = re.findall('\\d+', v2einfo)[1:]
    mesh = pf_29()
    sortedEdges = [ pf_33(mesh, 'edge', num) for num in sortedEdgeIds ]
    return sortedEdges


def pf_05(faceLoop, selMode = 'facet'):
    vtxs = mc.filterExpand(mc.polyListComponentConversion(faceLoop, ff=True, tv=True), sm=31)
    interEdges = pf_64(faceLoop)
    mesh = pf_29()
    ringIds = mc.polySelect(er=pf_32(interEdges[0]))[:-1]
    ringEdges = [ pf_33(mesh, 'edge', index) for index in ringIds ]
    firstVtx_A = vtxs[0]
    firstEdge = [ edge for edge in mc.filterExpand(mc.polyListComponentConversion(firstVtx_A, fv=True, te=True), sm=32) if edge in ringEdges ][0]
    firstVtx_B = [ vtx for vtx in mc.filterExpand(mc.polyListComponentConversion(firstEdge, fe=True, tv=True), sm=31) if vtx != firstVtx_A ][0]
    SortedVtxs_A = [firstVtx_A]
    SortedVtxs_B = [firstVtx_B]
    firstEdgeId = ringEdges.index(firstEdge)
    ringEdges = ringEdges[firstEdgeId:] + ringEdges[:firstEdgeId]
    for edge in ringEdges[1:]:
        e2v = mc.filterExpand(mc.polyListComponentConversion(edge, fe=True, tv=True), sm=31)
        for vtx in e2v:
            v2e = mc.polyListComponentConversion(vtx, SortedVtxs_A[-1], fv=True, te=True, internal=True)
            if v2e:
                SortedVtxs_A.append(vtx)
                SortedVtxs_B.extend([ vtx for vtx in e2v if vtx != SortedVtxs_A[-1] ])
                break

    if selMode == 'facet':
        mc.select(faceLoop)
    elif selMode == 'edge':
        mc.select(interEdges)
    return (SortedVtxs_A, SortedVtxs_B)


def pf_07(edge):
    e2fInfo = mc.polyInfo(edge, ef=True)[0]
    if len(re.findall('\\d+', e2fInfo)) == 2:
        return True
    else:
        return False


def pf_08(vtx):
    edges = mc.filterExpand(mc.polyListComponentConversion(vtx, fv=True, te=True), sm=32)
    for edge in edges:
        if pf_07(edge):
            return True


def pf_10(edges):
    if edges:
        e2fInfos = mc.polyInfo(edges, ef=True)
        for info in e2fInfos:
            if len(re.findall('\\d+', info)) == 2:
                return False

        return True


def pf_11(selFaces):
    if len(selFaces) >= 2 and pf_20(selFaces) and pf_18(selFaces):
        interEdges = pf_64(selFaces)
        centerVtxs = pf_65(selFaces)
        if interEdges and centerVtxs and len(centerVtxs) == 1:
            v2e = mc.filterExpand(mc.polyListComponentConversion(centerVtxs, fv=True, te=True), sm=32)
            if len(interEdges) == len(selFaces) == len(v2e):
                return True


def pf_12(selFaces):
    if len(selFaces) >= 2 and pf_20(selFaces) and pf_18(selFaces):
        interEdges = pf_64(selFaces)
        if interEdges and len(interEdges) == len(selFaces) - 1:
            edgeVtxs = mc.filterExpand(mc.polyListComponentConversion(interEdges, fe=True, tv=True), sm=31)
            if len(edgeVtxs) == len(interEdges) * 2:
                return True


def pf_13(selFaces):
    if len(selFaces) == 4 and pf_20(selFaces) and pf_18(selFaces):
        outlineEdgesNum = pf_09(selFaces, num=True)
        if outlineEdgesNum == 6:
            interEdges = pf_64(selFaces)
            if interEdges and len(interEdges) == 5:
                interVtxs = pf_65(selFaces)
                if interVtxs and len(interVtxs) == 2:
                    return True


gridDict1 = {10: ['2x3'],
 12: ['2x4', '3x3'],
 14: ['2x5', '3x4'],
 16: ['2x6', '3x5', '4x4'],
 18: ['2x7', '3x6', '4x5'],
 20: ['2x8',
      '3x7',
      '4x6',
      '5x5'],
 22: ['2x9',
      '3x8',
      '4x7',
      '5x6'],
 24: ['2x10',
      '3x9',
      '4x8',
      '5x7',
      '6x6'],
 26: ['2x11',
      '3x10',
      '4x9',
      '5x8',
      '6x7'],
 28: ['2x12',
      '3x11',
      '4x10',
      '5x9',
      '6x8',
      '7x7'],
 30: ['2x13',
      '3x12',
      '4x11',
      '5x10',
      '6x9',
      '7x8'],
 32: ['2x14',
      '3x13',
      '4x12',
      '5x11',
      '6x10',
      '7x9',
      '8x8'],
 34: ['2x15',
      '3x14',
      '4x13',
      '5x12',
      '6x11',
      '7x10',
      '8x9'],
 36: ['2x16',
      '3x15',
      '4x14',
      '5x13',
      '6x12',
      '7x11',
      '8x10',
      '9x9'],
 38: ['2x17',
      '3x16',
      '4x15',
      '5x14',
      '6x13',
      '7x12',
      '8x11',
      '9x10'],
 40: ['2x18',
      '3x17',
      '4x16',
      '5x15',
      '6x14',
      '7x13',
      '8x12',
      '9x11',
      '10x10']}
gridDict2 = {'[10,6,7,2]': '2x3',
 '[12,8,10,3]': '2x4',
 '[14,10,13,4]': '2x5',
 '[16,12,16,5]': '2x6',
 '[18,14,19,6]': '2x7',
 '[20,16,22,7]': '2x8',
 '[22,18,25,8]': '2x9',
 '[24,20,28,9]': '2x10',
 '[26,22,31,10]': '2x11',
 '[28,24,34,11]': '2x12',
 '[30,26,37,12]': '2x13',
 '[32,28,40,13]': '2x14',
 '[34,30,43,14]': '2x15',
 '[36,32,46,15]': '2x16',
 '[38,34,49,16]': '2x17',
 '[40,36,52,17]': '2x18',
 '[12,9,12,4]': '3x3',
 '[14,12,17,6]': '3x4',
 '[16,15,22,8]': '3x5',
 '[18,18,27,10]': '3x6',
 '[20,21,32,12]': '3x7',
 '[22,24,37,14]': '3x8',
 '[24,27,42,16]': '3x9',
 '[26,30,47,18]': '3x10',
 '[28,33,52,20]': '3x11',
 '[30,36,57,22]': '3x12',
 '[32,39,62,24]': '3x13',
 '[34,42,67,26]': '3x14',
 '[36,45,72,28]': '3x15',
 '[38,48,77,30]': '3x16',
 '[40,51,82,32]': '3x17',
 '[16,16,24,9]': '4x4',
 '[18,20,31,12]': '4x5',
 '[20,24,38,15]': '4x6',
 '[22,28,45,18]': '4x7',
 '[24,32,52,21]': '4x8',
 '[26,36,59,24]': '4x9',
 '[28,40,66,27]': '4x10',
 '[30,44,73,30]': '4x11',
 '[32,48,80,33]': '4x12',
 '[34,52,87,36]': '4x13',
 '[36,56,94,39]': '4x14',
 '[38,60,101,42]': '4x15',
 '[40,64,108,45]': '4x16',
 '[20,25,40,16]': '5x5',
 '[22,30,49,20]': '5x6',
 '[24,35,58,24]': '5x7',
 '[26,40,67,28]': '5x8',
 '[28,45,76,32]': '5x9',
 '[30,50,85,36]': '5x10',
 '[32,55,94,40]': '5x11',
 '[34,60,103,44]': '5x12',
 '[36,65,112,48]': '5x13',
 '[38,70,121,52]': '5x14',
 '[40,75,130,56]': '5x15',
 '[24,36,60,25]': '6x6',
 '[26,42,71,30]': '6x7',
 '[28,48,82,35]': '6x8',
 '[30,54,93,40]': '6x9',
 '[32,60,104,45]': '6x10',
 '[34,66,115,50]': '6x11',
 '[36,72,126,55]': '6x12',
 '[38,78,137,60]': '6x13',
 '[40,84,148,65]': '6x14',
 '[28,49,84,36]': '7x7',
 '[30,56,97,42]': '7x8',
 '[32,63,110,48]': '7x9',
 '[34,70,123,54]': '7x10',
 '[36,77,136,60]': '7x11',
 '[38,84,149,66]': '7x12',
 '[40,91,162,72]': '7x13',
 '[32,64,112,49]': '8x8',
 '[34,72,127,56]': '8x9',
 '[36,80,142,63]': '8x10',
 '[38,88,157,70]': '8x11',
 '[40,96,172,77]': '8x12',
 '[36,81,144,64]': '9x9',
 '[38,90,161,72]': '9x10',
 '[40,99,178,80]': '9x11',
 '[40,100,180,81]': '10x10'}

def pf_14(selFaces):
    if len(selFaces) >= 6 and pf_20(selFaces) and pf_18(selFaces):
        outlineVtxs = pf_63(selFaces)
        outlineVtxs2facesNumGroup = []
        for vtx in outlineVtxs:
            v2fNum = len([ face for face in mc.filterExpand(mc.polyListComponentConversion(vtx, fv=True, tf=True), sm=34) if face in selFaces ])
            outlineVtxs2facesNumGroup.append(v2fNum)

        if outlineVtxs2facesNumGroup.count(1) == 4 and not any([ num > 2 for num in outlineVtxs2facesNumGroup ]):
            interEdges = pf_64(selFaces)
            outlineEdges = pf_09(selFaces)
            interVtxs = pf_65(selFaces)
            if interEdges and interVtxs and pf_21(interVtxs):
                pat = repr([len(outlineEdges),
                 len(selFaces),
                 len(interEdges),
                 len(interVtxs)]).replace(' ', '')
                if pat in gridDict2:
                    return gridDict2[pat]                

def pf_15(faces, selMode = 'facet'):
    interEdges = pf_64(faces)
    selComps = pf_06()[0]
    if interEdges:
        ring = pf_16(interEdges)
        if selMode == 'facet':
            mc.select(faces)
        elif selMode == 'edge':
            mc.select(interEdges)
        if ring:
            return True
        mc.select(selComps)


def pf_16(edges):
    if len(edges) >= 3:
        edgesIds = sorted([ pf_32(edge) for edge in edges ])
        ringIds = sorted(mc.polySelect(er=pf_32(edges[0]))[:-1])
        if edgesIds == ringIds:
            return True


def pf_17(edges, returnMode = 'checkOnly'):
    if edges:
        mesh = pf_29()
        e2vInfos = mc.polyInfo(edges, ev=True)
        idGroups = []
        vtxIds = []
        for info in e2vInfos:
            ids = re.findall('\\d+', info)
            e2vIds = ids[1:]
            idGroups.append(ids)
            vtxIds.extend(e2vIds)

        vtxIdCounts = [ vtxIds.count(vtxId) for vtxId in vtxIds ]
        if all([ count == 2 for count in vtxIdCounts ]):
            curIdGroup = idGroups[0]
            curVtxId = curIdGroup[1]
            sortedVtxIds = []
            sortedEdgeIds = []
            while curIdGroup:
                idGroups.remove(curIdGroup)
                sortedVtxIds.append(curVtxId)
                sortedEdgeIds.append(curIdGroup[0])
                nextVtxId = [ vtxId for vtxId in curIdGroup[1:] if vtxId != curVtxId ][0]
                connectIdGroups = [ group for group in idGroups if nextVtxId in group[1:] ]
                if connectIdGroups:
                    curIdGroup = connectIdGroups[0]
                    curVtxId = nextVtxId
                else:
                    break

            if not idGroups:
                if returnMode == 'checkOnly':
                    return 'close'
                if returnMode == 'ids':
                    return ('close', sortedVtxIds, sortedEdgeIds)
                if returnMode == 'comps':
                    return ('close', [ pf_33(mesh, 'vtx', num) for num in sortedVtxIds ], [ pf_33(mesh, 'edge', num) for num in sortedEdgeIds ])
                if returnMode == 'ids_comps':
                    return ('close',
                     sortedVtxIds,
                     sortedEdgeIds,
                     [ pf_33(mesh, 'vtx', num) for num in sortedVtxIds ],
                     [ pf_33(mesh, 'edge', num) for num in sortedEdgeIds ])
            else:
                return False
        elif vtxIdCounts.count(1) == 2 and vtxIdCounts.count(2) == len(vtxIdCounts) - 2:
            curVtxId = vtxIds[vtxIdCounts.index(1)]
            curIdGroup = [ group for group in idGroups if curVtxId in group[1:] ][0]
            sortedVtxIds = [curVtxId]
            sortedEdgeIds = []
            while curIdGroup:
                idGroups.remove(curIdGroup)
                sortedEdgeIds.append(curIdGroup[0])
                nextVtxId = [ vtxId for vtxId in curIdGroup[1:] if vtxId != curVtxId ][0]
                sortedVtxIds.append(nextVtxId)
                curVtxId = nextVtxId
                connectIdGroups = [ group for group in idGroups if nextVtxId in group[1:] ]
                if connectIdGroups:
                    curIdGroup = connectIdGroups[0]
                else:
                    break

            if not idGroups:
                if returnMode == 'checkOnly':
                    return 'open'
                if returnMode == 'ids':
                    return ('open', sortedVtxIds, sortedEdgeIds)
                if returnMode == 'comps':
                    return ('open', [ pf_33(mesh, 'vtx', num) for num in sortedVtxIds ], [ pf_33(mesh, 'edge', num) for num in sortedEdgeIds ])
                if returnMode == 'ids_comps':
                    return ('open',
                     sortedVtxIds,
                     sortedEdgeIds,
                     [ pf_33(mesh, 'vtx', num) for num in sortedVtxIds ],
                     [ pf_33(mesh, 'edge', num) for num in sortedEdgeIds ])
            else:
                return False
        else:
            return False


def pf_18(faces, detailMode = False):
    if faces:
        allFacesSet = set(faces)
        curFacesSet = set([faces[0]])
        while curFacesSet:
            allFacesSet -= curFacesSet
            toFacesSet = set(mc.filterExpand(mc.polyListComponentConversion(mc.polyListComponentConversion(list(curFacesSet), ff=True, te=True), fe=True, tf=True), sm=34))
            curFacesSet = allFacesSet & toFacesSet
            allFacesSet -= toFacesSet

        if not allFacesSet:
            if not detailMode:
                return True
            outlineEdges = pf_09(faces)
            if not outlineEdges:
                return 'close mesh'
            grps = pf_03(outlineEdges, returnMode='edge')
            if grps:
                return '%d hole' % (len(grps[1]) - 1)
            else:
                return False
        else:
            return False


def pf_19(face):
    f2eInfo = mc.polyInfo(face, fe=True)[0]
    if len(re.findall('\\d+', f2eInfo)) == 5:
        return True


def pf_20(faces):
    if faces:
        f2eInfos = iter(mc.polyInfo(faces, fe=True))
        for info in f2eInfos:
            if len(re.findall('\\d+', info)) != 5:
                return False

        return True


def pf_21(vtxs):
    if vtxs:
        v2eInfos = iter(mc.polyInfo(vtxs, ve=True))
        for info in v2eInfos:
            if len(re.findall('\\d+', info)) != 5:
                return False

        return True


def pf_22():
    pass


def pf_23(mesh):
    openEdgeIds = []
    edgeNum = mc.polyEvaluate(mesh, e=True)
    infos = iter(mc.polyInfo('%s.e[0:%s]' % (mesh, edgeNum - 1), ef=True))
    for info in infos:
        nums = re.findall('\\d+', info)
        if len(nums) == 2:
            openEdgeIds.append(nums[0])

    if openEdgeIds:
        return [ '%s.e[%s]' % (mesh, edgeId) for edgeId in openEdgeIds ]


def pf_24(vtx_A, vtx_B):
    mc.polyConnectComponents(vtx_A, vtx_B)
    delMeshHistory()
    toEdge = mc.polyListComponentConversion(vtx_A, vtx_B, fv=True, te=True, internal=True)
    return toEdge[0]


def pf_25(vtx, edge):
    edge_vtxs = mc.filterExpand(mc.polyListComponentConversion(edge, fe=True, tv=True), sm=31)
    mc.polyConnectComponents(vtx, edge)
    delMeshHistory()
    newEdge_vtxs = mc.filterExpand(mc.polyListComponentConversion(edge, fe=True, tv=True), sm=31)
    newVtx = [ _vtx for _vtx in newEdge_vtxs if _vtx not in edge_vtxs ][0]
    newEdge = mc.filterExpand(mc.polyListComponentConversion(vtx, newVtx, fv=True, te=True, internal=True), sm=32)[0]
    return (newVtx, newEdge)


def pf_26(edge_A, edge_B):
    edge_A_vtxs = mc.filterExpand(mc.polyListComponentConversion(edge_A, fe=True, tv=True), sm=31)
    edge_B_vtxs = mc.filterExpand(mc.polyListComponentConversion(edge_B, fe=True, tv=True), sm=31)
    mc.polyConnectComponents(edge_A, edge_B)
    delMeshHistory()
    new_edge_A_vtxs = mc.filterExpand(mc.polyListComponentConversion(edge_A, fe=True, tv=True), sm=31)
    new_edge_B_vtxs = mc.filterExpand(mc.polyListComponentConversion(edge_B, fe=True, tv=True), sm=31)
    new_Vtx_A = [ _vtx for _vtx in new_edge_A_vtxs if _vtx not in edge_A_vtxs ][0]
    new_Vtx_B = [ _vtx for _vtx in new_edge_B_vtxs if _vtx not in edge_B_vtxs ][0]
    new_Edge = mc.polyListComponentConversion(new_Vtx_A, new_Vtx_B, fv=True, te=True, internal=True)[0]
    return (new_Vtx_A, new_Vtx_B, new_Edge)


def delMeshHistory():
    meshs = pf_30()
    if meshs:
        mc.delete(meshs, ch=True)


def pf_28(curve, outPoint, step = 3):
    outPointPos = pf_69(mc.xform(outPoint, q=True, ws=True, t=True))
    nearestPos = pf_69(mc.pointOnCurve(curve, top=True, pr=0.0))
    minDist = outPointPos.distance(nearestPos)
    precision = 0.1
    count = 0
    curCurvePos = 0
    num = 0
    for j in range(step):
        begin = -10 if curCurvePos > 0 else 0
        for i in range(begin, 11):
            count += 1
            pos = pf_69(mc.pointOnCurve(curve, top=True, pr=curCurvePos + precision * i))
            dist = outPointPos.distance(pos)
            if dist < minDist:
                minDist = dist
                nearestPos = pos
                num = curCurvePos + precision * i

        curCurvePos = num
        precision *= 0.1

    return nearestPos.toTuple()


def pf_29():
    sel = mc.ls(sl=True) + mc.ls(hl=True)
    mesh = None
    if sel:
        if mc.nodeType(sel[-1]) == 'transform':
            if mc.nodeType(mc.listRelatives(sel[-1], c=True)[0]) == 'mesh':
                mesh = sel[-1]
        elif mc.nodeType(sel[-1]) == 'mesh':
            if '.' in sel[-1]:
                mesh = sel[-1].split('.')[0]
            else:
                mesh = mc.listRelatives(sel[-1], p=True, type='transform')[0]
    return mesh


def pf_30():
    meshs = []
    sel = mc.ls(sl=True) + mc.ls(hl=True)
    if sel:
        for each in sel:
            if mc.nodeType(each) == 'transform':
                if mc.nodeType(mc.listRelatives(each, c=True)[0]) == 'mesh' and each not in meshs:
                    meshs.append(each)
            elif mc.nodeType(each) == 'mesh':
                if '.' in each:
                    mesh = each.split('.')[0]
                    if mesh not in meshs:
                        meshs.append(mesh)
                else:
                    mesh = mc.listRelatives(each, p=True, type='transform')[0]
                    if mesh not in meshs:
                        meshs.append(mesh)

    return meshs


def pf_31():
    mesh = pf_29()
    if mesh:
        shapes = mc.listRelatives(mesh, s=True)
        if shapes:
            meshShapes = [ i for i in shapes if mc.nodeType(i) == 'mesh' ]
            if meshShapes:
                meshShape = meshShapes[0]
                return meshShape


def pf_32(compName):
    return int(compName.split('[')[1].split(']')[0])


def pf_33(mesh, mode, num):
    modeDict = {'face': 'f',
     'edge': 'e',
     'vtx': 'vtx'}
    return '%s.%s[%s]' % (mesh, modeDict[mode], num)


def pf_06(returnMode = 'vtx', expand = True):
    selVtxs = mc.filterExpand(sm=31, expand=expand)
    selUVs = mc.filterExpand(sm=35, expand=expand)
    selEdges = mc.filterExpand(sm=32, expand=expand)
    selFaces = mc.filterExpand(sm=34, expand=expand)
    numList = [ bool(sel) for sel in (selVtxs,
     selUVs,
     selEdges,
     selFaces) ]
    if sum(numList) == 0:
        return False
    if sum(numList) > 1:
        selMode = 'meshComponents'
    elif sum(numList) == 1:
        if selVtxs:
            selMode = 'vertex'
        elif selUVs:
            selMode = 'puv'
        elif selEdges:
            selMode = 'edge'
        else:
            selMode = 'facet'
    if returnMode == 'selModeOnly':
        return selMode
    comps = []
    if selVtxs:
        comps += selVtxs
    if selUVs:
        comps += selUVs
    if selEdges:
        comps += selEdges
    if selFaces:
        comps += selFaces
    if returnMode == 'vtx':
        vtxs = []
        if selVtxs:
            vtxs += selVtxs
        if selUVs:
            vtxs += mc.filterExpand(mc.polyListComponentConversion(selUVs, fuv=True, tv=True), sm=31)
        if selEdges:
            vtxs += mc.filterExpand(mc.polyListComponentConversion(selEdges, fe=True, tv=True), sm=31)
        if selFaces:
            vtxs += mc.filterExpand(mc.polyListComponentConversion(selFaces, ff=True, tv=True), sm=31)
        return (comps, vtxs, selMode)
    if returnMode == 'puv':
        uvs = []
        if selUVs:
            uvs += selUVs
        if selVtxs:
            uvs += mc.filterExpand(mc.polyListComponentConversion(selVtxs, fv=True, tuv=True), sm=35)
        if selEdges:
            uvs += mc.filterExpand(mc.polyListComponentConversion(selEdges, fe=True, tuv=True), sm=35)
        if selFaces:
            uvs += mc.filterExpand(mc.polyListComponentConversion(selFaces, ff=True, tuv=True), sm=35)
        return (comps, uvs, selMode)
    if returnMode == 'edge':
        edges = []
        if selVtxs:
            edges += mc.filterExpand(mc.polyListComponentConversion(selVtxs, fv=True, te=True), sm=32)
        if selUVs:
            edges += mc.filterExpand(mc.polyListComponentConversion(selUVs, fuv=True, te=True), sm=32)
        if selEdges:
            edges += selEdges
        if selFaces:
            edges += mc.filterExpand(mc.polyListComponentConversion(selFaces, ff=True, te=True), sm=32)
        return (comps, edges, selMode)
    if returnMode == 'face':
        faces = []
        if selVtxs:
            faces += mc.filterExpand(mc.polyListComponentConversion(selVtxs, fv=True, tf=True), sm=34)
        if selUVs:
            faces += mc.filterExpand(mc.polyListComponentConversion(selUVs, fuv=True, tf=True), sm=34)
        if selEdges:
            faces += mc.filterExpand(mc.polyListComponentConversion(selEdges, fe=True, tf=True), sm=34)
        if selFaces:
            faces += selFaces
        return (comps, faces, selMode)


mirrorAttrs = ['mirrorMode', 'centerLine', 'threshold']
mirrorDefaultVals = ['mirror', True, 0.001]

def pf_34(mesh, attrVals = None):
    if not pf_74(mesh, 'mirrorMode'):
        mc.addAttr(mesh, ln='mirrorMode', dt='string', h=True)
        mc.addAttr(mesh, ln='centerLine', at='enum', en='False:True:', h=True)
        mc.addAttr(mesh, ln='threshold', at='float', h=True)
    if not attrVals:
        attrVals = mirrorDefaultVals
    mc.setAttr(mesh + '.mirrorMode', attrVals[0], type='string')
    mc.setAttr(mesh + '.centerLine', attrVals[1])
    mc.setAttr(mesh + '.threshold', attrVals[2])


def pf_68():
    hil = mc.ls(hl=True)
    if not hil:
        mesh = pf_29()
        selMode = pf_06('selModeOnly')
        if mesh and selMode:
            mc.undoInfo(swf=False)
            mm.eval('doMenuComponentSelection("%s", "%s")' % (mesh, selMode))
            mc.undoInfo(swf=True)


def pf_35():
    try:
        mc.undo()
        pf_68()
    except RuntimeError:
        pf_70('There are no more commands to undo.')


def pf_36():
    try:
        mc.redo()
        pf_68()
    except RuntimeError:
        pf_70('There are no more commands to redo.')


def pf_37(selFaces):
    facesNormals = []
    for face in selFaces:
        toVf = mc.polyListComponentConversion(face, ff=True, tvf=True)
        normals = pf_69.vectorList(mc.polyNormalPerVertex(toVf, q=True, xyz=True))
        faceNormal = pf_69.center(*normals)
        facesNormals.append(faceNormal)

    return pf_69.center(*facesNormals)


def pf_38():
    selFaces = mc.filterExpand(sm=34)
    if selFaces:
        facesNormals = []
        facesCenterPoses = []
        for face in selFaces:
            toV = mc.polyListComponentConversion(face, ff=True, tv=True)
            normals = pf_69.vectorList(mc.polyNormalPerVertex(toV, q=True, xyz=True))
            faceNormal = pf_69.center(*normals)
            facesNormals.append(faceNormal)
            vtxsPos = pf_69.vectorList(mc.xform(face, q=True, ws=True, t=True))
            faceCenterPos = pf_69.center(*vtxsPos)
            facesCenterPoses.append(faceCenterPos)
            temCurve = mc.curve(p=[(0, 0, 0), faceNormal.toTuple()], d=1)
            mc.xform(temCurve, ws=True, t=faceCenterPos.toTuple())

        normal = pf_69.center(*facesNormals)
        centerPos = pf_69.center(*facesCenterPoses)
        curve = mc.curve(p=[(0, 0, 0), (normal * 10).toTuple()], d=1)
        mc.xform(curve, ws=True, t=centerPos.toTuple())
        mc.select(selFaces)
        return curve


def pf_39(mesh):
    if not mesh:
        mesh = pf_29()
    if mesh:
        if pf_74(mesh, 'mirrorMode'):
            threshold = mc.getAttr(mesh + '.threshold')
            centerLine = mc.getAttr(mesh + '.centerLine')
        elif pf_73('zhcg_polyTools_mirrorPolyUI'):
            threshold = mc.floatSliderGrp(FSG_threshold, q=True, v=True)
            centerLine = mc.checkBox(CB_center, q=True, v=True)
        else:
            threshold = 0.001
            centerLine = True
        vtxsNum = mc.polyEvaluate(mesh, v=True)
        halfVtxs = []
        reverse = False
        selComps = pf_06()        
        if selComps:
            selComps = selComps[0]
            selCompsPosGroup = pf_69.vectorList(mc.xform(selComps, q=True, os=True, t=True))
            for pos in selCompsPosGroup:
                if pos.x < -threshold:
                    reverse = True
                    break

        vtxPosGrp = mc.xform('%s.vtx[0:%s]' % (mesh, vtxsNum - 1), q=True, os=True, t=True)
                
        for i in range(0, vtxsNum * 3, 3):
            if reverse:                
                if vtxPosGrp[i] >= -threshold:
                    halfVtxs.append(pf_33(mesh, 'vtx', int(i / 3)))
            elif vtxPosGrp[i] <= threshold:                
                halfVtxs.append(pf_33(mesh, 'vtx', int(i / 3)))        
        if halfVtxs:            
            if centerLine:
                halfFaces = mc.polyListComponentConversion(halfVtxs, fv=True, tf=True, internal=True)                
            else:
                halfFaces = mc.polyListComponentConversion(halfVtxs, fv=True, tf=True)
                
            if halfFaces:                            
                mc.delete(halfFaces)


def pf_40(mesh):
    mc.setAttr(mesh + '.mirrorMode', 'mirror', type='string')
    threshold = mc.getAttr(mesh + '.threshold')
    worldRotatePivot = mc.xform(mesh, ws=True, q=True, rp=True)
    translate = mc.getAttr(mesh + '.t')[0]
    localRotatepivot = (pf_69(worldRotatePivot) - pf_69(translate)).toTuple()
    centerLine = mc.getAttr(mesh + '.centerLine')
    mc.polyMirrorFace(mesh, p=localRotatepivot, mm=1 if centerLine else 2, mt=threshold, d=0)
    mc.delete(mesh, ch=True)


def pf_41(mesh):
    mc.setAttr(mesh + '.mirrorMode', 'instance', type='string')
    if mc.getAttr(mesh + '.centerLine'):
        hil = mc.ls(hl=True)
        instMesh = mc.instance(mesh, n='%s_instance' % mesh if '_instance' not in mesh else mesh.replace('_instance', ''))[0]
        mc.delete(instMesh, ch=True)
        mc.setAttr(instMesh + '.overrideEnabled', True)
        mc.setAttr(instMesh + '.overrideDisplayType', 2)
        mc.scale(-1, 1, 1, instMesh, r=True)
        if not hil:
            if '_instance' in mesh:
                mc.select(mesh.replace('_instance', ''))
            else:
                mc.select(mesh)


def pf_42(vtxGrp, even, radius, radiusValue, axis, mesh):
    vtxNum = len(vtxGrp)
    vtxPosGroup = [ pf_69(mc.xform(vtx, q=True, ws=True, t=True)) for vtx in vtxGrp ]
    temPoly = mc.polyCreateFacet(p=[ vec.toTuple() for vec in vtxPosGroup ])[0]
    mc.xform(temPoly, cp=True)
    centerPos = pf_69(mc.xform(temPoly, q=True, ws=True, rp=True))
    distGroup = [ vec.distance(centerPos) for vec in vtxPosGroup ]
    if radius == 'Mean':
        dist = sum(distGroup) / vtxNum
    elif radius == 'Min':
        dist = min(distGroup)
    elif radius == 'Max':
        dist = max(distGroup)
    elif radius == 'Custom':
        dist = radiusValue
    circle = mc.circle(s=vtxNum, r=dist, c=(0, 0, 0), d=3, ch=False)[0]
    circleShape = mc.listRelatives(circle, s=True)[0]
    mc.xform(circle, ws=True, t=centerPos.toTuple())
    if axis == 'Auto':
        firstId = distGroup.index(min(distGroup))
    else:
        if axis == 'YZ':
            pos_axis_grp = [ abs(vec.x - centerPos.x) for vec in vtxPosGroup ]
        elif axis == 'XZ':
            pos_axis_grp = [ abs(vec.y - centerPos.y) for vec in vtxPosGroup ]
        elif axis == 'XY':
            pos_axis_grp = [ abs(vec.z - centerPos.z) for vec in vtxPosGroup ]
        firstId = pos_axis_grp.index(min(pos_axis_grp))
    wuVec = (vtxPosGroup[firstId] - centerPos).toTuple()
    mc.delete(mc.normalConstraint(temPoly, circle, aim=[0, 0, 1], u=[0, 1, 0], wu=wuVec))
    mc.delete(temPoly)
    if even:
        for i in range(vtxNum):
            mc.xform(vtxGrp[(i + firstId) % vtxNum], ws=True, t=mc.xform('%s.ep[%s]' % (circleShape, i), q=True, ws=True, t=True))

    else:
        pf_48(circle, mesh, len(vtxGrp), [ pf_32(vtx) for vtx in vtxGrp ])
    mc.delete(circle)


def pf_43(vtxGrp, even):
    if not even:
        oldPosGroup = [ pf_69(mc.xform(vtx, q=True, os=True, t=True)) for vtx in vtxGrp ]
        edgeLenGroup = [ oldPosGroup[i].distance(oldPosGroup[i - 1]) for i in range(1, len(oldPosGroup)) ]
        oldLen = sum(edgeLenGroup)
        ratios = [ i / oldLen for i in edgeLenGroup ]
        for i in range(1, len(vtxGrp) - 1):
            pos = oldPosGroup[0] + (oldPosGroup[-1] - oldPosGroup[0]) * sum(ratios[:i])
            mc.xform(vtxGrp[i], os=True, t=pos.toTuple())

    else:        
        div = len(vtxGrp) - 1             
        startPos = pf_69(mc.xform(vtxGrp[0], q=True, os=True, t=True))
        endPos = pf_69(mc.xform(vtxGrp[-1], q=True, os=True, t=True)) 
        print("startPos: ", startPos)
        print("endPos: ", endPos)          
        for i in range(1, len(vtxGrp)):                                
            # separated each startPos and endPos to calculate individually. works!
            pos = pf_69(startPos.x + (endPos.x - startPos.x) * i / div,
            startPos.y + (endPos.y - startPos.y) * i / div,
            startPos.z + (endPos.z - startPos.z) * i / div)                                      
            mc.xform(vtxGrp[i], os=True, t=pos.toTuple())

        


def pf_44(vtxGrp, close, mesh, even, smooth, step, axis):
    vtxNum = len(vtxGrp)
    vtxPosGroup = [ pf_69(mc.xform(vtx, q=True, ws=True, t=True)) for vtx in vtxGrp ]
    vtxPosTupleGroup = [ vec.toTuple() for vec in vtxPosGroup ]
    centerPos = pf_69.center(*vtxPosGroup)
    distGroup = [ vec.distance(centerPos) for vec in vtxPosGroup ]
    if close:
        if axis == 'Auto':
            firstId = distGroup.index(min(distGroup))
        else:
            if axis == 'YZ':
                pos_axis_grp = [ abs(vec.x - centerPos.x) for vec in vtxPosGroup ]
            elif axis == 'XZ':
                pos_axis_grp = [ abs(vec.y - centerPos.y) for vec in vtxPosGroup ]
            elif axis == 'XY':
                pos_axis_grp = [ abs(vec.z - centerPos.z) for vec in vtxPosGroup ]
            firstId = pos_axis_grp.index(min(pos_axis_grp))
    else:
        firstId = 0
    if not close:
        span = vtxNum - 1
        averageVtxs = vtxGrp[1:-1]
        curve = mc.curve(p=vtxPosTupleGroup, d=2 if vtxNum <= 3 else 3) if smooth else mc.curve(ep=vtxPosTupleGroup, d=1)
    else:
        span = vtxNum
        averageVtxs = vtxGrp
        curve = mc.circle(s=vtxNum, c=(0, 0, 0), d=3 if smooth else 1, ch=False)[0]
        for i in range(vtxNum):
            mc.xform(curve + '.%s[%d]' % ('cv' if smooth else 'ep', (i + 1) % vtxNum if smooth else i), ws=True, t=vtxPosTupleGroup[(i + firstId) % vtxNum])

        if not smooth:
            mc.xform(curve + '.ep[%d]' % vtxNum, ws=True, t=vtxPosTupleGroup[firstId])
    if even:
        curve = mc.rebuildCurve(curve, s=span, d=3 if smooth or vtxNum <= 3 and not close else 1, ch=False)[0]
        vtxRange = range(1, vtxNum - 1) if not close else range(vtxNum)
        for i in vtxRange:
            mc.xform(vtxGrp[(i + firstId) % vtxNum], ws=True, t=mc.xform('%s.ep[%s]' % (curve, i), q=True, ws=True, t=True))

    else:
        for i in range(step):
            mc.polyAverageVertex(averageVtxs)
            pf_48(curve, mesh, len(averageVtxs), [ pf_32(vtx) for vtx in averageVtxs ])
            delMeshHistory()

    mc.delete(curve)


def pf_46(target, mesh, faceNum, allFaceIdsSet_1, progressBar = False):
    if progressBar:
        gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
        mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='shrinkWrapping...', maxValue=faceNum)
    while allFaceIdsSet_1:
        if progressBar and mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
            break
        allFaceIdsSet_2 = copy.deepcopy(allFaceIdsSet_1)
        while allFaceIdsSet_2:
            if progressBar and mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                break
            curFaceId = allFaceIdsSet_2.pop()
            allFaceIdsSet_1.remove(curFaceId)
            curFace = mesh + '.f[%d]' % curFaceId
            vectorList = pf_69.vectorList(mc.xform(curFace, q=True, ws=True, t=True))
            centerPos = pf_69.center(*vectorList)
            null = mc.group(w=True, em=True)
            mc.xform(null, ws=True, t=centerPos.toTuple())
            mc.geometryConstraint(target, null)
            nPos = pf_69(mc.xform(null, q=True, ws=True, t=True))
            mc.delete(null)
            mc.polyMoveFacet(curFace, t=(nPos - centerPos).toTuple())
            toVtxs = mc.polyListComponentConversion(curFace, ff=True, tv=True)
            toFaces = mc.filterExpand(mc.polyListComponentConversion(toVtxs, fv=True, tf=True), sm=34)
            allFaceIdsSet_2 -= set([ pf_32(face) for face in toFaces ])
            delMeshHistory()
            if progressBar:
                mc.progressBar(gMainProgressBar, edit=True, step=1)

    if progressBar:
        mc.progressBar(gMainProgressBar, edit=True, endProgress=True)


def pf_47(target, mesh, selBorderEdges, progressBar = False):
    if progressBar:
        gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
        mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='shrinkWrapping...', maxValue=len(selBorderEdges))
    allEdgeSet_1 = set(selBorderEdges)
    while allEdgeSet_1:
        if progressBar and mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
            break
        allEdgeSet_2 = copy.deepcopy(allEdgeSet_1)
        while allEdgeSet_2:
            if progressBar and mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
                break
            curEdge = allEdgeSet_2.pop()
            allEdgeSet_1.remove(curEdge)
            vectorList = pf_69.vectorList(mc.xform(curEdge, q=True, ws=True, t=True))
            centerPos = pf_69.center(*vectorList)
            null = mc.group(w=True, em=True)
            mc.xform(null, ws=True, t=centerPos.toTuple())
            mc.geometryConstraint(target, null)
            nPos = pf_69(mc.xform(null, q=True, ws=True, t=True))
            mc.delete(null)
            mc.polyMoveEdge(curEdge, t=(nPos - centerPos).toTuple())
            toVtxs = mc.polyListComponentConversion(curEdge, fe=True, tv=True)
            toEdges = mc.filterExpand(mc.polyListComponentConversion(toVtxs, fv=True, te=True), sm=32)
            allEdgeSet_2 -= set(toEdges)
            delMeshHistory()
            if progressBar:
                mc.progressBar(gMainProgressBar, edit=True, step=1)

    if progressBar:
        mc.progressBar(gMainProgressBar, edit=True, endProgress=True)


def pf_48(target, mesh, vtxNum, allVtxIds, progressBar = False):
    if progressBar:
        gMainProgressBar = mm.eval('$tmp=$gMainProgressBar')
        mc.progressBar(gMainProgressBar, edit=True, beginProgress=True, isInterruptable=True, status='shrinkWrapping...', maxValue=vtxNum)
    for vtxId in allVtxIds:
        if progressBar and mc.progressBar(gMainProgressBar, query=True, isCancelled=True):
            break
        vtx = pf_33(mesh, 'vtx', vtxId)
        pos = mc.xform(vtx, q=True, ws=True, t=True)
        null = mc.group(w=True, em=True)
        mc.xform(null, ws=True, t=pos)
        mc.geometryConstraint(target, null)
        nPos = mc.xform(null, q=True, ws=True, t=True)
        mc.xform(vtx, ws=True, t=nPos)
        mc.delete(null)
        if progressBar:
            mc.progressBar(gMainProgressBar, edit=True, step=1)

    if progressBar:
        mc.progressBar(gMainProgressBar, edit=True, endProgress=True)


def pf_49(selMode, reverse, speed):
    if selMode == 'facet':
        selFaces = mc.filterExpand(sm=34)
        selEdge = pf_64(selFaces)[0]
    elif selMode == 'edge':
        selEdge = mc.filterExpand(sm=32)[0]
    mc.polySpinEdge(selEdge, offset=speed if reverse else -1 * speed)
    delMeshHistory()
    newEdge = mc.filterExpand(sm=32)[0]
    if selMode == 'facet':
        newFaces = mc.polyListComponentConversion(newEdge, fe=True, tf=True)
        mc.select(newFaces)


def pf_50(selMode, vtxNum, sortedVtxs_A, sortedVtxs_B, firstID):
    if selMode == 'facet':
        selFaces = mc.filterExpand(sm=34)
    elif selMode == 'edge':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tf=True), sm=34)
    interEdges = pf_64(selFaces)
    for i in range(vtxNum):
        pf_24(sortedVtxs_A[i], sortedVtxs_B[(i + firstID) % vtxNum])

    mc.delete(interEdges)
    delMeshHistory()
    newInterEdges = []
    for i in range(vtxNum):
        newInterEdges += mc.polyListComponentConversion(sortedVtxs_A[i], sortedVtxs_B[(i + firstID) % vtxNum], fv=True, te=True, internal=True)

    if selMode == 'facet':
        newFaces = mc.filterExpand(mc.polyListComponentConversion(newInterEdges, fe=True, tf=True), sm=34)
        newFaces = [ face for face in newFaces if pf_19(face) ]
        mc.select(newFaces)
    elif selMode == 'edge':
        mc.select(newInterEdges)


def pf_51(selMode):
    if selMode == 'facet':
        selFaces = mc.filterExpand(sm=34)
    elif selMode == 'edge':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tf=True), sm=34)
    elif selMode == 'vertex':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=31), fv=True, tf=True), sm=34)
    outlineVtxs = pf_63(selFaces)
    interEdges = pf_64(selFaces)
    interEdges2vtxs = mc.filterExpand(mc.polyListComponentConversion(interEdges, fe=True, tv=True), sm=31)
    interVtx = pf_65(selFaces)[0]
    connectVtxs = [ vtx for vtx in outlineVtxs if vtx not in interEdges2vtxs ]
    for vtx in connectVtxs:
        pf_24(interVtx, vtx)

    mc.delete(interEdges)
    delMeshHistory()
    if selMode == 'facet':
        newFaces = mc.polyListComponentConversion(interVtx, fv=True, tf=True)
        mc.select(newFaces)
    elif selMode == 'vertex':
        mc.select(interVtx)
    elif selMode == 'edge':
        newEdges = mc.polyListComponentConversion(interVtx, fv=True, te=True)
        mc.select(newEdges)


def pf_52(selMode, reverse, speed):
    if selMode == 'facet':
        selFaces = mc.filterExpand(sm=34)
    elif selMode == 'edge':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tf=True), sm=34)
    internalEdges = pf_64(selFaces)
    edgeVtxs = mc.filterExpand(mc.polyListComponentConversion(internalEdges, fe=True, tv=True), sm=31)
    sortedVtxs = pf_02(selFaces)
    vtxNum = len(sortedVtxs)
    if not reverse:
        sortedVtxs.reverse()
    mc.delete(internalEdges)
    delMeshHistory()
    for i in range(vtxNum):
        if sortedVtxs[i] in edgeVtxs and sortedVtxs[(i - 1) % vtxNum] not in edgeVtxs:
            startId = i
            break

    step = vtxNum / 4 if speed == 3 else speed
    for i in range(vtxNum / 2 - 2):
        pf_24(sortedVtxs[(startId + i + step) % vtxNum], sortedVtxs[(startId - (i + 3) + step) % vtxNum])

    newFaces = mc.polyListComponentConversion(sortedVtxs, fv=True, tf=True, internal=True)
    if selMode == 'facet':
        mc.select(newFaces)
    elif selMode == 'edge':
        interEdges = pf_64(newFaces)
        mc.select(interEdges)


def pf_53(selMode, reverse, speed, gridType, mesh, targetMesh):
    if selMode == 'facet':
        selFaces = mc.filterExpand(sm=34)
    elif selMode == 'edge':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tf=True), sm=34)
    elif selMode == 'vertex':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=31), fv=True, tf=True), sm=34)
    oldSortedVtxs = pf_02(selFaces)
    vtxNum = len(oldSortedVtxs)
    oldSortedVtxsPosGroup = pf_69.vectorList(mc.xform(oldSortedVtxs, q=True, os=True, t=True))
    interEdges = pf_64(selFaces)
    toVtxs = mc.filterExpand(mc.polyListComponentConversion(interEdges, fe=True, tv=True), sm=31)
    oldConnerVtxs = [ vtx for vtx in oldSortedVtxs if vtx not in toVtxs ]
    connerVtxsIds = [ oldSortedVtxs.index(vtx) for vtx in oldConnerVtxs ]
    mc.select(selFaces)
    mc.polyExtrudeFacet()
    mm.eval('polyMergeToCenter')
    centerVtx = mc.filterExpand(sm=31)[0]
    centerEdges = mc.filterExpand(mc.polyListComponentConversion(centerVtx, fv=True, te=True), sm=32)
    mm.eval('PolySelectConvert 1')
    mc.delete(centerEdges)
    delMeshHistory()
    polyFace = mc.filterExpand(sm=34)[0]
    sortedVtxs = pf_02(polyFace)
    newSortedVtxsPosGroup = pf_69.vectorList(mc.xform(sortedVtxs, q=True, os=True, t=True))
    for i in range(6):
        if newSortedVtxsPosGroup[i] == oldSortedVtxsPosGroup[0]:
            if newSortedVtxsPosGroup[(i + 1) % 6] == oldSortedVtxsPosGroup[1]:
                sortedVtxs = sortedVtxs[i:] + sortedVtxs[:i]
            else:
                sortedVtxs.reverse()
                sortedVtxs = sortedVtxs[5 - i:] + sortedVtxs[:5 - i]
            break

    num1, num2 = gridType.split('x')
    num1, num2 = int(num1), int(num2)
    num1 -= 1
    num3 = num2 - 1
    num2 += 2
    step = vtxNum / 4 if speed == 3 else speed
    for i in range(vtxNum):
        if i not in connerVtxsIds and (i - num2) % vtxNum not in connerVtxsIds and (i - 1) % vtxNum in connerVtxsIds and (i - num2 + 1) % vtxNum in connerVtxsIds:
            startId = (i - step) % vtxNum
            if reverse:
                startId = (i + step) % vtxNum
            break

    for i in range(num1):
        pf_24(sortedVtxs[(startId + i) % vtxNum], sortedVtxs[(startId - (i + num2)) % vtxNum])

    newFaces = mc.filterExpand(mc.polyListComponentConversion(sortedVtxs, fv=True, tf=True, internal=True), sm=34)
    interEdges = pf_64(newFaces)
    mc.select(interEdges)
    mc.polySubdivideEdge(dv=num3)
    newVtxs = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tv=True, internal=True), sm=31)
    for face in newFaces:
        tem_sortedVtxs = pf_02(face)
        tem_vtxNum = len(tem_sortedVtxs)
        for i in range(len(tem_sortedVtxs)):
            if tem_sortedVtxs[i] in newVtxs and tem_sortedVtxs[i - 1] not in newVtxs:
                tem_startId = i
                break

        for i in range(tem_vtxNum / 2 - 2):
            pf_24(tem_sortedVtxs[(tem_startId + i) % tem_vtxNum], tem_sortedVtxs[(tem_startId - (i + 3)) % tem_vtxNum])

    mc.undoInfo(swf=False)
    for i in range(5):
        mc.polyAverageVertex(newVtxs)
        delMeshHistory()

    pf_48(targetMesh, mesh, len(newVtxs), [ pf_32(vtx) for vtx in newVtxs ])
    mc.undoInfo(swf=True)
    newFaces = mc.polyListComponentConversion(sortedVtxs + newVtxs, fv=True, tf=True, internal=True)
    if selMode == 'facet':
        mc.select(newFaces)
    elif selMode == 'vertex':
        mc.select(newVtxs)
    elif selMode == 'edge':
        interEdges = pf_64(newFaces)
        mc.select(interEdges)
    mm.eval('doMenuComponentSelection("%s", "%s")' % (mesh, selMode))


def pf_54(selMode, reverse, mesh, targetMesh):
    if selMode == 'facet':
        selFaces = mc.filterExpand(sm=34)
    elif selMode == 'vertex':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=31), fv=True, tf=True), sm=34)
    elif selMode == 'edge':
        selFaces = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tf=True), sm=34)
    oldSortedVtxs = pf_02(selFaces)
    oldSortedVtxsPosGroup = pf_69.vectorList(mc.xform(oldSortedVtxs, q=True, os=True, t=True))
    interEdges = pf_64(selFaces)
    toVtxs = mc.filterExpand(mc.polyListComponentConversion(interEdges, fe=True, tv=True), sm=31)
    oldConnerVtxs = [ vtx for vtx in oldSortedVtxs if vtx not in toVtxs ]
    connerVtxsIds = [ oldSortedVtxs.index(vtx) for vtx in oldConnerVtxs ]
    mc.select(selFaces)
    mc.polyExtrudeFacet()
    mm.eval('polyMergeToCenter')
    centerVtx = mc.filterExpand(sm=31)[0]
    centerEdges = mc.filterExpand(mc.polyListComponentConversion(centerVtx, fv=True, te=True), sm=32)
    mm.eval('PolySelectConvert 1')
    mc.delete(centerEdges)
    delMeshHistory()
    polyFace = mc.filterExpand(sm=34)[0]
    newSortedVtxs = pf_02(polyFace)
    newSortedVtxsPosGroup = pf_69.vectorList(mc.xform(newSortedVtxs, q=True, os=True, t=True))
    for i in range(6):
        if newSortedVtxsPosGroup[i] == oldSortedVtxsPosGroup[0]:
            if newSortedVtxsPosGroup[(i + 1) % 6] == oldSortedVtxsPosGroup[1]:
                newSortedVtxs = newSortedVtxs[i:] + newSortedVtxs[:i]
            else:
                newSortedVtxs.reverse()
                newSortedVtxs = newSortedVtxs[5 - i:] + newSortedVtxs[:5 - i]
            break

    for i in range(6):
        if i not in connerVtxsIds and (i + 1) % 6 in connerVtxsIds and (i + 2) % 6 not in connerVtxsIds:
            startId = (i - 1) % 6
            if reverse:
                startId = (i + 1) % 6
            break

    edge_A = pf_24(newSortedVtxs[startId], newSortedVtxs[(startId + 2) % 6])
    edge_B = pf_24(newSortedVtxs[(startId + 3) % 6], newSortedVtxs[(startId + 5) % 6])
    newVtxs = pf_26(edge_A, edge_B)[:2]
    newFaces = mc.polyListComponentConversion(newVtxs, fv=True, tf=True)
    mc.undoInfo(swf=False)
    for i in range(5):
        mc.polyAverageVertex(newVtxs)
        delMeshHistory()

    pf_48(targetMesh, mesh, len(newVtxs), [ pf_32(vtx) for vtx in newVtxs ])
    mc.undoInfo(swf=True)
    if selMode == 'facet':
        mc.select(newFaces)
    elif selMode == 'vertex':
        mc.select(newVtxs)
    elif selMode == 'edge':
        interEdges = pf_64(newFaces)
        mc.select(interEdges)
    mm.eval('doMenuComponentSelection("%s", "%s")' % (mesh, selMode))


def pf_55(gridType, mesh):
    target = None
    if pf_73('zhcg_polyTools_shrinkWrapUI'):
        target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
        if target:
            if mc.objExists(target):
                targetMesh = target
            else:
                target = None
    if not target:
        mc.undoInfo(swf=False)
        targetMesh = mc.duplicate(mesh)[0]
        mc.setAttr(targetMesh + '.v', False)
        mc.undoInfo(swf=True)
    mc.polyExtrudeFacet()
    mm.eval('polyMergeToCenter')
    centerVtx = mc.filterExpand(sm=31)[0]
    centerEdges = mc.filterExpand(mc.polyListComponentConversion(centerVtx, fv=True, te=True), sm=32)
    mm.eval('PolySelectConvert 1')
    mc.delete(centerEdges)
    delMeshHistory()
    polyFace = mc.filterExpand(sm=34)[0]
    sortedVtxs = pf_02(polyFace)
    sortedVtxsEdgeNums = [ len(mc.filterExpand(mc.polyListComponentConversion(vtx, fv=True, te=True), sm=32)) for vtx in sortedVtxs ]
    vtxNum = len(sortedVtxs)
    num1, num2 = gridType.split('x')
    num1, num2 = int(num1), int(num2)
    num1 -= 1
    num3 = num2 - 1
    num2 += 2
    for i in range(vtxNum):
        if sortedVtxsEdgeNums[i] < 3 and sortedVtxsEdgeNums[(i - num2) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] >= 3 and sortedVtxsEdgeNums[(i - num2 + 1) % vtxNum] >= 3:
            startId = i
            break
    else:
        for i in range(vtxNum):
            if sortedVtxsEdgeNums[i] <= 3 and sortedVtxsEdgeNums[(i - num2) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] > 3 and sortedVtxsEdgeNums[(i - num2 + 1) % vtxNum] > 3:
                startId = i
                break
        else:
            for i in range(vtxNum):
                if sortedVtxsEdgeNums[i] <= 3 and sortedVtxsEdgeNums[(i - num2) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] >= 3 and sortedVtxsEdgeNums[(i - num2 + 1) % vtxNum] >= 3:
                    startId = i
                    break
            else:
                startId = sortedVtxsEdgeNums.index(min(sortedVtxsEdgeNums))

    for i in range(num1):
        pf_24(sortedVtxs[(startId + i) % vtxNum], sortedVtxs[(startId - (i + num2)) % vtxNum])

    newFaces = mc.filterExpand(mc.polyListComponentConversion(sortedVtxs, fv=True, tf=True, internal=True), sm=34)
    interEdges = pf_64(newFaces)
    mc.select(interEdges)
    mc.polySubdivideEdge(dv=num3)
    delMeshHistory()
    newVtxs = mc.filterExpand(mc.polyListComponentConversion(mc.filterExpand(sm=32), fe=True, tv=True, internal=True), sm=31)
    for face in newFaces:
        tem_sortedVtxs = pf_02(face)
        tem_vtxNum = len(tem_sortedVtxs)
        for i in range(len(tem_sortedVtxs)):
            if tem_sortedVtxs[i] in newVtxs and tem_sortedVtxs[i - 1] not in newVtxs:
                tem_startId = i
                break

        for i in range(tem_vtxNum / 2 - 2):
            pf_24(tem_sortedVtxs[(tem_startId + i) % tem_vtxNum], tem_sortedVtxs[(tem_startId - (i + 3)) % tem_vtxNum])

    mc.undoInfo(swf=False)
    for i in range(5):
        mc.polyAverageVertex(newVtxs)
        delMeshHistory()

    pf_48(targetMesh, mesh, len(newVtxs), [ pf_32(vtx) for vtx in newVtxs ])
    if not target:
        mc.delete(targetMesh)
    mc.undoInfo(swf=True)
    newFaces = mc.polyListComponentConversion(sortedVtxs + newVtxs, fv=True, tf=True, internal=True)
    mm.eval('doMenuComponentSelection("%s", "facet")' % mesh)
    mc.select(newFaces)


def pf_56(mesh):
    selFaces = mc.filterExpand(sm=34)
    oldVtxs = pf_63(selFaces)
    oldVtxs_posGrp = pf_69.vectorList(mc.xform(oldVtxs, q=True, ws=True, t=True))
    mc.delete(selFaces)
    openEdges = pf_23(mesh)
    toVtxs = mc.filterExpand(mc.polyListComponentConversion(openEdges, fe=True, tv=True), sm=31)
    toVtxs_posGrp = pf_69.vectorList(mc.xform(toVtxs, q=True, ws=True, t=True))
    newVtxs = [ toVtxs[toVtxs_posGrp.index(vec)] for vec in toVtxs_posGrp if vec in oldVtxs_posGrp ]
    newEdges = mc.filterExpand(mc.polyListComponentConversion(newVtxs, fv=True, te=True, internal=True), sm=32)
    newEdges = [ edge for edge in newEdges if edge in openEdges ]
    mc.select(newEdges)
    mc.polyBridgeEdge(divisions=0)
    newFaces = mc.polyListComponentConversion(newVtxs, fv=True, tf=True, internal=True)
    mc.select(newFaces)


def pf_57(mesh):
    mc.polyExtrudeFacet()
    mm.eval('polyMergeToCenter')
    centerVtx = mc.filterExpand(sm=31)[0]
    centerEdges = mc.filterExpand(mc.polyListComponentConversion(centerVtx, fv=True, te=True), sm=32)
    mm.eval('PolySelectConvert 1')
    mc.delete(centerEdges)
    polyFace = mc.filterExpand(sm=34)[0]
    sortedVtxs = pf_02(polyFace)
    vtxNum = len(sortedVtxs)
    sortedVtxsEdgeNums = [ len(mc.filterExpand(mc.polyListComponentConversion(vtx, fv=True, te=True), sm=32)) for vtx in sortedVtxs ]
    if sortedVtxsEdgeNums.count(3) == 1:
        startId = sortedVtxsEdgeNums.index(3)
    else:
        for i in range(len(sortedVtxsEdgeNums)):
            if sortedVtxsEdgeNums[i] > 3 and sortedVtxsEdgeNums[(i - 3) % vtxNum] > 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 2) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i + 1) % vtxNum] <= 3:
                startId = i
                break
        else:
            for i in range(len(sortedVtxsEdgeNums)):
                if sortedVtxsEdgeNums[i] < 3 and sortedVtxsEdgeNums[(i - 3) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] >= 3 and sortedVtxsEdgeNums[(i - 2) % vtxNum] >= 3 and sortedVtxsEdgeNums[(i + 1) % vtxNum] < 3:
                    startId = i
                    break
            else:
                for i in range(len(sortedVtxsEdgeNums)):
                    if sortedVtxsEdgeNums[i] <= 3 and sortedVtxsEdgeNums[(i - 3) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] > 3 and sortedVtxsEdgeNums[(i - 2) % vtxNum] > 3 and sortedVtxsEdgeNums[(i + 1) % vtxNum] <= 3:
                        startId = i
                        break
                else:
                    for i in range(len(sortedVtxsEdgeNums)):
                        if sortedVtxsEdgeNums[i] <= 3 and sortedVtxsEdgeNums[(i - 3) % vtxNum] <= 3 and sortedVtxsEdgeNums[(i - 1) % vtxNum] >= 3 and sortedVtxsEdgeNums[(i - 2) % vtxNum] >= 3 and sortedVtxsEdgeNums[(i + 1) % vtxNum] <= 3:
                            startId = i
                            break
                    else:
                        startId = sortedVtxsEdgeNums.index(min(sortedVtxsEdgeNums))

    for i in range(vtxNum / 2 - 2):
        pf_24(sortedVtxs[(startId + i) % vtxNum], sortedVtxs[(startId - (i + 3)) % vtxNum])

    mc.select(mc.polyListComponentConversion(sortedVtxs, fv=True, tf=True, internal=True))


def pf_58(mesh):
    target = None
    if pf_73('zhcg_polyTools_shrinkWrapUI'):
        target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
        if target:
            if mc.objExists(target):
                targetMesh = target
            else:
                target = None
    if not target:
        mc.undoInfo(swf=False)
        targetMesh = mc.duplicate(mesh)[0]
        mc.setAttr(targetMesh + '.v', False)
        mc.undoInfo(swf=True)
    mc.polyExtrudeFacet()
    mm.eval('polyMergeToCenter')
    delMeshHistory()
    centerVtx = mc.filterExpand(sm=31)[0]
    sortedEdges = pf_04(centerVtx)
    edgeGroup1 = sortedEdges[::2]
    edgeGroup2 = sortedEdges[1::2]
    group1vtxs = [ vtx for vtx in mc.filterExpand(mc.polyListComponentConversion(edgeGroup1, fe=True, tv=True), sm=31) if vtx != centerVtx ]
    group2vtxs = [ vtx for vtx in mc.filterExpand(mc.polyListComponentConversion(edgeGroup2, fe=True, tv=True), sm=31) if vtx != centerVtx ]
    group1vtxsEdgeNums = len(mc.filterExpand(mc.polyListComponentConversion(group1vtxs, fv=True, te=True), sm=32))
    group2vtxsEdgeNums = len(mc.filterExpand(mc.polyListComponentConversion(group2vtxs, fv=True, te=True), sm=32))
    delEdgeGroup = edgeGroup1 if group1vtxsEdgeNums >= group2vtxsEdgeNums else edgeGroup2
    mc.delete(delEdgeGroup)
    mc.undoInfo(swf=False)
    for i in range(5):
        mc.polyAverageVertex(centerVtx)
        delMeshHistory()

    pf_48(targetMesh, mesh, 1, [pf_32(centerVtx)])
    if not target:
        mc.delete(targetMesh)
    mc.undoInfo(swf=True)
    newFaces = mc.polyListComponentConversion(centerVtx, fv=True, tf=True)
    mm.eval('doMenuComponentSelection("%s", "facet")' % mesh)
    mc.select(newFaces)


def pf_59(mesh):
    target = None
    if pf_73('zhcg_polyTools_shrinkWrapUI'):
        target = mc.textFieldButtonGrp(TFBG_shrinkWrap, q=True, tx=True)
        if target:
            if mc.objExists(target):
                targetMesh = target
            else:
                target = None
    if not target:
        mc.undoInfo(swf=False)
        targetMesh = mc.duplicate(mesh)[0]
        mc.setAttr(targetMesh + '.v', False)
        mc.undoInfo(swf=True)
    mc.polyExtrudeFacet()
    mm.eval('polyMergeToCenter')
    centerVtx = mc.filterExpand(sm=31)[0]
    centerEdges = mc.filterExpand(mc.polyListComponentConversion(centerVtx, fv=True, te=True), sm=32)
    mm.eval('PolySelectConvert 1')
    mc.delete(centerEdges)
    delMeshHistory()
    polyFace = mc.filterExpand(sm=34)[0]
    sortedVtxs = pf_02(polyFace)
    sortedVtxsEdgeNums = [ len(mc.filterExpand(mc.polyListComponentConversion(vtx, fv=True, te=True), sm=32)) for vtx in sortedVtxs ]
    startId = (sortedVtxsEdgeNums.index(min(sortedVtxsEdgeNums)) - 1) % 6
    edge_A = pf_24(sortedVtxs[startId], sortedVtxs[(startId + 2) % 6])
    edge_B = pf_24(sortedVtxs[(startId + 3) % 6], sortedVtxs[(startId + 5) % 6])
    newVtxs = pf_26(edge_A, edge_B)[:2]
    mc.undoInfo(swf=False)
    for i in range(5):
        mc.polyAverageVertex(newVtxs)
        delMeshHistory()

    pf_48(targetMesh, mesh, 2, [ pf_32(vtx) for vtx in newVtxs ])
    if not target:
        mc.delete(targetMesh)
    mc.undoInfo(swf=True)
    newFaces = mc.polyListComponentConversion(newVtxs, fv=True, tf=True)
    mm.eval('doMenuComponentSelection("%s", "facet")' % mesh)
    mc.select(newFaces)


def pf_60(toolbox, titleBarHeight = 21):
    state = mc.window(toolbox, q=True, tb=True)
    topEdge = mc.window(toolbox, q=True, te=True)
    leftEdge = mc.window(toolbox, q=True, le=True)
    teOffset = titleBarHeight
    height = mc.window(toolbox, q=True, h=True)
    if state:
        topEdge += teOffset
        leftEdge += 3
    else:
        topEdge -= teOffset
        leftEdge -= 3
    mc.window(toolbox, e=True, tb=not state, te=topEdge, le=leftEdge, h=height)
    return state


def pf_61():
    pass


def pf_62(smooth = True):
    allGrps = None
    selEdges = mc.filterExpand(sm=32)
    if selEdges and len(selEdges) >= 3:
        vtxGrps = pf_03(selEdges)
        if vtxGrps:
            allGrps = [ vtxsGrp for vtxsGrp in vtxGrps[0] + vtxGrps[1] if len(vtxsGrp) >= 3 ]
    else:
        selVtxs = mc.filterExpand(sm=31)
        if selVtxs and len(selVtxs) == 3:
            allGrps = [selVtxs]
        else:
            selFaces = mc.filterExpand(sm=34)
            if selFaces:
                outlineEdges = pf_09(selFaces)
                vtxGrps = pf_03(outlineEdges)
                allGrps = [ vtxsGrp for vtxsGrp in vtxGrps[1] if len(vtxsGrp) >= 3 ]
    if allGrps:
        for vtxsGrp in allGrps:
            vtxNum = len(vtxsGrp)
            vtxPosGroup = [ pf_69(mc.xform(vtx, q=True, ws=True, t=True)) for vtx in vtxsGrp ]
            temPoly = mc.polyCreateFacet(p=[ vec.toTuple() for vec in vtxPosGroup ])[0]
            mc.xform(temPoly, cp=True)
            centerPos = pf_69(mc.xform(temPoly, q=True, ws=True, rp=True))
            distGroup = [ vec.distance(centerPos) for vec in vtxPosGroup ]
            radius = sum(distGroup) / vtxNum
            circle = mc.circle(s=vtxNum, r=radius, c=(0, 0, 0), d=3 if smooth else 1, ch=False)[0]
            mc.xform(circle, ws=True, t=centerPos.toTuple())
            pos_axis_grp = [ abs(vec.x - centerPos.x) for vec in vtxPosGroup ]
            firstId = pos_axis_grp.index(min(pos_axis_grp))
            wuVec = (vtxPosGroup[firstId] - centerPos).toTuple()
            mc.delete(mc.normalConstraint(temPoly, circle, aim=[0, 0, 1], u=[0, 1, 0], wu=wuVec))
            mc.delete(temPoly)


def edge_pos(edge, vtx):
    if int(mc.polyInfo(edge, ev=True)[0].split()[2]) == pf_32(vtx):
        return 0
    else:
        return 1

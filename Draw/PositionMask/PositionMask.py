# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named PositionMaskExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from PositionMaskExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.comunity.plugins.PositionMask"

def getLabel():
    return "PositionMask"

def getVersion():
    return 1

def getIconPath():
    return "PositionMask.png"

def getGrouping():
    return "Draw/Relight"

def getPluginDescription():
    return "Take a world position pass and generate a rounded mask from it."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.userNatron = lastNode.createPageParam("userNatron", "Controls")
    param = lastNode.createChoiceParam("SeExpr1layerInput1", "Input Layer 1")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.SeExpr1layerInput1 = param
    del param

    param = lastNode.createColorParam("SeExpr1color1", "Position", False)
    param.setMinimum(-1.79769e+308, 0)
    param.setMaximum(1.79769e+308, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setMinimum(-1.79769e+308, 1)
    param.setMaximum(1.79769e+308, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setMinimum(-1.79769e+308, 2)
    param.setMaximum(1.79769e+308, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("The Position of the mask RGB = XYZ")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.SeExpr1color1 = param
    del param

    param = lastNode.createColorParam("SeExpr1color2", "Size", False)
    param.setMinimum(-1.79769e+308, 0)
    param.setMaximum(1.79769e+308, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-1.79769e+308, 1)
    param.setMaximum(1.79769e+308, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(10, 1)
    param.restoreDefaultValue(1)
    param.setMinimum(-1.79769e+308, 2)
    param.setMaximum(1.79769e+308, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(100, 2)
    param.setDefaultValue(10, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("The Size of the Mask RGB = XYZ")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(10, 0)
    param.setValue(10, 1)
    param.setValue(10, 2)
    lastNode.SeExpr1color2 = param
    del param

    param = lastNode.createSeparatorParam("sep", "")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep = param
    del param

    param = lastNode.createDoubleParam("SeExpr1x1", "Mask Contrast")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(50, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Use this slider to give contrast to the mask")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    lastNode.SeExpr1x1 = param
    del param

    param = lastNode.createColorParam("Grade1white", "Gain", True)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(4, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(4, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)
    param.setDisplayMinimum(0, 3)
    param.setDisplayMaximum(4, 3)
    param.setDefaultValue(1, 3)
    param.restoreDefaultValue(3)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Grade1white = param
    del param

    param = lastNode.createColorParam("Grade1offset", "Offset", True)
    param.setDisplayMinimum(-1, 0)
    param.setDisplayMaximum(1, 0)
    param.setDisplayMinimum(-1, 1)
    param.setDisplayMaximum(1, 1)
    param.setDisplayMinimum(-1, 2)
    param.setDisplayMaximum(1, 2)
    param.setDisplayMinimum(-1, 3)
    param.setDisplayMaximum(1, 3)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Grade1offset = param
    del param

    param = lastNode.createColorParam("Grade1gamma", "Gamma", True)
    param.setDisplayMinimum(0.2, 0)
    param.setDisplayMaximum(5, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0.2, 1)
    param.setDisplayMaximum(5, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDisplayMinimum(0.2, 2)
    param.setDisplayMaximum(5, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)
    param.setDisplayMinimum(0.2, 3)
    param.setDisplayMaximum(5, 3)
    param.setDefaultValue(1, 3)
    param.restoreDefaultValue(3)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Grade1gamma = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['userNatron', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "SeExpr1"
    lastNode = app.createNode("fr.inria.openfx.SeExpr", 2, group)
    lastNode.setScriptName("SeExpr1")
    lastNode.setLabel("SeExpr1")
    lastNode.setPosition(83, 630)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSeExpr1 = lastNode

    param = lastNode.getParam("rod")
    if param is not None:
        param.set("Input1")
        del param

    param = lastNode.getParam("layerInputChoice1")
    if param is not None:
        param.setValue("Color")
        del param

    param = lastNode.getParam("doubleParamsNb")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("x1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("colorParamsNb")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("color2")
    if param is not None:
        param.setValue(10, 0)
        param.setValue(10, 1)
        param.setValue(10, 2)
        del param

    param = lastNode.getParam("script")
    if param is not None:
        param.setValue("color1/=color2;\nCs/=color2;\nd = length(abs(color1-Cs)) ; \nd =pow(d,x1);\nclamp(invert(d),0,1)")
        del param

    param = lastNode.getParam("alphaScript")
    if param is not None:
        param.setValue("1")
        del param

    del lastNode
    # End of node "SeExpr1"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(85, 804)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(85, 722)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("white")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    param = lastNode.getParam("offset")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("gamma")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade1"

    # Start of node "Input"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input")
    lastNode.setLabel("Input")
    lastNode.setPosition(85, 484)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput = lastNode

    del lastNode
    # End of node "Input"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(85, 940)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupSeExpr1.connectInput(0, groupInput)
    groupShuffle1.connectInput(1, groupGrade1)
    groupGrade1.connectInput(0, groupSeExpr1)
    groupOutput1.connectInput(0, groupShuffle1)

    param = groupSeExpr1.getParam("layerInput1")
    group.getParam("SeExpr1layerInput1").setAsAlias(param)
    del param
    param = groupSeExpr1.getParam("x1")
    group.getParam("SeExpr1x1").setAsAlias(param)
    del param
    param = groupSeExpr1.getParam("color1")
    group.getParam("SeExpr1color1").setAsAlias(param)
    del param
    param = groupSeExpr1.getParam("color2")
    group.getParam("SeExpr1color2").setAsAlias(param)
    del param
    param = groupGrade1.getParam("white")
    group.getParam("Grade1white").setAsAlias(param)
    del param
    param = groupGrade1.getParam("offset")
    group.getParam("Grade1offset").setAsAlias(param)
    del param
    param = groupGrade1.getParam("gamma")
    group.getParam("Grade1gamma").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["PositionMaskExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)

# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Screen_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Screen_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Screen_GL"

def getLabel():
    return "Screen_GL"

def getVersion():
    return 1

def getIconPath():
    return "Screen_GL.png"

def getGrouping():
    return "Community/GLSL/Merge"

def getPluginDescription():
    return "GPU accelerated screen merge."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Screen_GL")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("line01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line01 = param
    del param

    param = lastNode.createStringParam("aChannels", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("A Channels")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.aChannels = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool1", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool1 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool2", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool2 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool3", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool3 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool4", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool4 = param
    del param

    param = lastNode.createStringParam("bChannels", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("B Channels")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.bChannels = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool5", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool5 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool6", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool6 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool7", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool7 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool8", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueBool8 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createSeparatorParam("line02", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2_2paramValueBool9", "mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.Shadertoy2_2paramValueBool9 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2_2paramValueFloat0", "Mix :")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2_2paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line03", "Screen_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
    del param

    param = lastNode.createSeparatorParam("line04", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line04 = param
    del param

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator27", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator27 = param
    del param

    param = lastNode.createStringParam("separator28", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator28 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("B")
    lastNode.setLabel("B")
    lastNode.setPosition(4139, 3647)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupB = lastNode

    del lastNode
    # End of node "B"

    # Start of node "A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("A")
    lastNode.setLabel("A")
    lastNode.setPosition(4286, 3845)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupA = lastNode

    del lastNode
    # End of node "A"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(4139, 3994)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Shadertoy2_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy2_2")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3842)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy2_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueBool1")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool2")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool4")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool6")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool8")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool9")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// iChannel0: B, filter = nearest\n// iChannel1: A, filter = nearest\n// iChannel2: Mask, filter = nearest\n// BBox: iChannel0\n\n\nuniform float opacity = 1; // Mix : (mix), min=0., max=1.\n\nuniform bool Ar = true; // red\nuniform bool Ag = true; // green\nuniform bool Ab = true; // blue\nuniform bool Aa = true; // alpha\n\nuniform bool Br = true; // red\nuniform bool Bg = true; // green\nuniform bool Bb = true; // blue\nuniform bool Ba = true; // alpha\n\nuniform bool maskCheck = false; // mask\n\n\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\n\tvec2 uv = fragCoord.xy / iResolution.xy;\n\n\t// source texture (upper layer)\n\tvec4 s = texture2D(iChannel1, uv);\n\t\n\t// destination texture (lower layer)\n\tvec4 d = texture2D(iChannel0, uv);\n\n\t// mask texture (mask entry)\n\tvec4 mask = texture2D(iChannel2, uv);\n\n\n\tif(Ar == false)\n\t\ts.r = 0;\n\n\tif(Ag == false)\n\t\ts.g = 0;\n\n\tif(Ab == false)\n\t\ts.b = 0;\n\n\tif(Aa == false)\n\t\ts.a = 0;\n\n\tif(Br == false)\n\t\td.r = 0;\n\n\tif(Bg == false)\n\t\td.g = 0;\n\n\tif(Bb == false)\n\t\td.b = 0;\n\n\tif(Ba == false)\n\t\td.a = 0;\n\n\t\t\n\tvec4 result = 1 - (1 - s) * (1 - d);\n\n\n\tif (maskCheck)\n\t\ts.a = s.a*mask.a;\n\n\n\tfragColor = mix(d, result, s.a*opacity);\n}")
        del param

    param = lastNode.getParam("inputEnable0")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("opacity")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Mix :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("mix")
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("Ar")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("R")
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("Ag")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("G")
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("Ab")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("Aa")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("Br")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("R")
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("Bg")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("G")
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("Bb")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("Ba")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("maskCheck")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("mask")
        del param

    del lastNode
    # End of node "Shadertoy2_2"

    # Start of node "mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("mask")
    lastNode.setLabel("mask")
    lastNode.setPosition(3982, 3845)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupmask = lastNode

    del lastNode
    # End of node "mask"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupShadertoy2_2)
    groupShadertoy2_2.connectInput(0, groupB)
    groupShadertoy2_2.connectInput(1, groupA)
    groupShadertoy2_2.connectInput(2, groupmask)

    param = groupShadertoy2_2.getParam("paramValueFloat0")
    group.getParam("Shadertoy2_2paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool1")
    group.getParam("Shadertoy2_2paramValueBool1").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool2")
    group.getParam("Shadertoy2_2paramValueBool2").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool3")
    group.getParam("Shadertoy2_2paramValueBool3").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool4")
    group.getParam("Shadertoy2_2paramValueBool4").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool5")
    group.getParam("Shadertoy2_2paramValueBool5").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool6")
    group.getParam("Shadertoy2_2paramValueBool6").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool7")
    group.getParam("Shadertoy2_2paramValueBool7").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool8")
    group.getParam("Shadertoy2_2paramValueBool8").setAsAlias(param)
    del param
    param = groupShadertoy2_2.getParam("paramValueBool9")
    group.getParam("Shadertoy2_2paramValueBool9").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Screen_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)

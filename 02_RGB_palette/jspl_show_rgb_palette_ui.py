import maya.cmds as cmds

#_____________SANITIZE
def jspl_sanitize_radius_input(*args):
    """
    Ensure radius input uses dot instead of comma.
    """
    text = cmds.textField("radiusField", query=True, text=True)
    new_text = text.replace(",", ".")
    if text != new_text:
        cmds.textField("radiusField", edit=True, text=new_text)

#_____________APPLY_COLOR
def jspl_apply_rgb_color(r, g, b, *args):
    """
    Apply RGB color and optional radius to selected joints.
    """
    selected = cmds.ls(selection=True, type='joint')
    if not selected:
        cmds.warning("No joints selected.")
        return

    use_radius = cmds.checkBox("useRadiusCheck", query=True, value=True)

    if use_radius:
        try:
            radius_text = cmds.textField("radiusField", query=True, text=True)
            radius = float(radius_text.replace(",", "."))
        except ValueError:
            cmds.warning("Enter a valid number for radius.")
            return

    for joint in selected:
        cmds.setAttr(joint + ".overrideEnabled", 1)
        cmds.setAttr(joint + ".overrideRGBColors", 1)
        cmds.setAttr(joint + ".overrideColorRGB", r, g, b, type="double3")

        if use_radius:
            cmds.setAttr(joint + ".radius", radius)

    if use_radius:
        print("Applied color: RGB({}, {}, {}), radius = {}".format(r, g, b, radius))
    else:
        print("Applied color only: RGB({}, {}, {})".format(r, g, b))

#_____________PREVIEW
def jspl_update_preview_color(*args):
    """
    Update preview box according to slider values.
    """
    r = cmds.floatSlider("rSlider", query=True, value=True)
    g = cmds.floatSlider("gSlider", query=True, value=True)
    b = cmds.floatSlider("bSlider", query=True, value=True)
    cmds.text("previewText", edit=True, bgc=(r, g, b))

#_____________APPLY_FROM_SLIDERS
def jspl_apply_from_sliders(*args):
    """
    Apply RGB color from custom sliders.
    """
    r = cmds.floatSlider("rSlider", query=True, value=True)
    g = cmds.floatSlider("gSlider", query=True, value=True)
    b = cmds.floatSlider("bSlider", query=True, value=True)
    jspl_apply_rgb_color(r, g, b)

#_____________RESET
def jspl_reset_color(*args):
    """
    Reset color override and UI settings to defaults.
    """
    selected = cmds.ls(selection=True, type='joint')
    if not selected:
        cmds.warning("No joints selected to reset color.")
        return

    for joint in selected:
        cmds.setAttr(joint + ".overrideEnabled", 0)
        cmds.setAttr(joint + ".overrideRGBColors", 0)

    cmds.floatSlider("rSlider", edit=True, value=1.0)
    cmds.floatSlider("gSlider", edit=True, value=1.0)
    cmds.floatSlider("bSlider", edit=True, value=1.0)
    cmds.text("previewText", edit=True, bgc=(1, 1, 1))
    cmds.textField("radiusField", edit=True, text="1.0")
    cmds.checkBox("useRadiusCheck", edit=True, value=True)

    print("Color reset and default radius restored.")

#_____________TOGGLE_RADIUS
def jspl_toggle_radius_field(*args):
    """
    Enable or disable radius field based on checkbox.
    """
    state = cmds.checkBox("useRadiusCheck", query=True, value=True)
    cmds.textField("radiusField", edit=True, enable=state)

#_____________UI
def jspl_show_rgb_palette_ui():
    if cmds.window("rgbPaletteWin", exists=True):
        cmds.deleteUI("rgbPaletteWin")

    cmds.window("rgbPaletteWin", title="RGB Joint Palette", widthHeight=(340, 680))
    cmds.columnLayout(adjustableColumn=True)

    cmds.separator(height=10, style='in')

    #_____________UI Radius controls
    cmds.rowLayout(numberOfColumns=3, adjustableColumn=3)
    cmds.checkBox("useRadiusCheck", label="Enable radius editing", value=True, changeCommand=jspl_toggle_radius_field)
    cmds.text(label="Radius:")
    cmds.textField("radiusField", text="1.5", changeCommand=jspl_sanitize_radius_input)
    cmds.setParent("..")

    cmds.separator(height=10, style='in')

    #_____________UI Color palette
    cmds.gridLayout(numberOfColumns=5, cellWidthHeight=(40, 40))

    rgb_colors = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 0.5, 0), (1, 1, 1), (0.5, 0.5, 0.5),
        (0, 0, 0), (0.9, 0.7, 0.8), (0.4, 0.2, 0.0),
        (0.6, 0.0, 0.8), (0.3, 0.6, 1.0), (0.6, 1.0, 0.8)
    ]

    for r, g, b in rgb_colors:
        cmds.button(
            label="",
            backgroundColor=(r, g, b),
            command=lambda x, r=r, g=g, b=b: jspl_apply_rgb_color(r, g, b)
        )

    cmds.setParent("..")
    cmds.separator(height=15, style='in')

    #_____________UI Custom color sliders
    cmds.frameLayout(label="Custom color (RGB)", collapsable=False, marginWidth=10, marginHeight=10)
    cmds.columnLayout(adjustableColumn=True)

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.text(label="R:")
    cmds.floatSlider("rSlider", min=0.0, max=1.0, value=1.0, step=0.01, changeCommand=jspl_update_preview_color)
    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.text(label="G:")
    cmds.floatSlider("gSlider", min=0.0, max=1.0, value=1.0, step=0.01, changeCommand=jspl_update_preview_color)
    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.text(label="B:")
    cmds.floatSlider("bSlider", min=0.0, max=1.0, value=1.0, step=0.01, changeCommand=jspl_update_preview_color)
    cmds.setParent("..")

    cmds.separator(height=10)
    cmds.text("previewText", label="", height=50, align="center", bgc=(1, 1, 1))
    cmds.separator(height=10)

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.button(label="Apply", height=30, command=jspl_apply_from_sliders)
    cmds.button(label="Reset", height=30, command=jspl_reset_color)
    cmds.setParent("..")

    cmds.setParent("..")
    cmds.setParent("..")

    cmds.separator(height=10, style='in')

    cmds.showWindow("rgbPaletteWin")

#_____________RUN
jspl_show_rgb_palette_ui()

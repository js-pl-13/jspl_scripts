import maya.cmds as cmds

#_____________jspl rename tool optimized
class jspl_RenameTool:
    def __init__(self):
        self.win = cmds.window(title="jsplTools_Rename", widthHeight=(260, 400), sizeable=False)
        cmds.columnLayout()

        #_____________UI separator
        cmds.rowLayout(numberOfColumns=1)
        cmds.separator(width=265, height=5)
        cmds.setParent("..")

        #_____________UI search field
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Search: ", width=45, align="right")
        self.inputSearch = cmds.textField(text="", width=210, placeholderText="Enter text to search (left_)")
        cmds.setParent("..")

        #_____________UI replace field
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Replace:", width=45, align="right")
        self.inputReplace = cmds.textField(width=210, placeholderText="Enter replacement text (right_)")
        cmds.setParent("..")

        #_____________UI quick search/replace buttons
        cmds.rowLayout(numberOfColumns=4)
        cmds.button(label="left -> right", height=25, width=65, command=lambda *args: self.search_replace("left_"))
        cmds.button(label="right -> left", height=25, width=65, command=lambda *args: self.search_replace("right_"))
        cmds.button(label="l -> r", height=25, width=45, command=lambda *args: self.search_replace("l_"))
        cmds.button(label="r -> l", height=25, width=45, command=lambda *args: self.search_replace("r_"))
        cmds.setParent("..")

        #_____________UI run search/replace
        cmds.rowLayout(numberOfColumns=2)
        cmds.button(label="Search and Replace", width=255, command=lambda *args: self.rename_objects(mode=0))
        cmds.setParent("..")

        #_____________UI separator
        cmds.rowLayout(numberOfColumns=1)
        cmds.separator(width=260, height=10)
        cmds.setParent("..")

        #_____________UI prefix input
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Prefix:", width=45, align="right")
        self.inputPrefix = cmds.textField(width=210, placeholderText="Enter prefix")
        cmds.setParent("..")

        #_____________UI quick prefix buttons
        cmds.rowLayout(numberOfColumns=5)
        cmds.button(label="left_", height=25, width=49, command=lambda *args: self.add_prefix("left_"))
        cmds.button(label="right_", height=25, width=49, command=lambda *args: self.add_prefix("right_"))
        cmds.button(label="l_", height=25, width=49, command=lambda *args: self.add_prefix("l_"))
        cmds.button(label="r_", height=25, width=49, command=lambda *args: self.add_prefix("r_"))
        cmds.setParent("..")

        #_____________UI run prefix
        cmds.rowLayout(numberOfColumns=2)
        cmds.button(label="Add Prefix", width=254, command=lambda *args: self.rename_objects(mode=1))
        cmds.setParent("..")

        #_____________UI separator
        cmds.rowLayout(numberOfColumns=1)
        cmds.separator(width=260, height=10)
        cmds.setParent("..")

        #_____________UI suffix input
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Suffix:", width=45, align="right")
        self.inputSuffix = cmds.textField(width=210, placeholderText="Enter suffix")
        cmds.setParent("..")

        #_____________UI quick suffix buttons
        cmds.rowLayout(numberOfColumns=6)
        cmds.button(label="_ctrl", height=25, width=49, command=lambda *args: self.add_suffix("_ctrl"))
        cmds.button(label="_grp", height=25, width=49, command=lambda *args: self.add_suffix("_grp"))
        cmds.button(label="_jiggle", height=25, width=49, command=lambda *args: self.add_suffix("_jiggle"))
        cmds.button(label="_end", height=25, width=49, command=lambda *args: self.add_suffix("_end"))
        cmds.setParent("..")

        #_____________UI run suffix
        cmds.rowLayout(numberOfColumns=2)
        cmds.button(label="Add Suffix", width=254, command=lambda *args: self.rename_objects(mode=2))
        cmds.setParent("..")

        #_____________UI separator
        cmds.rowLayout(numberOfColumns=1)
        cmds.separator(width=260, height=10)
        cmds.setParent("..")

        #_____________UI rename input
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Rename:", width=45, align="right")
        self.inputRename = cmds.textField(text="", width=210, placeholderText="Enter new name")
        cmds.setParent("..")

        #_____________UI start number
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Start#:", width=45, align="right")
        self.inputStart = cmds.intField(width=210, value=1)
        cmds.setParent("..")

        #_____________UI padding
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Padding:", width=45)
        self.inputPadding = cmds.intField(width=210)
        cmds.setParent("..")

        #_____________UI run rename-number
        cmds.rowLayout(numberOfColumns=2)
        cmds.button(label="Rename And Number", width=255, command=lambda *args: self.rename_objects(mode=3))
        cmds.setParent("..")

        #_____________UI separator
        cmds.rowLayout(numberOfColumns=1)
        cmds.separator(width=260, height=10)
        cmds.setParent("..")

        cmds.showWindow(self.win)

    #_____________search and replace helper
    def search_replace(self, pattern):
        """
        Fills search and replace fields based on quick buttons.
        """
        cmds.textField(self.inputSearch, e=True, text=pattern)
        if pattern == "left_":
            cmds.textField(self.inputReplace, e=True, text="right_")
        elif pattern == "right_":
            cmds.textField(self.inputReplace, e=True, text="left_")
        elif pattern == "l_":
            cmds.textField(self.inputReplace, e=True, text="r_")
        elif pattern == "r_":
            cmds.textField(self.inputReplace, e=True, text="l_")

    #_____________add prefix
    def add_prefix(self, prefix):
        """
        Add prefix to selected objects.
        """
        objs = cmds.ls(sl=True, long=True)
        if not objs:
            cmds.warning("No objects selected!")
            return
        for obj in objs:
            try:
                cmds.rename(obj, prefix + obj.split("|")[-1])
            except RuntimeError as e:
                cmds.warning("Failed to rename {}: {}".format(obj, e))

    #_____________add suffix
    def add_suffix(self, suffix):
        """
        Add suffix to selected objects.
        """
        objs = cmds.ls(sl=True, long=True)
        if not objs:
            cmds.warning("No objects selected!")
            return
        for obj in objs:
            try:
                short = obj.split("|")[-1]
                cmds.rename(obj, short + suffix)
            except RuntimeError as e:
                cmds.warning("Failed to rename {}: {}".format(obj, e))

    #_____________general rename handler
    def rename_objects(self, mode):
        """
        Main renaming logic:
        0 = search/replace
        1 = prefix
        2 = suffix
        3 = rename + number
        """
        objs = cmds.ls(sl=True, long=True)
        if not objs:
            cmds.warning("No objects selected!")
            return

        search = cmds.textField(self.inputSearch, q=True, text=True)
        replace = cmds.textField(self.inputReplace, q=True, text=True)
        prefix = cmds.textField(self.inputPrefix, q=True, text=True)
        suffix = cmds.textField(self.inputSuffix, q=True, text=True)
        rename = cmds.textField(self.inputRename, q=True, text=True)
        start = cmds.intField(self.inputStart, q=True, value=True)
        padding = cmds.intField(self.inputPadding, q=True, value=True)

        for i, obj in enumerate(objs):
            short = obj.split("|")[-1]

            if mode == 0:
                if not search:
                    cmds.warning("Search field is empty!")
                    return
                new = short.replace(search, replace)

            elif mode == 1:
                if not prefix:
                    cmds.warning("Prefix field is empty!")
                    return
                new = prefix + short

            elif mode == 2:
                if not suffix:
                    cmds.warning("Suffix field is empty!")
                    return
                new = short + suffix

            elif mode == 3:
                if not rename:
                    cmds.warning("Rename field is empty!")
                    return
                num = str(start + i).zfill(padding)
                new = rename + num

            try:
                cmds.rename(obj, new)
            except RuntimeError as e:
                cmds.warning("Failed to rename {}: {}".format(obj, e))


jspl_RenameTool()

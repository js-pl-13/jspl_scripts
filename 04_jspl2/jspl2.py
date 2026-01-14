import maya.cmds as cmds
import json
import io
import os

# deleting a namespace
def remove_namespace(object_name):
    if ":" in object_name:
        return object_name.split(":")[-1]
    return object_name
    
def remove_object_namespace(object_name):
    if ":" in object_name:
        namespace = object_name.split(":")[0]
        if cmds.namespace(exists=namespace):
            cmds.namespace(removeNamespace=namespace)
            print("namespace for the object has been deleted: %s" % object_name)

# Exporting transformations
def export_joint_transformations():
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.error("select at least one joint")
    
    joint_data = {}
    for joint in selected_joints:
        joint_name = remove_namespace(joint)
        translation = cmds.getAttr("{}.translate".format(joint))[0]
        rotation = cmds.getAttr("{}.rotate".format(joint))[0]
        joint_data[joint_name] = {
            "translation": {"x": translation[0], "y": translation[1], "z": translation[2]},
            "rotation": {"x": rotation[0], "y": rotation[1], "z": rotation[2]}
        }

    file_path = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=0)
    if file_path:
        with open(file_path[0], 'w') as f:
            json.dump(joint_data, f, indent=4)
        cmds.informDialog(message="Export is completed! file is saved on: %s" % file_path[0], button="OK")
    else:
        cmds.error("save path is not selected.")

def export_temp_joint_transformations():
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.error("select at least one joint.")
    
    joint_data = {}
    for joint in selected_joints:
        joint_name = remove_namespace(joint)
        translation = cmds.getAttr("{}.translate".format(joint))[0]
        rotation = cmds.getAttr("{}.rotate".format(joint))[0]
        joint_data[joint_name] = {
            "translation": {"x": translation[0], "y": translation[1], "z": translation[2]},
            "rotation": {"x": rotation[0], "y": rotation[1], "z": rotation[2]}
        }

    directory = r"C:\Users\vpushkarev\Desktop\ANIMS_IMP\temp"
    if not os.path.exists(directory):
        os.makedirs(directory)

    output_path = os.path.join(directory, "joint_export.json")
    try:
        with open(output_path, 'w') as f:
            json.dump(joint_data, f, indent=4)
        print("Export is completed! file is saved on: {}".format(output_path))
    except Exception as e:
        cmds.error("Error saving the file: {}".format(str(e)))

# Unblocking attributes
def unlock_attribute(attribute):
    if cmds.getAttr(attribute, lock=True):
        cmds.setAttr(attribute, lock=False)
        print(u"attribute is unlocked: %s" % attribute)

# Application 
def apply_joint_transformations(joint_data=None):
    if joint_data is None:
        file_path = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=1)
        if not file_path:
            cmds.error(u"The file to import is not selected.")
        try:
            with io.open(file_path[0], 'r', encoding='utf-8') as f:
                joint_data = json.load(f)
        except Exception as e:
            cmds.error(u"Error when uploading a file: %s" % str(e))
            return
    
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.error(u"select at least one joint.")
    
    for joint in selected_joints:
        joint_name = remove_namespace(joint)
        if joint_name in joint_data:
            translation = joint_data[joint_name]["translation"]
            rotation = joint_data[joint_name]["rotation"]
            unlock_attribute("{}.translateX".format(joint))
            unlock_attribute("{}.translateY".format(joint))
            unlock_attribute("{}.translateZ".format(joint))
            unlock_attribute("{}.rotateX".format(joint))
            unlock_attribute("{}.rotateY".format(joint))
            unlock_attribute("{}.rotateZ".format(joint))
            cmds.setAttr("{}.translate".format(joint), translation["x"], translation["y"], translation["z"])
            cmds.setAttr("{}.rotate".format(joint), rotation["x"], rotation["y"], rotation["z"])
            print(u"Transformations have been applied for the joint: %s" % joint)
        else:
            print(u"The joint was not found in the JSON file: %s" % joint)
    cmds.keyTangent(ott='step', animation='objects', g=True)

def apply_temp_joint_transformations(joint_data=None):
    file_path = r"C:\Users\vpushkarev\Desktop\ANIMS_IMP\temp\joint_export.json"
    if not os.path.exists(file_path):
        cmds.error(u"File not found: {}".format(file_path))
    try:
        with io.open(file_path, 'r', encoding='utf-8') as f:
            joint_data = json.load(f)
    except Exception as e:
        cmds.error(u"Error when uploading a file: {}".format(str(e)))
        return

    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.error(u"select at least one joint.")
    
    for joint in selected_joints:
        joint_name = remove_namespace(joint)
        if joint_name in joint_data:
            translation = joint_data[joint_name]["translation"]
            rotation = joint_data[joint_name]["rotation"]
            unlock_attribute("{}.translateX".format(joint))
            unlock_attribute("{}.translateY".format(joint))
            unlock_attribute("{}.translateZ".format(joint))
            unlock_attribute("{}.rotateX".format(joint))
            unlock_attribute("{}.rotateY".format(joint))
            unlock_attribute("{}.rotateZ".format(joint))
            cmds.setAttr("{}.translate".format(joint), translation["x"], translation["y"], translation["z"])
            cmds.setAttr("{}.rotate".format(joint), rotation["x"], rotation["y"], rotation["z"])
            print(u"Transformations have been applied for the joint: {}".format(joint))
        else:
            print(u"The joint was not found in the JSON file: {}".format(joint))

# setKeyframe
def key_all_keyable():
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.error("select at least one joint.")
    for obj in selected_objects:
        keyable_attrs = cmds.listAttr(obj, keyable=True)
        if keyable_attrs:
            cmds.setKeyframe(obj, attribute=keyable_attrs)
        else:
            print(u"no key attributes for the object: %s" % obj)


def import_wwz_aim_sequence():
    base_dir = r"C:\Users\vpushkarev\Desktop\ANIMS_IMP\amber\npc"
    # edit list, add or remove ##
    file_list = [
        "npc_charles_wpn0_loco_calm_idle_v02_1.json",
        "npc_charles_wpn0_loco_crouch_run_4m5_v01.json",
        "npc_charles_creeper_wall_up_move_step_l_v01.json",
        "npc_charles_wpn0_loco_run_6m_v01.json",
        "npc_charles_wpn0_loco_jogging_3m2_v01.json",
        "npc_charles_wpn0_loco_walk_1m6_v02.json",
        "npc_charles_to_consider.json",
        "npc_charles_wpn0_loco_calm_idle_v01.json",
        #"START_RUN_FWD.json"
    ]

    start_frame = 5
    frame_step = 10

    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.error(u"select at least one joint before importing.")

    for i, file_name in enumerate(file_list):
        frame = start_frame + i * frame_step
        file_path = os.path.join(base_dir, file_name)

        if not os.path.isfile(file_path):
            print(u"File not found: %s" % file_path)
            continue

        try:
            with io.open(file_path, 'r', encoding='utf-8') as f:
                joint_data = json.load(f)

            cmds.currentTime(frame, edit=True)

            for joint in selected_joints:
                joint_name = remove_namespace(joint)
                if joint_name in joint_data:
                    translation = joint_data[joint_name]["translation"]
                    rotation = joint_data[joint_name]["rotation"]

                    unlock_attribute("{}.translateX".format(joint))
                    unlock_attribute("{}.translateY".format(joint))
                    unlock_attribute("{}.translateZ".format(joint))
                    unlock_attribute("{}.rotateX".format(joint))
                    unlock_attribute("{}.rotateY".format(joint))
                    unlock_attribute("{}.rotateZ".format(joint))

                    cmds.setAttr("{}.translate".format(joint), translation["x"], translation["y"], translation["z"])
                    cmds.setAttr("{}.rotate".format(joint), rotation["x"], rotation["y"], rotation["z"])

                    keyable_attrs = cmds.listAttr(joint, keyable=True)
                    if keyable_attrs:
                        cmds.setKeyframe(joint, attribute=keyable_attrs)

            print(u"Imported file %s frame %d" % (file_name, frame))

        except Exception as e:
            cmds.error(u"Error when uploading %s: %s" % (file_path, str(e)))
    cmds.keyTangent(ott='step', animation='objects', g=True)




# UI
def create_joint_transforms_window():
    if cmds.window("jointTransformsWindow", exists=True):
        cmds.deleteUI("jointTransformsWindow", window=True)

    window = cmds.window("jointTransformsWindow", title="jsp_TransformTool", widthHeight=(260, 400), sizeable=False)
    cmds.columnLayout(adjustableColumn=True)
    cmds.separator(width=265, height=5)
    cmds.button(label="Copy to temp file", command=lambda x: export_temp_joint_transformations())
    cmds.button(label="Paste to temp file", command=lambda x: apply_temp_joint_transformations())
    cmds.separator(width=265, height=5)
    cmds.button(label="Export transform to file", command=lambda x: export_joint_transformations())
    cmds.button(label="Import transform to file", command=lambda x: apply_joint_transformations())
    cmds.button(label="Key All Keyable", command=lambda x: key_all_keyable())
    cmds.separator(width=265, height=5)

    #
    cmds.button(label="Import anim list", command=lambda x: import_wwz_aim_sequence())
    cmds.separator(width=265, height=5)

    cmds.frameLayout(label="Fast import", collapsable=True, collapse=False)
    cmds.columnLayout(adjustableColumn=True)
    cmds.setParent("..")

    cmds.columnLayout(adjustableColumn=True)
    cmds.frameLayout(label="Fast import WWZ anims", collapsable=True, collapse=True)
    cmds.separator(width=265, height=5)
    cmds.rowLayout(numberOfColumns=4)
    cmds.button(label="Bind", height=25, width=70, command=lambda x: import_wwz_bind_pose())
    cmds.button(label="Top_aim", height=25, width=70, command=lambda x: import_wwz_aim_top())
    cmds.button(label="test", height=25, width=70, command=lambda x: import_wwz_aim_top())
    cmds.button(label="test2", height=25, width=70, command=lambda x: import_wwz_aim_top())
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=4)
    cmds.button(label="test3", height=25, width=70, command=lambda x: import_wwz_bind_pose())
    cmds.button(label="test4", height=25, width=70, command=lambda x: import_wwz_aim_top())
    cmds.button(label="test5", height=25, width=70, command=lambda x: import_wwz_aim_top())
    cmds.button(label="test6", height=25, width=70, command=lambda x: import_wwz_aim_top())
    cmds.setParent("..")
    cmds.separator(width=265, height=5)
    cmds.setParent("..")

    cmds.frameLayout(label="Fast import Thunder anims", collapsable=True, collapse=True)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Bind pose", command=lambda x: import_thunder_bind_pose())
    cmds.setParent("..")

    cmds.showWindow(window)

####_____WWZ____###
def import_wwz_bind_pose():
    file_path = r"C:\Users\vpushkarev\Desktop\ANIMS_IMP\wwz\bind.json"
    if not os.path.isfile(file_path):
        cmds.error(u"file was not found on the way: %s" % file_path)
    try:
        with io.open(file_path, 'r', encoding='utf-8') as f:
            joint_data = json.load(f)
        print(u"file %s uploaded successfully." % file_path)
        apply_joint_transformations(joint_data)
        cmds.informDialog(message="successfully imported!", button="OK")
    except Exception as e:
        cmds.error(u"Error when uploading a file: %s" % str(e))

def import_wwz_aim_top():
    file_path = r"C:\Users\vpushkarev\Desktop\ANIMS_IMP\wwz\aim_top.json"
    if not os.path.isfile(file_path):
        cmds.error(u"file was not found on the way: %s" % file_path)
    try:
        with io.open(file_path, 'r', encoding='utf-8') as f:
            joint_data = json.load(f)
        print(u"file %s uploaded successfully." % file_path)
        apply_joint_transformations(joint_data)
        cmds.informDialog(message="successfully imported!", button="OK")
    except Exception as e:
        cmds.error(u"Error when uploading a file: %s" % str(e))

####_____Thunder____###
def import_thunder_bind_pose():
    file_path = r"C:\Users\vpushkarev\Desktop\ANIMS_IMP\thunder\bind.json"
    if not os.path.isfile(file_path):
        cmds.error(u"file was not found on the way: %s" % file_path)
    try:
        with io.open(file_path, 'r', encoding='utf-8') as f:
            joint_data = json.load(f)
        print(u"file %s uploaded successfully." % file_path)
        apply_joint_transformations(joint_data)
        cmds.informDialog(message="successfully imported!", button="OK")
    except Exception as e:
        cmds.error(u"Error when uploading a file: %s" % str(e))


create_joint_transforms_window()

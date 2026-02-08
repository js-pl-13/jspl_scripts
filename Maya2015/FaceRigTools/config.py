# -*- coding: utf-8 -*-

WINDOW_NAME = "FaceRigPipelineWindow"
LIST_WINDOW_NAME = "GeneratedBSListWindow"
DEFAULT_MAX_INF = 4
EXPORT_PATH = "D:/data_scripts/face_rig/"
EXPORT_FILE = "locators_data.json"

BS_DICT = {
    'lBrow_UP': 1, 'lBrow_DW': -1, 'rBrow_UP': 1, 'rBrow_DW': -1,
    'lBrowEvel_UP': 1, 'lBrowEvel_DW': -1, 'rBrowEvel_UP': 1,
    'rBrowEvel_DW': -1, 'lSuspect': 1, 'rSuspect': 1, 'lEyelid_UP': 1,
    'lEyelid_DW': -1, 'rEyelid_UP': 1, 'rEyelid_DW': -1, 'nose': 1,
    'lSquint': 1, 'rSquint': 1, 'lDogUp': 1, 'rDogUp': 1, 'lDogDw': 1,
    'rDogDw': 1, 'LipLowerUp': 1, 'LipLowerDw': 1, 'LipLowerDw_UP': -1,
    'LipLowerUp_UP': -1, 'lLip_OU': 0.7, 'lLip_IN': -1, 'lLip_UP': 1,
    'lLip_DW': -1, 'rLip_OU': 0.7, 'rLip_IN': -1, 'rLip_UP': 1, 'rLip_DW': -1,
    'cLip_UP': 1, 'cLip_DW': -1, 'Chin': -1, 'NeckApple': 1, 'NeckMuscle': -1,
    'lKiss_OU': 1, 'rKiss_OU': 1
}

ORDERED_NAMES = [
    "rBrowEvel_UP", "lBrowEvel_DW", "rSuspect", "lSuspect", "rBrow_UP", 
    "rLip_DW", "rBrowEvel_DW", "lEyelid_DW", "rLip_IN", "LipLowerDw_UP", 
    "rSquint", "LipLowerUp", "lEyelid_UP", "NeckApple", "LipLowerUp_UP", 
    "rEyelid_UP", "rDogUp", "lDogDw", "lLip_DW", "LipLowerDw", 
    "lLip_IN", "lBrow_UP", "cLip_DW", "cLip_UP", "rLip_OU", 
    "lBrowEvel_UP", "rDogDw", "lLip_UP", "Chin", "nose", 
    "lDogUp", "rLip_UP", "lBrow_DW", "lSquint", "rBrow_DW", 
    "rEyelid_DW", "NeckMuscle", "lLip_OU", "lKiss_OU", "rKiss_OU"
]

CONTROLLERS_LIST = [ 
    'cLip_CT', 'LipLowerUp_CT', 'LipLowerDw_CT', 'nose_CT', 
    'Chin_CT', 'NeckApple_CT', 'NeckMuscle_CT', 'lBrowEvel_CT', 
    'lBrow_CT', 'lSuspect_CT', 'lLip_CT', 'lDogUp_CT', 
    'lDogDw_CT', 'lEyelid_CT', 'lSquint_CT', 'rBrowEvel_CT', 
    'rBrow_CT', 'rSuspect_CT', 'rLip_CT', 'rDogDw_CT', 
    'rDogUp_CT', 'rEyelid_CT', 'rSquint_CT', 'lKiss_CT', 'rKiss_CT' 
]
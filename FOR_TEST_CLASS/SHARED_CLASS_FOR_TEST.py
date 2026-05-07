properties   =   {
   geom   =   {
      nameTpl   =   "cc_sm_constructor_raider"
   }
   prop_character_tags   =   {
      tags   =   {
         CLASS   =   {
            __value   =   "MARINE_RAIDER"
            __type   =   "CharacterTag"
         }
      }
   }
   prop_morpheme_controller   =   {
      morphemeController   =   {
         animSet   =   "raider"
         __type   =   "MorphemeController"
      }
   }
   prop_blueprints   =   {
      blueprints   =   {
         JETPACK_EFFECTS   =   {
            __type   =   "BlueprintJetpackEffects"
         }
         SOUND_MARINE_CAMO_CLOAK   =   {
            __type   =   "BlueprintMarineSoundCamoCloak"
         }
         VFX_MARINE_CAMOUFLAGE   =   {
            __type   =   "BlueprintMarineVfxCamouflage"
         }
         VFX_MARINE_POWER_FIST   =   {
            __type   =   "BlueprintMarineVfxPowerFist"
         }
         VFX_MARINE_POWER_SWORD   =   {
            __type   =   "BlueprintMarineVfxPowerSword"
         }
      }
   }
   sfx   =   {
      list   =   {
         fx_mgs_perk_raider_hot_tour   =   {
         }
      }
      __onlyOn   =   "visual"
   }
   prop_voiceover_speaker   =   {
      animList   =   "primaris/assault/lipsync/lipsync.animlist"
   }
   prop_character_view   =   {
      controllers   =   {
         StandingMode   =   {
            characterTypeMr   =   {
               value   =   4
               __type   =   "MorphemeFloat"
            }
            __type   =   "CharacterViewControllerStandingMode"
         }
      }
   }
   prop_geom_customizer_character   =   {
      characterInfo   =   {
         team   =   "LOYALIST"
         masteryType   =   "PVE_RAIDER"
         __type   =   "CharacterInfo"
      }
   }
   prop_character_customization_state_client   =   {
   }
   prop_power_fist_customizer_by_melee_state   =   {
   }
   prop_cloth_sim   =   {
      clothes   =   [
         {
            simMeshName   =   "raider_shin_L_01_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_L_01_seal_01"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.1
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shin_R_01_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_R_01_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   True
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shin_R_01_seal_02"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_R_01_seal_02"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_cuirasse_01_seal_02"
            renderMeshes   =   [
               {
                  name   =   "raider_cuirasse_01_seal_02"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_cuirasse_01_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_cuirasse_01_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shoulder_R_01_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_shoulder_R_01_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shoulder_L_03_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_shoulder_L_03_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_L"
                     boneFirst   =   "shoulder_L"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        -0.03
                     ]
                     boneSecond   =   "shoulder_L"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        0.25,
                        -0.01,
                        -0.03
                     ]
                  },
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_jetpack_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_jetpack_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "backpack"
                     bone   =   "powerplant_backpack"
                     radius   =   0.5
                     boneOffset   =   [
                        -0.25,
                        0,
                        -0.08
                     ]
                  },
                  {
                     name   =   "r_big_jet_cover"
                     bone   =   "r_big_jet_cover_skinned"
                     radius   =   0.22
                     boneOffset   =   [
                        -0.18,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "r_jet_small"
                     bone   =   "r_jet_small_up"
                     radius   =   0.13
                     boneOffset   =   [
                        -0.02,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "backpack"
                     bone   =   "powerplant_backpack"
                     radius   =   0.2
                     boneOffset   =   [
                        0.11,
                        0,
                        -0.07
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.4
                  airLift   =   0.5
                  localWindVelocity   =   [
                     1,
                     -10,
                     1
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               interCollision   =   True
            }
         },
         {
            simMeshName   =   "raider_jetpack_seal_02"
            renderMeshes   =   [
               {
                  name   =   "raider_jetpack_seal_02"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "backpack"
                     bone   =   "powerplant_backpack"
                     radius   =   0.5
                     boneOffset   =   [
                        -0.25,
                        0,
                        -0.08
                     ]
                  },
                  {
                     name   =   "l_big_jet_cover"
                     bone   =   "l_big_jet_cover_skinned"
                     radius   =   0.22
                     boneOffset   =   [
                        0.18,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "l_jet_small"
                     bone   =   "l_jet_small_up"
                     radius   =   0.13
                     boneOffset   =   [
                        0.02,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "backpack"
                     bone   =   "powerplant_backpack"
                     radius   =   0.2
                     boneOffset   =   [
                        0.11,
                        0,
                        -0.07
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.7
                  airLift   =   0.5
                  localWindVelocity   =   [
                     1,
                     -10,
                     1
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               interCollision   =   True
            }
         },
         {
            simMeshName   =   "raider_jetpack_seal_03"
            renderMeshes   =   [
               {
                  name   =   "raider_jetpack_seal_03"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "backpack"
                     bone   =   "powerplant_backpack"
                     radius   =   0.5
                     boneOffset   =   [
                        -0.25,
                        0,
                        -0.08
                     ]
                  },
                  {
                     name   =   "r_big_jet_cover"
                     bone   =   "r_big_jet_cover_skinned"
                     radius   =   0.22
                     boneOffset   =   [
                        -0.18,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "l_big_jet_cover"
                     bone   =   "l_big_jet_cover_skinned"
                     radius   =   0.22
                     boneOffset   =   [
                        0.18,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "r_jet_small"
                     bone   =   "r_jet_small_up"
                     radius   =   0.13
                     boneOffset   =   [
                        -0.02,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "backpack"
                     bone   =   "powerplant_backpack"
                     radius   =   0.2
                     boneOffset   =   [
                        0.11,
                        0,
                        -0.07
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.5
                  airLift   =   0.5
                  localWindVelocity   =   [
                     5,
                     -5,
                     5
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               stiffnessFrequencyScale   =   0.5
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               interCollision   =   True
               continuousCollision   =   False
            }
         },
         {
            simMeshName   =   "raider_jetpack_cloth_01_SIM"
            renderMeshes   =   [
               {
                  name   =   "raider_jetpack_cloth_01"
               }
            ]
            config   =   {
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -48,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "backpack"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.2
                     boneFirstOffset   =   [
                        0.05,
                        0,
                        -0.15
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        -0.15,
                        0,
                        -0.4
                     ]
                  },
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   True
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   30
               damping   =   0.4
            }
         },
         {
            simMeshName   =   "raider_hand_R_01_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_hand_R_01_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               stiffnessMultiplier   =   1
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.76
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               interCollision   =   False
               continuousCollision   =   False
            }
         },
         {
            simMeshName   =   "raider_shin_R_02_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_R_02_seal_01"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.1
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shin_R_02_seal_02"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_R_02_seal_02"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.1
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_cuirasse_02_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_cuirasse_02_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_cuirasse_03_seal_02"
            renderMeshes   =   [
               {
                  name   =   "raider_cuirasse_03_seal_02"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_cuirasse_03_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_cuirasse_03_seal_01"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "Spine"
                     boneFirst   =   "BACKup"
                     radiusFirst   =   0.42
                     boneFirstOffset   =   [
                        0,
                        -0.025,
                        0
                     ]
                     boneSecond   =   "BACKdown"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        -0.15,
                        0.03,
                        0
                     ]
                  },
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_cuirasse_02_seal_02"
            renderMeshes   =   [
               {
                  name   =   "raider_cuirasse_02_seal_02"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "pocket_jiggle"
                     boneFirst   =   "pocket_jiggle_01"
                     radiusFirst   =   0.105
                     boneFirstOffset   =   [
                        0.02,
                        -0.05,
                        0
                     ]
                     boneSecond   =   "pocket_jiggle_01"
                     radiusSecond   =   0.105
                     boneSecondOffset   =   [
                        0.025,
                        -0.15,
                        0
                     ]
                  },
                  {
                     name   =   "Spine"
                     boneFirst   =   "BACKup"
                     radiusFirst   =   0.4
                     boneFirstOffset   =   [
                        0.025,
                        -0.025,
                        0
                     ]
                     boneSecond   =   "BACKdown"
                     radiusSecond   =   0.26
                     boneSecondOffset   =   [
                        -0.15,
                        0.03,
                        0
                     ]
                  },
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shin_R_02_seal_03"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_R_02_seal_03"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.15
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "raider_shin_L_02_seal_01"
            renderMeshes   =   [
               {
                  name   =   "raider_shin_L_02_seal_01"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.1
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -9,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     8,
                     0,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   60
               friction   =   1
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "Shoulder_impfist_seal_01_REND"
            renderMeshes   =   [
               {
                  name   =   "Shoulder_impfist_seal_01_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.05
               distanceRemapPower   =   1
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -10,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.335
                     boneFirstOffset   =   [
                        -0.3,
                        0.01,
                        -0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.33
                     boneSecondOffset   =   [
                        0,
                        0,
                        -0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.19
                  airLift   =   0.27
                  localWindVelocity   =   [
                     0.5,
                     0.5,
                     8
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   160
               friction   =   0
               damping   =   0.08
               drag   =   {
                  linear   =   0.02
                  angular   =   0.1
               }
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "impfist_seal_01_T_REND"
            renderMeshes   =   [
               {
                  name   =   "impfist_seal_01_T_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.1
               distanceRemapPower   =   5
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -10,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.28
                  airLift   =   0.6
                  localWindVelocity   =   [
                     0.5,
                     0.5,
                     0
                  ]
                  useWindSystem   =   True
                  windSystemInfluenceScale   =   0.5
                  fluidDensity   =   2
               }
               solverFrequency   =   160
               friction   =   0
               damping   =   0.08
               drag   =   {
                  linear   =   0.02
                  angular   =   0.1
               }
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "impfist_seal_01_shoulder_L_REND"
            renderMeshes   =   [
               {
                  name   =   "impfist_seal_01_shoulder_L_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.05
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -10,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_L"
                     boneFirst   =   "shoulder_L"
                     radiusFirst   =   0.3
                     boneFirstOffset   =   [
                        0,
                        0,
                        -0.03
                     ]
                     boneSecond   =   "shoulder_L"
                     radiusSecond   =   0.275
                     boneSecondOffset   =   [
                        0.17,
                        -0.03,
                        -0.03
                     ]
                  },
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.19
                  airLift   =   0.47
                  localWindVelocity   =   [
                     0.5,
                     0.5,
                     8
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   160
               friction   =   0
               damping   =   0.08
               drag   =   {
                  linear   =   0.02
                  angular   =   0.1
               }
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "impfist_seal_01_REND"
            renderMeshes   =   [
               {
                  name   =   "impfist_seal_01_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.1
               distanceRemapPower   =   1
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -10,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_L"
                     boneFirst   =   "shoulder_L"
                     radiusFirst   =   0.3
                     boneFirstOffset   =   [
                        0,
                        0,
                        -0.03
                     ]
                     boneSecond   =   "shoulder_L"
                     radiusSecond   =   0.275
                     boneSecondOffset   =   [
                        0.17,
                        -0.03,
                        -0.03
                     ]
                  },
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.27
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.03
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.285
                     boneSecondOffset   =   [
                        -0.2,
                        0.02,
                        0.03
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.19
                  airLift   =   0.47
                  localWindVelocity   =   [
                     0.5,
                     0.5,
                     8
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.2
                  fluidDensity   =   2
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   160
               friction   =   0
               damping   =   0.08
               drag   =   {
                  linear   =   0.02
                  angular   =   0.1
               }
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "Plumage_SIM"
            renderMeshes   =   [
               {
                  name   =   "Plumage_01_REND"
               },
               {
                  name   =   "Plumage_02_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   6
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
                  stretchLimit   =   1
               }
               horizontal   =   {
                  stiffness   =   1
                  stretchLimit   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
                  stretchLimit   =   1
               }
               shear   =   {
                  stiffness   =   1
                  stretchLimit   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
                  distanceScale   =   0.13
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.025
               }
               gravity   =   [
                  0,
                  -30,
                  0
               ]
               environment   =   {
                  airDrag   =   0.38
                  airLift   =   0.25
                  localWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1.2
                  fluidDensity   =   1
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   120
               friction   =   0
               damping   =   0.15
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
            }
         },
         {
            simMeshName   =   "shoulder_cloth_challange_01_SIM"
            renderMeshes   =   [
               {
                  name   =   "shoulder_cloth_challange_01_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.3
               distanceRemapPower   =   5
               useTopologicalDistance   =   False
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
                  distanceScale   =   3
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.05
               }
               gravity   =   [
                  0,
                  -6,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ShoulderPad_R"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.31
                     boneFirstOffset   =   [
                        -0.3,
                        0,
                        0.09
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.2
                     boneSecondOffset   =   [
                        0.2,
                        0,
                        0.09
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.28
                  airLift   =   0.6
                  localWindVelocity   =   [
                     5,
                     0,
                     1.6
                  ]
                  useWindSystem   =   True
                  windSystemInfluenceScale   =   0.5
                  fluidDensity   =   2
               }
               solverFrequency   =   30
               collisionThickness   =   0.02
               friction   =   0
               damping   =   0.3
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "shoulder_R_poncho_01_SIM"
            renderMeshes   =   [
               {
                  name   =   "shoulder_R_poncho_01_RND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.25
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
                  scale   =   1.04
                  useTopologicalDistance   =   True
               }
               motion   =   {
                  enable   =   True
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.0325
               }
               gravity   =   [
                  0,
                  -40,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "shoulder_R_caps"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.2
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.007
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        -0.273,
                        0.052,
                        -0.017
                     ]
                  },
                  {
                     name   =   "ARM2R_caps"
                     boneFirst   =   "ARM2R"
                     radiusFirst   =   0.15
                     boneFirstOffset   =   [
                        0.044,
                        -0.051,
                        -0.009
                     ]
                     boneSecond   =   "ARM2R"
                     radiusSecond   =   0.13
                     boneSecondOffset   =   [
                        -0.423,
                        0,
                        0
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "shoulder_r_01"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.22
                     boneOffset   =   [
                        -0.21,
                        -0.035,
                        -0.003
                     ]
                  },
                  {
                     name   =   "shoulder_r_02"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.217
                     boneOffset   =   [
                        -0.081,
                        -0.01,
                        -0.015
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0
                  fluidDensity   =   0.1
               }
               solverFrequency   =   120
               collisionThickness   =   0.01
               friction   =   1
               damping   =   0.4
               drag   =   {
                  linear   =   0.08
                  angular   =   0.1
               }
            }
         },
         {
            simMeshName   =   "shoulder_R_poncho_02_SIM"
            renderMeshes   =   [
               {
                  name   =   "shoulder_R_poncho_02_RND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.25
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
                  scale   =   1.04
                  useTopologicalDistance   =   True
               }
               motion   =   {
                  enable   =   True
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.0325
               }
               gravity   =   [
                  0,
                  -40,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "shoulder_R_caps"
                     boneFirst   =   "shoulder_R"
                     radiusFirst   =   0.2
                     boneFirstOffset   =   [
                        0,
                        0,
                        0.007
                     ]
                     boneSecond   =   "shoulder_R"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        -0.273,
                        0.052,
                        -0.017
                     ]
                  },
                  {
                     name   =   "ARM2R_caps"
                     boneFirst   =   "ARM2R"
                     radiusFirst   =   0.15
                     boneFirstOffset   =   [
                        0.044,
                        -0.051,
                        -0.009
                     ]
                     boneSecond   =   "ARM2R"
                     radiusSecond   =   0.13
                     boneSecondOffset   =   [
                        -0.423,
                        0,
                        0
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "shoulder_r_01"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.22
                     boneOffset   =   [
                        -0.21,
                        -0.035,
                        -0.003
                     ]
                  },
                  {
                     name   =   "shoulder_r_02"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.217
                     boneOffset   =   [
                        -0.081,
                        -0.01,
                        -0.015
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0
                  fluidDensity   =   0.1
               }
               solverFrequency   =   120
               collisionThickness   =   0.01
               friction   =   1
               damping   =   0.4
               drag   =   {
                  linear   =   0.08
                  angular   =   0.1
               }
            }
         },
         {
            simMeshName   =   "blood_angels_champion_tabards_front_SIM"
            renderMeshes   =   [
               {
                  name   =   "blood_angels_champion_tabards_front_RND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.15
               distanceRemapPower   =   8
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   0.98
                  distance   =   0.08
               }
               stiffnessMultiplier   =   0.5
               gravity   =   [
                  0,
                  -18,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "Shin_L"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   0.21
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   0.31
                     boneSecondOffset   =   [
                        0,
                        -0.1,
                        0
                     ]
                  },
                  {
                     name   =   "HIP_R"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   0.26
                     boneSecondOffset   =   [
                        0.05,
                        0.025,
                        -0.02
                     ]
                  },
                  {
                     name   =   "Shin_R"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0,
                        -0.05,
                        -0.08
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   0.31
                  },
                  {
                     name   =   "HIP_L"
                     boneFirst   =   "LEG1L"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2L"
                     radiusSecond   =   0.2
                     boneSecondOffset   =   [
                        -0.05,
                        -0.05,
                        0.02
                     ]
                  },
                  {
                     name   =   "Centre_05"
                     boneFirst   =   "CENTRE"
                     radiusFirst   =   0.25
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "CENTRE"
                     radiusSecond   =   0.25
                     boneSecondOffset   =   [
                        -1,
                        0,
                        0
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "Leg_R"
                     bone   =   "LEG2R"
                     radius   =   0.16
                     boneOffset   =   [
                        0.19,
                        0.1,
                        0
                     ]
                  },
                  {
                     name   =   "Leg_L"
                     bone   =   "LEG2L"
                     radius   =   0.2
                     boneOffset   =   [
                        -0.13,
                        -0.06,
                        0
                     ]
                  },
                  {
                     name   =   "Centre_03"
                     bone   =   "CENTRE"
                     radius   =   0.13
                     boneOffset   =   [
                        -0.1,
                        0.11,
                        0
                     ]
                  }
               ]
               cdtBoxes   =   [
                  {
                     name   =   "block"
                     bone   =   "CENTRE"
                     size   =   [
                        3,
                        0.2,
                        1
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.28
                  airLift   =   0.6
                  localWindVelocity   =   [
                     0,
                     1,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1
                  fluidDensity   =   2
               }
               solverFrequency   =   160
               friction   =   0
               damping   =   0.08
               drag   =   {
                  linear   =   0.01
                  angular   =   0.01
               }
               interCollision   =   False
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "blood_angels_champion_tabards_back_SIM"
            renderMeshes   =   [
               {
                  name   =   "blood_angels_champion_tabards_back_RND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.16
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
                  stretchLimit   =   1.1
               }
               shear   =   {
                  stiffness   =   1
                  compressionLimit   =   0.9
                  stretchLimit   =   1.1
               }
               tether   =   {
                  stiffness   =   1
                  scale   =   1
               }
               motion   =   {
                  enable   =   True
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.08
               }
               stiffnessMultiplier   =   0.5
               gravity   =   [
                  0,
                  -16,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "Shin_L"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   0.24
                     boneFirstOffset   =   [
                        0,
                        0.05,
                        0.08
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   0.36
                     boneSecondOffset   =   [
                        0,
                        -0.1,
                        0
                     ]
                  },
                  {
                     name   =   "Shin_R"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   0.24
                     boneFirstOffset   =   [
                        0,
                        -0.05,
                        -0.08
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   0.36
                     boneSecondOffset   =   [
                        -0.1,
                        -0.05,
                        0
                     ]
                  },
                  {
                     name   =   "HIP_L"
                     boneFirst   =   "LEG1L"
                     radiusFirst   =   0.21
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2L"
                     radiusSecond   =   0.24
                     boneSecondOffset   =   [
                        -0.05,
                        -0.05,
                        0.02
                     ]
                  },
                  {
                     name   =   "HIP_R"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   0.2
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   0.26
                     boneSecondOffset   =   [
                        0.05,
                        0.025,
                        -0.02
                     ]
                  },
                  {
                     name   =   "Centre"
                     boneFirst   =   "CENTRE"
                     radiusFirst   =   0.2
                     boneFirstOffset   =   [
                        0,
                        -0.28,
                        0.25
                     ]
                     boneSecond   =   "CENTRE"
                     radiusSecond   =   0.2
                     boneSecondOffset   =   [
                        0,
                        -0.28,
                        0.3
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.5
                  airLift   =   0.6
                  localWindVelocity   =   [
                     -2,
                     -2,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.3
                  fluidDensity   =   1
               }
               solverFrequency   =   120
               collisionThickness   =   0
               friction   =   0
               damping   =   0.1
               drag   =   {
                  linear   =   0.02
                  angular   =   0.08
               }
               interCollision   =   False
               stiffnessFrequency   =   90
            }
         },
         {
            simMeshName   =   "rd_02_sh_feathers_SIM"
            renderMeshes   =   [
               {
                  name   =   "rd_02_sh_feathers_REND"
               }
            ]
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  enable   =   True
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.05
               }
               gravity   =   [
                  0,
                  -15,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "ARM1R_caps"
                     boneFirst   =   "shoulder_skinned_R"
                     radiusFirst   =   0.3
                     boneFirstOffset   =   [
                        -0.063,
                        0,
                        0.013
                     ]
                     boneSecond   =   "shoulder_skinned_R"
                     radiusSecond   =   0.38
                     boneSecondOffset   =   [
                        -0.422,
                        0.003,
                        0.13
                     ]
                  },
                  {
                     name   =   "shoulder_skinned_R2"
                     boneFirst   =   "shoulder_skinned_R"
                     radiusFirst   =   0.07
                     boneFirstOffset   =   [
                        -0.225,
                        0.062,
                        -0.225
                     ]
                     boneSecond   =   "shoulder_skinned_R"
                     radiusSecond   =   0.07
                     boneSecondOffset   =   [
                        -0.216,
                        0.147,
                        -0.2
                     ]
                  },
                  {
                     name   =   "shoulder_skinned_R3"
                     boneFirst   =   "shoulder_skinned_R"
                     radiusFirst   =   0.07
                     boneFirstOffset   =   [
                        -0.049,
                        -0.223,
                        -0.089
                     ]
                     boneSecond   =   "shoulder_skinned_R"
                     radiusSecond   =   0.07
                     boneSecondOffset   =   [
                        -0.27,
                        -0.304,
                        -0.1
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "shoulder_skinned_R_sph"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.07
                     boneOffset   =   [
                        -0.057,
                        0.273,
                        -0.028
                     ]
                  },
                  {
                     name   =   "shoulder_skinned_R_sph2"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.07
                     boneOffset   =   [
                        -0.073,
                        -0.278,
                        0.055
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.5
                  airLift   =   0.5
                  localWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  globalWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1
                  fluidDensity   =   1
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   120
               collisionThickness   =   0
               friction   =   0.05
               damping   =   0.15
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               collisionMassScale   =   20
            }
         },
         {
            simMeshName   =   "ironhands_seal_SIM"
            renderMeshes   =   [
               {
                  name   =   "ironhands_seal_REND"
               }
            ]
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -12,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "shoulder_skinned_R_caps1"
                     boneFirst   =   "shoulder_skinned_R"
                     radiusFirst   =   0.07
                     boneFirstOffset   =   [
                        -0.257,
                        -0.299,
                        0.052
                     ]
                     boneSecond   =   "shoulder_skinned_R"
                     radiusSecond   =   0.07
                     boneSecondOffset   =   [
                        -0.269,
                        -0.162,
                        -0.235
                     ]
                  },
                  {
                     name   =   "shoulder_skinned_R_caps2"
                     boneFirst   =   "shoulder_skinned_R"
                     radiusFirst   =   0.09
                     boneFirstOffset   =   [
                        0.122,
                        -0.255,
                        0.095
                     ]
                     boneSecond   =   "shoulder_skinned_R"
                     radiusSecond   =   0.09
                     boneSecondOffset   =   [
                        -0.095,
                        -0.295,
                        0.095
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "shoulder_skinned_R_sph"
                     bone   =   "shoulder_skinned_R"
                     radius   =   0.35
                     boneOffset   =   [
                        -0.176,
                        0.043,
                        0.091
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     -6.5,
                     -6.5,
                     -6.5
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.1
               }
               solverFrequency   =   160
               friction   =   0
               damping   =   0.08
               drag   =   {
                  linear   =   0.02
                  angular   =   0.1
               }
            }
         },
         {
            simMeshName   =   "coat_shared_snp_01_SIM"
            renderMeshes   =   [
               {
                  name   =   "coat_shared_snp_01_REND"
               }
            ]
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -25,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "L_shin"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "Torso"
                     boneFirst   =   "BACKup"
                     radiusFirst   =   0.41
                     boneFirstOffset   =   [
                        0.02,
                        0.05,
                        0
                     ]
                     boneSecond   =   "BACKdown"
                     radiusSecond   =   0.34
                  },
                  {
                     name   =   "backpack"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.4
                     boneFirstOffset   =   [
                        0.3,
                        0,
                        0.08
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.23
                     boneSecondOffset   =   [
                        0.05,
                        0,
                        -0.3
                     ]
                  },
                  {
                     name   =   "backpack_01"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.18
                     boneFirstOffset   =   [
                        0.04,
                        0.1,
                        -0.3
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.18
                     boneSecondOffset   =   [
                        0.04,
                        -0.1,
                        -0.3
                     ]
                  },
                  {
                     name   =   "R_shin"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "R_hip"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   0.25
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   0.25
                  },
                  {
                     name   =   " bugsLegR"
                     boneFirst   =   "HIP_R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.07,
                        -0.05,
                        -0.15
                     ]
                     boneSecond   =   "Shin_R_jiggle"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        0.5,
                        -0.2,
                        -0.15
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     0,
                     -2,
                     3
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.5
               }
               solverFrequency   =   120
               damping   =   0.15
               drag   =   {
                  linear   =   0.08
                  angular   =   0.15
               }
            }
         },
         {
            simMeshName   =   "coat_shared_snp_02_SIM"
            renderMeshes   =   [
               {
                  name   =   "coat_shared_snp_02_REND"
               }
            ]
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -25,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "L_shin"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "Torso"
                     boneFirst   =   "BACKup"
                     radiusFirst   =   0.41
                     boneFirstOffset   =   [
                        0.02,
                        0.05,
                        0
                     ]
                     boneSecond   =   "BACKdown"
                     radiusSecond   =   0.34
                  },
                  {
                     name   =   "backpack"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.4
                     boneFirstOffset   =   [
                        0.3,
                        0,
                        0.08
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.23
                     boneSecondOffset   =   [
                        0.05,
                        0,
                        -0.3
                     ]
                  },
                  {
                     name   =   "backpack_01"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.18
                     boneFirstOffset   =   [
                        0.04,
                        0.1,
                        -0.3
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.18
                     boneSecondOffset   =   [
                        0.04,
                        -0.1,
                        -0.3
                     ]
                  },
                  {
                     name   =   "R_shin"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "R_hip"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   0.25
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   0.25
                  },
                  {
                     name   =   " bugsLegR"
                     boneFirst   =   "HIP_R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.07,
                        -0.05,
                        -0.15
                     ]
                     boneSecond   =   "Shin_R_jiggle"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        0.5,
                        -0.2,
                        -0.15
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     0,
                     -2,
                     3
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.5
               }
               solverFrequency   =   120
               damping   =   0.15
               drag   =   {
                  linear   =   0.08
                  angular   =   0.15
               }
            }
         },
         {
            simMeshName   =   "coat_shared_cmp_snp_01_SIM"
            renderMeshes   =   [
               {
                  name   =   "coat_shared_cmp_snp_01_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.3
               useTopologicalDistance   =   True
            }
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -18,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "backpack"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.4
                     boneFirstOffset   =   [
                        0.3,
                        0,
                        0.08
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.23
                     boneSecondOffset   =   [
                        0.05,
                        0,
                        -0.3
                     ]
                  },
                  {
                     name   =   "backpack_01"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.18
                     boneFirstOffset   =   [
                        0.04,
                        0.1,
                        -0.3
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.18
                     boneSecondOffset   =   [
                        0.04,
                        -0.1,
                        -0.3
                     ]
                  },
                  {
                     name   =   "HIP_L"
                     boneFirst   =   "LEG1L"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2L"
                     radiusSecond   =   0.24
                  },
                  {
                     name   =   "HIP_R"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   0.23
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   0.24
                  },
                  {
                     name   =   "R_shin"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        -0.14,
                        -0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        -0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "L_shin"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   0.15
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   0.1
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   " bugsLegR"
                     boneFirst   =   "HIP_R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.07,
                        -0.05,
                        -0.15
                     ]
                     boneSecond   =   "Shin_R_jiggle"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        0.5,
                        -0.2,
                        -0.15
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "Centre"
                     bone   =   "CENTRE"
                     radius   =   0.33
                     boneOffset   =   [
                        -0.06,
                        0,
                        0
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     0,
                     -3,
                     -2
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.5
               }
               solverFrequency   =   200
               damping   =   0.08
               drag   =   {
                  linear   =   0.01
                  angular   =   0.05
               }
            }
         },
         {
            simMeshName   =   "coat_shared_feathers_01_SIM"
            renderMeshes   =   [
               {
                  name   =   "coat_shared_feathers_01_REND"
               }
            ]
            simRemapConfig   =   {
               maxInfluenceDist   =   0.2
            }
            config   =   {
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.045
               }
               gravity   =   [
                  0,
                  -15,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "BACKup_caps"
                     boneFirst   =   "BACKupS"
                     radiusFirst   =   1.35
                     boneFirstOffset   =   [
                        0.2,
                        0,
                        0
                     ]
                     boneSecond   =   "BACKdown"
                     radiusSecond   =   1.28
                     boneSecondOffset   =   [
                        -0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "hip_l"
                     boneFirst   =   "LEG1L"
                     radiusFirst   =   1.3
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2L"
                     radiusSecond   =   1.3
                     boneSecondOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "hip_r"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   1.3
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   1.3
                     boneSecondOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "shin_l"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   1.3
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   1.3
                     boneSecondOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "shin_r"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   1.3
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   1.3
                     boneSecondOffset   =   [
                        0,
                        0,
                        0
                     ]
                  }
               ]
               cdtSpheres   =   [
                  {
                     name   =   "CENTRE_sph"
                     bone   =   "CENTRE"
                     radius   =   1.3
                     boneOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "BACKup_sph"
                     bone   =   "BACKup"
                     radius   =   1.45
                     boneOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "BACKmiddle_sph"
                     bone   =   "BACKmiddle"
                     radius   =   1.25
                     boneOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "LEG1L_sph"
                     bone   =   "LEG1L"
                     radius   =   1.25
                     boneOffset   =   [
                        0,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "LEG1R_sph"
                     bone   =   "LEG1R"
                     radius   =   1.25
                     boneOffset   =   [
                        0,
                        0,
                        0
                     ]
                  }
               ]
               cdtBoxes   =   [
                  {
                     name   =   "powerplant_backpack_box_01"
                     bone   =   "powerplant_backpack"
                     size   =   [
                        0.2,
                        0.5,
                        0.9
                     ]
                  },
                  {
                     name   =   "powerplant_backpack_box_02"
                     bone   =   "powerplant_backpack"
                     size   =   [
                        0.2,
                        0.4,
                        1.1
                     ]
                  },
                  {
                     name   =   "Back_plate_jiggle_box"
                     bone   =   "Back_plate_jiggle"
                     size   =   [
                        0.414,
                        0.353,
                        0.161
                     ]
                  }
               ]
               environment   =   {
                  airDrag   =   0.5
                  airLift   =   0.5
                  localWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  globalWindVelocity   =   [
                     0,
                     0,
                     0
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   1
                  fluidDensity   =   1
                  collisionWithEnvironment   =   False
               }
               solverFrequency   =   120
               collisionThickness   =   -1
               friction   =   0.05
               damping   =   0.08
               drag   =   {
                  linear   =   0.02
                  angular   =   0.02
               }
               interCollision   =   False
            }
         },
         {
            simMeshName   =   "coat_raptors_01_cloak_cloth_SIM"
            renderMeshes   =   [
               {
                  name   =   "coat_raptors_01_cloak_cloth_REND"
               }
            ]
            config   =   {
               vertical   =   {
                  stiffness   =   1
               }
               horizontal   =   {
                  stiffness   =   1
               }
               bend   =   {
                  stiffness   =   1
                  compressionLimit   =   0.1
               }
               shear   =   {
                  stiffness   =   1
               }
               tether   =   {
                  stiffness   =   1
               }
               motion   =   {
                  stiffness   =   1
                  distanceScale   =   2
               }
               selfCollision   =   {
                  enable   =   True
                  stiffness   =   1
                  distance   =   0.04
               }
               gravity   =   [
                  0,
                  -25,
                  0
               ]
               cdtCapsules   =   [
                  {
                     name   =   "L_shin"
                     boneFirst   =   "LEG2L"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1L"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "Torso"
                     boneFirst   =   "BACKup"
                     radiusFirst   =   0.41
                     boneFirstOffset   =   [
                        0.02,
                        0.05,
                        0
                     ]
                     boneSecond   =   "BACKdown"
                     radiusSecond   =   0.34
                  },
                  {
                     name   =   "backpack"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.4
                     boneFirstOffset   =   [
                        0.3,
                        0,
                        0.08
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.23
                     boneSecondOffset   =   [
                        0.05,
                        0,
                        -0.3
                     ]
                  },
                  {
                     name   =   "backpack_01"
                     boneFirst   =   "powerplant_backpack"
                     radiusFirst   =   0.18
                     boneFirstOffset   =   [
                        0.04,
                        0.1,
                        -0.3
                     ]
                     boneSecond   =   "powerplant_backpack"
                     radiusSecond   =   0.18
                     boneSecondOffset   =   [
                        0.04,
                        -0.1,
                        -0.3
                     ]
                  },
                  {
                     name   =   "R_shin"
                     boneFirst   =   "LEG2R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.14,
                        0.03,
                        0
                     ]
                     boneSecond   =   "FOOT1R"
                     radiusSecond   =   0.3
                     boneSecondOffset   =   [
                        0.1,
                        0,
                        0
                     ]
                  },
                  {
                     name   =   "R_hip"
                     boneFirst   =   "LEG1R"
                     radiusFirst   =   0.25
                     boneFirstOffset   =   [
                        0,
                        0,
                        0
                     ]
                     boneSecond   =   "LEG2R"
                     radiusSecond   =   0.25
                  },
                  {
                     name   =   " bugsLegR"
                     boneFirst   =   "HIP_R"
                     radiusFirst   =   0.23
                     boneFirstOffset   =   [
                        0.07,
                        -0.05,
                        -0.15
                     ]
                     boneSecond   =   "Shin_R_jiggle"
                     radiusSecond   =   0.22
                     boneSecondOffset   =   [
                        0.5,
                        -0.2,
                        -0.15
                     ]
                  }
               ]
               environment   =   {
                  localWindVelocity   =   [
                     0,
                     -2,
                     3
                  ]
                  useWindSystem   =   False
                  windSystemInfluenceScale   =   0.5
               }
               solverFrequency   =   120
               damping   =   0.09
               drag   =   {
                  linear   =   0.08
                  angular   =   0.15
               }
               stiffnessFrequency   =   30
            }
         }
      ]
      sharedCDTCapsules   =   [
         {
            name   =   "HIP_L"
            boneFirst   =   "LEG1L"
            radiusFirst   =   0.21
            boneFirstOffset   =   [
               0.1,
               0,
               0.015
            ]
            boneSecond   =   "LEG2L"
            radiusSecond   =   0.21
            boneSecondOffset   =   [
               0,
               -0.01,
               0.01
            ]
         },
         {
            name   =   "HIP_R"
            boneFirst   =   "LEG1R"
            radiusFirst   =   0.21
            boneFirstOffset   =   [
               -0.1,
               0,
               -0.015
            ]
            boneSecond   =   "LEG2R"
            radiusSecond   =   0.21
            boneSecondOffset   =   [
               0,
               0.01,
               -0.01
            ]
         },
         {
            name   =   "L_shin"
            boneFirst   =   "LEG2L"
            radiusFirst   =   0.19
            boneFirstOffset   =   [
               0.18,
               0,
               0.011
            ]
            boneSecond   =   "FOOT1L"
            radiusSecond   =   0.29
            boneSecondOffset   =   [
               0.02,
               0.05,
               0
            ]
         },
         {
            name   =   "R_shin"
            boneFirst   =   "LEG2R"
            radiusFirst   =   0.2
            boneFirstOffset   =   [
               -0.18,
               0,
               -0.01
            ]
            boneSecond   =   "FOOT1R"
            radiusSecond   =   0.3
            boneSecondOffset   =   [
               -0.02,
               -0.05,
               -0.02
            ]
         },
         {
            name   =   "right_arm"
            boneFirst   =   "ARM2R"
            radiusFirst   =   0.17
            boneSecond   =   "HANDR"
            radiusSecond   =   0.1
         },
         {
            name   =   "left_arm"
            boneFirst   =   "ARM2L"
            radiusFirst   =   0.17
            boneSecond   =   "HANDL"
            radiusSecond   =   0.16
         },
         {
            name   =   "Spine"
            boneFirst   =   "BACKup"
            radiusFirst   =   0.4
            boneFirstOffset   =   [
               0.025,
               -0.025,
               0
            ]
            boneSecond   =   "BACKdown"
            radiusSecond   =   0.22
            boneSecondOffset   =   [
               -0.15,
               0.03,
               0
            ]
         }
      ]
      sharedCDTSpheres   =   [
         {
            name   =   "Kneepad_L"
            bone   =   "LEG2L"
            radius   =   0.22
            boneOffset   =   [
               -0.07,
               -0.08,
               0.02
            ]
         },
         {
            name   =   "Kneepad_R"
            bone   =   "LEG2R"
            radius   =   0.22
            boneOffset   =   [
               0.07,
               0.08,
               -0.02
            ]
         }
      ]
      sharedCDTBoxes   =   [
         {
            name   =   "LEG_Gun"
            bone   =   "LEG_L_Gun"
            size   =   [
               0.7,
               0.48,
               0.2
            ]
         },
         {
            name   =   "plate_back"
            bone   =   "Back_plate_jiggle"
            size   =   [
               0.35,
               0.5,
               0.3
            ]
         }
      ]
      interCollisionCfg   =   {
         iterations   =   16
         collisionDistance   =   0.04
         collisionStiffness   =   1
      }
   }
   prop_phys_jiggle   =   {
      physJiggle   =   {
         objectsSettings   =   {
            Plates   =   {
               __value   =   [
                  {
                     name   =   "Hip_plate_R_jiggleS"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   12
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.01
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Back_plate_jiggle"
                     stiffness   =   40
                     mass   =   1
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.02
                        y   =   -0.01
                        z   =   -0.15
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.001
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  }
               ]
            }
            jiggle   =   {
               __value   =   [
                  {
                     name   =   "Arm_Chain_R_jiggle"
                     stiffness   =   15
                     mass   =   0.02
                     damping   =   40
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.02
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.02
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.2
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  }
               ]
            }
            Armor   =   {
               __value   =   [
                  {
                     name   =   "Hip_R_jiggle"
                     stiffness   =   30
                     mass   =   0.06
                     damping   =   30
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.4
                     jumpsConstraintMin   =   -0.05
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "Hip_L_jiggle"
                     stiffness   =   30
                     mass   =   0.06
                     damping   =   30
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.4
                     jumpsConstraintMin   =   -0.05
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "Shin_R_jiggle"
                     stiffness   =   60
                     mass   =   0.08
                     damping   =   40
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.001
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.001
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.6
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.01
                  },
                  {
                     name   =   "Shin_L_jiggle"
                     stiffness   =   60
                     mass   =   0.08
                     damping   =   40
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.001
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.001
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.6
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.01
                  },
                  {
                     name   =   "Foot_R_jiggle"
                     stiffness   =   50
                     mass   =   0.04
                     damping   =   30
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.001
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.001
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.4
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "Foot_L_jiggle"
                     stiffness   =   50
                     mass   =   0.04
                     damping   =   30
                     offsetDirection   =   {
                        x   =   0
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.001
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.001
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.4
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "Arm_R_jiggle"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   17
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.3
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "shoulder_L_jiggle"
                     stiffness   =   15
                     mass   =   0.06
                     damping   =   18
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.4
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "shoulder_R_jiggle"
                     stiffness   =   15
                     mass   =   0.06
                     damping   =   18
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.4
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "elbow_L_jiggle"
                     stiffness   =   10
                     mass   =   0.03
                     damping   =   14
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -1
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "elbow_R_jiggle"
                     stiffness   =   10
                     mass   =   0.03
                     damping   =   14
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -1
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "knee_L_jiggle"
                     stiffness   =   15
                     mass   =   0.04
                     damping   =   14
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.4
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "knee_R_jiggle"
                     stiffness   =   15
                     mass   =   0.04
                     damping   =   14
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.4
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "Chest_jiggle"
                     stiffness   =   30
                     mass   =   0.03
                     damping   =   16
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.5
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  },
                  {
                     name   =   "backpack_jiggle"
                     stiffness   =   40
                     mass   =   0.05
                     damping   =   16
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.01
                     jumpsConstraintMin   =   -0.03
                     jumpsConstraintMax   =   0.03
                  },
                  {
                     name   =   "shoulder_chain_R"
                     stiffness   =   100
                     mass   =   0.1
                     damping   =   14
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.1
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_rope_L2"
                     stiffness   =   60
                     mass   =   2
                     damping   =   6
                     gravity   =   -5
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.8
                        z   =   -0.8
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.8
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                     isDynamicPositionConstrained   =   True
                  },
                  {
                     name   =   "shoulder_rope_L3"
                     stiffness   =   20
                     mass   =   0.4
                     damping   =   3
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_rope_R2"
                     stiffness   =   60
                     mass   =   2
                     damping   =   6
                     gravity   =   -5
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.7
                        z   =   -0.8
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.7
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_rope_R3"
                     stiffness   =   20
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_rope_R"
                     stiffness   =   120
                     mass   =   0.1
                     damping   =   12
                     gravity   =   -5
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "shoulder_rope_B"
                     stiffness   =   40
                     mass   =   1
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.05
                        z   =   -0.7
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.05
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_rope_B1"
                     stiffness   =   40
                     damping   =   4
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -1
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_rope_B2"
                     stiffness   =   40
                     damping   =   4
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        y   =   -1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Belt   =   {
               __value   =   [
                  {
                     name   =   "Belt_jiggle"
                     stiffness   =   30
                     mass   =   0.2
                     damping   =   15
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   1
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.05
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.05
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.05
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "pocket_jiggle_02"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   12
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.01
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "pocket_jiggle_01"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   12
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.01
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Hip_plate_R_jiggle"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   12
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.01
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Hip_plate_L_jiggle"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   12
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.01
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            Chest   =   {
               __value   =   [
                  {
                     name   =   "Chest_jiggle"
                     stiffness   =   80
                     mass   =   0.5
                     damping   =   16
                     gravity   =   -0.5
                     offsetDirection   =   {
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "rope1_chest_jiggle"
                     stiffness   =   60
                     mass   =   1
                     damping   =   8
                     gravity   =   -9
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                     isDynamicPositionConstrained   =   True
                  },
                  {
                     name   =   "rope1_chest_jiggle1"
                     stiffness   =   20
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.3
                        z   =   -1.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1.4
                        y   =   1.5
                        z   =   1.4
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "rope2_chest_jiggle"
                     stiffness   =   60
                     mass   =   1
                     damping   =   8
                     gravity   =   -9
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "rope2_chest_jiggle1"
                     stiffness   =   20
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.3
                        z   =   -1.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1.4
                        y   =   1.5
                        z   =   1.4
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "rope_chest_jiggle"
                     stiffness   =   50
                     mass   =   0.1
                     damping   =   30
                     gravity   =   -5
                     offsetDirection   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.03
                        z   =   -0.15
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.03
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  }
               ]
            }
            jetpack   =   {
               __value   =   [
                  {
                     name   =   "backpack_rope_01_jiggle"
                     stiffness   =   10
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.03
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.03
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "backpack_rope_01_jiggle1"
                     stiffness   =   5
                     mass   =   0.1
                     gravity   =   -1
                     offsetDirection   =   {
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "backpack_rope_01_jiggle2"
                     stiffness   =   10
                     mass   =   0.2
                     damping   =   6
                     gravity   =   -0.3
                     offsetDirection   =   {
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "backpack_chain_jiggle"
                     stiffness   =   40
                     mass   =   0.4
                     damping   =   10
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   0.7
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -0.2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "backpack_chain_jiggle1"
                     stiffness   =   5
                     mass   =   0.1
                     damping   =   2
                     gravity   =   -0.1
                     offsetDirection   =   {
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "backpack_chain_jiggle2"
                     stiffness   =   5
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.5
                     offsetDirection   =   {
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "backpack_rope_02_jiggle"
                     stiffness   =   10
                     mass   =   0.2
                     damping   =   5
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.3
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.3
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "backpack_rope_02_jiggle1"
                     stiffness   =   15
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "backpack_rope_02_jiggle2"
                     stiffness   =   10
                     mass   =   0.2
                     damping   =   2
                     gravity   =   -0.05
                     offsetDirection   =   {
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.3
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "backpack_rope_01_jiggle3"
                     stiffness   =   200
                     mass   =   1.5
                     damping   =   10
                     gravity   =   -0.2
                     offsetDirection   =   {
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  }
               ]
            }
            Shoulder_preoder   =   {
               __value   =   [
                  {
                     name   =   "shoulder_ropes_jiggle_01"
                     stiffness   =   10
                     mass   =   1.8
                     damping   =   1
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMin   =   {
                        x   =   -0.02
                        y   =   -0.01
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.02
                        y   =   0.01
                        z   =   0.02
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_ropes_jiggle_02"
                     stiffness   =   10
                     mass   =   2.8
                     damping   =   1
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMin   =   {
                        x   =   -0.02
                        y   =   -0.01
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.02
                        y   =   0.01
                        z   =   0.02
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_brush_B_jiggle_root"
                     stiffness   =   4
                     mass   =   0.8
                     damping   =   1
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.01
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.01
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_B_jiggle_01"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.01
                        z   =   -1.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   2
                        z   =   2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_B_jiggle_02"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   2
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_B_jiggle_03"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_A_jiggle_root"
                     stiffness   =   4
                     mass   =   0.8
                     damping   =   1
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.01
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_A_jiggle_01"
                     stiffness   =   4
                     mass   =   0.8
                     damping   =   1
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -2
                        z   =   -2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   0.01
                        z   =   0.8
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_A_jiggle_02"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   -4
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_brush_A_jiggle_03"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            Dark_angels   =   {
               __value   =   [
                  {
                     name   =   "darkangels_chain_jiggle"
                     stiffness   =   80
                     mass   =   0.5
                     damping   =   16
                     gravity   =   -0.5
                     offsetDirection   =   {
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "darkangels_bulet_jiggle_01"
                     stiffness   =   80
                     mass   =   1
                     damping   =   8
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   1.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.01
                  }
               ]
            }
            Raven_guard   =   {
               __value   =   [
                  {
                     name   =   "shoulder_R_ravenguard_01_skull_jiggle"
                     stiffness   =   60
                     mass   =   2
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        y   =   -0.7
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        y   =   0.7
                        z   =   1.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_R_ravenguard_01_skull_jiggle_01"
                     stiffness   =   80
                     mass   =   2
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_R_ravenguard_01_skull_jiggle_02"
                     stiffness   =   60
                     damping   =   8
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        y   =   0.3
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_R_ravenguard_01_skull_jiggle_03"
                     stiffness   =   60
                     damping   =   8
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        y   =   0.3
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Shoulder_blood_angel   =   {
               __value   =   [
                  {
                     name   =   "shoulder_bl_ang_jiggle"
                     stiffness   =   40
                     mass   =   0.2
                     damping   =   14
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.025
                        z   =   -0.025
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.025
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_bl_ang_jiggle_02"
                     stiffness   =   10
                     mass   =   0.15
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0.1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_bl_ang_jiggle_02_01"
                     stiffness   =   28
                     mass   =   0.4
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0.1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_bl_ang_jiggle_03"
                     stiffness   =   10
                     mass   =   0.15
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0.1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_bl_ang_jiggle_03_01"
                     stiffness   =   28
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0.1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Cuirasse_spaceWolfes   =   {
               __value   =   [
                  {
                     name   =   "cuirasse_sp_w_tac_chain_jiggle"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   20
                     gravity   =   -0.05
                     offsetDirection   =   {
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_cuirasse_sp_w_tac_chain_jiggle_1"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_cuirasse_sp_w_tac_chain_jiggle_2"
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_cuirasse_sp_w_tac_chain_jiggle_3"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_cuirasse_sp_w_tac_chain_jiggle_4"
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_cuirasse_sp_w_tac_chain_jiggle_5"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "l_cuirasse_sp_w_tac_chain_jiggle_0"
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "l_cuirasse_sp_w_tac_chain_jiggle_1"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "l_cuirasse_sp_w_tac_chain_jiggle_2"
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "l_cuirasse_sp_w_tac_chain_jiggle_3"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_sp_w_tac_chain_jiggle_0_2"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -0.2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Shoulder_spaceWolf   =   {
               __value   =   [
                  {
                     name   =   "shoulder_spW_jiggle"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   20
                     gravity   =   -0.05
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.02
                        y   =   -0.02
                        z   =   -0.02
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.02
                        y   =   0.02
                        z   =   0.02
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_spW_jiggle_05"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_spW_jiggle_04"
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_spW_jiggle_03"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_spW_jiggle_02"
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_spW_jiggle_01"
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_sp_wolf_jiggle_06"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            hand_R_P_librarium_01_lock   =   {
               __value   =   [
                  {
                     name   =   "hand_R_T_librarium_01_lock_jiggle1"
                     stiffness   =   40
                     mass   =   2
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   -0.75
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.175
                        y   =   -0.25
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "hand_R_T_librarium_01_lock_jiggle2"
                     stiffness   =   80
                     mass   =   2
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -0.5
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "hand_R_T_librarium_01_lock_jiggle"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   17
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   -0.3
                     jumpsConstraintMin   =   -0.2
                     jumpsConstraintMax   =   0.2
                  }
               ]
            }
            Shoulder_white_scars   =   {
               __value   =   [
                  {
                     name   =   "shoulder_L_whitescars_01_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_L_whitescars_01_jiggle_01"
                     mass   =   0.2
                     damping   =   6
                     gravity   =   -0.1
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_L_whitescars_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_L_whitescars_jiggle_01"
                     mass   =   0.2
                     damping   =   6
                     gravity   =   -0.1
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            cuirasse_T1_librarium   =   {
               __value   =   [
                  {
                     name   =   "cuirasse_lib_tac1_jiggle"
                     stiffness   =   20
                     mass   =   0.1
                     damping   =   12
                     gravity   =   -0.01
                     offsetDirection   =   {
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.007
                        y   =   0
                        z   =   -0.007
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.007
                        y   =   0.007
                        z   =   0.007
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_L"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_L1"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_L2"
                     stiffness   =   20
                     mass   =   0.25
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.4
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_R"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_R1"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_R2"
                     stiffness   =   20
                     mass   =   0.25
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.4
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_R_01"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_R_01_1"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "cuirasse_lib_tac1_jiggle_R_01_2"
                     stiffness   =   20
                     mass   =   0.25
                     damping   =   4
                     gravity   =   -0.15
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0.25
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.4
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Shoulder_r_prestige   =   {
               __value   =   [
                  {
                     name   =   "Shoulder_prestige_raid_rope_m_01_jiggle"
                     stiffness   =   10
                     mass   =   1
                     damping   =   1
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.02
                        y   =   0
                        z   =   -0.02
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.02
                        y   =   0
                        z   =   0.07
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_l_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   0
                        y   =   -2
                        z   =   -2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   0.01
                        z   =   2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_l_02_jiggle"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   -1
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_l_03_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_r_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.01
                        z   =   -2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   2
                        z   =   2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_r_02_jiggle"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_r_03_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_m_02_jiggle"
                     stiffness   =   70
                     mass   =   0.1
                     damping   =   16
                     gravity   =   -8
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.4
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.6
                        y   =   0.4
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Shoulder_prestige_raid_rope_m_03_jiggle"
                     stiffness   =   62
                     mass   =   1
                     damping   =   8
                     gravity   =   -8
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.4
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.4
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Shoulder_r_ImperialFist   =   {
               __value   =   [
                  {
                     name   =   "impfist_trinket_01_jiggle"
                     stiffness   =   8
                     mass   =   0.1
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -0.4
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "impfist_trinket_01_twist"
                     stiffness   =   5
                     mass   =   0.1
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "impfist_trinket_02_jiggle"
                     stiffness   =   16
                     mass   =   0.1
                     damping   =   4
                     gravity   =   -6
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "impfist_trinket_03_jiggle"
                     stiffness   =   8
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "impfist_rope_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_rope_02_jiggle"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0.3
                        y   =   -1
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_rope_03_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_bigrope_01_jiggle"
                     mass   =   0.1
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.01
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "impfist_sh_r_plate_jiggle"
                     stiffness   =   30
                     mass   =   7
                     damping   =   4
                     gravity   =   -15
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Cuirass_ImperialFist   =   {
               __value   =   [
                  {
                     name   =   "impfist_cuirass_T_ropedec_01_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_01_02_jiggle"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0.3
                        y   =   -1
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_02_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_02_02_jiggle"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   0.3
                        y   =   -1
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuiras_T_rope_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.03
                        y   =   -0.05
                        z   =   -0.02
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.1
                        z   =   0.02
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_03_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_03_02_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_03_04_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "impfist_cuirass_T_ropedec_03_05_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            Shoulder_r_ChallangeRewards   =   {
               __value   =   [
                  {
                     name   =   "challange_shoulder_r_03_ropedec_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_shoulder_r_03_ropedec_02_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_shoulder_r_03_BigRope_01_jiggle"
                     stiffness   =   40
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -0.8
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.05
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.04
                        z   =   0.001
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "challange_shouder_r_01_cross_01_jiggle"
                     stiffness   =   15
                     mass   =   0.2
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0
                        z   =   0.03
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "challange_shouder_r_01_cross_02_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   7
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.7
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "challange_shouder_r_01_cross_03_jiggle"
                     stiffness   =   6
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "challange_shouder_r_01_rope_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_shouder_r_01_rope_02_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   1
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   1
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_shouder_r_01_rope_03_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   2
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_shouder_r_01_rope_04_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   2
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            Shoulder_r_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "shoulder_fist_R1"
                     stiffness   =   20
                     mass   =   0.25
                     damping   =   6
                     gravity   =   -15
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -2
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   2
                        y   =   0.25
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulder_fist_R2"
                     stiffness   =   20
                     mass   =   0.25
                     damping   =   6
                     gravity   =   -4
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Soldier_Belt_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "Hip_plate_R_granade_jiggle"
                     stiffness   =   20
                     mass   =   0.05
                     damping   =   12
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Hip_plate_B_granade_jiggle"
                     stiffness   =   20
                     mass   =   0.05
                     damping   =   12
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Soldier_Helmet_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "hair_2_jnt_champ"
                     stiffness   =   80
                     mass   =   0.2
                     damping   =   16
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.025
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.025
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "hair_2_jnt1_champ"
                     stiffness   =   60
                     mass   =   0.35
                     damping   =   16
                     gravity   =   2
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   -0.05
                        z   =   -0.025
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.05
                        z   =   0.025
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Tank_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "Arm_cross"
                     mass   =   0.3
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.4
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Arm_cross1"
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.4
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Arm_rope"
                     stiffness   =   60
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -60
                     offsetDirection   =   {
                        x   =   1
                        y   =   -0.2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -100
                        y   =   -100
                        z   =   -100
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   100
                        y   =   100
                        z   =   100
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Arm_rope_mid"
                     stiffness   =   60
                     mass   =   0.5
                     damping   =   8
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Arm_rope1"
                     stiffness   =   50
                     mass   =   0.05
                     damping   =   8
                     gravity   =   -40
                     offsetDirection   =   {
                        x   =   1
                        y   =   0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -100
                        y   =   -100
                        z   =   -100
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   100
                        y   =   100
                        z   =   100
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Arm_rope1_mid"
                     stiffness   =   60
                     mass   =   0.5
                     damping   =   8
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chain_cross_jiggle"
                     stiffness   =   40
                     mass   =   0.5
                     damping   =   4
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   0
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   0
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.15
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chain_cross_jiggle1"
                     stiffness   =   10
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   0.2
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.4
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chain_cross_jiggle2"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.2
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "jetpack_cross_jiggle"
                     stiffness   =   20
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   0
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.5
                        z   =   -0.15
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "jetpack_cross_jiggle_L"
                     stiffness   =   60
                     mass   =   0.8
                     damping   =   4
                     gravity   =   -0.5
                     offsetDirection   =   {
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.5
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "jetpack_cross_jiggle_R"
                     stiffness   =   60
                     mass   =   0.8
                     damping   =   4
                     gravity   =   -0.5
                     offsetDirection   =   {
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.5
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "helmet_heather_R"
                     stiffness   =   20
                     mass   =   0.1
                     damping   =   6
                     offsetDirection   =   {
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   -0.05
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.05
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "helmet_heather_L"
                     stiffness   =   20
                     mass   =   0.1
                     damping   =   6
                     offsetDirection   =   {
                        y   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   -0.05
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.05
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Raider_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "powerplant_rope_01_jiggle"
                     stiffness   =   30
                     mass   =   0.75
                     damping   =   3
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.5
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.2
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_rope_02_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.8
                        z   =   -0.7
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.8
                        z   =   0.8
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "powerplant_coin_01_r_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.9
                        z   =   -0.8
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.8
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_rope_r_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.4
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_rope_r_02_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.4
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_rope_l_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.4
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_rope_l_02_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.4
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_coin_01_l_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.9
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_lightning_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.9
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "powerplant_lightning_02_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_rope_root_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.03
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Chest_coin_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Chest_coin_02_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Chest_coin_03_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Chest_coin_04_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_rope_a_01_jiggle"
                     stiffness   =   6
                     mass   =   0.8
                     damping   =   1.5
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_rope_a_02_jiggle"
                     stiffness   =   20
                     mass   =   1
                     damping   =   2
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_rope_a_03_jiggle"
                     stiffness   =   50
                     mass   =   1
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.9
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Lowerchest_rope_root_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.03
                        y   =   0
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.1
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Lowerchest_coin_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   2
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.9
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Lowerchest_coin_02_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   2
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.5
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.9
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Lowerchest_coin_03_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   2
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.9
                        y   =   0.9
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_brush_r_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.4
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_brush_r_02_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.4
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Glove_01_jiggle"
                     stiffness   =   10
                     mass   =   0.1
                     damping   =   7
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.025
                        y   =   -0.015
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.025
                        y   =   0.015
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Glove_02_jiggle"
                     stiffness   =   7
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   -0.6
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.2
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Glove_03_jiggle"
                     stiffness   =   7
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.6
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.9
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Cuirass_ChallangeRewards   =   {
               __value   =   [
                  {
                     name   =   "challange_cuirass_02_diamond_01_jiggle"
                     stiffness   =   0
                     mass   =   1
                     damping   =   3
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   1
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_cuirass_02_diamond_03_jiggle"
                     stiffness   =   15
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        y   =   0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.6
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.7
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_cuirass_02_skull_03_jiggle"
                     stiffness   =   15
                     mass   =   0.19
                     damping   =   5
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.7
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_cuirass_02_skull_01_jiggle"
                     stiffness   =   15
                     mass   =   0.15
                     damping   =   5
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.05
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "challange_cuirass_02_bigrope_01_jiggle"
                     stiffness   =   10
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.01
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.01
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            BlackTemplar_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "shoulderpad_chain_l"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   20
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.1
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulderpad_ring_jiggle"
                     stiffness   =   15
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   0
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.01
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulderpad_shield_jiggle"
                     stiffness   =   15
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.01
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "shoulderpad_chain_r"
                     stiffness   =   20
                     mass   =   0.06
                     damping   =   20
                     gravity   =   -0.1
                     offsetDirection   =   {
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   -0.05
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.05
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "Chest_chain_jiggle"
                     stiffness   =   10
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.15
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.05
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shield_neckless_ring_l_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   3
                     gravity   =   0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.05
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.05
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shield_neckless_l_jiggle"
                     stiffness   =   15
                     mass   =   0.9
                     damping   =   5
                     gravity   =   0.5
                     offsetDirection   =   {
                        x   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.15
                        y   =   -0.01
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.15
                        y   =   0.01
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shield_neckless_ring_r_jiggle"
                     stiffness   =   10
                     mass   =   0.07
                     damping   =   3
                     gravity   =   0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.05
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.05
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shield_neckless_r_jiggle"
                     stiffness   =   25
                     mass   =   0.2
                     damping   =   8
                     gravity   =   0.5
                     offsetDirection   =   {
                        x   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.15
                        y   =   -0.01
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.15
                        y   =   0.01
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "cross_ring_jiggle"
                     stiffness   =   10
                     mass   =   0.2
                     damping   =   3
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.05
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.05
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "cross_jiggle"
                     stiffness   =   15
                     mass   =   0.5
                     damping   =   5
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.1
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            Salamander_shoulder   =   {
               __value   =   [
                  {
                     name   =   "salamander_shoulderclaw_01_01_jiggle"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   7
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.2
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "salamander_shoulderchain_01_jiggle"
                     stiffness   =   160
                     mass   =   0.7
                     damping   =   5
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.8
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.03
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.04
                        y   =   0.03
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "salamander_shoulderclaw_02_01_jiggle"
                     stiffness   =   9
                     mass   =   0.18
                     damping   =   6
                     gravity   =   -0.15
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.2
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "salamander_shoulderclaw_01_02_jiggle"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   7
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.2
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "salamander_shoulderclaw_02_02_jiggle"
                     stiffness   =   25
                     mass   =   0.18
                     damping   =   6
                     gravity   =   -0.15
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.4
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.1
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "salamander_shoulderclaw_01_twist"
                     stiffness   =   4
                     mass   =   0.1
                     damping   =   4
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   0
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "salamander_shoulderclaw_02_twist"
                     stiffness   =   4
                     mass   =   0.1
                     damping   =   3
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   0
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   -3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0
                        z   =   3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "salamander_shoulderchain_02_jiggle"
                     stiffness   =   160
                     mass   =   0.7
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   0
                        y   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   1
                     constraintMin   =   {
                        x   =   0
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   3
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  }
               ]
            }
            shoulder_R_challenge_04   =   {
               __value   =   [
                  {
                     name   =   "r_shoulder_challenge_04_rope_short_jiggle"
                     stiffness   =   12
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.15
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.15
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_long_jiggle"
                     stiffness   =   12
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.01
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.15
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_l_1_jiggle"
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.4
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_l_2_jiggle"
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.25
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_l_3_jiggle"
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.2
                        z   =   0.35
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_r_1_jiggle"
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.3
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_r_2_jiggle"
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.25
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_challenge_04_rope_r_3_jiggle"
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.2
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            BloodAngel_02_champions_pack   =   {
               __value   =   [
                  {
                     name   =   "soldier_champion_02_blooddrop_01_01_jiggle"
                     stiffness   =   6
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_01_02_twist"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_02_02_twist"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_03_03_twist"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   0
                        y   =   -2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_01_02_jiggle"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.3
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_02_01_jiggle"
                     stiffness   =   6
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_02_02_jiggle"
                     stiffness   =   7
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.3
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_03_01_jiggle"
                     stiffness   =   6
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_blooddrop_03_03_jiggle"
                     stiffness   =   7
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.3
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "soldier_champion_02_chestrope_01_jiggle"
                     stiffness   =   8
                     mass   =   0.07
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.03
                        y   =   -0.05
                        z   =   -0.02
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.1
                        z   =   0.02
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_chestbrush_01_jiggle"
                     stiffness   =   20
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.3
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_chestbrush_02_jiggle"
                     stiffness   =   20
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.3
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_chestbrush_03_jiggle"
                     stiffness   =   20
                     gravity   =   -3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.3
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        z   =   0.9
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_midcloth_01_jiggle"
                     stiffness   =   14
                     mass   =   0.1
                     damping   =   10
                     gravity   =   0.03
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   -0.2
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0.1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backrope_01_jiggle"
                     stiffness   =   8
                     mass   =   0.2
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.2
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.2
                        y   =   0
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backampoule_01_jiggle"
                     stiffness   =   8
                     mass   =   0.1
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.5
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backampoule_02_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.2
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   2
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backbrush_01_01_jiggle"
                     stiffness   =   15
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backbrush_01_02_jiggle"
                     stiffness   =   15
                     mass   =   1
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backbrush_01_03_jiggle"
                     stiffness   =   90
                     mass   =   1
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backbrush_02_01_jiggle"
                     stiffness   =   15
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.7
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backbrush_02_02_jiggle"
                     stiffness   =   15
                     mass   =   1
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.7
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_backbrush_02_03_jiggle"
                     stiffness   =   90
                     mass   =   1
                     damping   =   4
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.7
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_waistrope_root"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   5
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   0
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_waistrope_01_01_jiggle"
                     stiffness   =   9
                     mass   =   0.1
                     damping   =   3
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.06
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.06
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "soldier_champion_02_waistrope_01_01_jiggle"
                     stiffness   =   9
                     mass   =   0.12
                     damping   =   3
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.3
                        y   =   -0.02
                        z   =   -0.3
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.3
                        y   =   0.02
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            Carcharadron_pack   =   {
               __value   =   [
                  {
                     name   =   "carcharadons_neck_rope_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.05
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_neck_rope_fangs_01_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_neck_rope_fangs_02_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_neck_rope_fangs_03_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.2
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_chain_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   12
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.15
                        z   =   -0.09
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.2
                        z   =   0.09
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_chain_fang_01_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -1
                        y   =   -1
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_chain_fang_02_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_chain_fang_03_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_rope_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   0
                        y   =   -0.1
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.1
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_rope_fang_01_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -1
                        y   =   0
                        z   =   -0.6
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.6
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_rope_fang_02_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -1
                        y   =   0
                        z   =   -0.6
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.6
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_rope_fang_03_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -1
                        y   =   0
                        z   =   -0.6
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.6
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_rope_fang_04_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -1
                        y   =   0
                        z   =   -0.6
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.6
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_chest_rope_fang_05_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -1
                        y   =   0
                        z   =   -0.6
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   1
                        z   =   0.6
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_ropre_long_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   15
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "carcharadons_shldr_ropre_long_ring_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_ropre_short_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   15
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "carcharadons_shldr_ropre_short_ring_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_ropre_short_fangs_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_01_jiggle"
                     stiffness   =   12
                     mass   =   0.08
                     damping   =   10
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.015
                        y   =   0
                        z   =   -0.08
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.015
                        y   =   0.3
                        z   =   0.08
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_jiggle"
                     stiffness   =   12
                     mass   =   0.08
                     damping   =   10
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.015
                        y   =   0
                        z   =   -0.08
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.015
                        y   =   0.35
                        z   =   0.08
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_ring_01_A_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   5
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.15
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_ring_02_A_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.15
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_fang_A_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.15
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_ring_01_B_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.25
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_01_fang_B_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.25
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_ring_01_C_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.25
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_ring_02_C_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.25
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_02_fang_C_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.25
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "carcharadons_shldr_chain_01_fang_A_jiggle"
                     stiffness   =   12
                     mass   =   0.7
                     damping   =   6
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.75
                        y   =   0
                        z   =   -0.75
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.75
                        y   =   0.75
                        z   =   0.75
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            champion_raider_02   =   {
               __value   =   [
                  {
                     name   =   "RD_02_chest_01_rope_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.15
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.03
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.01
                  },
                  {
                     name   =   "RD_02_chest_02_rope_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.15
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.03
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.01
                  },
                  {
                     name   =   "RD_02_chest_rope_long_01_jiggle"
                     stiffness   =   15
                     mass   =   0.65
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.9
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_long_02_jiggle"
                     stiffness   =   15
                     mass   =   0.65
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   -0.05
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.8
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_long_03_jiggle"
                     stiffness   =   15
                     mass   =   0.65
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   -0.05
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.7
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_long_04_jiggle"
                     stiffness   =   15
                     mass   =   0.4
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   -0.05
                        z   =   -0.15
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.6
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_short_01_jiggle"
                     stiffness   =   15
                     mass   =   0.8
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.4
                        z   =   0.15
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_short_02_jiggle"
                     stiffness   =   15
                     mass   =   0.7
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_short_03_jiggle"
                     stiffness   =   15
                     mass   =   0.6
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.4
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.6
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_rope_short_04_jiggle"
                     stiffness   =   15
                     mass   =   0.4
                     damping   =   3
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.7
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_chest_ring_01_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   4
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.05
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_chest_ring_02_jiggle"
                     stiffness   =   12
                     mass   =   0.2
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   -0.1
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_chest_ring_03_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   1
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_feather_small_1_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8
                     gravity   =   0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.5
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.5
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_feather_small_2_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.5
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.5
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_feather_small_3_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.5
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.5
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_feather_long_1_jiggle"
                     stiffness   =   12
                     mass   =   1
                     damping   =   12
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.3
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.5
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_feather_long_2_jiggle"
                     stiffness   =   12
                     mass   =   1
                     damping   =   12
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.3
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.5
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "RD_02_shoulder_L_rope_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   15
                     gravity   =   1
                     offsetDirection   =   {
                        x   =   0
                        y   =   0
                        z   =   1
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.1
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.35
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_small_skull_01_jiggle"
                     stiffness   =   12
                     mass   =   0.2
                     damping   =   6
                     gravity   =   0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   1
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_small_skull_02_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   1
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_small_skull_03_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -1
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   1
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_ring_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   0
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_ring_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_skull_leaves_01_jiggle"
                     stiffness   =   12
                     mass   =   0.6
                     damping   =   12
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_skull_leaves_02_jiggle"
                     stiffness   =   12
                     mass   =   0.6
                     damping   =   12
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.25
                        y   =   0
                        z   =   -0.25
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.25
                        y   =   0.5
                        z   =   0.25
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_long_01_jiggle"
                     stiffness   =   15
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   1.8
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_long_02_jiggle"
                     stiffness   =   15
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.8
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_rope_long_03_jiggle"
                     stiffness   =   15
                     mass   =   0.5
                     damping   =   4
                     gravity   =   -2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   0
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.8
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_sh_rope_small_01_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.01
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_sh_rope_small_02_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.04
                        z   =   0.6
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_sh_rope_small_03_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.01
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.08
                        z   =   0.7
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_sh_rope_small_04_jiggle"
                     stiffness   =   12
                     mass   =   0.3
                     damping   =   4
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.01
                        y   =   -0.001
                        z   =   -0.001
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.01
                        y   =   0.1
                        z   =   0.8
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_shoulder_R_chain_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   12
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.08
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_ring_skull_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   4
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.2
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_chain_skull_01_jiggle"
                     stiffness   =   10
                     mass   =   0.15
                     damping   =   4
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.8
                        y   =   -0.2
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.8
                        y   =   0.35
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_chain_skull_02_jiggle"
                     stiffness   =   10
                     mass   =   0.3
                     damping   =   4
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.2
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.2
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_chain_skull_03_jiggle"
                     stiffness   =   10
                     mass   =   0.15
                     damping   =   4
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.8
                        y   =   -0.2
                        z   =   -0.01
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.8
                        y   =   0.35
                        z   =   0.01
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -1
                     jumpsConstraintMax   =   1
                  },
                  {
                     name   =   "RD_02_belt_chain_jiggle"
                     stiffness   =   8
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.05
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.05
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.02
                  },
                  {
                     name   =   "RD_02_chain_raven_jiggle"
                     stiffness   =   8
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -0.5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.05
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.05
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.01
                  },
                  {
                     name   =   "RD_02_paw_jiggle"
                     stiffness   =   10
                     mass   =   0.25
                     damping   =   6
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -3
                        y   =   -1
                        z   =   -0.2
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   3
                        y   =   3
                        z   =   0.2
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_PawLeaves_01_jiggle"
                     stiffness   =   10
                     mass   =   0.25
                     damping   =   5
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.081
                     constraintMin   =   {
                        x   =   -3
                        y   =   -3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   3
                        y   =   3
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_PawLeaves_02_jiggle"
                     stiffness   =   10
                     mass   =   0.25
                     damping   =   5
                     gravity   =   -1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.081
                     constraintMin   =   {
                        x   =   -3
                        y   =   -3
                        z   =   -1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   3
                        y   =   3
                        z   =   1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_belt_bag_L_01_jiggle"
                     stiffness   =   20
                     mass   =   0.08
                     damping   =   12
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.025
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_belt_bag_L_02_jiggle"
                     stiffness   =   20
                     mass   =   0.08
                     damping   =   12
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.025
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_belt_bag_R_01_jiggle1"
                     stiffness   =   20
                     mass   =   0.08
                     damping   =   12
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.025
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_belt_bag_R_02_jiggle"
                     stiffness   =   20
                     mass   =   0.08
                     damping   =   12
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.025
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "RD_02_turbine_chain_jiggle"
                     stiffness   =   20
                     mass   =   0.08
                     damping   =   20
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.1
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.1
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_backpack_chain_01_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8
                     gravity   =   0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.005
                        y   =   -0.225
                        z   =   -0.005
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.005
                        y   =   0.225
                        z   =   0.005
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_backpack_chain_02_jiggle"
                     stiffness   =   12
                     mass   =   0.15
                     damping   =   8
                     gravity   =   0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.005
                        y   =   -0.275
                        z   =   -0.005
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.005
                        y   =   0.275
                        z   =   0.005
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "RD_02_chain_details_01_01_jiggle"
                     stiffness   =   12
                     mass   =   0.85
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.75
                        y   =   -0.5
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.75
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.5
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_01_02_jiggle"
                     stiffness   =   12
                     mass   =   0.85
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.25
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.25
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.25
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_01_03_jiggle"
                     stiffness   =   12
                     mass   =   0.5
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.15
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.15
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_02_01_jiggle"
                     stiffness   =   12
                     mass   =   0.5
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -1
                        y   =   -0.5
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   1
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.5
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_02_02_jiggle"
                     stiffness   =   12
                     mass   =   0.5
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.25
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.25
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_02_03_jiggle"
                     stiffness   =   12
                     mass   =   0.55
                     damping   =   8
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.35
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.25
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.25
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0.1
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_02_04_jiggle"
                     stiffness   =   12
                     mass   =   0.5
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   -0.1
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.1
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  },
                  {
                     name   =   "RD_02_chain_details_02_05_jiggle"
                     stiffness   =   12
                     mass   =   0.5
                     damping   =   6
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.15
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.25
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.25
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.5
                     jumpsConstraintMax   =   0.5
                  }
               ]
            }
            iron_hands_pack   =   {
               __value   =   [
                  {
                     name   =   "ironhands_l_shldr_chain_jiggle"
                     stiffness   =   12
                     mass   =   0.25
                     damping   =   4
                     gravity   =   -0.8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   0
                        z   =   -0.025
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.14
                        z   =   0.025
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "ironhands_leg_chain_jiggle"
                     stiffness   =   12
                     mass   =   0.08
                     damping   =   6
                     gravity   =   -0.8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.025
                        y   =   -0.05
                        z   =   -0.1
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.7
                        y   =   0.7
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "ironhands_r_shldr_chain_01_jiggle"
                     stiffness   =   12
                     mass   =   0.35
                     damping   =   4
                     gravity   =   -0.8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   0
                        z   =   -0.025
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.14
                        z   =   0.025
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "ironhands_r_shldr_chain_02_jiggle"
                     stiffness   =   12
                     mass   =   0.35
                     damping   =   4
                     gravity   =   -0.8
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.05
                        y   =   0
                        z   =   -0.025
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.5
                        y   =   0.14
                        z   =   0.025
                        __type   =   "Vector3d"
                     }
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "ironhands_r_shldr_medal_1_jiggle"
                     stiffness   =   30
                     mass   =   0.9
                     damping   =   2
                     gravity   =   -5
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.05
                     constraintMin   =   {
                        x   =   -5
                        y   =   -5
                        z   =   -4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   5
                        y   =   5
                        z   =   4
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
            champion_engineer   =   {
               __value   =   [
                  {
                     name   =   "techhero_sh_l_chain_01_jiggle"
                     mass   =   0.1
                     damping   =   20
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   -1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.3
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.03
                        z   =   -0.03
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.03
                        z   =   0.03
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  },
                  {
                     name   =   "techhero_sh_l_chain_02_jiggle"
                     stiffness   =   9
                     mass   =   0.1
                     damping   =   8
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.2
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   2
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                     jumpsConstraintMin   =   -0.1
                     jumpsConstraintMax   =   0.1
                  }
               ]
            }
            champion_berserk   =   {
               __value   =   [
                  {
                     name   =   "Shoulder_wolfhead_01_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.2
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.01
                        z   =   -0.09
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.01
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_wolfear_l_01_jiggle"
                     stiffness   =   5
                     mass   =   0.05
                     damping   =   10
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.2
                        z   =   -0.09
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.2
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "shoulder_wolfear_r_01_jiggle"
                     stiffness   =   5
                     mass   =   0.05
                     damping   =   10
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.2
                        z   =   -0.09
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.03
                        y   =   0.2
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_06_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_05_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.3
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_04_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.5
                        z   =   0.5
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_03_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_02_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_01_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.5
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_07_jiggle"
                     stiffness   =   8
                     mass   =   0.09
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   -0.3
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.7
                        y   =   0.5
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_08_jiggle"
                     stiffness   =   8
                     mass   =   0.09
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   -0.3
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.7
                        y   =   0.5
                        z   =   0.3
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_09_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.7
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_10_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.7
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_shoulder_11_jiggle"
                     stiffness   =   8
                     mass   =   0.05
                     damping   =   5
                     gravity   =   -0.01
                     offsetDirection   =   {
                        x   =   -1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.1
                     constraintMin   =   {
                        x   =   -0.5
                        y   =   -0.5
                        z   =   -0.9
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.7
                        y   =   0.5
                        z   =   0.1
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_Shoulder_rope_jiggle_02"
                     stiffness   =   8
                     mass   =   0.09
                     damping   =   7
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.8
                        z   =   -0.13
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0
                        z   =   0.13
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  },
                  {
                     name   =   "spacewolves_T_Shoulder_rope_jiggle_01"
                     stiffness   =   8
                     mass   =   0.09
                     damping   =   7
                     gravity   =   0
                     offsetDirection   =   {
                        x   =   1
                        y   =   0
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.2
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.01
                        z   =   -0.18
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.8
                        z   =   0.18
                        __type   =   "Vector3d"
                     }
                     jumpsIntensity   =   0
                  }
               ]
            }
            raptors_pack   =   {
               __value   =   [
                  {
                     name   =   "r_shoulder_raptors_bag_A_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8.5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.07
                        y   =   -0.07
                        z   =   -0.035
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.07
                        y   =   0.07
                        z   =   0.035
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_raptors_bag_B_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8.5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.07
                        y   =   -0.07
                        z   =   -0.035
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.07
                        y   =   0.07
                        z   =   0.035
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_raptors_bag_C_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8.5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.6
                     constraintMin   =   {
                        x   =   -0.07
                        y   =   -0.07
                        z   =   -0.035
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.07
                        y   =   0.07
                        z   =   0.035
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_raptors_bag_A_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8.5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.085
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.75
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_raptors_bag_B_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8.5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.085
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.75
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "chest_raptors_bag_C_jiggle"
                     stiffness   =   12
                     mass   =   0.1
                     damping   =   8.5
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.085
                     constraintMin   =   {
                        x   =   -0.4
                        y   =   0
                        z   =   -0.4
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.4
                        y   =   0.75
                        z   =   0.4
                        __type   =   "Vector3d"
                     }
                  },
                  {
                     name   =   "r_shoulder_raptors_knife_jiggle"
                     stiffness   =   12
                     mass   =   0.5
                     damping   =   6
                     gravity   =   -0.1
                     offsetDirection   =   {
                        x   =   1
                        z   =   0
                        __type   =   "Vector3d"
                     }
                     offsetDistance   =   0.5
                     constraintMin   =   {
                        x   =   -0.1
                        y   =   -0.05
                        z   =   -0.05
                        __type   =   "Vector3d"
                     }
                     constraintMax   =   {
                        x   =   0.1
                        y   =   0.05
                        z   =   0.05
                        __type   =   "Vector3d"
                     }
                  }
               ]
            }
         }
         __type   =   "PhysJiggle"
      }
   }
   prop_motion_damper_controller   =   {
      springDampers   =   [
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "chain_v_06_base_low_01"
                  stiffness   =   3
                  dampingRation   =   2
                  mass   =   0.5
                  jointAngle   =   30
                  gravity   =   0
               },
               {
                  name   =   "chain_v_06_base_low_02"
                  stiffness   =   0.25
                  dampingRation   =   1
                  mass   =   1
                  jointAngle   =   15
                  gravity   =   1
               },
               {
                  name   =   "chain_v_06_base_low_end"
                  stiffness   =   1
                  dampingRation   =   1
                  mass   =   0.5
                  jointAngle   =   65
                  isInvertedLook   =   False
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_4_a"
                  downLocatorName   =   "cloth_cdt_4_b"
                  radius   =   0.26
                  hasExternalLocators   =   False
               },
               {
                  upLocatorName   =   "cloth_cdt_3_a"
                  downLocatorName   =   "cloth_cdt_3_b"
                  radius   =   0.26
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "l_box_jiggle_end"
                  stiffness   =   1.5
                  dampingRation   =   2
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   45
                  isInvertedLook   =   False
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_1_a"
                  downLocatorName   =   "cloth_cdt_1_b"
                  radius   =   0.24
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "r_box_jiggle_end"
                  stiffness   =   1.8
                  dampingRation   =   1.5
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   45
                  isInvertedLook   =   True
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_3_a"
                  downLocatorName   =   "cloth_cdt_3_b"
                  radius   =   0.2
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "r_skullBox_jiggle_end"
                  stiffness   =   1.8
                  dampingRation   =   1.5
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   45
                  isInvertedLook   =   True
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_3_a"
                  downLocatorName   =   "cloth_cdt_3_b"
                  radius   =   0.2
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_darkangels_01_T_jiggle_01"
                  stiffness   =   7.21
                  dampingRation   =   2.18
                  mass   =   1
                  jointAngle   =   30
                  gravity   =   0
               },
               {
                  name   =   "belt_vanity_darkangels_01_T_jiggle_02_end"
                  stiffness   =   6.81
                  dampingRation   =   2.21
                  mass   =   2
                  jointAngle   =   45
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_1_a"
                  downLocatorName   =   "cloth_cdt_1_b"
                  radius   =   0.26
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_ravenguard_01_tacticus_jiggle_01"
                  stiffness   =   1.43
                  dampingRation   =   1.28
                  mass   =   0.75
                  jointAngle   =   45
                  isInvertedLook   =   True
                  gravity   =   0.5
               },
               {
                  name   =   "belt_vanity_ravenguard_01_tacticus_jiggle_02"
                  stiffness   =   9.33
                  dampingRation   =   8.58
                  mass   =   0.25
                  jointAngle   =   45
                  isInvertedLook   =   True
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_a"
                  downLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_b"
                  radius   =   0.28
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_blood_angels_01_T_jiggle_01"
                  stiffness   =   7.21
                  dampingRation   =   2.18
                  mass   =   1
                  jointAngle   =   45
                  gravity   =   0
               },
               {
                  name   =   "belt_vanity_blood_angels_01_T_jiggle_02_end"
                  stiffness   =   6.81
                  dampingRation   =   2.21
                  mass   =   2
                  jointAngle   =   45
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_1_a"
                  downLocatorName   =   "cloth_cdt_1_b"
                  radius   =   0.25
               },
               {
                  upLocatorName   =   "blood_angel_cdt_1_a"
                  downLocatorName   =   "blood_angel_cdt_1_b"
                  radius   =   0.2
               },
               {
                  upLocatorName   =   "blood_angel_cdt_2_a"
                  downLocatorName   =   "blood_angel_cdt_2_b"
                  radius   =   0.2
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_sp_w_01_T_jiggle_01"
                  stiffness   =   7.21
                  dampingRation   =   2.18
                  mass   =   1
                  jointAngle   =   45
                  gravity   =   0
               },
               {
                  name   =   "belt_vanity_sp_w_01_T_jiggle_02_end"
                  stiffness   =   6.81
                  dampingRation   =   2.21
                  mass   =   2
                  jointAngle   =   45
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.27
               },
               {
                  upLocatorName   =   "blood_angel_cdt_1_a"
                  downLocatorName   =   "blood_angel_cdt_1_b"
                  radius   =   0.23
               },
               {
                  upLocatorName   =   "cloth_darkangeles_cdt_1_a"
                  downLocatorName   =   "cloth_darkangeles_cdt_1_b"
                  radius   =   0.24
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_whitescars_01_t_jiggle_01"
                  stiffness   =   7.21
                  dampingRation   =   2.18
                  mass   =   1
                  jointAngle   =   8
                  isInvertedLook   =   False
                  gravity   =   0.5
               },
               {
                  name   =   "belt_vanity_whitescars_01_t_jiggle_02"
                  stiffness   =   7.21
                  dampingRation   =   2.18
                  mass   =   2
                  isParent   =   False
                  jointAngle   =   8
                  isInvertedLook   =   False
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.2
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_whitescars_01_t_jiggle_04"
                  stiffness   =   1.98
                  dampingRation   =   1.1
                  mass   =   1
                  jointAngle   =   25
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "belt_vanity_whitescars_01_t_jiggle_05"
                  stiffness   =   1.61
                  dampingRation   =   0.8
                  mass   =   0.7
                  isParent   =   False
                  jointAngle   =   25
                  isInvertedLook   =   False
                  gravity   =   0
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.28
                  hasExternalLocators   =   False
               },
               {
                  upLocatorName   =   "cloth_share_cdt_p_2_a"
                  downLocatorName   =   "cloth_share_cdt_p_2_b"
                  radius   =   0.11
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "belt_vanity_whitescars_02_t_chain_jiggle_01"
                  stiffness   =   3.64
                  dampingRation   =   2.25
                  mass   =   1
                  jointAngle   =   10
                  gravity   =   1
               },
               {
                  name   =   "belt_vanity_whitescars_02_t_chain_jiggle_02"
                  stiffness   =   2.3
                  dampingRation   =   0.79
                  mass   =   1.2
                  jointAngle   =   20
                  gravity   =   1
               },
               {
                  name   =   "belt_vanity_whitescars_02_t_chain_jiggle_03"
                  stiffness   =   1.83
                  dampingRation   =   0.56
                  mass   =   0.8
                  jointAngle   =   30
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_a"
                  downLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_b"
                  radius   =   0.23
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "impfist_beltvanity_T_02_jiggle"
                  stiffness   =   0.98
                  dampingRation   =   0.59
                  mass   =   0.5
                  jointAngle   =   20
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "impfist_beltvanity_T_03_jiggle"
                  stiffness   =   0.57
                  dampingRation   =   0.55
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   20
                  isInvertedLook   =   False
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.22
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "angel_jiggle_02"
                  stiffness   =   4.94
                  dampingRation   =   2.34
                  mass   =   1
                  jointAngle   =   30
                  gravity   =   0
               },
               {
                  name   =   "angel_jiggle_end"
                  stiffness   =   3.18
                  dampingRation   =   0.8
                  mass   =   2
                  jointAngle   =   45
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_1_a"
                  downLocatorName   =   "cloth_cdt_1_b"
                  radius   =   0.25
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "Belt_pendant_01_r_jiggle"
                  stiffness   =   0.81
                  dampingRation   =   2.23
                  mass   =   0.4
                  isParent   =   False
                  jointAngle   =   10
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_02_r_jiggle"
                  stiffness   =   2.22
                  dampingRation   =   1.91
                  mass   =   0.4
                  jointAngle   =   30
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_03_r_jiggle"
                  stiffness   =   1.74
                  dampingRation   =   0.75
                  mass   =   0.4
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_end_r_jiggle"
                  stiffness   =   2.04
                  dampingRation   =   0.94
                  mass   =   0.4
                  jointAngle   =   30
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_a"
                  downLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_b"
                  radius   =   0.23
                  hasExternalLocators   =   False
               },
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.23
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "Belt_pendant_01_l_jiggle"
                  stiffness   =   0.81
                  dampingRation   =   2.23
                  mass   =   0.4
                  isParent   =   False
                  jointAngle   =   10
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_02_l_jiggle"
                  stiffness   =   2.22
                  dampingRation   =   1.91
                  mass   =   0.4
                  jointAngle   =   30
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_03_l_jiggle"
                  stiffness   =   1.74
                  dampingRation   =   0.75
                  mass   =   0.4
                  jointAngle   =   30
                  gravity   =   1
               },
               {
                  name   =   "Belt_plumage_end_l_jiggle"
                  stiffness   =   2.04
                  dampingRation   =   0.94
                  mass   =   0.4
                  jointAngle   =   30
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_a"
                  downLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_b"
                  radius   =   0.23
                  hasExternalLocators   =   False
               },
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.23
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "Belt_pendant_01_c_jiggle"
                  stiffness   =   0.81
                  dampingRation   =   2.23
                  mass   =   0.4
                  isParent   =   False
                  jointAngle   =   10
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_02_c_jiggle"
                  stiffness   =   2.22
                  dampingRation   =   1.91
                  mass   =   0.4
                  isParent   =   False
                  jointAngle   =   30
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_03_c_jiggle"
                  stiffness   =   1.74
                  dampingRation   =   0.75
                  mass   =   0.4
                  isParent   =   False
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "Belt_pendant_end_c_jiggle"
                  stiffness   =   2.04
                  dampingRation   =   0.94
                  mass   =   0.4
                  isParent   =   False
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_a"
                  downLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_b"
                  radius   =   0.23
                  hasExternalLocators   =   False
               },
               {
                  upLocatorName   =   "cloth_share_cdt_1_a"
                  downLocatorName   =   "cloth_share_cdt_1_b"
                  radius   =   0.23
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "soldier_champion_02_lantern_02_jiggle"
                  stiffness   =   7
                  dampingRation   =   2
                  mass   =   1
                  jointAngle   =   25
                  gravity   =   1
               },
               {
                  name   =   "soldier_champion_02_lantern_03_jiggle"
                  stiffness   =   7
                  dampingRation   =   2
                  mass   =   1.5
                  jointAngle   =   30
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_3_a"
                  downLocatorName   =   "cloth_cdt_3_b"
                  radius   =   0.25
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "soldier_champion_02_ampoule_02_jiggle"
                  stiffness   =   7
                  dampingRation   =   2
                  jointAngle   =   25
                  isInvertedLook   =   False
                  gravity   =   1
               },
               {
                  name   =   "soldier_champion_02_ampoule_03_jiggle"
                  stiffness   =   7
                  dampingRation   =   2
                  mass   =   1.5
                  isParent   =   False
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_1_a"
                  downLocatorName   =   "cloth_cdt_1_b"
                  radius   =   0.25
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "carcharadons_belt_carabiner_jiggle"
                  stiffness   =   7
                  dampingRation   =   4
                  jointAngle   =   45
                  gravity   =   1
               },
               {
                  name   =   "carcharadons_belt_skull_jiggle"
                  stiffness   =   7
                  dampingRation   =   3
                  jointAngle   =   15
                  gravity   =   0
               },
               {
                  name   =   "carcharadons_belt_skull_end_jiggle"
                  stiffness   =   7
                  dampingRation   =   2
                  jointAngle   =   45
                  gravity   =   0
               },
               {
                  name   =   "carcharadons_belt_fang_jiggle"
                  stiffness   =   6
                  dampingRation   =   3
                  mass   =   1
                  jointAngle   =   45
                  gravity   =   0
               },
               {
                  name   =   "carcharadons_belt_fang_end_jiggle"
                  stiffness   =   7
                  dampingRation   =   2
                  jointAngle   =   45
                  gravity   =   0
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "cloth_cdt_10_a"
                  downLocatorName   =   "cloth_cdt_10_b"
                  radius   =   0.28
               },
               {
                  upLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_a"
                  downLocatorName   =   "belt_vanity_ravenguard_01_T_cloth_cdt_1_b"
                  radius   =   0.21
               },
               {
                  upLocatorName   =   "cloth_cdt_9_a"
                  downLocatorName   =   "cloth_cdt_9_b"
                  radius   =   0.23
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "RD_02_raven_amulet_01_jiggle"
                  stiffness   =   4
                  dampingRation   =   3
                  mass   =   1
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   0.5
               },
               {
                  name   =   "RD_02_raven_amulet_02_jiggle"
                  stiffness   =   4
                  dampingRation   =   3
                  mass   =   1
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   0.5
               },
               {
                  name   =   "RD_02_raven_amulet_end_jiggle"
                  stiffness   =   4
                  dampingRation   =   2
                  mass   =   1
                  isParent   =   False
                  jointAngle   =   30
                  isInvertedLook   =   False
                  gravity   =   0.5
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "rd02_CENTRE_cdt_1_a"
                  downLocatorName   =   "rd02_CENTRE_cdt_1_b"
                  radius   =   0.32
                  hasExternalLocators   =   False
               },
               {
                  upLocatorName   =   "rd02_LEG1R_cdt_1_a"
                  downLocatorName   =   "rd02_LEG1R_cdt_1_b"
                  radius   =   0.28
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "RD_02_paw_01_jiggle"
                  stiffness   =   2
                  dampingRation   =   1.5
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   90
                  isInvertedLook   =   False
                  gravity   =   0
               },
               {
                  name   =   "RD_02_paw_02_jiggle"
                  stiffness   =   2
                  dampingRation   =   1.5
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   90
                  isInvertedLook   =   False
                  gravity   =   0
               },
               {
                  name   =   "RD_02_paw_02_end_jiggle"
                  stiffness   =   2
                  dampingRation   =   1.5
                  mass   =   0.5
                  isParent   =   False
                  jointAngle   =   90
                  isInvertedLook   =   False
                  gravity   =   1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "rd02_LEG1L_cdt_1_a"
                  downLocatorName   =   "rd02_LEG1L_cdt_1_b"
                  radius   =   0.3
                  hasExternalLocators   =   False
               }
            ]
         },
         {
            timeScale   =   5
            joints   =   [
               {
                  name   =   "challange_04_tail_04_jiggle"
                  stiffness   =   1.64
                  dampingRation   =   1.16
                  mass   =   1
                  jointAngle   =   50
                  gravity   =   -1
               },
               {
                  name   =   "challange_04_tail_06_jiggle"
                  stiffness   =   2.03
                  dampingRation   =   1.5
                  mass   =   2
                  jointAngle   =   45
                  gravity   =   -1
               },
               {
                  name   =   "challange_04_tail_08_jiggle"
                  stiffness   =   2
                  dampingRation   =   1.2
                  mass   =   2
                  jointAngle   =   50
                  gravity   =   0.5
               },
               {
                  name   =   "challange_04_tail_09_jiggle"
                  stiffness   =   2
                  dampingRation   =   1.34
                  jointAngle   =   35
                  gravity   =   -1
               }
            ]
            constrains   =   [
               {
                  upLocatorName   =   "head_cdt_1_a"
                  downLocatorName   =   "head_cdt_1_b"
                  radius   =   0.27
               },
               {
                  upLocatorName   =   "headcuirass_cdt_1_a"
                  downLocatorName   =   "headcuirass_cdt_1_b"
                  radius   =   0.3
               }
            ]
         }
      ]
   }
}
__type   =   "pc_marine_pve_client"

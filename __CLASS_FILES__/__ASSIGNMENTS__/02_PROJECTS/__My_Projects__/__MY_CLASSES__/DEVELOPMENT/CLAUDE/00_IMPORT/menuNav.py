"""
═══════════════════════════════════════════════════════════════════════════════
                            CMS MENU NAVIGATION MAP
═══════════════════════════════════════════════════════════════════════════════

ENDPOINT TYPES
──────────────

    FORK        Branch point with multiple choices
                     |
              +------+------+
              |             |
          [Choice A]   [Choice B]

    FLOW        Sequential process with defined steps
                start >----------------> end

    STATION     Terminal endpoint
                ---------> end


═══════════════════════════════════════════════════════════════════════════════
                                 MAIN MENU
═══════════════════════════════════════════════════════════════════════════════

TYPE: FORK

    1   REGISTER NEW ITEM         → Flow
    2   VIEW COLLECTION            → Station
    3   SETTINGS                   → Fork
    4   EXIT                       → Terminal

    [ON HOLD: CHOOSE NEW COLLECTION]


DESIGN:
    MENU WRAPPER
        HEADER|TITLE
        CHOICES MENU WRAPPER
            PROMPT
            CHOICES WRAPPER
                CHOICE

STATES:
    DISPLAY
    WAITING ON INPUT
    SELECTION LOOP
    CHOICE SELECTED
    CHOICE CONFIRMED


{main_menu:{
    fork:{

        1: item_registration,
        2: view_collection, 
        3: settings,
        4: exit_app


    },
    states:{
    
        1: DISPLAY
        2: WAITING ON INPUT,
        3: SELECTION LOOP,
        4: CHOICE SELECTED,
        5: CHOICE CONFIRMED
    
    },
    design:{
    
        1: menu+_wrapper:{
        
            1.1: title,
            1.2: choice_menu_wrapper{
                1.2.1: prompt,
                1.2.2: choices_wrapper{

                    1.2.2.1: choice_object
                
                }
            }
        }
    }
}


═══════════════════════════════════════════════════════════════════════════════
                          1. REGISTER NEW ITEM (FLOW)
═══════════════════════════════════════════════════════════════════════════════

    1.1  GET SETUP PARAMS
         └─ Validate received data

    1.2  DISPLAY PARAMS SUMMARY
         └─ Offer revision option

    1.3  Return to MAIN MENU


{item_registration:{
    flow:{

        1.1: get_setup_params,
        1.2: display_params_summary,
        1.3: return_main_menu

    },
    states:{
        1.1:{
            1: DISPLAY,
            2: WAITING_ON_INPUT,
            3: RECEIVED_INPUT,
            4: CONFIRMATION_DIALOGUE
        },
        1.2:{
            1: DISPLAY_SUMMARY,
            2: WAITING_ON_USER_ACTION,
            3: CONFIRMED,
            4: REVISION_REQUESTED
        }
    },
    design:{
        1.1:{
            1: dialogue_wrapper:{
                1.1: dialogue_prompt,
                1.2: input_field,
                1.3: ok_button
            }
        },
        1.2:{
            1: summary_wrapper:{
                1.1: header,
                1.2: params_list,
                1.3: buttons_wrapper:{
                    1.3.1: confirm_button,
                    1.3.2: revise_button
                }
            }
        }
    }
}


═══════════════════════════════════════════════════════════════════════════════
                       2. VIEW COLLECTION (STATION)
═══════════════════════════════════════════════════════════════════════════════

TYPE: Iterable pages by count

    2.1  COLLECTIONS MENU (FORK)

    2.2  FILTERS
         └─ Apply filter criteria

    2.3  ARCHIVED
         └─ Toggle archived items visibility

    2.4  SELECT ITEM(S)
         └─ Get user selection
             ├─ 2.4.1  BATCH MODIFY PARAMS
             ├─ 2.4.2  COPY
             ├─ 2.4.3  MOVE
             └─ 2.4.4  ARCHIVE / DELETE

    2.5  Return to MAIN MENU


{view_collection:{
    fork:{

        2.1: collections_menu,
        2.2: filters,
        2.3: archived_toggle,
        2.4: select_items:{
            2.4.1: batch_modify,
            2.4.2: copy,
            2.4.3: move,
            2.4.4: archive_delete
        },
        2.5: return_main_menu

    },
    states:{
        2.1:{
            1: DISPLAY,
            2: WAITING_ON_SELECTION,
            3: COLLECTION_SELECTED
        },
        2.2:{
            1: FILTERS_INACTIVE,
            2: FILTERS_ACTIVE,
            3: APPLYING_FILTERS
        },
        2.3:{
            1: ARCHIVED_HIDDEN,
            2: ARCHIVED_VISIBLE
        },
        2.4:{
            1: NO_SELECTION,
            2: ITEMS_SELECTED,
            3: ACTION_IN_PROGRESS,
            4: ACTION_COMPLETED,
            2.4.1:{
                1: EDITING,
                2: VALIDATING,
                3: APPLYING_CHANGES
            },
            2.4.2:{
                1: SELECTING_DESTINATION,
                2: COPYING,
                3: COPY_COMPLETE
            },
            2.4.3:{
                1: SELECTING_DESTINATION,
                2: MOVING,
                3: MOVE_COMPLETE
            },
            2.4.4:{
                1: CONFIRMING_ACTION,
                2: ARCHIVING,
                3: DELETING,
                4: ACTION_COMPLETE
            }
        }
    },
    design:{
        2.1:{
            1: menu_wrapper:{
                1.1: header,
                1.2: collection_list,
                1.3: navigation_controls
            }
        },
        2.2:{
            1: filter_panel:{
                1.1: filter_options,
                1.2: apply_button,
                1.3: clear_button
            }
        },
        2.3:{
            1: toggle_control:{
                1.1: label,
                1.2: switch
            }
        },
        2.4:{
            1: selection_panel:{
                1.1: item_list_checkboxes,
                1.2: action_buttons,
                1.3: cancel_button
            },
            2.4.1:{
                1: modify_dialogue:{
                    1.1: selected_items_display,
                    1.2: param_fields,
                    1.3: apply_button
                }
            },
            2.4.2:{
                1: copy_dialogue:{
                    1.1: source_items,
                    1.2: destination_selector,
                    1.3: copy_button
                }
            },
            2.4.3:{
                1: move_dialogue:{
                    1.1: source_items,
                    1.2: destination_selector,
                    1.3: move_button
                }
            },
            2.4.4:{
                1: confirmation_dialogue:{
                    1.1: warning_message,
                    1.2: selected_items_list,
                    1.3: archive_button,
                    1.4: delete_button,
                    1.5: cancel_button
                }
            }
        }
    }
}


═══════════════════════════════════════════════════════════════════════════════
                  3. CHOOSE NEW COLLECTION (FLOW) [AMBITIOUS]
═══════════════════════════════════════════════════════════════════════════════

FILE BROWSER UI DASHBOARD

    3.1  Navigate directory tree

    3.2  Input target (file/directory) name

    3.3  Save location
         ├─ 3.3.1  Change directory
         └─ 3.3.2  Provide input


{choose_collection:{
    flow:{

        3.1: navigate_directory,
        3.2: input_target_name,
        3.3: save_location:{
            3.3.1: change_directory,
            3.3.2: provide_input
        }

    },
    states:{
        3.1:{
            1: BROWSING,
            2: DIRECTORY_SELECTED,
            3: NAVIGATING
        },
        3.2:{
            1: AWAITING_INPUT,
            2: VALIDATING_NAME,
            3: NAME_ACCEPTED
        },
        3.3:{
            1: CONFIGURING_SAVE,
            2: CHANGING_DIRECTORY,
            3: SAVING,
            4: SAVE_COMPLETE
        }
    },
    design:{
        3.1:{
            1: browser_panel:{
                1.1: directory_tree,
                1.2: path_breadcrumbs,
                1.3: navigation_buttons
            }
        },
        3.2:{
            1: input_dialogue:{
                1.1: prompt,
                1.2: text_field,
                1.3: file_directory_toggle,
                1.4: ok_button
            }
        },
        3.3:{
            1: save_dialogue:{
                1.1: current_path_display,
                1.2: name_field,
                1.3: change_dir_button,
                1.4: save_button
            }
        }
    }
}


═══════════════════════════════════════════════════════════════════════════════
                              4. SETTINGS (FORK)
═══════════════════════════════════════════════════════════════════════════════

    4.1  CHANGE ITEM FIELDS

    4.2  ROTATE COLOR SCHEME

    4.3  CHANGE TITLES


{settings:{
    fork:{

        4.1: change_item_fields,
        4.2: rotate_color_scheme,
        4.3: change_titles

    },
    states:{
        4.1:{
            1: VIEWING_FIELDS,
            2: EDITING_FIELDS,
            3: SAVING_CHANGES
        },
        4.2:{
            1: PREVIEWING,
            2: APPLYING_SCHEME
        },
        4.3:{
            1: EDITING_TITLES,
            2: PREVIEWING_CHANGES,
            3: SAVING_TITLES
        }
    },
    design:{
        4.1:{
            1: settings_panel:{
                1.1: fields_list,
                1.2: add_field_button,
                1.3: remove_field_button,
                1.4: save_button
            }
        },
        4.2:{
            1: color_picker_panel:{
                1.1: scheme_preview,
                1.2: scheme_options,
                1.3: apply_button
            }
        },
        4.3:{
            1: titles_panel:{
                1.1: title_fields,
                1.2: preview,
                1.3: save_button
            }
        }
    }
}
"""





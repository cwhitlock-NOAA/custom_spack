#!/bin/python
#toggle_config_settings.py
#toggles production settings on a set of production files: 
# - the spack.yaml files for the environments

import argparse
import shutil
import os, sys
from os import path as osp
import re
import fileinput

def get_env_file_paths():
    '''
    gets the paths to all spack.yaml files for the environments
    assumes that this file is located in $spack_root/scripts/
    returns: list of paths to spak.yaml files
    '''
    rootdir = osp.dirname(osp.abspath(__file__))
    envdir = osp.join(rootdir, "var/spack/environments/")
    env_file_paths = [osp.join(envidr, el, 'spack.yaml') for el in os.listdir(envdir) if os.isdir(el)]
    print(env_file_paths)    
    return env_file_paths

def toggle_config(cfg_file, cfg_val):
    '''
    uncomments the line below cfg_val and comments the other line
    (thus toggling settings on/off)
    '''
    toggle_vals = ["dev", 'test', 'prod']
    if not cfg_val in toggle_vals:
        print("Error in toggle_config: cfg_val must be one of dev, test or prod!")
        sys.exit(1)
    else:
        searchstrings = [el + " setting toggle" for el in toggle_vals]
        togglestring = cfg_val + " setting toggle"
    edit_next = False
    for line in fileinput.input(cfg_file, inplace=True):
        for searhstr in searchstrings:
            if re.search(searchstr, line) is not None:
                edit_next = True
                if re.search(togglestring, line) is not None:
                    set_on=True
                else:
                    set_on=False
            else:
                edit_next = False
            if edit_next:
                edit_next=False #don't edit 2 lines in a row
                '''
                Below will break if:
                    - value includes a # for non-comment reasons
                    - more than one # in a line
                '''
                if set_on:
                    #remove all '#' before the text - look, this is sloppy but it doesn't need to work perfectly
                    line = re.sub('#', '', line)
                else:
                    #put a '#' before the text if it's not commented already
                    if re.search('#', line) is None:
                        newline = "#" + line
                    line = newline

parser = argparse.ArgumentParser(description='Edits config files to toggle on dev, test or prod settings, as determined by prior line commented with #dev setting toggle', 
epilog="Currently edits: environment spack.yaml files")
parser.add_argument('-t','--toggle', help='Toggle value to turn on; one of dev, test or prod.', 
  required=True)
#parser.add_argument('-d','--dry-run', help='If on, prints settings without editing', required=False, default=False)
args = vars(parser.parse_args())

cfg_files = get_env_file_paths()
for cf in cfg_files:
    toggle_config(cf, args['toggle'])

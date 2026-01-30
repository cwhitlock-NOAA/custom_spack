#!/bin/python
#Makes changes to 3 intel compiler config files: ifx.cfg, icx.cfg, icpx.cfg
#takes locations of intel and gcc locations as arguments

import argparse
import shutil
import os, sys
from os import path as osp

def make_icx_config(intel_path, sys_gcc_path):
  '''
  -Wl,-rpath,/app/spack/2025.02/__spack_path_placeholder__/__spack_path_place/linux-rhel8-x86_64/none-none/intel-oneapi-compilers/2025.2.0-f44atlfpx4ms6qeocxd4ndmpqm4mwnyc/compiler/2025.2/lib --gcc-toolchain=/usr
  '''
  outfile=osp.join(intel_path, "compiler/latest/bin/icx.cfg")
  oldfile=osp.join(intel_path, "compiler/latest/bin/icx.old.cfg")
  #If you run this more than once, you want the oldfile to point to the original config, not the changes you were making
  if not osp.exists(oldfile):
    shutil.copyfile(outfile, oldfile)
  with open(outfile, 'w') as f:
    intel_lib=osp.join(intel_path, "compiler/2025.2/lib")
    if not osp.exists(intel_lib):
      print("Error in make_icx_config: intel_lib path " + intel_lib + " does not exist! Check on the path formation and try again.")
      sys.exit(1)    
    config_string="-Wl,-rpath,"+intel_lib+" --gcc-toolchain="+sys_gcc_path
    f.write(config_string)

def make_icpx_config(intel_path, sys_gcc_path):
  '''
  -Wl,-rpath,/app/spack/2025.02/__spack_path_placeholder__/__spack_path_place/linux-rhel8-x86_64/none-none/intel-oneapi-compilers/2025.2.0-f44atlfpx4ms6qeocxd4ndmpqm4mwnyc/compiler/2025.2/lib --gcc-toolchain=/usr
  '''
  outfile=osp.join(intel_path, "compiler/latest/bin/icpx.cfg")
  oldfile=osp.join(intel_path, "compiler/latest/bin/icpx.old.cfg")
  if not osp.exists(oldfile):
    shutil.copyfile(outfile, oldfile)
  with open(outfile, 'w') as f:
    intel_lib=osp.join(intel_path, "compiler/2025.2/lib")
    if not osp.exists(intel_lib):
      print("Error in make_icpx_config: intel_lib path " + intel_lib + " does not exist! Check on the path formation and try again.")
      sys.exit(1)
    config_string="-Wl,-rpath,"+intel_lib+" --gcc-toolchain="+sys_gcc_path
    f.write(config_string)

def make_ifx_config(intel_path, spack_gcc_path):
  '''
  -Wl,-rpath,/app/spack/2025.02/__spack_path_placeholder__/__spack_path_place/linux-rhel8-x86_64/none-none/intel-oneapi-compilers/2025.2.0-f44atlfpx4ms6qeocxd4ndmpqm4mwnyc/compiler/2025.2/lib -gcc-name=/app/spack/2025.02/__spack_path_placeholder__/__spack_path_place/linux-rhel8-x86_64/gcc-13.4.0/gcc/13.4.0-bqkcbwz5nlnvlchsuejmuywvbebkpsnu/bin/gcc -gxx-name=/app/spack/2025.02/__spack_path_placeholder__/__spack_path_place/linux-rhel8-x86_64/gcc-13.4.0/gcc/13.4.0-bqkcbwz5nlnvlchsuejmuywvbebkpsnu/bin/g++
  '''
  outfile=osp.join(intel_path, "compiler/latest/bin/ifx.cfg")
  oldfile=osp.join(intel_path, "compiler/latest/bin/ifx.old.cfg")
  if not osp.exists(oldfile):
    shutil.copyfile(outfile, oldfile)
  with open(outfile, 'w') as f:
    intel_lib=osp.join(intel_path, "compiler/2025.2/lib")
    gcc_name=osp.join(spack_gcc_path, "bin/gcc")
    gxx_name=osp.join(spack_gcc_path, "bin/g++")
    for path in [intel_lib, gcc_name, gxx_name]:
      if not osp.exists(path):
        print("Error in make_ifx_config: path " + path + " does not exist!")
        sys.exit(1)
    config_string="-Wl,-rpath,"+intel_lib+" -gcc-name="+gcc_name+" -gxx-name="+gxx_name
    f.write(config_string)
    
# Source - https://stackoverflow.com/a
# Posted by Diego Navarro, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-22, License - CC BY-SA 4.0
#taken from diego navarro on stackoverflow
parser = argparse.ArgumentParser(description='Makes config file edits to 3 files in the intel compilers binary files: ifx.cfg, icx.cfg and icpx.cfg', 
epilog="You can get pacakge paths by doing `spack find --paths | grep $pacakge-name`; running this with just the intel arg cats ifx.cfg")
parser.add_argument('-i','--intel', help='Path to intel compilers', required=True)
parser.add_argument('-g','--gcc', default="empty", help='Path to spack gcc (higher than system gcc); obtained from ifx.cfg', required=False)
parser.add_argument('-s','--sys-gcc', default='/usr', help='Path to system gcc; defaults to /usr', required=False)
args = vars(parser.parse_args())

#intel value: /app/spack/2025.02/__spack_path_placeholder__/__spack_path_place/linux-rhel8-x86_64/none-none/intel-oneapi-compilers/2025.2.0-5wvmkz6fqzgpac2d6i7b7q5eikzadsac
#gcc value: /decp/oar.gfdl.sw/spack/v1.0-2025.02-sepR-prod/spack/opt/spack/_/linux-rhel8-x86_64/gcc-13.4.0/gcc/13.4.0-u5jdzy5exfmp4w2los6vtmrfrg4wij5l
#sys gcc value: /usr (/usr/bin/gcc)

if args['gcc'] == 'empty':
  fname = args['intel'] + "/compiler/latest/bin/ifx.cfg"
  print(fname)
  with open(fname, 'r') as f:
      print(f.read())
else:
  make_icx_config(args['intel'], args['sys_gcc'])
  make_icpx_config(args['intel'], args['sys_gcc'])
  make_ifx_config(args['intel'], args['gcc'])

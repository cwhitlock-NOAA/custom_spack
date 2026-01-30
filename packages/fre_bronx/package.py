# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class FreBronx(Package):
    """This library contains the code and environment setup needed to run
       the FMS Runtime Environment (FRE) Bronx edition.
       This is deprecated; we are trying very hard to switch to FRE Canopy."""

    homepage = "https://github.com/NOAA-GFDL/FRE"
    git = "https://github.com/NOAA-GFDL/FRE.git"

    # list of GitHub accounts to
    # notify when the package is updated.
    maintainers("cwhitlock-NOAA")

    #versions (listed from most recent to least recent)
    #add md5 checksum at some point
    version("v2.22.3",  submodules=True)
    #If we try to tie this to git branch releases,
    #the slashes are bad characters - need to rename?

    # dependencies
    depends_on("nccmp")
    depends_on("netcdf-c")
    depends_on("nco")
    depends_on("fre-nctools")
    #Note: we also depend on gcp and hsm, but that's lab-local and not built in spack:
    # we need to add a module load to the modulefile after the fact

    def setup_run_environment(self, env):
        pkg_prefix = self.spec.prefix
        
        #This specific set of variables is being left alone for now -
        #it points to things that don't lvie in spack
        env.set('FRE_ANALYSIS_HOME', '/home/fms/local/opt/fre-analysis/test')
        env.set('FRE_ANALYSIS_GIT_URL', 'file:///home/fms/local/opt/fre-analysis/git')
        env.set('FRE_ANALYSIS_ARCHIVE', '/archive/fms/fre-analysis/test')
        env.append_path('PATH', '/home/fms/local/opt/fre-analysis/test/shared/bin')
    
        env.set('FRE_SYSTEM_MODULEFILES_DIR', 
                 join_path(self.spec.prefix, "share/spack/modules/linux-rhel8-x86_64/"))
        env.set('FRE_SYSTEM_SITE', 'gfdl-ws')
        #taken from https://github.com/NOAA-GFDL/FRE/tree/main/site
        env.set('FRE_SYSTEM_SITES', 'gfdl-ws:gfdl:ncrc5:ncrc_common:ncrc')
        env.set('FRE_SYSTEM_TMP', '/tmp')
        pathvars = [join_path(self.spec.prefix, "bin"), 
		    join_path(self.spec.prefix, "sbin"), 
		    join_path(self.spec.prefix, "site/gfdl-ws/bin")]
        env.prepend_path('PATH', ":".join(pathvars))
        env.prepend_path('PERL5LIB', join_path(self.spec.prefix, 'lib'))
        env.prepend_path('MANPATH', join_path(self.spec.prefix, 'man'))

        env.set('FRE_COMMANDS_HOME', self.spec.prefix)
        env.set('FRE_COMMANDS_VERSION', 'bronx-22')

    def install(self, spec, prefix):
        #install_tree(self.stage.source_path, prefix)
        install_tree(".", prefix)


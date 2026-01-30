# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack.package import *


class FreNctools(AutotoolsPackage):
    """FRE-NCtools is a collection of tools to help with the creation and manipulation of netCDF
       files used for or written by the climate models developed at the Geophysical Fluid Dynaics
       Laboratory (GFDL)."""

    homepage = "https://github.com/NOAA-GFDL/FRE-NCtools"
#   url = "https://github.com/NOAA-GFDL/FRE-NCtools/archive/refs/tags/2024.05.02.tar.gz"
    git = "https://github.com/NOAA-GFDL/FRE-NCtools.git"

    maintainers("underwoo", "ceblanton", "ngs333")

    license("LGPL-3.0")

    # Versions
    version("2022.02", tag="2022.02")
    version("2023.01", tag="2023.01")
    version("2023.01.01", tag="2023.01.01")
    version("2023.01.02", tag="2023.01.02")
    version("2024.01", tag="2024.01")
    version("2024.02", tag="2024.02")
    version("2024.03", tag="2024.03")
    version("2024.04", tag="2024.04")
    version("2024.05", tag="2024.05")
    version("2024.05.01", tag="2024.05.01")
    version("2024.05.02", tag="2024.05.02")

    # Variants
    variant("quad-precision", default=False, description="Enable higher (quad) precision")
    variant("mpi", default=True, description="Enable MPI support")

    # Add dependencies if required.
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("nco")
    depends_on("netcdf-c~mpi", when="~mpi")
    depends_on("netcdf-c+mpi", when="+mpi")
    depends_on("netcdf-fortran")
    depends_on("mpi", when="+mpi")

    install_targets = ['install-exec']

    def configure_args(self):
        args = self.enable_or_disable("quad-precision")
        args += self.with_or_without("mpi")
        return args

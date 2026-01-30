# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Rstudio(Package):
    """RStudio is integrated development environment (IDE) for R."""

    homepage = "https://www.rstudio.com"

    version('2024.12.1', sha256='5740785f4f53019e23b71f21c476e20e528a11c6b5cf3663d66719753b92c5a1', url='https://download1.rstudio.org/electron/rhel8/x86_64/rstudio-2024.12.1-563-x86_64-fedora.tar.gz')
    version('2024.12.0', sha256='f8fc9b5165a08b9495906adf4e13fe03c0e86f9c432b689bb5b1c680825f93e0', url='https://download1.rstudio.org/electron/rhel8/x86_64/rstudio-2024.12.0-467-x86_64-fedora.tar.gz')
    version('2024.09.1', sha256='61494dac3b8d06b03ed5300ae16142da67279128a7d90ab5973f154bba000c36', url='https://download1.rstudio.org/electron/rhel8/x86_64/rstudio-2024.09.1-394-x86_64-fedora.tar.gz')
    version('2024.09.0', sha256='2d5b80830f95fe0248423ac9e390b2e0c7b996cb388bde54735a102c4b5c7a6d', url='https://download1.rstudio.org/electron/rhel8/x86_64/rstudio-2024.09.0-375-x86_64-fedora.tar.gz')
    version('2023.09.1', sha256='6c23578a1a4d47baa502d8ce3b8bdddcb759020919ac8f34535588c19cc06ffd', url='https://download1.rstudio.org/electron/centos7/x86_64/rstudio-2023.09.1-494-x86_64-fedora.tar.gz')
    version('2022.02.1', sha256='29cb4d5f84bbacd15ecd1b62d3b7bb152081a6372ef20e4602ea717cc45fb256', url='https://download1.rstudio.org/desktop/centos7/x86_64/rstudio-2022.02.1-461-x86_64-fedora.tar.gz')
    version('2022.12.0', sha256='bf4087ff5810cf5deec70190ab0c462c8b10c0961d64faa3a77c28ca77b6e318', url='https://download1.rstudio.org/electron/centos7/x86_64/rstudio-2022.12.0-353-x86_64-fedora.tar.gz')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

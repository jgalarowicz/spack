##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RShiny(Package):
    """Makes it incredibly easy to build interactive web applications with R.
    Automatic "reactive" binding between inputs and outputs and extensive
    pre-built widgets make it possible to build beautiful, responsive, and
    powerful applications with minimal effort."""

    homepage = "http://shiny.rstudio.com/"
    url      = "https://cran.r-project.org/src/contrib/shiny_0.13.2.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/shiny"

    version('0.13.2', 'cb5bff7a28ad59ec2883cd0912ca9611')

    extends('r')

    depends_on('r-httpuv', type=nolink)
    depends_on('r-mime', type=nolink)
    depends_on('r-jsonlite', type=nolink)
    depends_on('r-xtable', type=nolink)
    depends_on('r-digest', type=nolink)
    depends_on('r-htmltools', type=nolink)
    depends_on('r-r6', type=nolink)

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)

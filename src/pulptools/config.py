#
# Copyright (c) 2010 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
#


import os
from iniparse import INIConfig as Base


class Config(Base):
    """
    The pulp client configuration.
    @cvar PATH: The absolute path to the config directory.
    @type PATH: str
    """

    PATH = '/etc/pulp/client.conf'

    def __init__(self):
        """
        Open the configuration.
        """
        fp = open(self.PATH)
        try:
            Base.__init__(self, fp)
        finally:
            fp.close()

    def write(self):
        """
        Write the configuration.
        """
        fp = open(self.PATH, 'w')
        try:
            fp.write(str(self))
        finally:
            fp.close()

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

from suds import *
from suds.schema import XBuiltin
from suds.bindings.binding import Binding
from suds.schema import qualified_reference

log = logger(__name__)

class RPC(Binding):
    """
    RPC/Literal binding style.
    """

    def __init__(self, wsdl):
        """
        @param wsdl: A WSDL object.
        @type wsdl: L{suds.wsdl.WSDL}
        """
        Binding.__init__(self, wsdl)
        
    def part_refattr(self):
        """
        Get the part attribute that defines the part's I{type}.
        @return: An attribute name.
        @rtype: basestring 
        """
        return "type"
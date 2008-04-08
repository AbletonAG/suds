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

import logging

VERSION = "0.1.7"

#
# Exceptions
#

class MethodNotFound(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __unicode__(self):
        return 'service method: %s not-found' % unicode(self.name)
    
class TypeNotFound(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __unicode__(self):
        return 'WSDL type: %s not-found' % unicode(self.name)
    
class BuildError(Exception):
    def __init__(self, type):
        self.type = type
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __unicode__(self):
        return \
            """
            An error occured while building a instance of (%s).  As a result
            the object you requested could not be constructed.  It is recommended
            that you construct the type manually uisng a Property object.
            Please notify the project mantainer of this error.
            """ % unicode(self.type)
    
class WebFault(Exception):
    def __init__(self, type):
        self.type = type
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __unicode__(self):
        return 'service endpoint raised fault %s\n' % unicode(self.type)

#
# Logging
#

def logger(name=None):
    if name is None:
        return logging.getLogger()
    fmt =\
        '%(asctime)s {%(process)d} (%(filename)s, %(lineno)d) [%(levelname)s] %(message)s'
    logger = logging.getLogger('suds.%s' % name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        __handler = logging.StreamHandler()
        __handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(__handler)
    return logger


#
# Utility
#

def tostr(object):
    """ get a unicode safe string representation of an object """
    if isinstance(object, basestring):
        return object
    if isinstance(object, tuple):
        s = ['(']
        for item in object:
            if isinstance(item, basestring):
                s.append(item)
                continue
            if hasattr(item, '__unicode__'):
                s.append(unicode(item))
            else:
                s.append(str(item))
        s.append(')')
        return ''.join(s)
    if isinstance(object, list):
        s = ['[']
        for item in object:
            if isinstance(item, basestring):
                s.append(item)
                continue
            if hasattr(item, '__unicode__'):
                s.append(unicode(item))
            else:
                s.append(str(item))
        s.append(']')
        return ''.join(s)
    if isinstance(object, dict):
        s = ['{']
        for item in object.items():
            if isinstance(item, basestring):
                s.append(item)
                continue
            if hasattr(item[0], '__unicode__'):
                s.append(unicode(item[0]))
            else:
                s.append(str(item[0]))
            s.append(' = ')
            if hasattr(item[1], '__unicode__'):
                s.append(unicode(item[1]))
            else:
                s.append(str(item[1]))
        s.append('}')
        return ''.join(s)
    if hasattr(object, '__unicode__'):
        return unicode(object)
    else:
        return str(object)

# vim: foldmethod=marker
#{{{ License header: GPLv2+
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
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#}}}
'''
Testing the addressbook module
'''
from nose import with_setup
import gbirthday

AB = None

def setup():
    '''Setup addressbook.'''
    global AB
    AB = gbirthday.AddressBook()

def teardown():
    '''Clean addressbook.'''
    global AB
    AB = None

@with_setup(setup, teardown)
def test1():
    '''dummy1'''
    assert AB

@with_setup(setup, teardown)
def test2():
    '''dummy2'''
    assert AB

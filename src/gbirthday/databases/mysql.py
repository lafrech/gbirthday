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

from PyQt4 import QtCore, QtGui

from gbirthday import load_ui
from gbirthday.databases import DataBase
from gbirthday.gtk_funcs import show_error_msg

class MySqlPreferencesDialog(QtGui.QDialog):
    '''MySQL backend settings dialog'''

    def __init__(self, settings, parent):

        super().__init__(parent)

        load_ui('mysqlpreferencesdialog.ui', self)

        self.settings = settings

        # TODO: add code here

        self.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.save)
        self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.save)

        # TODO: disable OK and Apply if no path provided

    def save(self):
        '''Save MySQL backend settings'''
        pass

class MySQL(DataBase):
    '''MySQL database import'''

    TITLE = 'MySQL'
    CAN_SAVE = True
    HAS_CONFIG = True
    CONFIG_DLG = MySqlPreferencesDialog

    def __init__(self, addressbook, settings):

        super().__init__(addressbook, settings)
        
        self.host = 'localhost'
        self.port = '3306'
        self.username = ''
        self.password = ''
        self.database = ''
        self.table = 'person'
        self.name_row = 'name'
        self.date_row = 'date'
        self.cursor = None
        self.conn = None

    def connect(self):
        '''establish connection'''
        try:
            import MySQLdb
        except:
            show_error_msg(_("Package %s is not installed." % "MySQLdb"))
        try:
            self.conn = MySQLdb.connect(host=self.host,
                                    port=int(self.port),
                                    user=self.username,
                                    passwd=self.password,
                                    db=self.database)
            self.cursor = self.conn.cursor()
        except Exception as msg:
            show_error_msg(_('Could not connect to MySQL-Server')
                            + str(msg))
            return False
        return True

    def parse(self):
        '''connect to mysql-database and get data'''
        if not self.connect():
            return
        try:
            qry = ("SELECT %s, %s FROM %s"
                        % (self.name_row, self.date_row, self.table))
            self.cursor.execute(qry)
            rows = self.cursor.fetchall()
            for row in rows:
                addressbook.add(row[0], str(row[1]))
        except Exception as msg:
            show_error_msg(_('Could not execute MySQL-query')
                            + ': %s\n %s' % (qry, str(msg)))
        self.conn.close()

    def add(self, name, birthday):
        '''insert new Birthday to database'''
        birthday = str(birthday)
        self.connect()
        try:
            qry = ("INSERT INTO %s (%s, %s) VALUES ('%s', '%s')" %
                (self.table, self.name_row, self.date_row, name, birthday))
            self.cursor.execute(qry)
        except Exception as msg:
            show_error_msg(_('Could not execute MySQL-query')
                            + ': %s\n %s' % (qry, str(msg)))
        self.conn.close()
        self.addressbook.add(name, birthday)

    def save_config(self, conf):
        '''Save modifications'''
        self.host = self.entries[0].get_text()
        self.port = self.entries[1].get_text()
        self.username = self.entries[2].get_text()
        self.password = self.entries[3].get_text()
        self.database = self.entries[4].get_text()
        self.table = self.entries[5].get_text()
        self.name_row = self.entries[6].get_text()
        self.date_row = self.entries[7].get_text()
        conf.MySQL = self


    def create_config(self, vbox, conf):
        '''create additional mysql config in config menu'''

        # TODO
        pass

#         values = [
#                   ['Host', self.host],
#                   ['Port', self.port],
#                   ['Username', self.username],
#                   ['Password', self.password],
#                   ['Database', self.database],
#                   ['Table', self.table],
#                   ['Name row', self.name_row],
#                   ['Date row', self.date_row]
#                  ]
#         self.entries = []
# 
#         sqltable = gtk.Table(len(values), 2, False)
#         sqltable.set_col_spacings(5)
#         for i, value in enumerate(values):
#             label = gtk.Label(value[0])
#             label.set_alignment(1, 0.5)
#             label.show()
#             sqltable.attach(label, 0, 1, i, i + 1)
# 
#             entry = gtk.Entry()
#             entry.set_text(value[1])
#             entry.show()
#             self.entries.append(entry)
#             sqltable.attach(entry, 1, 2, i, i + 1)
#         
#         sqltable.show()
#         vbox.pack_start(sqltable, False, False, 0)
# 

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import PathnamePlugin

from calibre.utils.filenames import ascii_filename

class PathnameBySeriesStrategy(PathnamePlugin):

    def __init__(self, database):
        self.database = database

    def construct_path_name(self, book_id):
        print("PathnameBySeries: Me is %s" % PathnameBySeriesStrategy.__name__)
        print("PathnameBySeries: self: %s" % (self))
        print("PathnameBySeries: db  : %s" % (self.database))
        print("PathnameBySeries: bkid: %s" % (book_id))

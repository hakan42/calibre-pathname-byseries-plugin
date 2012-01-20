#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import PathnamePlugin

from calibre.utils.filenames import ascii_filename

class PathnameBySeries(PathnamePlugin):

    name = 'Pathname By Series'
    description = _('Adds the "series" metadata field into the path')
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Hakan Tandogan'
    version = (1, 0, 0)
    # TODO change m_c_version to whatever version has my changes added to it
    minimum_calibre_version = (0, 8, 33)

    # Actual code that constructs the path name
    def __init__(self, database):
        self.database = database

    def construct_path_name(self, book_id):
        print("PathnameBySeries: Me is %s" % PathnameBySeries.__name__)
        print("PathnameBySeries: self: %s" % (self))
        print("PathnameBySeries: db  : %s" % (self.database))
        print("PathnameBySeries: bkid: %s" % (book_id))

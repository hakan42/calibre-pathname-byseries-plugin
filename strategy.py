#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

import traceback

from calibre.customize import PathnamePlugin
from calibre.constants import filesystem_encoding
from calibre.utils.filenames import ascii_filename


class PathnameBySeriesStrategy(PathnamePlugin):

    def __init__(self, database):
        self.database = database
        # TODO make prefix configurable
        self.series_prefix = _('Series')
        # TODO make default source configurable
        self.default_series = None

    def construct_path_name(self, book_id):
        print("  PbSeriesS is %s" % (__name__))
        print("  PbSeriesS: self : %s" % (self))
        print("  PbSeriesS: database: %s" % (self.database))
        print("  PbSeriesS: book id : %s" % (book_id))

        path_element = None

        try:
            series = self.database.series(book_id, index_is_id=True)
            print("    PbSourceS: series: '%s'" % (series))

            if series:
                series_prefix = self.series_prefix
                series_prefix = ascii_filename(series_prefix[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                series_name = ascii_filename(series[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                path_element = series_prefix + "/" + series_name
        except:
            traceback.print_exc()

        # print("PathnameBySeriesStrategy: path_name_element: '%s'" % (path_name_element))

        return path_element

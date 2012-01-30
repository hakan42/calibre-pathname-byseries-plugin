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

    def construct_path_name(self, book_id):
        # print("PathnameBySeriesStrategy: Me is %s" % PathnameBySeriesStrategy.__name__)
        # print("PathnameBySeriesStrategy: self: %s" % (self))
        # print("PathnameBySeriesStrategy: db  : %s" % (self.database))
        # print("PathnameBySeriesStrategy: bkid: %s" % (book_id))

        path_name_element = None

        try:
            series = self.database.series(book_id, index_is_id=True)
            # print("PathnameBySeriesStrategy: series: '%s'" % (series))
            if series:
                series_prefix = self.series_prefix
                series_prefix = ascii_filename(series_prefix[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                series_name = ascii_filename(series[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                path_name_element = series_prefix + "/" + series_name
        except:
            traceback.print_exc()

        # print("PathnameBySeriesStrategy: path_name_element: '%s'" % (path_name_element))

        return path_name_element

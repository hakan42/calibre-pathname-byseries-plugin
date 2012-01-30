#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import PathnamePlugin

class PathnameBySeries(PathnamePlugin):

    name = 'Pathname By Series'
    description = _('Adds the "series" metadata field into the path')
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Hakan Tandogan'
    version = (1, 0, 0)
    # TODO change m_c_version to whatever version has my changes added to it
    minimum_calibre_version = (0, 8, 33)

    # The order in which enabled pathname plugins are evaluated.
    # TODO make configurable
    order = 20

    # Setup stuff
    def __init__(self, database):
        from calibre_plugins.pathname_byseries.strategy import PathnameBySeriesStrategy
        self.strategy = PathnameBySeriesStrategy(database)

    # Facade for the actual code that constructs the path name
    def construct_path_name(self, book_id):
        return self.strategy.construct_path_name(book_id)

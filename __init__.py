#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import PathnamePlugin

class PathnameBySeries(PathnamePlugin):

    name = 'Pathname By Series'
    actual_plugin = 'calibre_plugins.pathname_byseries.strategy:PathnameBySeriesStrategy'
    description = _('Adds the "series" metadata field into the path')
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Hakan Tandogan'
    version = (1, 0, 0)
    minimum_calibre_version = (0, 9, 1)

    # The order in which enabled pathname plugins are evaluated.
    # TODO make configurable
    order = 10

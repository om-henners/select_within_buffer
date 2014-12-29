# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectWithinBuffer
                                 A QGIS plugin
 Select data within a buffer
                             -------------------
        begin                : 2014-12-29
        copyright            : (C) 2014 by we-do-IT
        email                : info@we-do-it.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SelectWithinBuffer class from file SelectWithinBuffer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .select_within_buffer import SelectWithinBuffer
    return SelectWithinBuffer(iface)

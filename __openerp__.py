# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Order Directly to Done',
    'category': 'Sales',
    'version': '1.0',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['sale_stock'],
    'description': """
Sale Order Directly to Done
===========================
 * Sale orders with a total of 0.00 EUR go directly to done state when they are confirmed
 * Only useful in very limited cases where 0.00€ SOs may exist, and they want to be put to done state to avoid cluttering list views. 

""",
    'data': [
    ],

}

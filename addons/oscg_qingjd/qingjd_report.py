# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from report import report_sxw

class oscg_qingjd(report_sxw.rml_parse):      #解析类
    def __init__(self, cr, uid, name, context=None):
        super(oscg_qingjd, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'helloworld':self.helloworld,
        })
        
    def helloworld(self):
	    return 'Hello World!!'

report_sxw.report_sxw('report.qingjd', 'oscg_qingjd', 'addons/oscg_qingjd/qingjd_report.rml', parser=oscg_qingjd, header="external")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
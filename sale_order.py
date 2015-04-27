# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class sale_order(osv.Model):

    _inherit = 'sale.order'
    
    def action_wait(self, cr, uid, ids, context=None):
        
        context = context or {}
        res = super(sale_order, self).action_wait(cr, uid, ids, context)
    
        for o in self.browse(cr, uid, ids):
            if o.amount_total == 0:
                self.write(cr, uid, [o.id], {'state': 'done', 'date_confirm': fields.date.context_today(self, cr, uid, context=context)})
                self.pool.get('sale.order.line').write(cr, uid, [x.id for x in o.order_line], {'state':'done'}, context=context)        
        return res                 

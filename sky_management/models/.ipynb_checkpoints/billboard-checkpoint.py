from odoo import models, fields, api


class SkyBillboard(models.Model):
    _name = 'sky.billboard'
    _description = 'Sky Billboard'
    
    
    name = fields.Char(string = "Billboard Name")
    site = fields.Many2one('billboard.site', string = 'Billboards Location')
    start_date = fields.Date(string = "Start Reservation Date")
    end_date = fields.Date(string = "End Reservation Date")

       
    status = fields.Selection([
        ('occupied', 'Occupied'),
        ('available', 'Available')
        ], default='available',readonly="1")
    
    image = fields.Binary(string = 'Billboard Image')
    
#      @api.onchange("start_date")
#     def _onchange_start_date(self):
#         if self.start_date:
#             self.update({ "status":'occupied', })
#         else: 
#             self.update({ "status":'available', })
            
    
    
    

    
    
class BillboardSite(models.Model):
    
    _name = 'billboard.site'
    _description = 'Billboard Site'
    
    
    name = fields.Char(string = "Site Name")
    
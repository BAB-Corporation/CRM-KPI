from odoo import models, fields, api

class CrmLeadKpi(models.Model):
    _name = 'crm.lead.kpi'
    _description = 'CRM Lead KPI'

    name = fields.Char(string='KPI Name', required=True)
    lead_id = fields.Many2one('crm.lead', string='Lead/Opportunity', required=True)
    month_1 = fields.Float(string='January')
    month_2 = fields.Float(string='February')
    month_3 = fields.Float(string='March')
    month_4 = fields.Float(string='April')
    month_5 = fields.Float(string='May')
    month_6 = fields.Float(string='June')
    month_7 = fields.Float(string='July')
    month_8 = fields.Float(string='August')
    month_9 = fields.Float(string='September')
    month_10 = fields.Float(string='October')
    month_11 = fields.Float(string='November')
    month_12 = fields.Float(string='December')
    total = fields.Float(string='Total', compute='_compute_total')
    average_deal_size = fields.Float(string='Average Deal Size')
    required_deals = fields.Float(string='Required Deals')

    @api.depends('month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6',
                 'month_7', 'month_8', 'month_9', 'month_10', 'month_11', 'month_12')
    def _compute_total(self):
        for record in self:
            record.total = sum([
                record.month_1, record.month_2, record.month_3,
                record.month_4, record.month_5, record.month_6,
                record.month_7, record.month_8, record.month_9,
                record.month_10, record.month_11, record.month_12
            ])

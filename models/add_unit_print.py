# -*- coding: utf-8 -*-
from odoo import models, fields, api



class AddFieldDun(models.Model):
    _inherit = 'product.template'

    unit_print = fields.Many2one('product.packaging', string='Unidad Impresión', related='packaging_ids.product_id')
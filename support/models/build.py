# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Support(models.Model):
    _name = "support_pipeline"
    _description = "Support Pipeline 24/7"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')

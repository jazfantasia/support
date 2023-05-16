# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EstateDev(models.Model):
    _name = "estate.development"
    _description = "Estate Development"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string="Age")
    description = fields.Text(string="Desc")
    notes = fields.Text(string="Notes")
    
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Forma(models.Model):
     _name = 'forma'
     _description = 'son las formas farmaceuticas del medicamento'

     name = fields.Char("Nombre")

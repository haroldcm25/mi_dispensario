# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Principio(models.Model):
     _name = 'principio'
     _description = 'son los principios activos del medicamento'

     name = fields.Char("Nombre")

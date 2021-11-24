# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClasificaProducto(models.Model):
     _name = 'clasifica_producto'
     _description = 'son las bodegas de la empresa'

     name = fields.Char("Nombre")

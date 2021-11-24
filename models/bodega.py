# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Bodega(models.Model):
     _name = 'bodega'
     _description = 'son las bodegas de la empresa'

     name = fields.Char('Nombre')

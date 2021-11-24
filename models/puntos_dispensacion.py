# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PuntosDispensacion(models.Model):
     _name = 'puntos_dispensacion'
     _description = 'Son los puntos de dispensacion que reciben medicamentos de la empresa'

     bodega_id = fields.Many2one('bodega', string="Bodega" ) #required=False
     descripcion = fields.Char("Descripción")

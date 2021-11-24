# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movimiento(models.Model):
     _name = 'movimiento'
     _description = 'identifica si el movimiento es de salida o entrada'

     name = fields.Char("Nombre")

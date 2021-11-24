# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
     _name = 'cliente'
     _description = 'son las bodegas de la empresa'

     nit_cliente = fields.Char(string="Nit")
     razon_social = fields.Char(string="Razón Social")

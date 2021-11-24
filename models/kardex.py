# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Kardex(models.Model):
     _name = 'kardex'
     _description = 'tiene los movimientos de entradas y salidas de productos'

     lote = fields.Char("Lote")
     fecha_vencimiento = fields.Date("Fecha vencimiento")
     entrada = fields.Integer("Entrada")
     salida = fields.Integer("Salida")

     #bodega
     bodega_id = fields.Many2one('bodega', string="Bodega" ) #required=False

     #producto
     producto_id = fields.Many2one('producto', string="Producto")

     #movimiento
     movimiento_id = fields.Many2one('movimiento', string="Movimiento")





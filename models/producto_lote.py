# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductoLote(models.Model):
     _name = 'producto_lote'
     _description = 'Son los lotes que ingresan de cada producto'

     lote = fields.Char("Lote")
     fecha_vencimiento = fields.Date("Fecha vencimiento")
     cantidad = fields.Integer("Cantidad")
     total = fields.Float("Total")
     costo = fields.Float("Costo")

     #producto
     producto_id = fields.Many2one('producto', string="Producto" ) #required=False

     #Bodega
     bodega_id = fields.Many2one('bodega', string="Bodega")

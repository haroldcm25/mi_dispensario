# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DetalleCompra(models.Model):
     _name = 'detalle_compra'
     _description = 'son los items agregados a la compra'

     lote = fields.Char("Lote")
     fecha_vencimiento = fields.Date("Fecha vencimiento")
     cantidad = fields.Integer("Cantidad")

     #orden de compra
     orden_compra_id = fields.Many2one('orden', string="Orden de Compra")  # required=False

     #producto
     producto_id = fields.Many2one('producto', string="Producto" )

     #bodega
     bodega_id = fields.Many2one('bodega', string="Bodega")





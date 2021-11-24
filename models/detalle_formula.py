# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DetalleFormula(models.Model):
     _name = 'detalle_formula'
     _description = 'Son los productos que se agregan a las formulas'

     lote = fields.Char("Lote")
     fecha_vencimiento = fields.Date("Fecha vencimiento")
     entrada = fields.Integer("Entrada")
     salida = fields.Integer("Salida")

     #puntos dispensación
     puntos_dispensacion_id = fields.Many2one('puntos_dispensacion', string="Puntos dispensación")

     #bodega
     bodega_id = fields.Many2one('bodega', string="Bodega" ) #required=False

     #formula
     formula_id = fields.Many2one('formula', string="Formula")

     #producto
     producto_id = fields.Many2one('producto', string="Producto")

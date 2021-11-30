# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenCompra(models.Model):
     _name = 'orden_compra'
     _description = 'son las solicitudes u ordenes que se ingresan al inventario(falta recepcionar, se ingresará directo para la prueba)'

     descripcion = fields.Char("Descripción")
     formas_pago = fields.Char("Formas de pago")
     total = fields.Float("Total")

     #proveedor
     proveedor_id = fields.Many2one('proveedor', string="Proveedor")

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Producto(models.Model):
     _name = 'producto'
     _description = 'medicamentos de mi dispensario'

     costo = fields.Float("Costo")
     costo_promedio = fields.Float("Costo promedio")
     existencias = fields.Integer("Existencias")
     active = fields.Boolean("Estado", default=True)

     #principio
     principio_id = fields.Many2one('principio', string="Principio")  # required=False

     #forma
     forma_id = fields.Many2one('forma', string="Forma")

     #presentacion
     presentacion_id = fields.Many2one('presentacion', string="Presentación")

     #laboratorio
     laboratorio_id = fields.Many2one('laboratorio', string="Laboratorio")

     #proveedor
     proveedor_id = fields.Many2one('proveedor', string="Proveedor")

     #clasificacion
     clasificacion_id = fields.Many2one('clasifica_producto', string="Clasificación")

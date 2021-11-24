
from odoo import models, fields, api


class Presentacion(models.Model):
     _name = 'presentacion'
     _description = 'son la presentacion del medicamento'

     name = fields.Char("Nombre")
     cantidad_x_presentacion = fields.Integer("Cantidad por presentación")

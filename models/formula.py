# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Formula(models.Model):
     _name = 'formula'
     _description = 'Es donde se registra los datos de la fromula dada'

     edad = fields.Char("Edad")
     fecha_formula = fields.Date("Fecha fórmula")
     fecha_dispensacion = fields.Date("Fecha dispensación")
     fecha_factura = fields.Date("Fecha factura")

     #punto dispensacion
     punto_dispensacion_id = fields.Many2one('punto_dispensacion', string="Punto dispensación" ) #required=False

     #cliente
     cliente_id = fields.Many2one('cliente', string="Cliente Relacionado")
     nit_cliente = fields.Char(string="Cliente", related="cliente_id.nit_cliente")

     #medico
     medico_id = fields.Many2one('medico', string="Medico")
     cedula_medico = fields.Char('medico', related="medico_id.cedula")

     #paciente
     paciente_id = fields.Many2one('paciente', string="Paciente")
     cedula_paciente = fields.Char(string='Cedula Paciente', related="paciente_id.cedula")





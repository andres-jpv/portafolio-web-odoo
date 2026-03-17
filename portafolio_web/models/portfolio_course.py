# -*- coding: utf-8 -*-
from odoo import models, fields


class PortfolioCourse(models.Model):
    _name = 'portfolio.course'
    _description = 'Curso o certificación'
    _order = 'year desc, id'

    developer_id = fields.Many2one(
        'portfolio.developer',
        string='Desarrollador',
        required=True,
        ondelete='cascade',
    )
    name = fields.Char('Nombre del curso', required=True)
    institution = fields.Char('Institución / Plataforma')
    year = fields.Integer('Año')

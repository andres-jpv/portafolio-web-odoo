# -*- coding: utf-8 -*-
from odoo import models, fields


class PortfolioEducation(models.Model):
    _name = 'portfolio.education'
    _description = 'Formación académica'
    _order = 'date_end desc'

    developer_id = fields.Many2one(
        'portfolio.developer',
        string='Desarrollador',
        required=True,
        ondelete='cascade',
    )
    institution = fields.Char('Institución', required=True)
    area = fields.Char('Área / Especialidad')
    degree = fields.Char('Título / Grado')
    location = fields.Char('Ubicación')
    date_start = fields.Date('Fecha inicio')
    date_end = fields.Date('Fecha fin')
    highlights = fields.Text('Descripción / Logros')

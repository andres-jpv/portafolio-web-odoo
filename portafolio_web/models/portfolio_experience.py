# -*- coding: utf-8 -*-
from odoo import models, fields


class PortfolioExperience(models.Model):
    _name = 'portfolio.experience'
    _description = 'Experiencia laboral'
    _order = 'date_start desc'

    developer_id = fields.Many2one(
        'portfolio.developer',
        string='Desarrollador',
        required=True,
        ondelete='cascade',
    )
    company = fields.Char('Empresa', required=True)
    position = fields.Char('Puesto', required=True)
    location = fields.Char('Ubicación')
    date_start = fields.Date('Fecha inicio')
    date_end = fields.Date('Fecha fin')
    is_current = fields.Boolean('Trabajo actual', default=False)
    highlights = fields.Text('Logros / Descripción')

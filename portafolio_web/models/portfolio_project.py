# -*- coding: utf-8 -*-
from odoo import models, fields


class PortfolioProject(models.Model):
    _name = 'portfolio.project'
    _description = 'Proyecto del portafolio'
    _order = 'sequence, id'

    sequence = fields.Integer('Orden', default=10)
    developer_id = fields.Many2one(
        'portfolio.developer',
        string='Desarrollador',
        required=True,
        ondelete='cascade',
    )
    name = fields.Char('Nombre del proyecto', required=True)
    summary = fields.Char('Resumen')
    highlights = fields.Text('Detalles / Highlights')
    github_url = fields.Char('GitHub URL')

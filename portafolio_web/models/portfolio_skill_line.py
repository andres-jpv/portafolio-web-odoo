# -*- coding: utf-8 -*-
from odoo import models, fields


class PortfolioSkillLine(models.Model):
    _name = 'portfolio.skill.line'
    _description = 'Línea de habilidad técnica'
    _order = 'sequence, id'

    sequence = fields.Integer('Orden', default=10)
    name = fields.Char('Habilidad', required=True)
    checked = fields.Boolean('Dominada', default=True)

    # Relaciones: puede pertenecer a hard skills o ecosystem del developer
    developer_hard_id = fields.Many2one(
        'portfolio.developer',
        string='Desarrollador (Hard Skill)',
        ondelete='cascade',
    )
    developer_ecosystem_id = fields.Many2one(
        'portfolio.developer',
        string='Desarrollador (Ecosistema)',
        ondelete='cascade',
    )

# -*- coding: utf-8 -*-
from odoo import models, fields


class PortfolioSkillTag(models.Model):
    _name = 'portfolio.skill.tag'
    _description = 'Etiqueta de habilidad (chip de tecnología)'
    _order = 'name'

    name = fields.Char('Tecnología', required=True)
    color = fields.Integer('Color', default=0)
    developer_ids = fields.Many2many(
        'portfolio.developer',
        'portfolio_developer_skill_tag_rel',
        'tag_id', 'developer_id',
        string='Desarrolladores',
    )

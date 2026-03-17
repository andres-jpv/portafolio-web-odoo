# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PortfolioDeveloper(models.Model):
    _name = 'portfolio.developer'
    _description = 'Desarrollador - Portafolio Profesional'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    # Información básica
    name = fields.Char('Nombre completo', required=True, tracking=True)
    job_title = fields.Char('Título profesional', tracking=True)
    email = fields.Char('Correo electrónico')
    phone = fields.Char('Teléfono')
    location = fields.Char('Ubicación')
    photo = fields.Binary('Foto', attachment=True)
    photo_filename = fields.Char('Nombre del archivo de foto')

    # Disponibilidad
    is_available = fields.Boolean(
        'Disponible para proyectos',
        default=True,
        tracking=True,
    )

    # Stats del encabezado
    project_count = fields.Integer('Proyectos realizados', compute='_compute_project_count', store=True)
    odoo_version = fields.Char('Versión Odoo', default='v19')
    ia_ready_pct = fields.Integer('IA Ready %', default=100)

    # Perfil
    profile_bio = fields.Html('Perfil profesional')

    # Redes sociales
    linkedin = fields.Char('LinkedIn (usuario)')
    github = fields.Char('GitHub (usuario)')

    # Tecnologías (chips de color)
    skill_tag_ids = fields.Many2many(
        'portfolio.skill.tag',
        'portfolio_developer_skill_tag_rel',
        'developer_id', 'tag_id',
        string='Tecnologías',
    )

    # Hard Skills (tabla con checkbox)
    hard_skill_ids = fields.One2many(
        'portfolio.skill.line',
        'developer_hard_id',
        string='Hard Skills',
    )

    # Ecosystem Skills (tabla con checkbox)
    ecosystem_skill_ids = fields.One2many(
        'portfolio.skill.line',
        'developer_ecosystem_id',
        string='Ecosistema',
    )

    # Módulos / Proyectos
    project_ids = fields.One2many(
        'portfolio.project',
        'developer_id',
        string='Proyectos',
    )

    # Experiencia
    experience_ids = fields.One2many(
        'portfolio.experience',
        'developer_id',
        string='Experiencia',
    )

    # Cursos
    course_ids = fields.One2many(
        'portfolio.course',
        'developer_id',
        string='Cursos',
    )

    # Educación
    education_ids = fields.One2many(
        'portfolio.education',
        'developer_id',
        string='Educación',
    )

    # Campo categoría para el list view
    category = fields.Selection([
        ('junior', 'Developer / Junior'),
        ('mid', 'Developer / Mid'),
        ('senior', 'Developer / Senior'),
        ('lead', 'Tech Lead'),
    ], string='Categoría', default='junior')

    @api.depends('project_ids')
    def _compute_project_count(self):
        for rec in self:
            rec.project_count = len(rec.project_ids)

    def action_open_projects(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Proyectos',
            'res_model': 'portfolio.project',
            'view_mode': 'list,form',
            'domain': [('developer_id', '=', self.id)],
            'context': {'default_developer_id': self.id},
        }

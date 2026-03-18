# -*- coding: utf-8 -*-
from odoo import models, fields, api

OPTS = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')]
CORRECT = {'q1': 'a', 'q2': 'a', 'q3': 'c', 'q4': 'a', 'q5': 'b'}


class PortfolioQuizResult(models.Model):
    _name = 'portfolio.quiz.result'
    _description = 'Resultado Test Técnico Odoo'
    _order = 'create_date desc'

    name = fields.Char('Nombre', required=True)
    email = fields.Char('Email')
    company = fields.Char('Empresa')
    q1 = fields.Selection(OPTS, 'P1')
    q2 = fields.Selection(OPTS, 'P2')
    q3 = fields.Selection(OPTS, 'P3')
    q4 = fields.Selection(OPTS, 'P4')
    q5 = fields.Selection(OPTS, 'P5')
    score = fields.Integer('Puntaje', compute='_compute_score', store=True)
    date = fields.Datetime('Fecha', default=fields.Datetime.now)

    @api.depends('q1', 'q2', 'q3', 'q4', 'q5')
    def _compute_score(self):
        for rec in self:
            rec.score = sum(1 for k, v in CORRECT.items() if getattr(rec, k) == v)

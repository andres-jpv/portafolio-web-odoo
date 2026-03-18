# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PortfolioWebController(http.Controller):

    @http.route('/portafolio', auth='public', website=True, sitemap=True)
    def portafolio(self, **kwargs):
        developer = request.env['portfolio.developer'].sudo().search([], limit=1)
        return request.render('portafolio_web.portafolio_page', {
            'developer': developer,
        })

    @http.route('/portafolioweb', auth='public', website=True, sitemap=True)
    def portafolio_backend(self, **kwargs):
        developer = request.env['portfolio.developer'].sudo().search([], limit=1)
        messages = developer.message_ids.sorted('date', reverse=True)[:5] if developer else []
        return request.render('portafolio_web.portafolio_backend_page', {
            'developer': developer,
            'messages': messages,
        })

    _QUIZ_ANSWERS = {'q1': 'a', 'q2': 'a', 'q3': 'c', 'q4': 'a', 'q5': 'b'}

    @http.route('/portafolioweb/test', auth='public', website=True, methods=['GET'])
    def quiz(self, **kw):
        return request.render('portafolio_web.quiz_page', {})

    @http.route('/portafolioweb/test', auth='public', website=True, methods=['POST'], csrf=False)
    def quiz_submit(self, nombre='', email='', company='', q1=None, q2=None, q3=None, q4=None, q5=None, **kw):
        answers = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5}
        score = sum(1 for k, v in self._QUIZ_ANSWERS.items() if answers.get(k) == v)
        request.env['portfolio.quiz.result'].sudo().create({
            'name': nombre or 'Anónimo',
            'email': email,
            'company': company,
            'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5,
        })
        return request.render('portafolio_web.quiz_result_page', {
            'score': score,
            'total': 5,
            'nombre': nombre or 'Visitante',
        })

    @http.route('/portafolioweb/nota', type='json', auth='public', website=True, methods=['POST'], csrf=False)
    def portafolio_nota(self, developer_id, nombre='', nota='', **kwargs):
        developer = request.env['portfolio.developer'].sudo().browse(developer_id)
        if not developer.exists():
            return {'success': False, 'error': 'Desarrollador no encontrado'}
        body = '<p><strong>%s:</strong><br/>%s</p>' % (nombre or 'Visitante', nota)
        developer.sudo().message_post(
            body=body,
            message_type='comment',
            subtype_xmlid='mail.mt_note',
            author_id=request.env.ref('base.partner_root').id,
        )
        return {'success': True}

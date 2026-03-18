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
        return request.render('portafolio_web.portafolio_backend_page', {
            'developer': developer,
        })

    @http.route('/portafolioweb/cv', auth='public', website=True, sitemap=False)
    def cv_pdf(self, **kwargs):
        developer = request.env['portfolio.developer'].sudo().search([], limit=1)
        if not developer:
            return request.not_found()
        pdf_content, _ = request.env['ir.actions.report'].sudo()._render_qweb_pdf(
            'portafolio_web.report_cv_document',
            [developer.id],
        )
        headers = [
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', 'attachment; filename="CV_Jordan_Pincay.pdf"'),
            ('Content-Length', len(pdf_content)),
        ]
        return request.make_response(pdf_content, headers=headers)

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


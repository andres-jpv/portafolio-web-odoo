# -*- coding: utf-8 -*-
import json
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

    @http.route('/portafolioweb/contactar', auth='public', website=True, methods=['POST'], csrf=True)
    def contactar(self, nombre='', email='', empresa='', cargo='', mensaje='', **kw):
        def json_resp(data):
            return request.make_response(
                json.dumps(data),
                headers=[('Content-Type', 'application/json')],
            )

        if not nombre.strip() or not email.strip() or not mensaje.strip():
            return json_resp({'ok': False, 'error': 'Completa los campos obligatorios.'})

        developer = request.env['portfolio.developer'].sudo().search([], limit=1)
        dest_email = developer.email if developer and developer.email else 'j.pincayvinces@gmail.com'

        lineas = []
        if empresa: lineas.append(f'<b>Empresa:</b> {empresa}')
        if cargo:   lineas.append(f'<b>Cargo:</b> {cargo}')
        cuerpo = f"""
        <div style="font-family:Arial,sans-serif;font-size:14px;color:#212529;">
            <h2 style="color:#714b67;">Nuevo mensaje desde tu portafolio</h2>
            <p><b>Nombre:</b> {nombre}</p>
            <p><b>Correo:</b> <a href="mailto:{email}">{email}</a></p>
            {''.join(f'<p>{l}</p>' for l in lineas)}
            <hr style="margin:16px 0;border:none;border-top:1px solid #dee2e6;"/>
            <p><b>Mensaje:</b></p>
            <blockquote style="border-left:4px solid #714b67;margin:0;padding:8px 16px;color:#495057;">
                {mensaje.replace(chr(10), '<br/>')}
            </blockquote>
        </div>
        """

        try:
            request.env['mail.mail'].sudo().create({
                'subject': f'[Portafolio] Contacto de {nombre}',
                'email_from': dest_email,
                'email_to': dest_email,
                'reply_to': email,
                'body_html': cuerpo,
            }).send()
            return json_resp({'ok': True})
        except Exception as e:
            return json_resp({'ok': False, 'error': str(e)})

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


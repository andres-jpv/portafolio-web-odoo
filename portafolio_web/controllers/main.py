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

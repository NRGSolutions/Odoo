# -*- coding: utf-8 -*-
from openerp import http

# class SejinTodoApp(http.Controller):
#     @http.route('/sejin_todo_app/sejin_todo_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sejin_todo_app/sejin_todo_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sejin_todo_app.listing', {
#             'root': '/sejin_todo_app/sejin_todo_app',
#             'objects': http.request.env['sejin_todo_app.sejin_todo_app'].search([]),
#         })

#     @http.route('/sejin_todo_app/sejin_todo_app/objects/<model("sejin_todo_app.sejin_todo_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sejin_todo_app.object', {
#             'object': obj
#         })
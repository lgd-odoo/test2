from odoo import fields, models

class Estate(models.model):
   _name = "estate"
   _description = "Estate"

   name = fields.char()

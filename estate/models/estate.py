from odoo import fields, models

class Estate(models.Model):
   _name = "estate"
   _description = "Estate"

   name = fields.char()

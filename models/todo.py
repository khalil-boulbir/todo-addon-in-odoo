from odoo import api,fields,models

class Todo(models.Model):
    _name = 'todo.task'
    _inherit=['mail.thread','mail.activity.mixin']
    #_inherit='res.partner'
    task_name=fields.Char(string='Task Name',required=True)
    due_date=fields.Date(string='Due Date',tracking=True)
    task_description=fields.Text(string='Task Description')
    status=fields.Selection([
        
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        
        
        ],default='New',string="Status")

    def start_task(self):
        for rec in self:
            rec.status='New'
    def release_task(self):
        for rec in self:
            rec.status='In Progress'
    def complet_task(self):
        for rec in self:
            rec.status='Completed'
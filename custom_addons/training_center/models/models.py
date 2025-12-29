# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# 1. MODEL MÔN HỌC
class TrainingSubject(models.Model):
    _name = 'training.subject'
    _description = 'Môn học'

    name = fields.Char(string="Tên môn", required=True)
    code = fields.Char(string="Mã môn")
    description = fields.Text(string="Mô tả đề cương")

# 2. MODEL GIẢNG VIÊN
class TrainingTeacher(models.Model):
    _name = 'training.teacher'
    _description = 'Giảng viên'

    name = fields.Char(string="Tên giảng viên", required=True)
    phone = fields.Char(string="Số điện thoại")
    skills = fields.Text(string="Kỹ năng")

# 3. MODEL SINH VIÊN
class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Sinh viên'

    name = fields.Char(string="Tên sinh viên", required=True)
    email = fields.Char(string="Email")
    student_id = fields.Char(string="Mã sinh viên")

# 4. MODEL LỚP HỌC
class TrainingClass(models.Model):
    _name = 'training.class'
    _description = 'Lớp học'

    name = fields.Char(string="Tên lớp")
    start_date = fields.Date(string="Ngày bắt đầu")
    end_date = fields.Date(string="Ngày kết thúc")
    duration = fields.Integer(string="Thời lượng học (buổi)")
    description = fields.Char(string="Mô tả lớp học")

    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('open', 'Đang mở'),
        ('closed', 'Đã đóng')
    ], string="Trạng thái", default='draft')
    
    price_per_student = fields.Integer(string="Học phí/người", default=1000000)
    total_revenue = fields.Integer(string="Tổng doanh thu 1 lớp", compute='_compute_total_revenue', store=True)

    # Relationships
    subject_id = fields.Many2one('training.subject', string="Môn học", required=True)
    teacher_id = fields.Many2one('training.teacher', string="Giảng viên")
    student_ids = fields.Many2many('training.student', string="Danh sách sinh viên")
    session_ids = fields.One2many('training.session', 'class_id', string="Lịch học chi tiết")

    _sql_constraints = [
        ('duration_contraints', 'check(duration > 3)', 'Thời lượng học phải lớn hơn 3 buổi, không thì Dốt!!!')
    ]

    # Tính toán tổng doanh thu dựa trên số sinh viên và học phí/người
    @api.depends('student_ids', 'price_per_student')
    def _compute_total_revenue(self):
        for record in self:
            record.total_revenue = len(record.student_ids) * record.price_per_student    

    # Tự động điền mô tả lớp học khi thay đổi tên lớp hoặc ngày bắt đầu
    @api.onchange('name', 'start_date')
    def _onchange_description(self):
        for record in self:
            if record.name and record.start_date:
                record.description = f"Học Lớp {record.name} bắt đầu từ ngày {record.start_date} thì ngon luôn!!"

    # Cảnh báo nếu học phí/người < 1 củ
    @api.onchange('price_per_student')
    def _onchange_price_per_student(self):
        if self.price_per_student < 1000000:
            return {
                'warning': {
                    'title': "Cảnh báo về học phí!",
                    'message': "Học phí/người phải lớn hơn 1 củ - không thì như muối bỏ biển!"
                }
            }
    # Ràng buộc tên lớp không được để trống và phải dài từ 8 đến 20 ký tự
    @api.constrains('name')
    def _check_name_not_empty(self):
        for record in self:
            if not record.name:
                raise ValidationError("Tên không được để trống, không thì như muối bỏ biển!")
            if len(record.name) < 8 or len(record.name) > 20:
                raise ValidationError("Tên phải dài từ 8 ký tự đến 20 ký tự, không thì Dốt!!!")

    def action_open_class(self):
        for record in self:
            record.state = 'open'

    def action_close_class(self):
        for record in self:
            record.state = 'closed'

    def action_set_draft(self):
        for record in self:
            record.state = 'draft'

# 5. MODEL BUỔI HỌC (SESSION)
class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Buổi học'

    name = fields.Char(string="Nội dung buổi học", required=True)
    date = fields.Date(string="Ngày học", default=fields.Date.today)
    duration = fields.Integer(string="Thời lượng (phút)")
    
    # Many2one ngược về Lớp học
    class_id = fields.Many2one('training.class', string="Lớp học")
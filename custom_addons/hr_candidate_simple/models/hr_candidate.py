from odoo import models, fields

class HrCandidate(models.Model):
    _name = 'hr.candidate'
    _description = 'Candidate Profile'

    name = fields.Char(string="Họ tên", required=True)

    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'),
    ], string="Giới tính")

    birthday = fields.Date(string="Ngày sinh")

    expected_salary = fields.Float(string="Mức lương mong muốn")

    # Chỉ Manager mới nhìn thấy
    manager_note = fields.Text(
        string="Đánh giá nội bộ",
        groups="hr_candidate_simple.group_hr_manager"
    )

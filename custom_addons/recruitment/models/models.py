# -*- coding: utf-8 -*-

from odoo import models, fields


class HrCandidate(models.Model):
    _name = 'hr.candidate'
    _description = 'Danh sách ứng viên tuyển dụng'

    name = fields.Char(string='Tên ứng viên', required=True)
    gender = fields.Selection(
        string='Giới tính',
        selection=[
            ('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')
        ],
        help="Giới tính của ứng viên"
    )
    birthday = fields.Date(string='Ngày sinh')
    cv_content = fields.Text(string='Nội dung CV')
    expected_salary = fields.Integer(string='Mức lương mong muốn')
    is_hired = fields.Boolean(string='Đã tuyển?', default=False)
    manager_note = fields.Text(string='Ghi chú tuyển dụng')
    job_id = fields.Many2one(
        comodel_name='hr.job.position',
        string='Vị trí ứng tuyển'
    )
    offer_ids = fields.One2many(
        comodel_name='hr.candidate.offer',
        inverse_name='candidate_id',
        string='Lịch sử Offer'
    )
    tag_ids = fields.Many2many(
        comodel_name='hr.candidate.tag', 
        string='Kỹ năng (Tags)'
    )


class HrJobPosition(models.Model):
    _name = 'hr.job.position'
    _description = 'Vị trí công việc'

    name = fields.Char(string='Tên vị trí', required=True)
    description = fields.Text(string='Mô tả công việc')


class HrCandidateOffer(models.Model):
    _name = 'hr.candidate.offer'
    _description = 'Lịch sử mời làm việc'

    price = fields.Integer(string='Mức lương đề nghị')
    status = fields.Selection([
        ('accepted', 'Đồng ý'),
        ('refused', 'Từ chối')
    ], string='Trạng thái')

    candidate_id = fields.Many2one(
        comodel_name='hr.candidate', 
        string='Ứng viên', 
        required=True
    )


class HrCandidateTag(models.Model):
    _name = 'hr.candidate.tag'
    _description = 'Kỹ năng ứng viên'

    name = fields.Char(string='Tên kỹ năng', required=True)
    color = fields.Integer(string='Màu sắc')
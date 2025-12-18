from odoo import models, fields

class ITTicket(models.Model):
    _name = 'it.ticket'
    _description = 'IT Support Ticket'

    name = fields.Char(
        string="Tiêu đề sự cố",
        required=True,
        help="Tiêu đề ngắn gọn mô tả sự cố"
    )

    user_name = fields.Char(
        string="Người báo cáo",
        required=True,
        help="Tên người tạo phiếu"
    )

    email = fields.Char(
        string="Email liên hệ",
        help="Email để liên hệ khi xử lý sự cố"
    )

    description = fields.Text(
        string="Mô tả chi tiết",
        help="Mô tả chi tiết lỗi hoặc sự cố gặp phải"
    )

    priority = fields.Selection(
        [
            ('low', 'Thấp'),
            ('medium', 'Trung bình'),
            ('high', 'Cao'),
            ('critical', 'Khẩn cấp')
        ],
        string="Mức độ ưu tiên",
        default='medium',
        help="Mức độ nghiêm trọng của sự cố"
    )

    category = fields.Selection(
        [
            ('hardware', 'Phần cứng'),
            ('software', 'Phần mềm'),
            ('network', 'Mạng')
        ],
        string="Danh mục",
        help="Loại sự cố"
    )

    date_created = fields.Date(
        string="Ngày báo cáo",
        default=fields.Date.today,
        help="Ngày tạo phiếu"
    )

    deadline = fields.Date(
        string="Hạn xử lý",
        help="Hạn cuối cần xử lý xong"
    )

    is_solved = fields.Boolean(
        string="Đã xử lý?",
        default=False,
        help="Đánh dấu phiếu đã được xử lý xong hay chưa"
    )

    # 🔒 Bảo mật trường
    tech_note = fields.Text(
        string="Ghi chú kỹ thuật",
        help="Cách sửa, nguyên nhân lỗi (dành cho IT)",
        groups="it_ticket_simple.group_it_technician,it_ticket_simple.group_it_manager"
    )

    repair_cost = fields.Integer(
        string="Chi phí sửa chữa",
        help="Chi phí sửa chữa (chỉ Manager xem)",
        groups="it_ticket_simple.group_it_manager"
    )

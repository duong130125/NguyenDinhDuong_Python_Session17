{
    'name': 'Hotel Manager',
    'version': '1.0',
    'summary': 'Quản lý khách sạn và booking',
    'description': """
        Module quản lý khách sạn với các chức năng:
        - Quản lý phòng và loại phòng
        - Quản lý khách hàng
        - Quản lý đặt phòng (booking)
        - Quản lý dịch vụ kèm theo
        - Tính toán tự động tổng tiền
    """,
    'category': 'Services/Hotel',
    'author': 'Dương',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        'security/hotel_record_rules.xml',
        'data/sequence_data.xml',
        'views/hotel_room_type_views.xml',
        'views/hotel_service_views.xml',
        'views/hotel_customer_views.xml',
        'views/hotel_room_views.xml',
        'views/hotel_booking_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': "LGPL-3"
}
# ORM Mapping – Model inventory.product

## Python ↔ PostgreSQL

| Python            | PostgreSQL        |
| ----------------- | ----------------- |
| inventory.product | inventory_product |
| fields.Char       | character varying |
| fields.Float      | double precision  |
| fields.Integer    | integer           |

## Ghi chú

- Bảng do ORM sinh ra có tên: **inventory_product**
- Odoo sẽ tự thêm các cột hệ thống: id, create_uid, write_uid, create_date, write_date.

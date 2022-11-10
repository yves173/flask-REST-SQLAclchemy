from marshmallow import fields,Schema

class PlainItemSchema(Schema):

    item_id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    price=fields.Float(required=True)

class PlainStoreSchema(Schema):
    store_id=fields.Int(dump_only=True)
    name=fields.Str(required=True)

class ItemSchema(PlainItemSchema):
    store_id=fields.Int(required=True)
    store=fields.Nested(PlainStoreSchema(),dump_only=True)

class ItemUpdateSchema(Schema):
    name=fields.Str()
    price=fields.Float()

class StoreSchema(PlainStoreSchema):
    Items=fields.List(fields.Nested(PlainItemSchema()),dump_only=True)
# from lib.Cassandra.lib.test_flow import SchemaContext
from lib.test_flow import *
import time
rich_console = RichConsole()
no_console = NoConsole()
test_instance = Container(name = 'root', output = no_console)

happy_path = test_instance.create_container('scenario: o caminho feliz')

generic_object_validator = BaseValidatorManager()
# serializer = YamlSerializer(folder = 'mock')

schema_object_validator = YamlSerializer(folder = 'dist', name = 'data.yaml')
default_schema_manager = DefaultSchemaManager(validator = generic_object_validator, serializer = schema_object_validator)



ctx = TestContext(no_console)
hook_status_in_context(ctx)


from datetime import datetime

def is_valid_date(date_string, date_format="%Y-%m-%d"):
    """
    Verifica se uma string é uma data válida.

    :param date_string: A string a ser validada.
    :param date_format: O formato da data (padrão: "%Y-%m-%d").
    :return: True se a string for uma data válida, False caso contrário.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

class DateBaseFormat(SerialType):

    def acceptable_field_type(self):
        return str,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, str) and is_valid_date(ctx.field):
            ctx.approve()
        else:
            ctx.reject("tipo inválido")
            
    def schema_format(self):
        return {'type' : "date"}

class ArrayValidator(SerialType):

    def acceptable_field_type(self):
        return list,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, list):
            ctx.approve()
        else:
            ctx.reject()

    def schema_format(self):
        return {'type' : 'list'}


class StringValidator(SerialType):

    def acceptable_field_type(self):
        return str,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, str):
            ctx.approve()
        else:
            ctx.reject()

    def schema_format(self):
        return {'type' : 'text'}


class NumberValidator(SerialType):

    def acceptable_field_type(self):
        return float,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, float):
            ctx.approve()
        else:
            ctx.reject()

    def schema_format(self):
        return {'type' : 'number'}


class GenericObjectValidator(SerialType):

    def acceptable_field_type(self):
        return dict,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, dict):
            ctx.approve()
        else:
            ctx.reject()

    def schema_format(self):
        return {'type' : 'object'}



class IntegerValidator(SerialType):

    def acceptable_field_type(self):
        return int,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, int):
            ctx.approve()
        else:
            ctx.reject()

    def schema_format(self):
        return {'type' : 'integer'}

class BooleanValidator(SerialType):

    def acceptable_field_type(self):
        return bool,

    def validate(self, ctx: SchemaContext):
        if isinstance(ctx.field, bool):
            ctx.approve()
        else:
            ctx.reject()

    def schema_format(self):
        return {'type' : 'boolean'}




default_schema_manager.create_mapping_type(IntegerValidator)
default_schema_manager.create_mapping_type(GenericObjectValidator)
default_schema_manager.create_mapping_type(NumberValidator)
default_schema_manager.create_mapping_type(StringValidator)
default_schema_manager.create_mapping_type(ArrayValidator)
default_schema_manager.create_mapping_type(DateBaseFormat)


snapshot = SnapshotManager(name = "happy path", schema_manager = default_schema_manager, max_store = 10)

ctx.set('snapshot', snapshot)

def load_snapshot(ctx: TestContext):
    snapshot = ctx.get('snapshot')
    ctx.approve()



# def take_photos(ctx: TestContext):
#     snapshot = ctx.get('snapshot')
#     snapshot.take_snapshot(description = "photo",data = {
#         'data': 'henrique',
#         'age': 27,
#         'other': '2025-05-05'
#     })

#     snapshot.take_snapshot(description = "photo",data = {
#         'data': 'henrique',
#         'age': 27,
#         'other': '2025-05-05'
#     })

#     snapshot.take_snapshot(description = "photo",data = {
#         'data': 'henrique',
#         'age': 27,
#         'other': {
#             "aa" : 'mauler',
#             "bb" : '2025-05-05'
#         },
#         'aother': [
#             "henrique",
#             '2025-05-05'
#         ]
#     })
#     ctx.approve()



def assertions(ctx: TestContext):
    snapshot = ctx.get('snapshot')

    rr = snapshot.assert_value({
        'data': 'henrique'
    }, mode = 'total', by = '')

    rr = snapshot.assert_value({
        'data': 'henrique'
    }, mode = 'partial', by = 'input')

    rr = snapshot.assert_value({
        'data': 'henrique'
    }, mode = 'partial', by = 'snapshot')


    ctx.approve()


test_instance.before_each(load_snapshot, isolated = False)
# test_instance.add_step("tirar fotos", take_photos, isolated = False)
test_instance.add_step("assertions", assertions, isolated = False) # assertions
# test_instance.after_each(save_snapshot, isolated = False)


test_instance.execute(context=ctx, event_loop=asyncio.new_event_loop(), thread_pool_executor=ThreadPoolExecutor(max_workers=10, thread_name_prefix="pipe"))
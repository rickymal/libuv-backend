# from lib.Cassandra.lib.test_flow import SchemaContext

import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
from lib.Iexecutable import Container
from lib.context import TestContext
from lib.output import NoConsole, RichConsole
from lib.schema_manager import DefaultSchemaManager
from lib.serial_type import ArrayValidator, DateBaseFormat, GenericObjectValidator, IntegerValidator, NumberValidator, StringValidator
from lib.serializer import YamlSerializer
from lib.snapshot_manager import SnapshotManager
from lib.utils import hook_status_in_context


rich_console = RichConsole()
no_console = NoConsole()
test_instance = Container(name = 'root', output = no_console)

happy_path = test_instance.create_container('scenario: o caminho feliz')

schema_object_validator = YamlSerializer(folder = 'dist', name = 'data.yaml')
default_schema_manager = DefaultSchemaManager(serializer = schema_object_validator)



ctx = TestContext(no_console)
hook_status_in_context(ctx)



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


test_instance.before(load_snapshot, isolated = False)
# test_instance.add_step("tirar fotos", take_photos, isolated = False)
test_instance.add_step("assertions", assertions, isolated = False) # assertions
# test_instance.after(save_snapshot, isolated = False)


test_instance.execute(context=ctx, event_loop=asyncio.new_event_loop(), thread_pool_executor=ThreadPoolExecutor(max_workers=10, thread_name_prefix="pipe"))
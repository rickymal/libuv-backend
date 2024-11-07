from lib.test_flow import *
import time
rich_console = RichConsole()
no_console = NoConsole()
test_instance = Container(name = 'root', output = no_console)

happy_path = test_instance.create_container('scenario: o caminho feliz')

generic_object_validator = BaseValidatorManager()
# serializer = YamlSerializer(folder = 'mock')

schema_object_validator = YamlSerializer(folder = 'mock')
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


def check_date(ctx: SchemaContext):
    if isinstance(ctx.field, str) and is_valid_date(ctx.field):
        ctx.approve()
    else:
        ctx.reject("tipo inválido")

default_schema_manager.create_contract('date', check_date, include_nested = True) # método responsável por ler o schema e caso identifique um objeto ele irá avaliar se esse objeto pode ser tratado de outra forma


snapshot = SnapshotManager(name = "happy path", schema_manager = default_schema_manager, max_store = 10)

ctx.set('snapshot', snapshot)

def load_snapshot(ctx: TestContext):
    snapshot = ctx.get('snapshot')
    # snapshot.load()
    ctx.approve()



def take_photos(ctx: TestContext):
    snapshot = ctx.get('snapshot')
    snapshot.take_snapshot(description = "photo",data = {
        'data': 'henrique',
        'age': 27,
        'other': '2025-05-05'
    })
    ctx.approve()


def save_snapshot(ctx: TestContext):
    snapshot = ctx.get('snapshot')
    snapshot.save_album()
    ctx.approve()


test_instance.before_each(load_snapshot, isolated = False)
test_instance.add_step("tirar fotos", take_photos, isolated = False)
test_instance.after_each(save_snapshot, isolated = False)


test_instance.execute(context=ctx, event_loop=asyncio.new_event_loop(), thread_pool_executor=ThreadPoolExecutor(max_workers=10, thread_name_prefix="pipe"))
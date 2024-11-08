
# Importações necessárias
import datetime
from abc import ABC, abstractmethod
from collections import defaultdict
import json
import logging
import hashlib
import pickle
import random
from typing import Iterator
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio
import os
# SnapshotManager(name = "happy path", max_store = lambda snapshot: snapshot * 10, schema_builder = default_schema_builder, validators = generic_object_validator, serializer = serializer)



# snapshot = SnapshotManager(name = "happy path", schema_manager = default_schema_managFCadeer)

class SnapshotManager:
    def __init__(self, name, schema_manager, max_store: int):
        self.name = name
        self.schema_manager = schema_manager
        self.max_store = max_store
        self.snapshots = []
        self.file = None

        from functools import partial, partialmethod
        

    @classmethod
    def create(cls):
        cls.__new__(cls)
        return cls

    def create_sub_snapshot(self, snaphot: str):
        new_snapshot = SnapshotManager.create()
        new_snapshot.name = snaphot
        new_snapshot.backward = self
        new_snapshot.forward = None
        new_snapshot.max_store = self.max_store
        new_snapshot.schema_builder = self.schema_builder
        new_snapshot.validator = self.validator
        new_snapshot.serializer = self.serializer
        new_snapshot.backward = self
        pass


    def calculate_hash(self, obj):
        """Calcula o hash do objeto para garantir a integridade."""
        return hashlib.sha256(pickle.dumps(obj)).hexdigest()
    
    def take_snapshot(self, data: any, description: str, **metadata):
        if self.max_store >= len(self.snapshots):
            self.snapshots.append((data, description, metadata))
            return 
        
        raise Exception("exceto de fotos tirada")

    def save_album(self):
        # Verificar se a pasta exist 

        snapshots_final = []
        
        schema = self.schema_manager.generate(self.snapshots)
        self.schema_manager.save(schema)


    def assert_value(self, data, mode: str, by: str):
        # Tenta carregar o reality_data (se não existir, salva data como referência)
        if not self.schema_manager.serializer.has_file():
            try:
                reality_data = self.schema_manager.serializer.load()
            except FileNotFoundError:
                self.schema_manager.take_snapshot(data=data, description='')
                self.schema_manager.save_album()
                reality_data = {'data': data}

        # Define o dado de referência para comparação
        reference = reality_data['data']

        # Verificação completa (modo 'total')
        if mode == 'total':
            if type(data) != type(reference):
                raise AssertionError(f"Tipo incorreto: esperado '{type(reference).__name__}', mas encontrado '{type(data).__name__}'")

            if isinstance(data, dict):
                # Verificação exata para dicionários
                if data != reference:
                    raise AssertionError("Estrutura e valores não correspondem no modo 'total'.")
            
            elif isinstance(data, list):
                # Verificação exata para listas
                if len(data) != len(reference) or any(item != ref for item, ref in zip(data, reference)):
                    raise AssertionError("Listas não correspondem no modo 'total'.")
            
            else:
                # Verificação para dados primitivos
                if data != reference:
                    raise AssertionError(f"Valor incorreto: esperado '{reference}', mas encontrado '{data}'")

        # Verificação parcial (modo 'partial')
        elif mode == 'partial':
            if by == 'input':
                # Verifica se cada item de `data` está presente e correto em `reference`
                if isinstance(data, dict):
                    for key, value in data.items():
                        if key in reference and reference[key] != value:
                            raise AssertionError(f"Valor incorreto para '{key}': esperado '{reference[key]}', mas encontrado '{value}'")
                elif isinstance(data, list):
                    # Compara cada item da lista `data` com os itens de `reference` (assumindo uma verificação parcial de correspondência)
                    for item in data:
                        if item not in reference:
                            raise AssertionError(f"Item '{item}' não encontrado na referência.")
                else:
                    # Para dados primitivos, verifica igualdade direta com `reference`
                    if data != reference:
                        raise AssertionError(f"Valor incorreto: esperado '{reference}', mas encontrado '{data}'")

            elif by == 'snapshot':
                # Verifica se cada item de `reference` está presente e correto em `data`
                if isinstance(reference, dict):
                    for key, value in reference.items():
                        if key in data and data[key] != value:
                            raise AssertionError(f"Valor incorreto para '{key}': esperado '{value}', mas encontrado '{data.get(key)}'")
                elif isinstance(reference, list):
                    # Verifica se todos os itens de `reference` estão em `data`
                    for item in reference:
                        if item not in data:
                            raise AssertionError(f"Item '{item}' da referência não encontrado no dado.")
                else:
                    # Para dados primitivos, verifica igualdade direta com `data`
                    if reference != data:
                        raise AssertionError(f"Valor incorreto: esperado '{reference}', mas encontrado '{data}'")
            else:
                raise Exception("Formato 'by' inválido")
        else:
            raise Exception("Formato 'mode' inválido")


    def assert_type(self, data: dict):
        raise NotImplementedError()




class BaseValidatorManager:
    pass


import os
import yaml

class YamlSerializer:
    # serializer = YamlSerializer(folder = 'mock')
    def __init__(self, folder: str, name: str):
        self.folder = folder
        self.name = name
        self.data = None

    def save(self, data: dict, extra_path=[]):
        # Cria o caminho completo do diretório
        full_path = os.path.join(self.folder, *extra_path)
        if not os.path.isdir(full_path):
            os.makedirs(full_path)  # Cria todos os diretórios necessários
        
        # Define o caminho completo do arquivo (pode ser ajustado conforme necessário)
        file_path = os.path.join(full_path, self.name)
        with open(file_path, 'w') as f:
            self.data = data
            yaml.dump(data, f)

    def load(self, extra_path = []):
        full_path = os.path.join(self.folder, *extra_path)
        file_path = os.path.join(full_path, self.name)
        with open(file_path, 'r') as f:
            self.data = yaml.safe_load(f)
            return self.data

    def has_file(self):
        return self.data is not None

# Configuração do Logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Classe BaseOutput (para gerenciamento de saída)
class BaseOutput(ABC):
    @abstractmethod
    def start_test_instance(self, test_instance):
        pass

    @abstractmethod
    def end_test_instance(self, test_instance):
        pass

    @abstractmethod
    def start_container(self, container):
        pass

    @abstractmethod
    def end_container(self, container):
        pass

    @abstractmethod
    def start_pipeline(self, pipeline):
        pass

    @abstractmethod
    def end_pipeline(self, pipeline, status):
        pass

    @abstractmethod
    def start_step(self, step):
        pass

    @abstractmethod
    def end_step(self, step, status):
        pass

    @abstractmethod
    def log(self, message: str):
        pass




# Classe BaseOutput (para gerenciamento de saída)
class NoConsole(BaseOutput):
    
    def start_test_instance(self, test_instance):
        pass

    
    def end_test_instance(self, test_instance):
        pass

    
    def start_container(self, container):
        pass

    
    def end_container(self, container):
        pass

    
    def start_pipeline(self, pipeline):
        pass

    
    def end_pipeline(self, pipeline, status):
        pass

    
    def start_step(self, step):
        pass

    
    def end_step(self, step, status):
        pass

    
    def log(self, message: str):
        print(message)
        pass



from rich.console import Console
from rich.tree import Tree
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

# Classe RichConsole que herda de BaseOutput
class RichConsole(BaseOutput):
    def __init__(self):
        self.console = Console()
        self.test_tree = None
        self.current_nodes = []
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TimeElapsedColumn(),
            console=self.console,
            transient=True,
        )
        self.tasks = {}
        self.progress_started = False

    def start_test_instance(self, test_instance):
        self.test_tree = Tree(f"[bold cyan]{test_instance.name}[/bold cyan]")
        self.current_nodes.append(self.test_tree)
        if not self.progress_started:
            self.progress_started = True
            self.progress.__enter__()

    def end_test_instance(self, test_instance):
        if self.progress_started:
            self.progress.__exit__(None, None, None)
        self.console.print(self.test_tree)
        self.current_nodes.pop()

    def start_container(self, container):
        node = self.current_nodes[-1].add(f"[bold]{container.name}[/bold]")
        self.current_nodes.append(node)

    def end_container(self, container):
        self.current_nodes.pop()

    def start_pipeline(self, pipeline):
        node = self.current_nodes[-1].add(f"[yellow]{pipeline.name}[/yellow]")
        self.current_nodes.append(node)
        task_id = self.progress.add_task(f"Executando Pipeline: {pipeline.name}", total=None)
        self.tasks[pipeline] = task_id

    def end_pipeline(self, pipeline, status):
        task_id = self.tasks.pop(pipeline, None)
        if task_id is not None:
            self.progress.remove_task(task_id)
        status_text = "[green]SUCESSO[/green]" if status == "PASSED" else "[red]FALHA[/red]"
        self.current_nodes[-1].label = f"[yellow]{pipeline.name}[/yellow] - {status_text}"
        self.current_nodes.pop()

    def start_step(self, step):
        node = self.current_nodes[-1].add(f"{step.description}")
        self.current_nodes.append(node)
        task_id = self.progress.add_task(f"Executando Step: {step.description}", total=None)
        self.tasks[step] = task_id

    def end_step(self, step, status):
        task_id = self.tasks.pop(step, None)
        if task_id is not None:
            self.progress.remove_task(task_id)
        status_text = "[green]SUCESSO[/green]" if status == "PASSED" else "[red]FALHA[/red]"
        self.current_nodes[-1].label = f"{step.description} - {status_text}"
        self.current_nodes.pop()

    def log(self, message: str):
        # Loga a mensagem no console atual
        self.console.log(message)


# default_schema_builder.set_serializer(serializer = yamlSerializer)
class DefaultSchemaManager:
    def __init__(self, validator, serializer):
        self.transformers = []
        self.serializer = serializer
        self.validator = validator

    def create_contract(self, new_type: str, func_validator, include_nested: bool):
        self.transformers.append((new_type, func_validator, include_nested))

    def build_schema_sketch(self, obj, transformers):
        """Gera um esquema de tipos a partir do objeto fornecido."""
        if isinstance(obj, dict):
            schema_type = ['object']
            schema = {'type': schema_type, 'properties': {}, 'required': []}
            n_transformers = self.apply_transformer(transformers, schema_type, obj)


            for key, value in obj.items():
                schema['properties'][key] = self.build_schema_sketch(value, transformers=n_transformers)
                schema['required'].append(key)  # Por padrão, todos os campos são obrigatórios

            return schema
        elif isinstance(obj, list):
            if obj:
                # Assume que todos os itens da lista são do mesmo tipo
                schema_type = ['array']
                n_transformers = self.apply_transformer(transformers, schema_type, obj)
                schema = {'type': schema_type, 'items': self.build_schema_sketch(obj[0], n_transformers)}
            else:
                schema = {'type': schema_type, 'items': {}}
            return schema
        elif isinstance(obj, str):
            schema_type = ['string']
            self.apply_transformer(transformers, schema_type, obj)
            return {'type': schema_type}
        elif isinstance(obj, int):
            schema_type = ['integer']
            self.apply_transformer(transformers, schema_type, obj)
            return {'type': schema_type}
        elif isinstance(obj, float):
            schema_type = ['number']
            self.apply_transformer(transformers, schema_type, obj)
            return {'type': schema_type}
        elif isinstance(obj, bool):
            schema_type = ['boolean']
            self.apply_transformer(transformers, schema_type, obj)
            return {'type': schema_type}
        elif obj is None:
            return {'type': 'null'}
        else:
            raise TypeError(f'Unsupported type: {type(obj)}')

    def apply_transformer(self, transformers, schema_type, obj):
        nested_transformer = []
        for transformer in transformers:
            new_type, func_validator, include_nested = transformer
            schemaContext = SchemaContext(None, field = obj)
            state = {'status' : 'not initialized'}
            schemaContext = hook_status_in_context(schemaContext, state = state)
            func_validator(schemaContext)

            if schemaContext.get_status() == 'approved':
                schema_type.append(new_type)

            if include_nested:
                nested_transformer.append(transformer)

        return nested_transformer

    def calculate_hash(self, obj):
        """Calcula o hash do objeto para garantir a integridade."""
        return hashlib.sha256(pickle.dumps(obj)).hexdigest()
    

    def generate(self, content):
        current_time = time.time()
        schemas = []

        for obj_tuple in content:
            obj, description, metadata = obj_tuple
            
            schemas.append({
                **self.build_schema_sketch(obj, self.transformers),
                'description' : description,
                'data' : obj,
                'metadata' : metadata,
                'hash' : self.calculate_hash(obj),
                'created_at': datetime.datetime.fromtimestamp(current_time).isoformat(),
                'last_access': datetime.datetime.fromtimestamp(current_time).isoformat(),
            })

        return schemas


    def save(self, final_data: dict):
        self.serializer.save(final_data)

    def load(self):
        self.serializer.load()

    def assert_type(self, data: dict):
        # mesma ideia do assert_type com a diferença de que checa o tipo
        pass 


class PrototypeInstance:
    pass



# Classe Context
class TestContext(PrototypeInstance):
    def __init__(self, output):
        self.data = {}
        self.errors = []
        self.container = None
        self.alucinator = None
        self.output = output
        self.status = 'not initialized'
        self.forward_ctx = None
        self.backward_ctx = None
        self.on_approved = None
        self.on_rejected = None
        self.on_concluded = None
        self.on_status_checked = None

    def set(self, key, value):
        self.data[key] = value


    def get_status(self):
        return self.on_status_checked()

    def get(self, key, default=None):
        value = self.data.get(key, default)
        if value is None and self.backward_ctx is not None:
            value = self.backward_ctx.get(key, value)    
        return value

    def approve(self):
        self.on_approved()

    def reject(self, error_message: str):
        self.on_rejected()
        self.errors.append(error_message)

    def conclude(self):
        self.on_concluded()


    def chain_new_context(self, status = 'not initialized', ctx = None):
        new_ctx = TestContext(self.output) if ctx is None else ctx
        self.forward_ctx = new_ctx
        new_ctx.container = self.container
        new_ctx.status = status
        new_ctx.backward_ctx = self
        return new_ctx


    def get_status(self):
        return self.on_status_checked()

    

    def iter_ctx(self):
        ctx = self
        while ctx:
            yield ctx
            ctx = ctx.forward_ctx

    def iter_items(self):
        for ctx in self.iter_ctx():
            yield from ctx.data.items()



class IExecutable(ABC):

    @abstractmethod
    def execute(self, context = None, event_loop = None, thread_pool_executor = None,):
        pass


# Classe Step
class Step(IExecutable):
    def __init__(self, description: str, func, isolated: bool, **kwargs):
        self.description = description
        self.func = func
        self.kwargs = kwargs
        self.isolated = isolated


    def __repr__(self) -> str:
        return "step: {}".format(self.description)

    def execute(self, context: TestContext, event_loop: asyncio.BaseEventLoop = None,  thread_pool_executor: ThreadPoolExecutor = None) -> asyncio.Future:
        context.output.start_step(self)
        future_result = asyncio.Future()
        context.step_description = self.description
        if self.isolated:
            thread_pool_executor = thread_pool_executor.submit(self.func, context)
        else:
            if context is None:
                print("OI")
            rr = self.func(context,)
            future_result.set_result(rr)
        status = "PASSED" if context.status == 'approved' else "FAILED"
        context.output.end_step(self, status)
        # try:
        # except Exception as e:
        #     context.reject(f"Exceção no Step '{self.description}': {e}")
        #     context.output.end_step(self, "FAILED")
        #     raise e

        if future_result is None:
            pass
        return future_result



# Classe Container # event_loop_executor = asyncio.new_event_loop(), thread_pool_executor = ThreadPoolExecutor(max_workers=10, thread_name_prefix="pipe")
class Container(IExecutable):
    def __init__(self, name : str, output,):
        
        self.futures = []
        self.output = output
        self.actual_context = TestContext(output)

        self.name = name
        # self.subcontainers: list[IExecutable] = []
        self.pipelines = []
        self.hooks_before_each: list[Step] = []
        self.hooks_after_each: list[Step] = []
        self.fixtures = {}
        self.factories = {}
        self.steps: list[IExecutable] = []
        self.annotations = {}
        self.tags = []
        self.parent = None
        self.output = output
        self.actual_context = TestContext(self.output)



    def add_step(self, description: str, func, isolated: bool, **kwargs):
        step = Step(description, func, isolated, **kwargs)
        self.steps.append(step)

    def wait_ctx(self, ctx: TestContext, time_sleep: int = 1, timeout: int = 10, event_loop = None, thread_pool_executor = None,):
        future = event_loop.run_in_executor(thread_pool_executor, lambda: time.sleep(timeout))
        event_loop.run_until_complete(future)
        while ctx.status == 'pending' and not future.done():
            time.sleep(time_sleep)

    def wait_future(self, func_execution: asyncio.Future, time_sleep: int = 1, timeout: int = 10):
        future = self.event_loop.run_in_executor(self.thread_pool_executor, lambda: time.sleep(timeout))
        self.event_loop.run_until_complete(future)
        while not func_execution.done() and not future.done():
            time.sleep(time_sleep)

    def create_container(self, name: str):
        new_container = Container(name = name, output= self.output)
        self.steps.append(new_container)
        return new_container

    def before_each(self, func, isolated: bool):
        step = Step("before", func, isolated=isolated)
        self.hooks_before_each.append(step)

    def after_each(self, func, isolated: bool):
            step = Step("before", func, isolated=isolated)
            self.hooks_after_each.append(step)
            

    def execute(self, context = None, event_loop = None, thread_pool_executor = None,):
        self.output.start_test_instance(self)
        future = asyncio.Future()
        ctx_hk_before, ctx_hk_after, ctx_step, ctx_all = self.get_status_builder()
        
        self._run_sequence(context, event_loop, thread_pool_executor, ctx_hk_before, self.hooks_before_each, 'before')

        self._run_sequence(context, event_loop, thread_pool_executor, ctx_step, self.steps, 'middle')

        self._run_sequence(context, event_loop, thread_pool_executor, ctx_hk_after, self.hooks_after_each, 'end')

        future.set_result(ctx_all)

        context.approve()
        self.output.end_test_instance(self)

        return future

    def _run_sequence(self, context, event_loop, thread_pool_executor, ctx_hk_before, iterable, status_progress: str):
        ctx_hk_before['status'] = 'pending'
        futures_list: list[asyncio.Future] = []
        for hook in iterable:
            status = {'status': 'not initialized'}
            hook_status_in_context(context, status)
            # context.on_approved = lambda : status.update({'status': 'approved'})
            # context.on_rejected = lambda : status.update({'status': 'rejected'})
            # context.on_concluded = lambda : status.update({'status': 'concluded'})
            # context.on_status_checked = lambda : status['status']
            status.update({'status': 'pending'})
            ctx_hk_before['values'].append(status)
            future = hook.execute(context = context, event_loop = event_loop, thread_pool_executor=thread_pool_executor)
            futures_list.append(future)
            if not future.done():
                self.wait_ctx(context, time_sleep= 1, timeout= 10, event_loop = event_loop, thread_pool_executor = thread_pool_executor) # and self.wait_future(future)
            
            if context.get_status() != "approved":
                ctx_hk_before['status'] = 'error'
                raise Exception("Error")
        ctx_hk_before['status'] = 'concluded'

        if not all(ctx['status'] == 'approved' for ctx in ctx_hk_before['values']):
            raise Exception("Opa meu patrão")


    
    def __str__(self) -> str:
        return "Container: {}".format(self.name)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def get_status_builder(self):
        before_hook_statuses = {
            'status': 'not initialized',
            'values': []
        }

        after_hook_statuses = {
            'status': 'not initialized',
            'values': []
        }

        step_hook_statuses = {
            'status': 'not initialized',
            'values': []
        }

        all_pipeline_status = {
            'hook': {
                'before': before_hook_statuses,
                'after': after_hook_statuses,
            },
            'step': step_hook_statuses
        }

        return before_hook_statuses, after_hook_statuses, step_hook_statuses, all_pipeline_status

    def add_fixture(self, key, value):
        self.fixtures[key] = value

    def get_fixture(self, key, default=None):
        if key in self.fixtures:
            return self.fixtures[key]
        elif self.parent:
            return self.parent.get_fixture(key, default)
        else:
            return default

    def add_factory(self, name, factory_func, alucinator=None):
        self.factories[name] = {'func': factory_func, 'alucinator': alucinator}

    def get_factory(self, name):
        if name in self.factories:
            return self.factories[name]
        elif self.parent:
            return self.parent.get_factory(name)
        else:
            return None

from concurrent.futures import ThreadPoolExecutor
import asyncio
import inspect
# Classe Pipeline

# Funções de setup e teardown
def global_setup():
    logger.info("Configurando o ambiente global de testes...")

def global_teardown():
    logger.info("Limpando o ambiente global de testes...")

# Funções de teste (steps)
def send_numbers(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))  # Atraso entre 1 e 2 segundos
    if ctx.alucinator:
        data = ctx.data.copy()
        data = ctx.alucinator.do_something(data)
        ctx.data.update(data)
    ctx.set('n1', ctx.get('n1', 10))
    ctx.set('n2', ctx.get('n2', 20))
    ctx.output.log(f"Números enviados: n1={ctx.get('n1')}, n2={ctx.get('n2')}")
    ctx.approve()

def process_numbers(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    n1 = ctx.get('n1')
    n2 = ctx.get('n2')
    result = n1 + n2
    ctx.set('result', result)
    ctx.output.log(f"Números processados: {n1} + {n2} = {result}")
    ctx.approve()

def check_result(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    n1 = ctx.get('n1', 10)
    n2 = ctx.get('n2', 20)
    result = ctx.get('result')
    expected = n1 + n2
    if result == expected:
        ctx.approve()
        ctx.output.log(f"Resultado verificado: {result} == {expected}")
    else:
        ctx.reject(f"Resultado incorreto: {result} != {expected}")
        ctx.output.log(f"Resultado incorreto: {result} != {expected}")

def alucinador_modificar_result(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    ctx.set('result', ctx.get('result') + 5)
    ctx.output.log("Alucinação: Resultado foi alterado para um valor incorreto")
    ctx.approve()

def start_microservice(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    ctx.set('microservice', 'auth_service')
    ctx.output.log("Microserviço 'auth_service' iniciado.")
    ctx.approve()

def stop_microservice(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    microservice = ctx.get('microservice')
    if microservice:
        ctx.output.log(f"Microserviço '{microservice}' encerrado.")
        ctx.set('microservice', None)
    ctx.approve()

def check_login_success(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    success = ctx.get('login_success', True)
    if success:
        ctx.approve()
        ctx.output.log("Login realizado com sucesso.")
    else:
        ctx.reject("Falha no login.")
        ctx.output.log("Falha no login.")

def acessar_api(ctx: TestContext, **kwargs):
    time.sleep(random.uniform(1, 2))
    api_url = ctx.container.get_global_var('api_endpoint')
    ctx.set('api_response', f"Resposta da API em {api_url}")
    ctx.output.log(f"Acessando API em {api_url}")
    ctx.approve()

# Fixtures e Factories
def user_fixture():
    return {
        'username': 'test_user',
        'password': 'secure_password'
    }

def dynamic_number_factory():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    return {'n1': n1, 'n2': n2}



if __name__ == "__main__":
    # Instância do Output
    output = RichConsole()

    # Criação da instância de testes
    test_instance = Container(name = 'root', output=output)

    # Adicionando hooks de setup e teardown
    test_instance.before_each(global_setup)
    test_instance.after_each(global_teardown)

    # Adicionando fixtures e factories
    test_instance.add_fixture('user', user_fixture())
    test_instance.add_factory('dynamic_numbers', dynamic_number_factory, AlucinatorSpecial())
    test_instance.add_factory('combined_params', generate_random_params, AlucinatorSpecial())

    # Criação de containers e pipelines
    container_base = test_instance.create_container("Cenário", "Cenário Base de Teste")
    container_login = test_instance.create_container("Cenário", "Cenário de Login")

    container_login.before_each(lambda: output.log("Hook before_each no Cenário de Login"))
    sub_description_login = container_login.create_container('Subdescrição', 'Uma sub-descrição para o login')
    sub_description_login.before_each(lambda: output.log("Hook before_each na Subdescrição de Login"))

    description_jornada = container_base.create_container('Subdescrição', 'Simular a jornada do usuário')
    sub_description_jornada = description_jornada.create_container('Subdescrição', 'Uma sub-descrição para a jornada')

    # Pipeline de soma
    pipeline_soma = sub_description_jornada.create_pipeline('Deve ser capaz de somar dois números')
    pipeline_soma.before_each(lambda: output.log("Hook before_each no Pipeline Soma"))
    pipeline_soma.add_step('Enviando os números', send_numbers)
    pipeline_soma.add_step('Processando os números', process_numbers)
    pipeline_soma.add_step('Verificando resultados', check_result)

    # Pipeline com alucinação
    pipeline_alucinacao = sub_description_jornada.create_pipeline('Testar comportamento com alucinação')
    pipeline_alucinacao.add_step('Enviando os números', send_numbers, alucinator=AlucinatorSpecial())
    pipeline_alucinacao.add_step('Processando os números', process_numbers)
    pipeline_alucinacao.add_step('Alucinando o resultado', alucinador_modificar_result)
    pipeline_alucinacao.add_step('Verificando resultados', check_result)

    # Pipeline que controla microserviços
    pipeline_microservice = sub_description_jornada.create_pipeline('Testar controle de microserviços')
    pipeline_microservice.add_step('Iniciando microserviço', start_microservice)
    pipeline_microservice.add_step('Enviando os números', send_numbers)
    pipeline_microservice.add_step('Processando os números', process_numbers)
    pipeline_microservice.add_step('Verificando resultados', check_result)
    pipeline_microservice.add_step('Encerrando microserviço', stop_microservice)

    # Adicionando anotações e tags
    pipeline_soma.add_annotation('priority', 'high')
    pipeline_soma.add_annotation('author', 'Rickymal')
    pipeline_alucinacao.add_annotation('priority', 'medium')
    pipeline_alucinacao.add_annotation('author', 'Rickymal')
    pipeline_microservice.add_annotation('priority', 'critical')
    pipeline_microservice.add_annotation('author', 'Rickymal')

    pipeline_soma.add_tags(['soma', 'calculadora'])
    pipeline_alucinacao.add_tags(['alucinacao', 'teste_de_resiliencia'])
    pipeline_microservice.add_tags(['microservice', 'auth_service'])

    # Pipelines parametrizados via Monte Carlo
    NUM_SCENARIOS = 10  # Ajuste conforme necessário
    import time

    def setup_combined_params(ctx: TestContext, factory_name='combined_params', **kwargs):
        time.sleep(2)
        factory = ctx.container.get_factory(factory_name)
        if not factory:
            ctx.reject(f"Factory '{factory_name}' não registrada.")
            return
        data = factory['func']()
        if factory.get('alucinator'):
            data = factory['alucinator'].do_something(data)
        for key, value in data.items():
            ctx.set(key, value)
        ctx.output.log(f"Parâmetros gerados: {data}")
        ctx.approve()

    for i in range(NUM_SCENARIOS):
        pipeline = sub_description_jornada.create_pipeline(f'Somar Monte Carlo {i+1}')
        pipeline.add_step('Configurar Parâmetros', setup_combined_params)
        pipeline.add_step('Enviando os números', send_numbers)
        pipeline.add_step('Processando os números', process_numbers)
        pipeline.add_step('Verificando resultados', check_result)
        if random.random() < 0.1:
            pipeline.add_step('Alucinando o resultado', alucinador_modificar_result)

    # Pipeline de login
    def perform_login(ctx: TestContext, **kwargs):
        user = ctx.container.get_fixture('user')
        if not user:
            ctx.reject("Fixture 'user' não encontrada.")
            return
        ctx.set('username', user['username'])
        ctx.set('password', user['password'])
        if user['username'] == 'test_user' and user['password'] == 'secure_password':
            ctx.set('login_success', True)
            ctx.output.log("Login realizado com sucesso.")
        else:
            ctx.set('login_success', False)
            ctx.reject("Falha no login.")

    pipeline_login = sub_description_login.create_pipeline('Deve realizar login com usuário válido')
    pipeline_login.add_step('Realizando login', perform_login)
    pipeline_login.add_step('Verificando login', check_login_success)

    # Pipeline que acessa a API
    pipeline_api = sub_description_jornada.create_pipeline('Deve ser capaz de acessar a API')
    pipeline_api.add_step('Acessando a API', acessar_api)
    pipeline_api.add_step('Verificando resposta da API', lambda ctx, **kwargs: (
        ctx.approve() if 'Resposta da API' in ctx.get('api_response') else ctx.reject("Resposta da API inválida")
    ))

    # Adicionando variável global
    test_instance.set_global_var('api_endpoint', 'https://api.test.example.com')

    # Execução dos testes
    test_instance.run()

    # Salvando métricas
    metrics = test_instance.get_metrics()
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)

    # Integração com Sistema de Monitoramento e Alertas
    def send_alert(message: str):
        output.log(f"Alerta: {message}")

    # Verificação das métricas e envio de alertas se necessário
    for metric in metrics:
        if metric.get('status') == 'FAILED':
            send_alert(f"Teste '{metric.get('pipeline')}' falhou com o erro: {metric.get('errors')}")

    # Salvando métricas atualizadas após execuções adicionais
    metrics_updated = test_instance.get_metrics()
    with open('metrics_updated.json', 'w') as f:
        json.dump(metrics_updated, f, indent=4)


class SchemaContext(TestContext):

    def __init__(self, output, field):
        super().__init__(output)
        self.field = field
    pass





def hook_status_in_context(actual_context, state = {'status': 'not initialized'}):
    actual_context.on_approved = lambda : state.update({'status': 'approved'})
    actual_context.on_rejected = lambda : state.update({'status': 'rejected'})
    actual_context.on_concluded = lambda : state.update({'status': 'concluded'})
    actual_context.on_status_checked = lambda : state['status']

    return actual_context

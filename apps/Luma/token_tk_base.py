# Definição do Token
from dataclasses import field, dataclass
from typing import Callable, Dict, Any, List, Tuple, Optional, Union
from enums import Personality


@dataclass
class TokenTK:
    name: str
    pattern: str
    is_primitive: bool
    scan: any
    # extract: Callable[[Dict[str, Any], str], List[Tuple[int, int, str]]]
    contexts: List['ParserContext'] = field(default_factory=list)
    is_owner: bool = False
    personality: Optional[Personality] = None
    parents: List['TokenTK'] = field(default_factory=list)
    children: List['TokenTK'] = field(default_factory=list)
    specification: Dict[str, Any] = field(default_factory=dict)
    value: Optional[Dict[str, Union[int, str]]] = None
    ntokens: list['TokenTK'] = field(default_factory=list)

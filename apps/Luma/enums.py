from enum import Enum, auto


class Personality(Enum):
    LAZY = auto()          # Delegar o proprietário para o novo token encontrado
    DELEGATOR = auto()    # Similar ao LAZY
    COLLABORATIVE = auto()# Leitura em conjunto com novos tokens
    BOSSY = auto()        # Não delega, lê até o final antes de passar para o próximo token


class Dimension(Enum):
    HIDDEN = auto()
    VISIT = auto()


class PropagationType(Enum):
    UNDEFINED = auto()
    ZERO_TO_ONE = auto()
    ZERO_TO_MANY = auto()
    ONE_TO_MANY = auto()
    ONLY_ONE = auto()

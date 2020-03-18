import toml
from bonito.model import Model


def network(insize=1, size=256, winlen=19, stride=2, alphabet_info=None):
    config = toml.load('$BONITO_MODEL_CONFIG')
    return Model(config)

import toml
from bonito.model import Model


def network(insize=1, size=256, winlen=19, stride=2, alphabet_info=None):
    config = toml.load('/Users/manh/Development/bonito/config/quartznet5x5.toml')
    return Model(config)

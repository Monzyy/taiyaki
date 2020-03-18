import toml
from bonito.model import Model

toml_string = """
model = "QuartzNetFlipFlop"

[labels]
labels = ["A", "C", "G", "T"]

[input]
features = 1

[encoder]
activation = "relu"

# C1 
[[block]]
filters = 256
repeat = 1
kernel = [33]
stride = [3]
dilation = [1]
dropout = 0.0
residual = false
separable = false

# B1
[[block]]
filters = 256
repeat = 5
kernel = [33]
stride = [1]
dilation = [1]
dropout = 0.0
residual = true
separable = true

# B2
[[block]]
filters = 256
repeat = 5
kernel = [39]
stride = [1]
dilation = [1]
dropout = 0.0
residual = true
separable = true

# B3
[[block]]
filters = 512
repeat = 5
kernel = [51]
stride = [1]
dilation = [1]
dropout = 0.0
residual = true
separable = true

# B4
[[block]]
filters = 512
repeat = 5
kernel = [63]
stride = [1]
dilation = [1]
dropout = 0.0
residual = true
separable = true

# B5
[[block]]
filters = 512
repeat = 5
kernel = [75]
stride = [1]
dilation = [1]
dropout = 0.0
residual = true
separable = true

# C2
[[block]]
filters = 512
repeat = 1
kernel = [87]
stride = [1]
dilation = [1]
dropout = 0.0
residual = false
separable = true

# C3
[[block]]
filters = 1024
repeat = 1
kernel = [1]
stride = [1]
dilation = [1]
dropout = 0.0
residual = false
separable = false
"""


def network(insize=1, size=256, winlen=19, stride=2, alphabet_info=None):
    config = toml.loads(toml_string)
    return Model(config)

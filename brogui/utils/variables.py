import importlib
from abc import ABC
from enum import Enum

from nextorch import parameter

class ParameterType(Enum):
    continuous="continuous"
    categorical="categorical"
    ordinal="ordinal"

# Init viable acqucision functions
AF_OPTIONS = ["EI", "PI", "UCB", "qEI", "qPI", "qUCB", "qEHVI"]

# Init viable sampling strategies
DOE_OPTIONS = ["Full Factorial", "Latin Hypercube", "Norm Transform", "Randomized Design"]

# Init viable parameters
OPTION_PARAMS = ["T", "P", "GR", "LR", "C"]
def VariableFactory(class_name):

    """Factory Method"""
    parameters = {
        "T": T, "P": P, "GR": GR, "LR": LR, "C": C
    }

    return parameters[class_name]()

class Variable(ABC):
    def __init__(self):
        self.symbol = None
        self.parameter_name = None
        self.parameter_type = None
        self.unit = None
        self.parameter_range = None
        self.interval = None
    
    def parameter(self):
        NotImplemented

# Res. Time is depended on the volume of reactor
# class RT(Variable):
#     def __init__(self):
#         self.symbol = "RT"
#         self.parameter_name = "Res. Time"
#         self.parameter_type = ParameterType.continuous.value
#         self.unit = 'min'
#         self.parameter_range = [0, 100]
    
class T(Variable):
    def __init__(self):
        self.symbol = "T"
        self.parameter_name = "Temperature"
        self.parameter_type = ParameterType.ordinal.value
        self.unit = "C"
        self.parameter_range = [80, 150]
        self.interval = 5
    
    def parameter(self):
        return parameter.Parameter(
            x_type = self.parameter_type,
            x_range = self.parameter_range,
            interval = self.interval
        )

class P(Variable):
    def __init__(self):
        self.symbol = "P"
        self.parameter_name = "Pressure"
        self.parameter_type = ParameterType.ordinal.value
        self.unit = "MPa"
        self.parameter_range = [0.1, 6]
        self.interval = 1
    
    def parameter(self):
        return parameter.Parameter(
            x_type = self.parameter_type,
            x_range = self.parameter_range,
            interval = self.interval
        )

class GR(Variable):
    def __init__(self):
        self.symbol = "GR"
        self.parameter_name = "Gas Flow Rate"
        self.parameter_type = ParameterType.ordinal.value
        self.unit = "mL/min"
        self.parameter_range = [0, 100]
        self.interval = 10

    def parameter(self):
        return parameter.Parameter(
            x_type = self.parameter_type,
            x_range = self.parameter_range,
            interval = self.interval
        )

class LR(Variable):
    def __init__(self):
        self.symbol = "LR"
        self.parameter_name = "Liquid FLow Rate"
        self.parameter_type = ParameterType.ordinal.value
        self.unit = "mL/min"
        self.parameter_range = [0.1, 10]
        self.interval = 0.5

    def parameter(self):
        return parameter.Parameter(
            x_type = self.parameter_type,
            x_range = self.parameter_range,
            interval = self.interval
        )

class C(Variable):
    def __init__(self):
        self.symbol = "C"
        self.parameter_name = "Concentration"
        self.parameter_type = ParameterType.ordinal.value
        self.unit = "wt%"
        self.parameter_range = [10, 20]
        self.interval = 5

    def parameter(self):
        return parameter.Parameter(
            x_type = self.parameter_type,
            x_range = self.parameter_range,
            interval = self.interval
        )
"""
.. include:: ../README.md

.. include:: ../examples/regression_example.md
.. include:: ../examples/calibration_example.md
"""
REGRESSION = 'regression'
CLASSIFICATION = 'classification'

from Laplace.laplace.baselaplace import BaseLaplace, ParametricLaplace, FullLaplace, KronLaplace, DiagLaplace, LowRankLaplace
from Laplace.laplace.lllaplace import LLLaplace, FullLLLaplace, KronLLLaplace, DiagLLLaplace
from Laplace.laplace.subnetlaplace import SubnetLaplace, FullSubnetLaplace, DiagSubnetLaplace
from Laplace.laplace.laplace import Laplace
from Laplace.laplace.marglik_training import marglik_training

__all__ = ['Laplace',  # direct access to all Laplace classes via unified interface
           'BaseLaplace', 'ParametricLaplace',  # base-class and its (first-level) subclasses
           'FullLaplace', 'KronLaplace', 'DiagLaplace', 'LowRankLaplace',  # all-weights
           'LLLaplace',  # base-class last-layer
           'FullLLLaplace', 'KronLLLaplace', 'DiagLLLaplace',  # last-layer
           'SubnetLaplace',  # base-class subnetwork
           'FullSubnetLaplace', 'DiagSubnetLaplace',  # subnetwork
           'marglik_training', '']  # methods

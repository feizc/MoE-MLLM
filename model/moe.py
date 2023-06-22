# Sparsely-gated mixture-of-experts contexted on text information 


import torch 
import torch.nn as nn 
import numpy as np 


class MoE(nn.Module): 
    """
    input_size: int
    output_size: int 
    num_experts: int 
    hidden_size: int 
    k: int, how many experts to use 
    """
    def __init__(
        self,
        k=4,
    ): 
        

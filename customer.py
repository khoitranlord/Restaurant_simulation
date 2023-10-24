import numpy as np
import random
import math
from enum import Enum


class CustomerStatus(Enum):
    ARRIVAL = "arrival"
    DEPART = "depart"

class Customer:
    def __init__(self, arrivalTime, CustomerStatus = CustomerStatus.ARRIVAL ):
        self.arrivalTime = arrivalTime
        self.CustomerStatus = CustomerStatus.ARRIVAL


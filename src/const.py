from typing import Callable
from src.algo.sorts import *

ALGO_MAP: dict[str, Callable] = {
    "bubble": bubble_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "radix": radix_sort,
    "bucket": bucket_sort,
    "counting": counting_sort,
}

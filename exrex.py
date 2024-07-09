# Inside exrex.py of lk21
try:
    from re import sre_parse, U
except ImportError:
    import re._sre as sre_parse
    from re import UNICODE as U

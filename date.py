# -*- coding: utf-8 -*-
from datetime import *

res = date.today() - timedelta(days=5)
value = res < date.today()
print(date.today() )
print(res)
print(value)
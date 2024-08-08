from fastapi import FastAPI

import os
import sys
sys.path.append(os.path.join(sys.path[0], 'src'))


app = FastAPI(
    title="Family Shop App"
)

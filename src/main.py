from fastapi import FastAPI

import os
import sys

sys.path.append(os.path.join(sys.path[0], "src"))


app = FastAPI(title="Family Shop App")

from auth.auth_router import router as auth_router
app.include_router(auth_router)

from api.product import router as product_router
app.include_router(product_router)
from typing import Annotated

from fastapi import Depends

from unitofwork import IUnitOfWork, UnitOfWork

from auth.models import User
from auth.base_config import current_user

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]

UserDep = Annotated[User, Depends(current_user)]
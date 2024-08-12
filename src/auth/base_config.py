from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from auth.manager import get_user_manager
from auth.models import User
from config import SECRET_AUTH

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600 * 24)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600 * 24)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()



# test = await uow.role.check_role(user_id, 'Admin')
# print(test)

# Annotated[User, Depends(current_user)]
# class RoleChecker:
#     def __init__(self, allowed_role: str):
#         self.allowed_role = allowed_role

#     def __call__(self, user: Annotated[User, Depends(current_user)]):
#         user.role_id == 1
#         if user.role == self.allowed_role:
#             return True
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="You don't have enough permissions",
#         )

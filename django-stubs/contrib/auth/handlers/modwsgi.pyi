from typing import Any, Dict, Optional

UserModel: Any

def check_password(
    environ: Dict[Any, Any], username: str, password: str
) -> Any: ...
def groups_for_user(environ: Dict[Any, Any], username: str) -> Any: ...

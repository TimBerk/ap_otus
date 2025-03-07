import threading
from collections.abc import Callable
from typing import Any


class IoCContainer:
    HANDLERS = {
        'IoC.Register': 'register',
        'Scopes.New': 'new_scope',
        'Scopes.Current': 'set_current_scope',
    }

    def __init__(self):
        self.registry: dict[str, Callable[..., Any]] = {}
        self.scopes: dict[str, dict[str, Callable[..., Any]]] = {}
        self.current_scope = threading.local()

    def resolve(self, key: str, *args) -> Any:
        if key in self.HANDLERS:
            return getattr(self, self.HANDLERS[key])(*args)
        return self.resolve_dependency(key, *args)

    def register(self, key: str, factory: Callable[..., Any]) -> 'IoCContainer':
        if not hasattr(self.current_scope, 'scope_id'):
            self.registry[key] = factory
        else:
            scope_id = self.current_scope.scope_id
            if scope_id not in self.scopes:
                self.scopes[scope_id] = {}
            self.scopes[scope_id][key] = factory
        return self

    def new_scope(self, scope_id: str) -> 'IoCContainer':
        if scope_id not in self.scopes:
            self.scopes[scope_id] = {}
        return self

    def set_current_scope(self, scope_id: str) -> 'IoCContainer':
        self.current_scope.scope_id = scope_id
        return self

    def resolve_dependency(self, key: str, *args) -> Any:
        if not hasattr(self.current_scope, 'scope_id'):
            if key in self.registry:
                return self.registry[key](*args)
            raise KeyError(f"Dependency '{key}' not found in global scope.")

        scope_id = self.current_scope.scope_id
        if scope_id in self.scopes and key in self.scopes[scope_id]:
            return self.scopes[scope_id][key](*args)
        elif key in self.registry:
            return self.registry[key](*args)

        raise KeyError(f"Dependency '{key}' not found in scope '{scope_id}' or global scope.")

from functools import wraps
import asyncio
from .package import Package


class ProcedureResult:
    pass


class UnsupportedFeature(ProcedureResult):
    pass


def require_features(features):
    def wrapper(func):
        @wraps(func)
        def newfunc(self, *args, **kwargs):
            if not self.schema.has_features(features):
                return UnsupportedFeature
            return func(*args, **kwargs)
        return newfunc
    return wrapper


def require_feature(feature):
    return require_features({feature})


class Session:
    def __init__(self, package: Package):
        self._package = package

    def install(self):
        pass

    @require_feature('DEPS')
    async def install_deps(self) -> ProcedureResult:
        async for dep in self._package.schema.deps:
            await asyncio.sleep(0)

    @require_feature('OPTDEPS')
    async def install_optdeps(self) -> ProcedureResult:
        pass

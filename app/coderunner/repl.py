import sys
import os
import contextlib
from io import StringIO
from wrapt_timeout_decorator import *

class CodeExecutor:
    @contextlib.contextmanager
    def stdoutIO(self, stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    @timeout(5)
    def execute_python(self, code: str) -> str:
        with self.stdoutIO() as c:
            try:
                exec(code, {'__builtins__': __builtins__})
            except Exception as e:
                print(e)
        return c.getvalue() if c else ""
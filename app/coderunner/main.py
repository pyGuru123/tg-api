import io
import matplotlib.pyplot as plt
from timeit import default_timer as timer

from app.coderunner.repl import CodeExecutor


append_string = """
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
"""

async def execute_code(code: str) -> str:
    code = code.strip().strip("\n")

    try:
        executor = CodeExecutor()
        start = timer()
        output = executor.execute_python(code)
        end = timer()
    except Exception as e:
        raise Exception(e)

    return f"Result \n{output.rstrip()}\nExecution time: {end-start:.3f}s"


async def plot_graph(code):
    code = f"import io\nimport numpy as np\n{code.strip()}\nimport matplotlib.pyplot as plt\n{append_string}"

    namespace = {}
    exec(code, namespace)
    binary_data = namespace['buffer'].getvalue()
    return binary_data
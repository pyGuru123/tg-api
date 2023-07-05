import io
import os
import requests
import platform
import matplotlib.pyplot as plt
from timeit import default_timer as timer

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

from app.coderunner.repl import CodeExecutor

prepend_string = """
import io
import numpy as np
import matplotlib.pyplot as plt
plt.figure()
"""

append_string = """
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
plt.close()
"""


def get_themes():
    return [
        "abyss",
        "dark-plus",
        "light-plus",
        "github-dark",
        "github-light",
        "visual-studio-dark",
        "visual-studio-light",
        "high-contrast",
        "kimbie-dark",
        "dimmed-monokai",
        "monokai",
        "night-owl",
        "night-owl-no-italic",
        "night-owl-light",
        "quietlight",
        "red",
        "solarized-dark",
        "solarized-light",
        "tomorrow-night-blue",
    ]


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


async def plot_graph(code: str):
    code = f"{prepend_string}\n{code.strip()}\n{append_string}"

    namespace = {}
    exec(code, namespace)
    binary_data = namespace["buffer"].getvalue()
    namespace["buffer"].close()
    namespace.clear()

    return binary_data


async def render_code(code: str, theme: str):
    url = "https://sourcecodeshots.com/api/image"
    json = {"code": code.strip(), "settings": {"language": "python", "theme": theme}}

    response = requests.post(url, json=json)
    return response.content


async def pastebin(code: str, title: str =""):
    pastebin_endpoint = "https://pastebin.com/api/api_post.php"
    api_dev_key = os.environ.get("PASTEBIN_TOKEN")

    data = {
        "api_dev_key": api_dev_key,
        "api_option": "paste",
        "api_paste_code": code.strip(),
        "api_paste_expire_date": "1D",
        "api_paste_format": "python",
        "api_paste_name": title
    }

    r = requests.post(url=pastebin_endpoint, data=data)
    return r.text

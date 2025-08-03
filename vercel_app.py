import litellm
from litellm.proxy.proxy_server import app
import os

# Set the config file path
os.environ["LITELLM_CONFIG_PATH"] = os.path.join(os.getcwd(), "config.yml")

# The 'app' object from litellm.proxy.proxy_server is the FastAPI app.
# Vercel will automatically detect and serve it.
# No need to run uvicorn manually.
litellm.set_verbose=True

import sys
import importlib.metadata

print(f"Python: {sys.version.split()[0]}")
print(f"Flask: {importlib.metadata.version('flask')}")
print(f"Django: {importlib.metadata.version('django')}")
print("Environment is ready!")

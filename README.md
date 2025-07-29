# Define functions in py file and use them in Notebook

1. Top cell
   ```python
   %load_ext autoreload
   %autoreload 2
   ```



```python
import functions as fn
import importlib
importlib.reload(fn)  # ? force reload from updated source
```
# measuretime
---

python decorator to measure function time.

### Usage:
```python:hello.py
import time
from measuretime.secound import measuresecound

@measuresecound
def main():
    time.sleep(1)
    return

if __name__ == "__main__":
    main()

```

```
$ python hello.py
Call main 5.5e-05 second
```

#### Install:
```
$pip install measuretime
```

### LISENCE
MIT

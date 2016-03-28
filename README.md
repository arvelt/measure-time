# measuretime
---

Python decorator to measure function time.

## USAGE:
Saved hello.py
``` python

import time
from measuretime.secound import measuresecound

@measuresecound
def main():
    time.sleep(1)
    return

if __name__ == "__main__":
    main()

```

Run hello.py
```
$ python hello.py
Call main 0.00001 second
```

## INSTALL:
```
$pip install measuretime
```

## LICENSE
MIT

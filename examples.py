# -*- coding: utf-8 -*-
import time
from measuretime.secound import measuresecound

@measuresecound
def main():
    time.sleep(1)
    return

if __name__ == "__main__":
    main()

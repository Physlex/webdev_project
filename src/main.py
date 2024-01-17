#!/usr/bin/env python3

import sys, asyncio

from application import Application

## MAIN

async def main():
    exit_code = 0

    app = Application()
    app.initialize()
    while (not app.should_close):
        await app.run()
    app.terminate()

    return exit_code


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
    pass

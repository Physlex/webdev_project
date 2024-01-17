from logging import Logger
import asyncio


class Application(object):
    """
    """

    def __init__(self) -> None:
        """
        """

        app_logger_name: str = "Application logger"
        self.logger = Logger(app_logger_name)

        self.should_close = False
        pass

    def initialize(self):
        """
        """

        pass

    async def run(self):
        """
        """

        print("Hello!")
        await asyncio.sleep(1)
        print("Goodbye!")

        self.should_close = True
        pass

    def terminate(self):
        """
        """

        pass

    logger: Logger
    should_close: int

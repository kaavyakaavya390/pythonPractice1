import logging


class Basic_log:
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Example usage
    def calculate_sum(self, a, b):
        logging.debug(f"Calculating sum of {a} and {b}")
        result = a + b
        logging.info(f"Sum calculated successfully: {result}")
        return result

    # Main program
    def basic(self):
        logging.info("Starting the program")
        result = self.calculate_sum(10, 20)
        logging.info("Program completed")


def config_log():

    # Create logger
    logger = logging.getLogger("my_app")
    logger.setLevel(
        logging.DEBUG
    )  # Set global log level DEBUG < INFO < WARNING < ERROR < CRITICAL
    logger.propagate = False  # To avoid root handler

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(console_handler)

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


def main():
    config_log()
    # Basic_log.basic()
    # #------------Syntax warning--------
    # num=10
    # if num is 10:
    #     print(num)


main()

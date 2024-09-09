import logging

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Function to set up a logger with a specific name and log level.
    Logs are output to the console.
    """
    logger = logging.getLoger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.setLevel(level)
        logger.addHandler(handler)

    return logger



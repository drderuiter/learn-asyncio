import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s.%(msecs)03d - line %(lineno)2s: %(funcName)20s() - %(message)s"
        ),
        datefmt="%H:%M:%S",
    )

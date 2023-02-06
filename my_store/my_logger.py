import logging


def main():
    # logging.DEBUG
    # logging.INFO
    # logging.WARNING
    # logging.ERROR
    # logging.CRITICAL

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%F-%m-%d %H:%M:%S",
        filename="basic.log",
    )

    logging.debug("This is a debug message")
    logging.info("This is a debug message")
    logging.warning("This is a debug message")
    logging.error("This is a debug message")
    logging.critical("This is a debug message")


if __name__ == "__main__":
    main()

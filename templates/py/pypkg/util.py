import subprocess

import colorlog

LEVELS = {0: "ERROR", 1: "WARNING", 2: "INFO", 3: "DEBUG"}

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-6s%(reset)s [%(asctime)s] %(blue)s%(message)s",
    datefmt="%H:%M:%S",
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
    secondary_log_colors={},
    style="%",
)


def configure_stream(level="INFO"):
    """Configure root logger using a colored stream handler and stderr."""
    # get the root logger
    root_logger = colorlog.getLogger()
    # set the logger level to the same as will be used by the handler
    root_logger.setLevel(level)

    # add a basic STDERR handler to the logger
    handler = colorlog.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)

    root_logger.addHandler(handler)
    return root_logger


def count_lines(fp):
    out = subprocess.Popen(
        ["wc", "-l", fp], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).communicate()[0]
    return int(out.partition(b" ")[0])

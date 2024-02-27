import coloredlogs, logging

logger = logging.getLogger(__name__)

coloredlogs.install(
    logger=logger, fmt='%(asctime)s 🎉 %(message)s', use_chroot=False,
    field_styles={'asctime': {'color': 'white', 'bold': True}}, datefmt='%d.%m.%Y %H:%M:%S',
    level_styles={
        'info': {'color': 'green', 'bold': True},
        'warn': {'color': 'red', 'bold': True},
        'debug': {'color': 'magenta', 'bold': False}
    },
    isatty=True
)

logger.debug("a debug message")
logger.info("an info message")
logger.warning("a warning message")
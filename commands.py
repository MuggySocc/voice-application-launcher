import config
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

logger = logging.getLogger(__name__)



def parse_command(transcript):
    logger.debug(transcript)
    words = transcript.split()

    if len(words) < 2:
        logger.warning("Incomplete command")
        return None, None
    if not words:
        print("No command Recognized")
        return None, None
    action = words[0]
    target = " ".join(words[1:])

    if target in config.aliaes:
        target = config.aliaes[target]
    return action, target
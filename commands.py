import config


def parse_command(transcript):
    print(transcript)
    words = transcript.split()

    if len(words) < 2:
        print("Incomplete command")
        return None, None
    if not words:
        print("No command Recognized")
        return None, None
    action = words[0]
    target = " ".join(words[1:])

    if target in config.aliaes:
        target = config.aliaes[target]
    return action, target
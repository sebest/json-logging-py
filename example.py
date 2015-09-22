import logging
import jsonlogging


logger = logging.getLogger()

logHandler = logging.StreamHandler()

# You can also use LogstashFormatterV0 or LogstashFormatterV1
formatter = jsonlogging.JSONFormatter(
    hostname="server-01.example.com",
    tags=["env=prod", "role=www"],
    indent=4)
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)

logger.error('hello world!', extra={"tags": ["hello=world"]})

import os
import tempfile
import json
from contextlib import contextmanager


@contextmanager
def google_cloud_platform_credential():
    HEROKU_CONFIG_KEY = 'GOOG_CLOUD_CREDENTIAL'
    json_credential = os.environ.get(HEROKU_CONFIG_KEY)
    json_credential_escape = json_credential.replace('\n', '\\n')
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(str.encode(json.dumps(json.loads(json_credential_escape))))
        temp.flush()
        yield temp.name

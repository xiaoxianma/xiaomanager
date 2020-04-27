import logging
from google.cloud import vision
from libs.credentials import google_cloud_platform_credential


logger = logging.getLogger(__name__)


def detect_logos(image_binary):
    """Detects logos in the file."""
    with google_cloud_platform_credential() as json_credential:
        client = vision.ImageAnnotatorClient.from_service_account_json(json_credential)

    logo_desc = None
    image = vision.types.Image(content=image_binary)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    logger.info(f"totally {len(logos)} logos detected!")
    for logo in logos:
        logger.info(f'Logo:{logo.description}')
        logo_desc = logo.description

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return logo_desc

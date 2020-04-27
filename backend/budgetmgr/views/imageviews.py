from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from libs.image_detection import detect_logos
import logging

logger = logging.getLogger(__name__)


class MerchantImageView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        f = request.data['file']
        logger.info(f'processing image={f}')
        content = f.read()
        logo_desc = detect_logos(content)
        logger.info(f'image={f} complete')
        if logo_desc:
            logger.info(f'merchant={logo_desc}')
            return Response(data={'name': logo_desc}, status=200)
        else:
            logger.info(f'No merchant name detected')
            return Response(data={'name': None}, status=400)

from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
        logger.info(f'image={f} complete')
        return Response(status=201)

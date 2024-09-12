from PIL import Image
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers.post import PostSerializer


class PostCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Получаем авторизованного пользователя
        user = request.user

        # Проверяем наличие изображения в запросе
        if 'image' not in request.FILES:
            return Response({'error': 'Image file is required'}, status=status.HTTP_400_BAD_REQUEST)

        image_file = request.FILES['image']

        try:
            # Открываем изображение
            image = Image.open(image_file)
            # Извлекаем метаданные
            exif_data = image._getexif()  # _getexif() возвращает данные EXIF

            if exif_data:
                # Пример: получение координат GPS из EXIF (это просто пример, вы можете получить другие данные)
                gps_info = exif_data.get(34853)  # GPS info tag
                if gps_info:
                    latitude = gps_info[2][0]
                    longitude = gps_info[4][0]
                else:
                    latitude, longitude = None, None
            else:
                latitude, longitude = None, None

            # Создаем объект Post
            post = Post(author=user, image=image_file, likes=0, views=0, latitude=latitude, longitude=longitude)
            post.save()

            # Создаем сериализатор для возврата ответа
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

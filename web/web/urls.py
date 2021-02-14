"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import auction.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', auction.views.signup, name = 'signup'),
    path('', auction.views.home, name = 'home'),
    path('status', auction.views.status, name = 'status'),
    path('statusResult', auction.views.status, name = 'status_result'),
    path('lot', auction.views.lot, name = 'lot'),
    path('lotWinner', auction.views.lot, name = 'lot_winner'),

    path('bookList', auction.views.book_list, name = 'book_list'),
    path('book/<int:book_id>', auction.views.book, name = 'book'),
    path('registerBook', auction.views.register_book, name = 'register_book'),
    path('registerBook/<int:book_id>', auction.views.register_book, name = 'register_book'),
    path('unRegisterBook', auction.views.unRegister_book, name = 'unRegister_book'),
    path('unRegisterBook/<int:book_id>', auction.views.unRegister_book, name = 'unRegister_book'),

    path('boardGameList', auction.views.board_game_list, name = 'board_game_list'),
    path('boardGame/<int:board_game_id>', auction.views.board_game, name = 'board_game'),
    path('registerBoardGame', auction.views.register_board_game, name = 'register_board_game'),
    path('registerBoardGame/<int:board_game_id>', auction.views.register_board_game, name = 'register_board_game'),
    path('unRegisterBoardGame', auction.views.unRegister_board_game, name = 'unRegister_board_game'),
    path('unRegisterBoardGame/<int:board_game_id>', auction.views.unRegister_board_game, name = 'unRegister_board_game'),

    path('furnitureList', auction.views.furniture_list, name = 'furniture_list'),
    path('furniture/<int:furniture_id>', auction.views.furniture, name = 'furniture'),
    path('registerFurniture', auction.views.register_furniture, name = 'register_furniture'),
    path('registerFurniture/<int:furniture_id>', auction.views.register_furniture, name = 'register_furniture'),
    path('unRegisterFurniture', auction.views.unRegister_furniture, name = 'unRegister_furniture'),
    path('unRegisterFurniture/<int:furniture_id>', auction.views.unRegister_furniture, name = 'unRegister_furniture'),

    path('etcList', auction.views.etc_list, name = 'etc_list'),
    path('etc/<int:etc_id>', auction.views.etc, name = 'etc'),
    path('registerETC', auction.views.register_etc, name = 'register_etc'),
    path('registerETC/<int:etc_id>', auction.views.register_etc, name = 'register_etc'),
    path('unRegisterETC', auction.views.unRegister_etc, name = 'unRegister_etc'),
    path('unRegisterETC/<int:etc_id>', auction.views.unRegister_etc, name = 'unRegister_etc'),
] + static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)


from django.urls import path
from main.views import (
    show_main, create_football_item, show_football_item_detail, 
    show_xml, show_json, show_xml_by_id, show_json_by_id, 
    register, login_user, logout_user, 
    edit_football_item, delete_football_item,
    create_football_item_ajax, edit_football_item_ajax, delete_football_item_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_football_item/', create_football_item, name='create_football_item'),
    path('football_item/<int:id>/', show_football_item_detail, name='show_football_item_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_football_item/<int:id>/edit', edit_football_item, name='edit_football_item'),
    path('delete_football_item/<int:id>/delete', delete_football_item, name='delete_football_item'),
    # AJAX endpoints
    path('api/create/', create_football_item_ajax, name='create_football_item_ajax'),
    path('api/edit/<int:id>/', edit_football_item_ajax, name='edit_football_item_ajax'),
    path('api/delete/<int:id>/', delete_football_item_ajax, name='delete_football_item_ajax'),
]
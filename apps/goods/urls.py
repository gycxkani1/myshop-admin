from django.urls import path,include
from apps.goods import views

urlpatterns = [
    #path('index/',views.GoodsListView.as_view()),
    #path('goods/',views.GoodsList.as_view()),

    #path('goods_mixin/',views.GoodsListView_mixins.as_view()),
    #path('goods_list/',views.GoodsListView_List.as_view()),

    path('goods_category_add/',views.GoodsCategoryAddView.as_view(),name="cate_add"),
    path('cate_index/',views.GoodsCategoryView.as_view(),name='cate_index'),

    path('add/',views.GoodsAddView.as_view(),name='good_add'),
    path('index/',views.GoodsView.as_view(),name='index'),

    path("ajax_goods/",views.ajax_goods),
]

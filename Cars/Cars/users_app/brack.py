# # <!doctype html>
# # <html lang="en">
# # <head>
# #     <meta charset="UTF-8">
# #     <meta name="viewport"
# #           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
# #     <meta http-equiv="X-UA-Compatible" content="ie=edge">
# #     <link rel="stylesheet" href="{% static 'login.css' %}">
# #     <script type="text/JavaScript" src="{% static 'index.js' %}"> </script>
# #     <title>Document</title>
# # </head>
# # <body onload="startTime()">
# # <div id="txt"></div>
# # <h1> DENI CARS</h1>
# # <div id="root">
# #     <div class="list-products">
# #
# #     </div>
# #     <div class="details-products">
# #
# #     </div>
# # </div>
# #
# # <script>
# #     window.URLS = {
# #         productsAll: () => '/restpart/car/',
# #         productDetails: (id) => `/restpart/car/${id}/`,
# #     };
# #
# #     const getAllProducts = () => {
# #         const {productsAll} = window.URLS;
# #         return fetch(productsAll())
# #             .then(response => response.json())
# #
# #     };
# #     const LoadAllProducts = () => {
# #          getAllProducts()
# #          .then(products => {});
# #
# #     };
# #
# #
# #
# # </script>
# #
# #
# #
# #
# # </body>
# # </html>
#
#
#
# //     window.URLS = {
# //         productsAll: () => '/restpart/car/',
# //         productDetails: (id) => `/restpart/car/${id}/`,
# //     };
# //
# //     const getAllProducts = () => {
# //         const {productsAll} = window.URLS;
# //         return fetch(productsAll())
# //             .then(response => response.json())
# //     };
# //
# //     const getProductDetails = (id) => {
# //         const {productDetails} = window.URLS;
# //         return fetch(productDetails(id))
# //             .then(response => response.json());
# //     }
# //
# //     const renderProductsList = (products) => {
# //         let productsListItems = '';
# //         for (const product of products) {
# //             productsListItems += `
# // <li>
# //     <a class="btn-show-product-details" data-product-id="${product.id}" href="#">${product.name}</a>
# // </li>
# //             `;
# //         }
# //
# //         return `
# // <ul>
# // ${productsListItems}
# // </ul>`
# //     };
# //
# //     const renderProductDetails = (product) => `
# //     <h2>${product.name}</h2>`
# //
# //     const loadProductsList = () => {
# //         getAllProducts()
# //             .then(products => renderProductsList(products))
# //             .then(productsList => {
# //                 document.querySelector('.list-products').innerHTML = productsList;
# //             });
# //     };
# //
# //     const loadProductDetails = (id) => {
# //         getProductDetails(id)
# //             .then(product => renderProductDetails(product))
# //             .then(productDetails => {
# //                 document.querySelector('.details-products').innerHTML = productDetails;
# //             });
# //     };
# //
# //     const attachEvents = () => {
# //         document.body.addEventListener('click', (ev) => {
# //             const element = ev.target;
# //             if (element.classList.contains('btn-show-product-details')) {
# //                 const productId = element.getAttribute('data-product-id');
# //                 loadProductDetails(productId);
# //             }
# //         });
# //     };
# //
# //     loadProductsList();
# //     attachEvents();
#
# # ///// watch


# def get_queryset(self,**kwargs):
    #     query=''
    #     search_user = self.request.query_params.get('user', None)
    #     queryset=UserCar.objects.all()
    #     if search_user:
    #         query=queryset.filter(user=search_user)
    #     else:
    #         query=queryset
    #     return query


# def get_queryset(self,*args,**kwargs):
#     # query=''
#     # search_id = self.request.query_params.get('id', None)
#     queryset=CustomCarUser.objects.all()
#     # if search_id:
#     #     query=queryset.filter(id=search_id)
#     # else:
#     #     query=queryset
#     serializers=InfoAllUsersSerializer(queryset)
#     return Response(serializers.data)

# def list(self, request, *args, **kwargs):
#     queryset = CustomCarUser.objects.get(id=1)
#     serializers_ = ListUsersSerializer(queryset)
#     return Response(serializers_.data)

# def get_queryset(self):
#     user = self.request.user
#     if user.is_superuser:
#         return CustomCarUser.objects.all()
#     return CustomCarUser.objects.filter(username=user.username)

# class SingleCarModelView(api_views.RetrieveUpdateDestroyAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarModelSerializer

# class SingleCarView(api_views.RetrieveUpdateDestroyAPIView):
#     queryset = UserCar.objects.all()
#     serializer_class = CarSerializer

# <div>
#         <form class="app" method='post' action="{% url 'create car' %}">
#          <button class="regi">Create new car </button>
#             {% csrf_token %}
#
#         </form>
#     </div>

# def list(self, request):
    #     queryset = CarBrand.objects.all()
    #     serializer = CarBrandListSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def create(self,request):
    #     pass

#class ListUsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomCarUser
#         fields = '__all__'

# class CreateCarView(api_views.CreateAPIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#     serializer_class = CreateCarSerializer
##########################################
# def get_queryset(self, **kwargs):
#     query = ''
#     search_id = self.request.query_params.get('id', None)
#     search_hometown = self.request.query_params.get('hometown', None)
#     queryset = CustomCarUser.objects.all()
#     if search_id:
#         query = queryset.filter(id=search_id)
#     elif search_hometown:
#         query = queryset.filter(hometown=search_hometown)
#     else:
#         query = queryset
#     return query

#from django.urls import path
#
#
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )
#
# urlpatterns = [
#    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#    ...
# ]

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
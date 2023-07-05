{% load static %}
let shop = document.getElementById("shop");

let shopItemsData = [
	{
		id: "abcde",
		name: "vasual Shirt",
		price: 45,
		desc: "ustaad new h lo isse",
		img: "{% static 'images/products/product-1.jpg' %}",
	},
];

let generateShop = () => {
	return (shop.innerHTML = shopItemsData.map((x) => {
		return `
		<div class="col-4">
    	<img src="{% static 'images/products/product-1.jpg' %}">
   		<h4>Red Printed T-shirt</h4>
 		<p>Rs. 1000</p>
    	<button class="update-cart">Add to Cart</button>
    	</div>
		`;
	 }).join(""));
};

generateShop();
from django.shortcuts import render,redirect
from django.views import view


# Create your views here.

class Home(View):

	def get(self,request):
		cart = request.session.get('cart')
		categories = Category.getAllCategory()
		products = Product.getAllProduct().order_by('-id')

		if request.GET.get('id'):
			filterProductById = Product.objects.get(id=int(request.GET.get('id')))
			return render(request, 'productDetail.html',{"product":filterProductById,"categories":categories})

		if not cart:
			request.session['cart'] = {}

		if request.GET.get('category_id'):
			filterProduct = Product.getProductByFilter(request.GET['category_id'])
			return render(request, 'home.html',{"products":filterProduct,"categories":categories})

		return render(request, 'home.html',{"products":products,"categories":categories})

	def post(self,request):
		product = request.POST.get('product')

		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		print(cart)
		request.session['cart'] = cart
		return redirect('cart')


class OrderView(View):
	def get(self,request):
		customer_id = request.session.get('customer')
		orders = Order.objects.filter(customer=customer_id).order_by("-date").order_by("-id")
		print(orders)
		return render(request,'order.html',{"orders":orders})


class Checkout(View):
	def get(self,request):
		return redirect('cart')
	
	def post(self,request):
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		cart = request.session.get('cart')
		products = Product.getProductById(list(cart.keys()))
		customer = request.session.get('customer')
		print(address,phone,cart,products,customer)

		for product in products:
			newOrder = Order(
					product=product,
					customer=Customer(id=customer),
					quantity=cart[str(product.id)],
					price=product.price,
					address=address,
					phone=phone,
				)
			newOrder.save()

		request.session['cart'] = {}
		return redirect('order')


class Cart(View):
	def get(self,request):
		productList = list(request.session.get('cart').keys())
		if request.GET.get('increase'):
			pId = request.GET.get('increase')
			products = request.session.get('cart')
			products[pId] += 1
			request.session['cart'] = products

		if request.GET.get('decrease'):
			pId = request.GET.get('decrease')
			products = request.session.get('cart')
			print(products[pId])
			if products[pId] > 1:
				products[pId] -= 1
				request.session['cart'] = products
				productList = list(request.session.get('cart').keys())
			else :
				del products[pId]
				request.session['cart'] = products
				productList = list(request.session.get('cart').keys())
				

		allProduct = Product.getProductById(productList)
		return render(request,'cart.html',{"allProduct":allProduct})		
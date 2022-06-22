from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Category, Order, OrderItem


def home(request):
    return render(request, 'index.html', context={'name': "Ali", })


def shop(request):
    # product = Product.objects.get(pk=1)
    # product = Product.objects.filter(pk=1).first()
    # query_set = Product.objects.filter(unit_price__range=(20, 30))

    # Q object
    # query_set = Product.objects.filter(Q(title__icontains='coffee') | Q(title__icontains='wine'))
    # query_set = Product.objects.filter(~Q(title__icontains='wine'))

    # F object
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.filter()
    # query_set = Product.objects.filter(~Q(title__icontains='wine'))

    # filter ex
    # query_set = Product.objects.filter(title__icontains='coffee')
    # query_set = Product.objects.filter(title__istartswith='coffee ')
    # query_set = Product.objects.filter(description__isnull=True)
    # query_set = Product.objects.filter(last_update__year=2020)

    # sorting ex
    query_set = Product.objects.order_by('-title')

    # limiting results
    query_set = Product.objects.all()[5:10]

    # select some columns [return dict]
    # query_set = Product.objects.values('title', 'unit_price')  # [return dict]
    # query_set = Product.objects.values_list('title', 'unit_price')  # [return tuple]

    # Categories that don’t have a featured product
    # I can also call featured_product_id__isnull cuz this is ForeignKey
    # query_set = Category.objects.filter(featured_product__isnull=True)

    # Products with low inventory (less than 10)
    # query_set = Product.objects.filter(inventory__lt=10)

    # Orders placed by customer with id = 1
    # I can also call customer_id cuz this is ForeignKey
    # query_set = Order.objects.filter(customer=1)

    # Order items for products in category 3
    # my bad solution
    # category_3_products = list(map(lambda record: record.id, Product.objects.filter(category_id=3)))
    # solution [also product__category_id works]
    # query_set = OrderItem.objects.filter(product__category=3)

    # select all products that ordered + sort by title
    # query_set = Product.objects.filter(
    #     id__in=OrderItem.objects.values_list('product').distinct()
    # ).order_by('title')

    # selecting related objects
    query_set = Product.objects.select_related('category').prefetch_related('promotions').all()

    # get last 5 orders with their customer  and items
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'shop.html', context={'products': list(query_set)})


def customers(request):
    # Customers with .com accounts
    query_set = Customer.objects.filter(email__iendswith='.com')
    return render(request, 'customers.html', context={'customers': list(query_set)})

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
             cart = self.session['cart'] = {}
        self.cart = cart

    def clear(self):
        self.session['cart']={}
        self.save()

    def get_total_price(self):
        return sum(float(item['price']) * int(item['quantity']) for item in self.cart.values())

    def save(self):
        self.session.modified = True

    def add(self,id,product):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        self.save()

    def get_items(self):
        items=[]
        for product_id,details in self.cart.items():
            items.append({
                'id': product_id,
                'quantity': details['quantity'],
                'price': float(details['price'])
            })
        return items
        
    def remove(self,id,product):
        product_id = str(product.id)
        #print(product.id)
        if product_id in self.cart.keys():
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] - 1
            #print(self.cart[product_id]['quantity'])
        if self.cart[product_id]['quantity'] == 0:
            del self.cart[product_id]
        self.save()

    


from printful import Printful
import json

KEY = '65g4bdvh-93ov-nqzs:gnh1-myo5jz3yv6ak'

pf = Printful(KEY)

products = pf.get('store/products')
variants = pf.get('products/variants/185768984')

print(variants)

with open("data.json", "w") as write_file:
    json.dump(products, write_file)

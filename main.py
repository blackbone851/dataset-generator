import pandas as pd
import numpy as np
import random, json
from datetime import datetime


with open('files/products.json', 'r') as f:
    products = json.load(f)
with open('files/payment_met.json', 'r') as f:
    payment_met = json.load(f)
with open('files/cities_weights.json', 'r') as f:
    locations = json.load(f)
with open('files/cities_customers.json', 'r') as f:
    customers = json.load(f)

dates_range = pd.date_range(start=datetime(2019, 1, 1, 1, 1, 1), end=datetime(2025, 1, 1, 1, 1, 1), freq='D')
years = list(set([i.year for i in dates_range]))
years = {key: round(random.uniform(0.01, 0.09), 4) for key in years}
years[2019] = 0

to_dataframe = []
for i in range(100000):
    hour = np.random.randint(0, 24)
    minute = np.random.randint(0, 60)
    second = np.random.randint(0, 60)
    order_date = pd.to_datetime(random.choice(dates_range)).replace(hour=hour, minute=minute, second=second)
    payment = random.choices(list(payment_met.keys()), weights=payment_met.values(), k=1)[0]
    city = random.choices(list(locations.keys()), weights=locations.values(), k=1)[0]
    customer = random.choices(customers[city], k=1)[0]
    details = []
    for j in range(1, random.randint(1, 7)):
        cat = np.random.randint(0, 7)
        prod = np.random.randint(0, len(products[0]['ecommerce']['categories'][cat]['products']))
        category = products[0]['ecommerce']['categories'][cat]['name']
        product = products[0]['ecommerce']['categories'][cat]['products'][prod]['name']
        years_list = {k: v for k, v in years.items() if k <= order_date.year}
        price = products[0]['ecommerce']['categories'][cat]['products'][prod]['price']
        quantity = np.random.randint(1, 5)
        total = quantity * price
        new_price = price
        for rate in years_list.values():
            new_price *= (1 + rate)
        promotion = random.choices(['Yes', 'No'], weights=[0.2, 0.8], k=1)[0]
        if promotion == 'Yes':
            discount = round(random.uniform(0.05, 0.5), 2)
            total = round(total - (total * discount),2)
        else:
            discount = 0
        details.append({
            'category': category,
            'product': product,
            'price': round(new_price, 2),
            'quantity': quantity,
            'total': round(total, 2),
            'promotion': promotion,
            'discount': discount
        })        
    # order_date = str(order_date)
    data = {
        'customer_id': customer,
        'order_date': order_date,
        'details': details,
        'city': city,
        'payment_method': payment
    }
    to_dataframe.append(data)

df = pd.json_normalize(to_dataframe,
                       record_path='details',
                       meta=['customer_id', 'order_date', 'city', 'payment_method']).sort_values('order_date').reset_index(drop=True)

df['year'] = df['order_date'].dt.year
df['order_id'] = df.groupby(['order_date', 'year']).ngroup() + 1
df['order_id'] = df.groupby('year')['order_id'].rank(method='dense').astype(int)
df['order_id'] = df.apply(lambda row: 'O' + str(row['year'])[-2:] + str(row['order_id']).zfill(4), axis=1)
df = df[['order_id', 'customer_id', 'order_date', 'category', 'product', 'price', 'quantity', 'total', 'promotion', 'discount', 'city', 'payment_method']]
print(len(df))
df.to_csv('files/ecommerce_data.csv', index=False)

# save to_dataframe in a json file
# with open('files/ecommerce_data.json', 'w') as f:
#     json.dump(to_dataframe, f, indent=4)
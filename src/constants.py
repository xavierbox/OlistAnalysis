KNOWN_DATE_COLUMNS = [
    "shipping_limit_date",
    "review_creation_date",
    "review_answer_timestamp",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

date_format = "%Y/%m/%d"

base_url = './data/'
config = {
    'date_format' : "%Y/%m/%d",
    'base_url': './data/',
    'customers':'olist_customers_dataset.csv',
    'geolocation':'olist_geolocation_dataset.csv',
    'order_items':'olist_order_items_dataset.csv',
    
    'order_payments':'olist_order_payments_dataset.csv',
    'order_reviews':'olist_order_reviews_dataset.csv',
    'orders':'olist_orders_dataset.csv',
    
    'products':'olist_products_dataset.csv',
    'sellers':'olist_sellers_dataset.csv',
    'product_category_english': 'product_category_name_english.csv'

}

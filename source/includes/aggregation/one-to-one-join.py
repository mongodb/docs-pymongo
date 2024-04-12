from pymongo import MongoClient

uri = "<connection string>"
client = MongoClient(uri)

try:
    agg_db = client["agg_tutorials_db"]

    # start-colls
    orders_coll = agg_db["orders"]
    products_coll = agg_db["products"]
    # end-colls

    # start-insert-orders
    orders_coll.delete_many({})

    order_data = [
        {
            "customer_id": "elise_smith@myemail.com",
            "orderdate": datetime.datetime("2020-05-30T08:35:52Z"),
            "product_id": "a1b2c3d4",
            "value": 431.43,
        },
        {
            "customer_id": "tj@wheresmyemail.com",
            "orderdate": datetime.datetime("2019-05-28T19:13:32Z"),
            "product_id": "z9y8x7w6",
            "value": 5.01,
        },
        {
            "customer_id": "oranieri@warmmail.com",
            "orderdate": datetime.datetime("2020-01-01T08:25:37Z"),
            "product_id": "ff11gg22hh33",
            "value": 63.13,
        },
        {
            "customer_id": "jjones@tepidmail.com",
            "orderdate": datetime.datetime("2020-12-26T08:55:46Z"),
            "product_id": "a1b2c3d4",
            "value": 429.65,
        }
    ]

    orders_coll.insert_many(order_data)
    # end-insert-orders

    # start-insert-products
    products_coll.delete_many({})

    product_data = [
        {
            "id": "a1b2c3d4",
            "name": "Asus Laptop",
            "category": "ELECTRONICS",
            "description": "Good value laptop for students",
        },
        {
            "id": "z9y8x7w6",
            "name": "The Day Of The Triffids",
            "category": "BOOKS",
            "description": "Classic post-apocalyptic novel",
        },
        {
            "id": "ff11gg22hh33",
            "name": "Morphy Richardds Food Mixer",
            "category": "KITCHENWARE",
            "description": "Luxury mixer turning good cakes into great",
        },
        {
            "id": "pqr678st",
            "name": "Karcher Hose Set",
            "category": "GARDEN",
            "description": "Hose + nosels + winder for tidy storage",
        }
    ]

    products_coll.insert_many(product_data)
    # end-insert-products

    pipeline = []

    # start-match
    pipeline.append({"$match": {
        "orderdate": {
            "$gte": datetime.datetime("2020-01-01T00:00:00Z"),
            "$lt": datetime.datetime("2021-01-01T00:00:00Z")
        }
    }
    })
    # end-match

    # start-lookup
    pipeline.append({"$lookup": {
        "from": "products",
        "localField": "product_id",
        "foreignField": "id",
        "as": "product_mapping",
    }
    })
    # end-lookup

    # start-set
    pipeline.append(
        {"$set": {
            "product_mapping": {"$first": "$product_mapping"},
        },
        },
        {"$set": {
            "product_name": "$product_mapping.name",
            "product_category": "$product_mapping.category",
        }
        }
    )
    # end-set

    # start-unset
    pipeline.append({"$unset": ["_id", "product_id", "product_mapping"]})
    # end-unset

    # start-run-agg
    aggregation_result = orders_coll.aggregate(pipeline)
    # end-run-agg

    for document in aggregation_result:
        print(document)

finally:
    client.close()

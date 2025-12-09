def decode_mongo(data):
    decode = list(data.as_pymongo())
    
    for item in decode:
        item['_id'] = str(item['_id'])
        
    return decode
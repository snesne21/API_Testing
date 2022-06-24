def search_created_sku_in(items, unique_sku):
    return [item for item in items if item['sku'] == unique_sku]

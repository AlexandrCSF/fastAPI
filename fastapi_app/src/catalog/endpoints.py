from main import app


@app.get("products/{product_id}")
async def get_product_card():
    pass

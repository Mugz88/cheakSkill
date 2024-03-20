from pyspark.sql.functions import col, lit

def get_product_category_pairs(df):
    # Создаем датафрейм с парами "Имя продукта - Имя категории"
    product_category_pairs = df.select("product_name", "category_name")

    # Создаем датафрейм с продуктами, у которых нет категорий
    products_without_category = df.filter(col("category_name").isNull()).select("product_name")
    products_without_category = products_without_category.withColumn("category_name", lit("No Category"))

    # Объединяем оба датафрейма
    result_df = product_category_pairs.union(products_without_category)

    return result_df
from pyspark.sql import DataFrame as df
from pyspark.sql import SparkSession


def get_pairs_with_sql(p: df, c: df, r: df, session: SparkSession) -> df:
    """ Метод возвращает набор пар продукт-категория (Реализация через sql).

    :param p: Продукты
    :param c: Категории
    :param r: Связь между продуктами и категориями.
    :param session: Сессия Спарк
    :return: ДатаФрейм пар "Продукт - Категория"
    """

    # создание sql-view
    p.createTempView('db_products')
    c.createTempView('db_categories')
    r.createTempView('db_relations')

    # Присоединение к ДатаФрейму связей ДатаФрейма категорий
    joined = session.sql("SELECT prId, category "
                       "FROM db_relations LEFT JOIN db_categories "
                       "ON db_relations.catId = db_categories.catId")
    joined.createTempView('db_product_category')

    # Присоединение к ДатаФрейму продуктов, предыдущего ДатаФрейма
    joined = session.sql("SELECT product, category "
                       "FROM db_products LEFT JOIN db_product_category "
                       "ON db_products.prId == db_product_category.prId")

    return joined


def get_pairs_with_join(p: df, c: df, r: df) -> df:
    """ Метод возвращает набор пар 'Продукт-Категория' (реализация через join)

    :param p: Продукты
    :param c: Категории
    :param r: Связь между продуктами и категориями.
    :return: ДатаФрейм пар "Продукт - Категория"
    """
    # Объединение таблицы продуктов и связей
    joined = p.join(r, 'prId', 'left')
    # Добавление таблицы категорий.
    joined = joined.join(c, 'catId', 'left').select('product', 'category')
    return joined


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()
    # Датафрейм "Идентификатор продукта - Название продукта"
    products: df = spark.read.csv('products.csv', header=True)
    # Дата фрейм "Идентификатор категории - название категории"
    categories: df = spark.read.csv('category.csv', header=True)
    # Дата фрейм связей вида "Идентификатор продукта - Идентификатор Категории" (Утюг не имеет категории)
    relations: df = spark.read.csv('relation.csv', header=True)

    get_pairs_with_sql(products, categories, relations, spark).show()
    get_pairs_with_join(products, categories, relations).show()

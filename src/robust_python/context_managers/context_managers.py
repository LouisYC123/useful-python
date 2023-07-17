# %%
import pandas as pd
from contextlib import contextmanager


@dataclass(frozen=True)
class Material:
    name: str
    strength_rating: int
    texture: str


@dataclass
class _ProductList:
    name: str
    materials: list[Material]
    price_in_cents: int


@contextmanager
def create_product_list(order: Order, inventory: Inventory):
    product_list = _ProductList(order, inventory)
    try:
        yield product_list
    finally: # We return here when the below <with> block exits
        if product_list.has_reserved_items():
            product_list.unreserve_items()

# which can be used as follows:

if order.is_confirmed():
    product_inventory = get_product_inventory()
    with create_product_list(order, product_inventory) as product_list:
        product_list.reserve_items_from_stores()
        wait_for_user_product_confirmation(product_list)
        product_list.order_and_unreserve_items()
        deliver_ingredients(product_list)

"""
In the above example, the yielded value becomes product_list. When the <with> block exits, 
execution is returned to the context manager, right after the yield statement.
It doesn't matter if an exception is thrown, or if the with block finishes normally; 
because I wrapped our yield in a try...finally block, the product list will always
clear any reserved items. This is how you can effectively force a user to clean up
after themselves.

You are eliminating an entire class of errors that can happen when you use context 
managers—the errors of omission. Errors of omission are so easy to make; you literally 
have to do nothing. Instead, a context manager lets users do the right thing, even when 
they do nothing.

The interfaces you build should be easy to use correctly and hard to use incorrectly.

"""


"""
Heres another example

This code ensures the dataframe is deleted when finished with
"""
@contextmanager
def dataframe_loader(file_path):
    dataframe = pd.read_csv(file_path)
    try:
        yield dataframe
    finally:
        del dataframe

# Usage example
file_path = 'data.csv'

with dataframe_loader(file_path) as df:
    # Perform dataframe operations
    processed_df = df.dropna()
    aggregated_df = processed_df.groupby('category').sum()
    # Use the processed and aggregated dataframe for further analysis


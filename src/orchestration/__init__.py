from invoke import Collection

from orchestration import jaffle_shop

ns = Collection("orchestration")
ns.add_collection(jaffle_shop, "jaffle_shop")

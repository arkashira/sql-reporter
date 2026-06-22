import argparse
from src.data_warehouse import DataWarehouseManager
from src.oauth import OAuthManager

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--warehouse", help="Data warehouse name")
    parser.add_argument("--credentials", help="Data warehouse credentials")
    args = parser.parse_args()

    data_warehouse_manager = DataWarehouseManager()
    oauth_manager = OAuthManager()

    if args.warehouse and args.credentials:
        warehouse = DataWarehouse(args.warehouse, json.loads(args.credentials))
        data_warehouse_manager.add_warehouse(warehouse)
        token = oauth_manager.authenticate(warehouse.credentials["client_id"], warehouse.credentials["client_secret"])
        data_warehouse_manager.store_token(warehouse.name, token)
        print(data_warehouse_manager.get_connection_status(warehouse.name))

if __name__ == "__main__":
    main()

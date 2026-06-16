from datetime import datetime
import pandas as pd

data = [
    {"shipment_id": 1, "status": "DELIVERED"},
    {"shipment_id": 2, "status": "IN_TRANSIT"},
    {"shipment_id": 3, "status": "CREATED"},
]

df = pd.DataFrame(data)

filename = f"/tmp/shipments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

df.to_csv(filename, index=False)

print(f"Export completed: {filename}")
print(df.head())
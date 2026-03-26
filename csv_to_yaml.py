import yaml
import json
import pandas as pd
from pathlib import Path

# load the csv
df = pd.read_csv('<YOUR_FILE>.csv')

with open('config.json') as f:
    config = json.loads(f)

output_dir = Path(config['output_path'])
output_dir.mkdir(exist_ok=True)

# create the yaml file based on the Boltz2 schema
for _, row in df.iterrows():
    yaml_data = {
        "sequence": [
            {
                "protein": {
                    "id": "A",
                    "sequence": row['sequence']
                }
            },
            {
                "ligand": {
                    "id": "L",
                    "smiles": row['smiles']
                }
            }
        ],
        "version": 1
    }

    filename = f"{row['pdb_id']}_{row['ligand'].replace(' ', '_')}.yaml"
    with open(output_dir / filename, 'w') as f:
        yaml.dump(yaml_data, f, sort_keys=False)


print("ALL YAML FILES CREATED SUCCESSFULLY!")

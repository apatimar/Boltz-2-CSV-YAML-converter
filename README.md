# Boltz-2 YAML Generator from CSV

Generates Boltz-2 input YAML files from a CSV. Built to work with AF3-style CSV exports.

---

## Prerequisites
```bash
pip install pyyaml pandas
```

## Configuration

Edit the `config.json` in the same directory:
```json
{
    "output_path": "/path/to/output/yaml/directory"
}
```

## CSV Format

Required columns: `pdb_id`, `ligand`, `sequence` (protein, single-letter), `smiles`.
```csv
pdb_id,ligand,sequence,smiles
1ABC,ATP,MKTAYIAKQRQISFVK...,C1=NC2=C(N1)C(=O)N...
```

## Usage

1. Edit the script to point to your CSV: `df = pd.read_csv('your_file.csv')`
2. Run: `python generate_yamls.py`

Output files are named `<pdb_id>_<ligand>.yaml` and written to `output_path`.


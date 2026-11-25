"""Execute the analysis and model-preparation notebooks in separate fresh kernels."""

import argparse
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--data-dir', type=Path, default=root,
        help='Directory containing BankChurners.csv; generated CSV/SQLite files go here.',
    )
    parser.add_argument(
        '--output-dir', type=Path, default=root / 'artifacts' / 'executed_notebooks',
        help='Directory for executed notebook copies; source notebooks are preserved.',
    )
    args = parser.parse_args()
    data_dir = args.data_dir.resolve()
    output_dir = args.output_dir.resolve()
    if not (data_dir / 'BankChurners.csv').is_file():
        parser.error(
            'BankChurners.csv is missing. Download it from the Kaggle source linked '
            'in README.md and place it in --data-dir.'
        )
    output_dir.mkdir(parents=True, exist_ok=True)

    for filename in ['01_data_analysis.ipynb', '02_model_training.ipynb']:
        notebook = nbformat.read(root / filename, as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == 'code':
                cell.outputs = []
                cell.execution_count = None
        print(f'Running {filename}', flush=True)
        NotebookClient(
            notebook,
            timeout=180,
            kernel_name='python3',
            resources={'metadata': {'path': str(data_dir)}},
        ).execute()
        nbformat.write(notebook, output_dir / filename)
        print(f'Saved {output_dir / filename}', flush=True)

    print(f'Prepared CSV: {data_dir / "bank_churn_prepared.csv"}')
    print(f'SQLite database: {data_dir / "customer_churn.db"}')
    print('Both notebooks completed. Model training remains a separate next step.')


if __name__ == '__main__':
    main()

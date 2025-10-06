"""pandas_assignment.py
Simple script that shows basic pandas steps.
Edit the 'YOUR_FULL_NAME' placeholder with your name.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print('pandas version:', pd.__version__)

    # Small DataFrame with personal info (edit these entries)
    my_info = pd.DataFrame({
        'Name': ['YOUR_FULL_NAME', 'Friend A', 'Friend B'],
        'Age': [25, 30, 40],
        'Sex': ['female', 'male', 'female'],
    })
    print('\nMy DataFrame:')
    print(my_info)

    ages = my_info['Age']
    print('\nMax age:', ages.max())
    print('\nDescribe numeric columns:')
    print(my_info.describe())

    # Read the titanic CSV
    csv_path = os.path.join('data', 'titanic.csv')
    if not os.path.exists(csv_path):
        print(f"CSV not found at {csv_path}. Make sure data/titanic.csv exists.")
        return

    titanic = pd.read_csv(csv_path)
    print('\nTitanic shape:', titanic.shape)
    print(titanic.head())

    # Filter example
    older_30 = titanic[titanic['Age'] > 30]
    print('\nPassengers older than 30:', older_30.shape[0])

    # Save outputs
    os.makedirs('outputs', exist_ok=True)
    out_path = os.path.join('outputs', 'titanic_older_30.csv')
    older_30.to_csv(out_path, index=False)
    print('Saved', out_path)

    # Quick plot (may open a window when run locally)
    try:
        ax = titanic['Age'].plot(kind='hist', bins=8, title='Age distribution')
        ax.set_xlabel('Age')
        plt.tight_layout()
        plt.show()
    except Exception:
        # If running on a machine without a display, plotting may fail.
        print('Plotting skipped or failed (no display available)')


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('tests.csv')

plt.plot(df['n'], df['binary_tree'], label='Balanced Binary Tree')
plt.plot(df['n'], df['hash_table'], label='Hash Table')

plt.title('Dictionary Insertion Times: Balanced Binary Tree vs Hash Table')
plt.xlabel('Array Size (n)')
plt.ylabel('Time to Insert (milliseconds)')
plt.legend()

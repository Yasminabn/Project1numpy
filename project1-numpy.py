import numpy as np

# 1. Create Expression Data Matrix (4 samples x 3 genes)
# Rows: Sample 1 to 4 | Columns: Gene A, Gene B, Gene C
expression_data = np.array([
    [12.5, 45.0, 8.2],
    [3.1,  88.4, 15.6],
    [22.0, 10.1, 5.0],
    [18.4, 62.3, 41.0]
])

# 2. Basic Matrix Info
print("Matrix Shape:", expression_data.shape)

# 3. Statistical Analysis per Gene (Columns -> axis=0)
mean_per_gene = np.mean(expression_data, axis=0)
print("Mean per gene [Gene A, Gene B, Gene C]:")
print(mean_per_gene)

# 4. Extracting Specific Data (Gene B -> Column index 1)
gene_b_data = expression_data[:, 1]
print("Gene B values:", gene_b_data)

# 5. Filtering (Values greater than 20.0)
high_expression = expression_data[expression_data > 20.0]
print("High expression values (>20):")
print(high_expression)
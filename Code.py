import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Define population size
n = 40000

# Define possible age groups and corresponding weights
age_groups = [20, 30, 40, 50, 60, 70]

# Define purchase probabilities by age group (weighted)
purchase_probs = {
    20: 0.10,
    30: 0.20,
    40: 0.30,
    50: 0.40,
    60: 0.50,
    70: 0.60
}

# Randomly assign ages
ages = np.random.choice(age_groups, size=n, replace=True)

# Generate purchases using age-specific probabilities (weighted model)
purchases = [np.random.rand() < purchase_probs[age] for age in ages]

# Create DataFrame
df_weighted = pd.DataFrame({
    'age': ages,
    'purchased': purchases
})

# Simulate uniform purchase model (same probability for all)
uniform_prob = df_weighted['purchased'].mean()
df_weighted['uniform_purchased'] = np.random.rand(n) < uniform_prob

# Aggregate purchase probabilities by age
weighted_grouped = df_weighted.groupby('age')['purchased'].mean().reset_index(name='weighted_prob')
uniform_grouped = df_weighted.groupby('age')['uniform_purchased'].mean().reset_index(name='uniform_prob')
comparison_df = pd.merge(weighted_grouped, uniform_grouped, on='age')

# Plotting comparison
plt.figure(figsize=(10, 6))
sns.lineplot(x='age', y='weighted_prob', data=comparison_df, marker='o', label='Weighted Model')
sns.lineplot(x='age', y='uniform_prob', data=comparison_df, marker='s', linestyle='--', label='Uniform Model')
plt.title('Purchase Probability by Age Group: Weighted vs Uniform Models')
plt.xlabel('Age')
plt.ylabel('Purchase Probability')
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Print key conditional probabilities
weighted_70 = comparison_df[comparison_df['age'] == 70]['weighted_prob'].values[0]
uniform_70 = comparison_df[comparison_df['age'] == 70]['uniform_prob'].values[0]
print(f"Weighted P(Purchase | Age = 70): {weighted_70:.2%}")
print(f"Uniform P(Purchase | Age = 70): {uniform_70:.2%}")



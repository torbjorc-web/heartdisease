# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency

# load data
heart = pd.read_csv('heart_disease.csv')

# TASK 1: Inspect the Data
print(heart.head())

# TASK 2: Box plot of thalach by heart disease
sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.xlabel("Heart Disease")
plt.ylabel("Maximum Heart Rate (thalach)")
plt.title("Maximum Heart Rate by Heart Disease Diagnosis")
plt.show()

# TASK 3: Save thalach values for patients with and without heart disease
thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

# TASK 4: Calculate mean and median differences
mean_hd = thalach_hd.mean()
mean_no_hd = thalach_no_hd.mean()
mean_diff = mean_hd - mean_no_hd
print(f"Mean difference: {mean_diff}")

median_hd = thalach_hd.median()
median_no_hd = thalach_no_hd.median()
median_diff = median_hd - median_no_hd
print(f"Median difference: {median_diff}")

# TASK 5: Import the statistical test (t-test for two independent samples)
# Using ttest_ind from scipy.stats

# TASK 6: Run the hypothesis test
t_stat, p_value = ttest_ind(thalach_hd, thalach_no_hd)
print(f"p-value: {p_value}")
if p_value < 0.05:
    print("Yes, there is a significant difference in average thalach")
else:
    print("No, there is not a significant difference in average thalach")

# TASK 7: Investigate another quantitative variable (age)
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.xlabel("Heart Disease")
plt.ylabel("Age")
plt.title("Age by Heart Disease Diagnosis")
plt.show()

age_hd = heart.age[heart.heart_disease == 'presence']
age_no_hd = heart.age[heart.heart_disease == 'absence']
t_stat_age, p_value_age = ttest_ind(age_hd, age_no_hd)
print(f"p-value for age: {p_value_age}")

# Also check cholesterol (chol)
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.chol)
plt.xlabel("Heart Disease")
plt.ylabel("Cholesterol (mg/dl)")
plt.title("Cholesterol by Heart Disease Diagnosis")
plt.show()

chol_hd = heart.chol[heart.heart_disease == 'presence']
chol_no_hd = heart.chol[heart.heart_disease == 'absence']
t_stat_chol, p_value_chol = ttest_ind(chol_hd, chol_no_hd)
print(f"p-value for cholesterol: {p_value_chol}")

# TASK 8: Box plots of thalach by chest pain type
plt.clf()
sns.boxplot(x=heart.cp, y=heart.thalach)
plt.xlabel("Chest Pain Type")
plt.ylabel("Maximum Heart Rate (thalach)")
plt.title("Maximum Heart Rate by Chest Pain Type")
plt.xticks(rotation=45)
plt.show()

# TASK 9: Save thalach values for each chest pain type
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

# TASK 10: ANOVA test for multiple groups
f_stat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print(f"p-value: {pval}")
if pval < 0.05:
    print("Yes, there is at least one pair of chest pain categories with significantly different thalach")
else:
    print("No, there is no significant difference among chest pain types")

# TASK 11: Pairwise t-tests with Bonferroni correction
bonferroni_alpha = 0.05 / 6

# typical vs atypical
t1, p1 = ttest_ind(thalach_typical, thalach_atypical)
print(f"typical vs atypical: p-value = {p1}, Significant = {p1 < bonferroni_alpha}")

# typical vs non-anginal
t2, p2 = ttest_ind(thalach_typical, thalach_nonangin)
print(f"typical vs non-anginal: p-value = {p2}, Significant = {p2 < bonferroni_alpha}")

# typical vs asymptomatic
t3, p3 = ttest_ind(thalach_typical, thalach_asymptom)
print(f"typical vs asymptomatic: p-value = {p3}, Significant = {p3 < bonferroni_alpha}")

# atypical vs non-anginal
t4, p4 = ttest_ind(thalach_atypical, thalach_nonangin)
print(f"atypical vs non-anginal: p-value = {p4}, Significant = {p4 < bonferroni_alpha}")

# atypical vs asymptomatic
t5, p5 = ttest_ind(thalach_atypical, thalach_asymptom)
print(f"atypical vs asymptomatic: p-value = {p5}, Significant = {p5 < bonferroni_alpha}")

# non-anginal vs asymptomatic
t6, p6 = ttest_ind(thalach_nonangin, thalach_asymptom)
print(f"non-anginal vs asymptomatic: p-value = {p6}, Significant = {p6 < bonferroni_alpha}")

# TASK 12: Contingency table of cp and heart_disease
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

# TASK 13: Chi-square test for association
chi2, pval_chi, dof, expected = chi2_contingency(Xtab)
print(f"p-value: {pval_chi}")
if pval_chi < 0.05:
    print("Yes, there is a significant association between chest pain type and heart disease")
else:
    print("No, there is no significant association between chest pain type and heart disease")

# TASK 14: Further Exploration - Test other variables
# Test sex (categorical - use chi-square)
sex_table = pd.crosstab(heart.sex, heart.heart_disease)
chi2_sex, p_sex, _, _ = chi2_contingency(sex_table)
print(f"Sex p-value: {p_sex}")

# Test exang (categorical - use chi-square)
exang_table = pd.crosstab(heart.exang, heart.heart_disease)
chi2_exang, p_exang, _, _ = chi2_contingency(exang_table)
print(f"Exercise-induced angina (exang) p-value: {p_exang}")

# Test trestbps (quantitative - use t-test)
trestbps_hd = heart.trestbps[heart.heart_disease == 'presence']
trestbps_no_hd = heart.trestbps[heart.heart_disease == 'absence']
t_stat_trest, p_val_trest = ttest_ind(trestbps_hd, trestbps_no_hd)
print(f"Resting blood pressure (trestbps) p-value: {p_val_trest}")

# Heart Disease Research Part II

## Project Description

This project analyzes a heart disease dataset from the UCI Machine Learning Repository. The dataset contains patient information such as age, sex, cholesterol, resting blood pressure, chest pain type, and maximum heart rate achieved during exercise.

The goal of the project is to investigate whether certain variables are associated with heart disease. In particular, this project explores:
- The relationship between maximum heart rate (`thalach`) and heart disease.
- The relationship between chest pain type (`cp`) and maximum heart rate.
- The relationship between chest pain type (`cp`) and heart disease.

The project uses data visualization and hypothesis testing to determine whether differences between groups are statistically significant.

## Variables in the Dataset

- `age`: Age in years.
- `sex`: Sex assigned at birth.
- `trestbps`: Resting blood pressure in mm Hg.
- `chol`: Serum cholesterol in mg/dl.
- `cp`: Chest pain type.
- `exang`: Exercise-induced angina.
- `fbs`: Fasting blood sugar > 120 mg/dl.
- `thalach`: Maximum heart rate achieved during exercise.
- `heart_disease`: Whether the patient was diagnosed with heart disease.

## Hypothesis Tests Used

- **Two-sample t-test**: Used to compare the average value of a quantitative variable between two groups.
- **ANOVA**: Used to compare the average value of a quantitative variable across more than two groups.
- **Chi-square test**: Used to test whether two categorical variables are associated.

## How to Understand P-Values

A p-value tells you how likely it is to see the results you got, or something more extreme, if the null hypothesis were true.

### Interpreting p-values
- **Small p-value (less than 0.05)**: The result is statistically significant. This means the observed difference or association is unlikely to be due to random chance alone, so we reject the null hypothesis.
- **Large p-value (0.05 or greater)**: The result is not statistically significant. This means there is not enough evidence to reject the null hypothesis.

### Example
If you compare `thalach` for patients with and without heart disease and get a p-value of 0.01, that means there is strong evidence that the average maximum heart rate is different between the two groups.

If the p-value is 0.40, then the difference you see could easily have happened by chance, so you would not conclude that the groups are different.

## Conclusion

This project shows how statistics can be used to explore possible predictors of heart disease. By combining box plots, hypothesis tests, and contingency tables, we can better understand which variables may be associated with heart disease.

## Files
- `script.py`: Main analysis code.
- `heart_disease.csv`: Dataset used for the analysis.
- `README.md`: Project overview and explanation of results.

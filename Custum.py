import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
a=pd.read_csv("Customer-Churn.csv")
print(a.isnull().sum())
print(a.duplicated().sum())
print(a.info())
print(a["TotalCharges"].dtype)
print(a["TotalCharges"].unique())
a["TotalCharges"] = pd.to_numeric(a["TotalCharges"],errors="coerce")
print(a["TotalCharges"].dtype)
print(a["TotalCharges"].unique())
print(a["gender"].dtype)
print(a["gender"].unique())
print(a["SeniorCitizen"].dtype)
print(a["SeniorCitizen"].unique())
print(a["Partner"].dtype)
print(a["Partner"].unique())
print(a["Dependents"].dtype)
print(a["Dependents"].unique())
print(a["tenure"].dtype)
print(a["tenure"].unique())
print(a["PhoneService"].dtype)
print(a["PhoneService"].unique())
print(a["MultipleLines"].dtype)
print(a["MultipleLines"].unique())
print(a["InternetService"].dtype)
print(a["InternetService"].unique())
print(a["OnlineSecurity"].dtype)
print(a["OnlineSecurity"].unique())
print(a["OnlineBackup"].dtype)
print(a["OnlineBackup"].unique())
print(a["DeviceProtection"].dtype)
print(a["DeviceProtection"].unique())
print(a["TechSupport"].dtype)
print(a["TechSupport"].unique())
print(a["StreamingTV"].dtype)
print(a["StreamingTV"].unique())
print(a["StreamingMovies"].dtype)
print(a["StreamingMovies"].unique())
print(a["Contract"].dtype)
print(a["Contract"].unique())
print(a["PaperlessBilling"].dtype)
print(a["PaperlessBilling"].unique())
print(a["PaymentMethod"].dtype)
print(a["PaymentMethod"].unique())
print(a["MonthlyCharges"].dtype)
print(a["MonthlyCharges"].unique())
print(a.isnull().sum())

print(a["Churn"].value_counts())
print(a["gender"].value_counts())
print(a["SeniorCitizen"].value_counts())
print(a["Partner"].value_counts())
print(a["Dependents"].value_counts())
print(a["PhoneService"].value_counts())
print(a["MultipleLines"].value_counts())
print(a["InternetService"].value_counts())
print(a["OnlineSecurity"].value_counts())
print(a["OnlineBackup"].value_counts())
print(a["DeviceProtection"].value_counts())
print(a["TechSupport"].value_counts())
print(a["StreamingTV"].value_counts())
print(a["StreamingMovies"].value_counts())
print(a["Contract"].value_counts())
print(a["PaperlessBilling"].value_counts())
print(a["PaymentMethod"].value_counts())
print(a["Churn"].value_counts(normalize=True))
print(a["Churn"].value_counts(normalize=True)*100)
print(pd.crosstab(
    a["Contract"],
    a["Churn"]
))
print(pd.crosstab(
    a["InternetService"],
    a["Churn"]
))
print(pd.crosstab(
    a["PaymentMethod"],
    a["Churn"]
))

sns.boxplot(x="Churn",y="TotalCharges",data=a)
plt.title("Customer Churn by Total Charges")
plt.show()

sns.boxplot(x="Contract",y="Churn",data=a)
plt.title("Customer Churn by Contract Type")
plt.show()

sns.countplot(x="Churn" ,data=a)
plt.title("Customer Churn Count")
plt.show()
sns.countplot(
    x="Contract",
    hue="Churn",
    data=a

)
plt.title("Customer Churn by Contract Type")
plt.show()
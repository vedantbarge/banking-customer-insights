import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

try:
    print("Connecting to MySQL...")
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",        
        database="banking_case"
    )
    print("Connected successfully!")

    query = "SELECT * FROM customer"
    print(" Executing SQL:", query)
    df = pd.read_sql(query, cnx)

    print(" DataFrame Shape:", df.shape)
    print("First 5 rows:")
    print(df.head())

    cnx.close()
    print("✅ Connection closed.")

except Exception as e:
    print(" Error:", e)


print(df.describe())


# import os
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# # Setup
# output_dir = "images"
# os.makedirs(output_dir, exist_ok=True)
# df.columns = df.columns.str.replace('ï»¿', '', regex=False)

# # Cleanup
# df['Joined Bank'] = pd.to_datetime(df['Joined Bank'], errors='coerce')
# df['Tenure (Years)'] = (pd.Timestamp('today') - df['Joined Bank']).dt.days // 365

# # Plot style
# sns.set_style("whitegrid")
# plt.rcParams.update({'font.size': 10})

# # Start dashboard
# fig, axs = plt.subplots(3, 3, figsize=(20, 16))
# fig.suptitle("📊 Customer Behavior & Risk Insights - Retail Bank", fontsize=18, fontweight='bold', color='#333')

# # 1. Age Distribution
# sns.histplot(df['Age'], kde=True, ax=axs[0, 0], color='#4C72B0')
# axs[0, 0].set_title("🔵 Majority Customers Are 25–40 Years Old")
# axs[0, 0].set_xlabel("Customer Age")
# axs[0, 0].set_ylabel("Number of Customers")

# # 2. Gender Pie Chart
# gender_counts = df['GenderId'].value_counts()
# axs[0, 1].pie(
#     gender_counts,
#     labels=['Male' if i == 1 else 'Female' for i in gender_counts.index],
#     autopct='%1.1f%%',
#     startangle=90,
#     colors=sns.color_palette('pastel')
# )
# axs[0, 1].set_title("🧑‍🤝‍🧑 Gender Distribution: Majority Male")

# # 3. Business Lending Usage
# sns.countplot(x='Business Lending', data=df, ax=axs[0, 2], palette='Blues')
# axs[0, 2].set_title("🏦 Business Lending: Few Customers Use It")
# axs[0, 2].set_xlabel("Has Business Lending?")
# axs[0, 2].set_ylabel("Customer Count")

# # 4. Risk Weighting
# sns.histplot(df['Risk Weighting'], kde=True, ax=axs[1, 0], color='#E17C05')
# axs[1, 0].set_title("⚠️ Risk Levels Skew Toward Moderate")
# axs[1, 0].set_xlabel("Risk Score")
# axs[1, 0].set_ylabel("Customers")

# # 5. Tenure
# sns.histplot(df['Tenure (Years)'], kde=True, ax=axs[1, 1], color='#59A14F')
# axs[1, 1].set_title("📆 Most Customers Are With Us > 3 Years")
# axs[1, 1].set_xlabel("Tenure in Years")
# axs[1, 1].set_ylabel("Customers")

# # 6. Properties Owned
# sns.countplot(x='Properties Owned', data=df, ax=axs[1, 2], palette='Purples')
# axs[1, 2].set_title("🏠 Many Customers Own 0 or 1 Property")
# axs[1, 2].set_xlabel("No. of Properties")
# axs[1, 2].set_ylabel("Customers")

# # 7. Top 5 Locations
# top_locs = df['Location ID'].value_counts().nlargest(5)
# sns.barplot(x=top_locs.index, y=top_locs.values, ax=axs[2, 0], palette='coolwarm')
# axs[2, 0].set_title("📍 Top 5 Customer Locations")
# axs[2, 0].set_xlabel("Location ID")
# axs[2, 0].set_ylabel("Customers")

# # 8. Foreign Currency Account
# sns.countplot(x='Foreign Currency Account', data=df, ax=axs[2, 1], palette='Greens')
# axs[2, 1].set_title("💱 Foreign Currency: Rarely Used")
# axs[2, 1].set_xlabel("Uses Foreign Currency Account?")
# axs[2, 1].set_ylabel("Customers")

# # 9. Empty
# axs[2, 2].axis('off')

# # Save with spacing for title
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.savefig(f"{output_dir}/customer_insights_clean.png", dpi=300)
# plt.close()

# print("✅ Final user-friendly dashboard saved at: images/customer_insights_clean.png")

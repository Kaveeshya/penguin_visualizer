import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Title of your app
st.title("🐧 Penguin Data Visualizer")
st.write("An interactive scatter plot built from a Jupyter Notebook.")

# 2. Load the built-in dataset directly from Seaborn
df = sns.load_dataset("penguins")

# 3. Create the scatter plot using your exact configuration
fig, ax = plt.subplots()
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="flipper_length_mm",
    hue="species",
    ax=ax
)

# 4. Render the plot in the web browser
st.pyplot(fig)

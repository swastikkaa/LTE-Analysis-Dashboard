import streamlit as st
st.title("LTE Dashboard")
project_folder = st.text_input("copy paste the PRE folder path:")
project_folder = project_folder.strip('"')
project_folder2= st.text_input("copy paste the POST folder path:")
project_folder2 = project_folder2.strip('"')
from main import run_analysis
from plots import plotting
if st.button("Run analysis"):
    pre_results = run_analysis(project_folder)
    pre_results.to_excel("PRE_LTE_KPI_Report.xlsx", index=False)
    post_results = run_analysis(project_folder2)
    comparison = pre_results.copy()
    comparison["Post"] = post_results["Value (%)"]
    comparison.rename(
    columns={"Value (%)":"Pre"},
    inplace=True
    )
    comparison["Difference"] = comparison["Post"] - comparison["Pre"]
    st.subheader("Pre vs Post Comparison")
    st.write(comparison)
    post_results.to_excel("POST_LTE_KPI_Report.xlsx", index=False)
    st.write("you can also download your results from excel sheet LTE_KPI_REPORT that is now saved on your project folder :)")
    fig=plotting(comparison)
    st.pyplot(fig)
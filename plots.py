import numpy as np
import matplotlib.pyplot as plt
def plotting(comparison_df):
 # Filter only Accessibility KPIs
 accessibility_df = comparison_df[
    comparison_df["Folder"] == "Accessbility"
 ]
 # Create x positions
 x = np.arange(len(accessibility_df))
 # Width of each bar
 width = 0.4
 # Create blank figure
 fig, ax = plt.subplots(figsize=(10,5))
 # Draw Pre bars
 ax.bar(
    x - width/2,
    accessibility_df["Pre"],
    width=width,
    label="Pre"
 )
 # Draw Post bars
 ax.bar(
    x + width/2,
    accessibility_df["Post"],
    width=width,
    label="Post"
 )
 ax.set_xticks(x)
 ax.set_xticklabels(accessibility_df["KPI"], rotation=20)
 ax.set_title("Accessibility KPIs")
 ax.set_ylabel("Percentage")
 ax.legend()
 ax.set_ylim(80, 100)
 
 return fig 
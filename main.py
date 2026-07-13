import os

from loader import *
from analysis import *
from constants import *


def run_analysis(project_folder):
 cssr_folder = os.path.join(project_folder,cssr_info["cssr_folder"])
 cssr_path=find_file(cssr_folder,cssr_info["keyword"])
 df_cssr = load_csv(cssr_path)

 dcr_folder=os.path.join(project_folder,dcr_info["dcr_folder"])
 dcr_path=find_file(dcr_folder,dcr_info["keyword"])
 df_dcr=load_csv(dcr_path)
 
 cst_folder= os.path.join(project_folder,cst_info["cst_folder"])
 cst_path=find_file(cst_folder,cst_info["keyword"])
 df_cst=load_csv(cst_path)
 

 hosr_folder=os.path.join(project_folder,hosr_info["hosr_folder"])
 hosr_path=find_file(hosr_folder,hosr_info["keyword"])
 df_hosr=load_csv(hosr_path)

 vci_folder=os.path.join(project_folder,vci_info["vci_folder"])
 vci_path=find_file(vci_folder,vci_info["keyword"])
 df_vci=load_csv(vci_path)

 acssr_folder=os.path.join(project_folder,acssr_info["acssr_folder"])
 acssr_path=find_file(acssr_folder,acssr_info["keyword"])
 df_acssr=load_csv(acssr_path)

 RRCdcr_folder=os.path.join(project_folder,RRCdcr_info["RRCdcr_folder"])
 RRCdcr_path=find_file(RRCdcr_folder,RRCdcr_info["keyword"])
 df_RRCdcr=load_csv(RRCdcr_path)
 
 hosr2_folder=os.path.join(project_folder,hosr2_info["hosr2_folder"])
 hosr2_path=find_file(hosr2_folder,hosr2_info["keyword"])
 df_hosr2=load_csv(hosr2_path)

 ERABesr_folder=os.path.join(project_folder,ERABesr_info["ERABesr_folder"])
 ERABesr_path=find_file(ERABesr_folder,ERABesr_info["keyword"])
 df_ERABesr=load_csv(ERABesr_path)

 mudr_folder=os.path.join(project_folder,mudr_info["mudr_folder"])
 mudr_path=find_file(mudr_folder,mudr_info["keyword"])
 df_mudr=load_csv(mudr_path)

 result_cssr = cssr(df_cssr,cssr_info["cssr_count"],cssr_info["cssr_fail"])
 print("Call Setup Success ratio = %.2f%%" % result_cssr)

 result_dcr = dcr(df_dcr, dcr_info["dcr_count"], dcr_info["dcr_drop"])
 print("Dropped Call ratio = %.2f%%" % result_dcr)
 
 result_cst= cst(df_cst, cst_info["cst_time"])
 print("Call setup time in ms = ", result_cst)

 result_hosr = srvcc_hosr(df_hosr, hosr_info["hosr_count"],hosr_info["hosr_success"])
 print("SRVCC Handover Success rate = %.2f%%" % result_hosr)

 result_vci = vci(df_vci,vci_info["vci_count"],vci_info["vci_fail"])
 print("Voice call initiated on LTE = %.2f%%" % result_vci)

 result_acssr = acssr(df_acssr,acssr_info["acssr_count"],acssr_info["acssr_success"])
 print("Attach Call Setup Success Ratio = %.2f%%" % result_acssr)

 result_RRCdcr = RRCdcr(df_RRCdcr,RRCdcr_info["RRCdcr_count"],RRCdcr_info["RRCdcr_drop"])
 print("RRC drop call ratio = %.2f%%" % result_RRCdcr)

 result_hosr2 = hosr2(df_hosr2,hosr2_info["hosr2_count"],hosr2_info["hosr2_drop"])
 print("Handover SuccessRate= %.2f%%" % result_hosr2)
 
 result_ERABesr = ERABesr(df_ERABesr,ERABesr_info["ERABesr_count"],ERABesr_info["ERABesr_success"])
 print("ERAB establishment success rate = %.2f%%" % result_ERABesr)

 result_mudrDLmean = mudrDLmean(df_mudr,mudr_info["mudrDL"])
 print("Mean User data rate Download = ", result_mudrDLmean)

 result_mudrDL = mudrDL(df_mudr,mudr_info["mudrDL"])
 print("Mean User data rate Download greater than 5mbps = %.2f%%" % result_mudrDL)
 
 result_mudrULmean = mudrULmean(df_mudr,mudr_info["mudrUL"])
 print("Mean User data rate upload =",result_mudrULmean)

 result_mudrUL = mudrUL(df_mudr,mudr_info["mudrUL"])
 print("Mean User data rate upload greater than 0.2mbps = %.2f%%" % result_mudrUL)
 
 result_mudrDL2=mudrDL2(df_mudr,mudr_info["mudrDL"])
 print("Percentage of the number of data download samples where data download throughput was >= 1Mbps out of total number of data download samples")

 results = pd.DataFrame({
    "KPI": [
        "Call Setup Success Ratio",
        "Dropped Call Ratio",
        "Call setup time in ms",
        "SRVCC Handover Success Rate",
        "Voice call initiated on LTE",
        "Attach Call Setup Success Ratio",
        "RRC drop call ratio",
        "ERAB establishment success rate",
        "Mean User data rate Download",
        "Mean User data rate Download greater than 5mbps",
        "Mean User data rate upload",
        "Mean User data rate upload greater than 0.2mbps",
        "Percentage of the number of data download samples where data download throughput was >= 1Mbps out of total number of data download samples"
    ],
    "Value (%)": [
        result_cssr,
        result_dcr,
        result_cst,
        result_hosr,
        result_vci,
        result_acssr,
        result_RRCdcr,
        result_ERABesr,
        result_mudrDLmean,
        result_mudrDL,
        result_mudrULmean,
        result_mudrUL,
        result_mudrDL2      
    ],
    "Folder":[
    cssr_info["cssr_folder"],
    dcr_info["dcr_folder"],
    cst_info["cst_folder"],
    hosr_info["hosr_folder"],
    vci_info["vci_folder"],
    acssr_info["acssr_folder"],
    RRCdcr_info["RRCdcr_folder"],
    ERABesr_info["ERABesr_folder"],
    mudr_info["mudr_folder"],
    mudr_info["mudr_folder"],
    mudr_info["mudr_folder"],
    mudr_info["mudr_folder"],
    mudr_info["mudr_folder"]
    ],
    "Keyword":[
    cssr_info["keyword"],
    dcr_info["keyword"],
    cst_info["keyword"],
    hosr_info["keyword"],
    vci_info["keyword"],
    acssr_info["keyword"],
    RRCdcr_info["keyword"],
    ERABesr_info["keyword"],
    mudr_info["keyword"],
    mudr_info["keyword"],
    mudr_info["keyword"],
    mudr_info["keyword"],
    mudr_info["keyword"]
    ]
    
 })

 return results
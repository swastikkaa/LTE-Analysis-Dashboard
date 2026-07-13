import pandas as pd


def to_num(series):
    # Strip commas and convert to numeric
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False),
        errors="coerce"
    )


def find_column(df, keyword):
    

    words = (
        keyword.lower()
        .replace("/", " ")
        .replace("-", " ")
        .replace("(", " ")
        .replace(")", " ")
        .replace("#", " ")
        .split()
    )

    for col in df.columns:
        col_lower = (
            col.lower()
            .replace("/", " ")
            .replace("-", " ")
            .replace("(", " ")
            .replace(")", " ")
            .replace("#", " ")
        )

        if all(word in col_lower for word in words):
            return col

    # Last attempt return any column containing the last word
    last_word = words[-1]
    for col in df.columns:
        if last_word in col.lower():
            print(f"Warning: Using similar column '{col}' for '{keyword}'")
            return col

    raise KeyError(f"Could not find a column similar to '{keyword}'")


def average(df, colname):
    return to_num(df[colname]).mean()


def findmax(df, colname):
    return to_num(df[colname]).max()


def findmin(df, colname):
    return to_num(df[colname]).min()


def size(df):
    print("The number of rows and columns are:", df.shape)

def cssr(df, count, failure):

    count_col = find_column(df, count)
    fail_col = find_column(df, failure)

    total_attempts = to_num(df[count_col]).sum()
    total_fail = to_num(df[fail_col]).sum()

    if total_attempts == 0:
        return 0

    return ((total_attempts - total_fail) / total_attempts) * 100

def dcr(df, count, drop):

    count_col = find_column(df, count)
    drop_col = find_column(df, drop)

    total_count = to_num(df[count_col]).sum()
    total_drop = to_num(df[drop_col]).sum()

    if total_count == 0:
        return 0

    return (total_drop / total_count) * 100
    
def cst(df,time):
    time_col=find_column(df,time)
    avg_time=to_num(df[time_col]).mean()
    return avg_time
    

def srvcc_hosr(df, count, success):

    count_col = find_column(df, count)
    success_col = find_column(df, success)

    total_attempts = to_num(df[count_col]).sum()
    total_success = to_num(df[success_col]).sum()

    if total_attempts == 0:
        return 0

    return (total_success / total_attempts) * 100

def vci(df, count, failure):

    count_col = find_column(df, count)
    fail_col = find_column(df, failure)

    total_count = to_num(df[count_col]).sum()
    total_fail = to_num(df[fail_col]).sum()

    if total_count == 0:
        return 0

    total_success = total_count - total_fail

    return (total_success / total_count) * 100


def acssr(df, count, success):

    count_col = find_column(df, count)
    success_col = find_column(df, success)

    total_count = to_num(df[count_col]).sum()
    total_success = to_num(df[success_col]).sum()

    if total_count == 0:
        return 0

    return (total_success / total_count) * 100

def RRCdcr(df, count, drop):

    count_col = find_column(df, count)
    drop_col = find_column(df, drop)

    total_count = to_num(df[count_col]).sum()
    total_drop = to_num(df[drop_col]).sum()

    if total_count == 0:
        return 0

    return (total_drop / total_count) * 100
    
def hosr2(df,attempt,drop):
    count_col = find_column(df,attempt)
    drop_col=find_column(df,drop)
    total_count = to_num(df[count_col]).sum()
    total_drop = to_num(df[drop_col]).sum()
    total_success=total_count-total_drop
    if total_count == 0:
        return 0
        
    return (total_success/total_count)*100
    


def ERABesr(df, count, success):

    count_col = find_column(df, count)
    success_col = find_column(df, success)

    total_count = to_num(df[count_col]).sum()
    total_success = to_num(df[success_col]).sum()

    if total_count == 0:
        return 0

    return (total_success / total_count) * 100

def mudrDLmean(df, DL):

    dl_col = find_column(df, DL)

    return to_num(df[dl_col]).mean()


def mudrDL(df, DL):

    dl_col = find_column(df, DL)

    samples_over_5 = ((to_num(df[dl_col]) / 1024) > 5).sum()
    total_samples = len(df)

    if total_samples == 0:
        return 0

    return (samples_over_5 / total_samples) * 100


def mudrULmean(df, UL):

    ul_col = find_column(df, UL)

    return to_num(df[ul_col]).mean()


def mudrUL(df, UL):

    ul_col = find_column(df, UL)

    samples_over_point2 = ((to_num(df[ul_col]) / 1024) > 0.2).sum()
    total_samples = len(df)

    if total_samples == 0:
        return 0

    return (samples_over_point2 / total_samples) * 100
    
def mudrDL2(df,DL):
    dl_col = find_column(df, DL)

    samples_over_1mbps = ((to_num(df[dl_col]) / 1024) >=1).sum()
    total_samples = len(df)

    if total_samples == 0:
        return 0

    return (samples_over_1mbps / total_samples) * 100
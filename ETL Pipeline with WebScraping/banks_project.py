import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

f = open("code_log.txt", "w+")

def log_progress(text):
    f.write(text + "\n")

def extract():
    log_progress("Extraction started")
    url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
    df = pd.DataFrame(columns=["Name", "MC_USD_Billion"])
    
    html_page = requests.get(url).text
    bs = BeautifulSoup(html_page, "html.parser")
    dataBodies = bs.find("tbody")
    dataRows = dataBodies.find_all("tr")[1:]
    for i in dataRows:
        dataBanks = i.find_all("td")
        #dataBanks[1].find_all("a")[1].contents[0]
        newDf = pd.DataFrame({
            "Name" : [dataBanks[1].find_all("a")[1].contents[0]],
            "MC_USD_Billion" : [float(dataBanks[2].contents[0])]
        })
        df = pd.concat([df, newDf], ignore_index=True)
    log_progress("Extraction Successed")
    return df

def transform():
    log_progress("Transformation Started")
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
    marketRates = pd.read_csv(url)
    for i in marketRates["Currency"].values:
        df[f"MC_{i}_Billion"] = df["MC_USD_Billion"] * marketRates[marketRates["Currency"] == i]["Rate"].values[0]
        df[f"MC_{i}_Billion"] = df[f"MC_{i}_Billion"].round(2)
    log_progress("Transformation Successed")

def load_to_csv():
    log_progress("Save as CSV started")
    PATH = "./Largest_banks_data.csv"
    df.to_csv(PATH)
    log_progress("Save as CSV successed")

def load_to_db():
    log_progress("Save to Sqlite started")
    db_name = "Banks.db"
    table_name = "Largest_banks"
    #query_statement = f"SELECT * FROM {table_name}"
    
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    # Verified with these codes
    #query_output = pd.read_sql(query_statement, conn)
    #print(query_output)
    conn.close()
    log_progress("Save to Sqlite successed")

df = extract()
transform()
load_to_csv()
load_to_db()

print("\n\n")
f.seek(0)
print(f.read())
f.close()
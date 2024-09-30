from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from mydblib2 import my_select
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import f_oneway

app = Flask(__name__, static_folder="static")

def tukey_hsd(ind, *args):
    data_arr = np.hstack(args)
    ind_arr = np.array([])
    for x in range(len(args)):
        ind_arr = np.append(ind_arr, np.repeat(ind[x], len(args[x])))
    return pairwise_tukeyhsd(data_arr, ind_arr)

@app.route("/")
def top():
    return render_template("En0406.html", title="年代ごとの気象データ一元配置分散ページ", image="")

@app.route("/search", methods=["POST"])
def top2():
    Area = request.form["Area"]
    Weather_data_from_temp = request.form["temp"]

    sqlstring_all = f"""
        SELECT  MONTH,
                AVG(CASE WHEN YEAR BETWEEN 1960 AND 1979 THEN {Weather_data_from_temp} END) AS '1960-1979',
                AVG(CASE WHEN YEAR BETWEEN 1980 AND 1999 THEN {Weather_data_from_temp} END) AS '1980-1999',
                AVG(CASE WHEN YEAR BETWEEN 2000 AND 2019 THEN {Weather_data_from_temp} END) AS '2000-2019'
        FROM weather
        WHERE AREA = '{Area}'
        GROUP BY MONTH
        ORDER BY MONTH
    """

    sqlstring_1960 = f"""
        SELECT Month, AVG({Weather_data_from_temp}) AS Weather_data_changed_name
        FROM weather
        WHERE YEAR >= 1960 AND YEAR <= 1979
        AND AREA = '{Area}'
        GROUP BY Month;
    """
    sqlstring_1980 = f"""
        SELECT Month, AVG({Weather_data_from_temp}) AS Weather_data_changed_name
        FROM weather
        WHERE YEAR >= 1980 AND YEAR <= 1999
        AND AREA = '{Area}'
        GROUP BY Month;
    """
    sqlstring_2000 = f"""
        SELECT Month, AVG({Weather_data_from_temp}) AS Weather_data_changed_name
        FROM weather
        WHERE YEAR >= 2000 AND YEAR <= 2019
        AND AREA = '{Area}'
        GROUP BY Month;
    """

    Weather = my_select("webprog", sqlstring_all)
    Weather1 = my_select("webprog", sqlstring_1960)
    Weather2 = my_select("webprog", sqlstring_1980)
    Weather3 = my_select("webprog", sqlstring_2000)

    title = request.form["Area"] + Weather_data_from_temp

    b_val, p_val = f_oneway(Weather1["Weather_data_changed_name"], Weather2["Weather_data_changed_name"], Weather3["Weather_data_changed_name"])
    msg = f"一元配置分散分析の結果， p_val={p_val}\n\n"

    tukey_result = tukey_hsd(["Y1960-Y1980", "Y1980-Y2000", "Y2000-Y2020"], Weather1["Weather_data_changed_name"], Weather2["Weather_data_changed_name"], Weather3["Weather_data_changed_name"])
    msg += str(tukey_result)

    plt.plot(Weather1["Month"], Weather1["Weather_data_changed_name"])
    plt.plot(Weather2["Month"], Weather2["Weather_data_changed_name"])
    plt.plot(Weather3["Month"], Weather3["Weather_data_changed_name"])
    plt.title(f"{title}の一元配置分散の結果")
    plt.xlabel(Weather_data_from_temp)
    plt.ylabel("温度")
    plt.savefig("./static/En0406.png")
    plt.close()

    return render_template("message.html", title=f"{title}の一元配置分散の結果", message=msg, table_data=Weather.values, image="/static/En0406.png")

app.run(host="localhost", port=5000, debug=True)

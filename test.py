from re import M
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import date as d, timedelta
import datetime

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station


# session = Session(engine)

# most_active = session.query(Measurement.station, func.count(Measurement.station)).group_by(
#     Measurement.station).order_by((func.count(Measurement.station).desc())).first()

# station_results = session.query(Measurement.date).filter(
#     Measurement.station == most_active[0]).order_by(Measurement.date.desc()).first()

# station = list(np.ravel(station_results))

# prev_year = datetime.datetime.strptime(station[0], '%Y-%m-%d')- datetime.timedelta(days=365)
# prev_year = prev_year.strftime("%Y-%m-%d")

# prev_year_results = session.query(Measurement.date, Measurement.station).filter(
#     Measurement.station >= prev_year).order_by(Measurement.date.desc()).all()

# prev_year_list = list(np.ravel(prev_year_results))

# print(prev_year_list)

start = "2016,10,24"
session = Session(engine)
date_format = datetime.datetime(start, "%Y-%m-%d")

find_measurement = session.query(Measurement.date, Measurement.tobs).filter(
    Measurement.date.strptime("%Y-%m-%d") >= date_format).all()

result_ = list(np.ravel(find_measurement))

print(result_)

# print( jsonify(result_))

# a = session.query(Measurement.date, Measurement.tobs).all()
# print(a[0][0])

        # if find_measurement[0][0] == date_format:
        #     list(np.ravel(find_measurement))

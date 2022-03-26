from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def homepage():
    return(
        f"List of available routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"<br>Note: Date should be YYYY-MM-DD format."
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    prec_results = session.query(Measurement.date, Measurement.prcp).all()

    to_list = list(np.ravel(prec_results))

    session.close()

    return jsonify(to_list)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    station_results = session.query(Station.station).all()

    station = list(np.ravel(station_results))

    session.close()

    return jsonify(station)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    most_active = session.query(Measurement.station, func.count(Measurement.station)).group_by(
        Measurement.station).order_by((func.count(Measurement.station).desc())).first()

    station_results = session.query(Measurement.date).filter(
        Measurement.station == most_active[0]).order_by(Measurement.date.desc()).first()

    station = list(np.ravel(station_results))

    prev_year = datetime.datetime.strptime(
        station[0], '%Y-%m-%d') - datetime.timedelta(days=365)
    prev_year = prev_year.strftime("%Y-%m-%d")

    prev_year_results = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.date >= prev_year).order_by(Measurement.date.desc()).all()

    prev_year_list = list(np.ravel(prev_year_results))
    
    session.close()

    return jsonify(prev_year_list)

# @app.route("/api/v1.0/<start>    (Y-M-D Format)")
# def start_date(start):
#     session = Session(engine)
    
#     date_format = start.strptime("%Y-%m-%d")
    
#     for date in date_format:
        
#         find_measurement = session.query(Measurement.date, Measurement.tobs).all()
        
#         if find_measurement     



# @app.route("/api/v1.0/<start>/<end>")
# def start_date():
#     return
if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/env python

#Import kafka and flask
from kafka import KafkaProducer
from flask import Flask

#Define the app
app = Flask(__name__)
event_logger = KafkaProducer(bootstrap_servers='kafka:29092')
events_topic = 'events'

#Setting up the default address.  The default response returns a string.
@app.route("/")
def default_response():
    event_logger.send(events_topic, 'default'.encode())
    return "This is the default response!"

#Post purchase_a_sword, calls the purchase_sword function, returns the string.
@app.route("/purchase_a_sword")
def purchase_sword():
    # business logic to purchase sword
    # log event to kafka
    event_logger.send(events_topic, 'purchased_sword'.encode())
    return "Sword Purchased!"

package goetz.masters.simulation.project2;

import static spark.Spark.get;
import static spark.Spark.port;
import static spark.Spark.staticFiles;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import goetz.masters.simulation.project2.models.Event;
import goetz.masters.simulation.project2.persistence.EsWriter;

public class SimServer {

	static Logger log = LogManager.getLogger(SimServer.class);

	public static void main(String[] args) {

		log.debug("starting service with configuration below:");
		EsWriter es = EsWriter.getInstance();
		port(7777);
		staticFiles.location("/public");

		get("/event/arrival", (req, res) -> {
			Event newArrival = Event.newArrival();
			es.write(newArrival);
			return newArrival;
		}, new JsonTransformer());

		get("/event/orderstart", (req, res) -> {
			Event orderStart = Event.orderStart();
			es.write(orderStart);
			return orderStart;
		}, new JsonTransformer());

		get("/event/orderend", (req, res) -> {
			Event orderComplete = Event.orderComplete();
			es.write(orderComplete);
			return orderComplete;
		}, new JsonTransformer());

		get("/event/paymentstart", (req, res) -> {
			Event paymentStart = Event.paymentStart();
			es.write(paymentStart);
			return paymentStart;
		}, new JsonTransformer());

		get("/event/paymentend", (req, res) -> {
			Event paymentComplete = Event.paymentComplete();
			es.write(paymentComplete);
			return paymentComplete;
		}, new JsonTransformer());

		get("/event/pickupstart", (req, res) -> {
			Event pickupStart = Event.pickupStart();
			es.write(pickupStart);
			return pickupStart;
		}, new JsonTransformer());

		get("/event/pickupend", (req, res) -> {
			Event pickupComplete = Event.pickupComplete();
			es.write(pickupComplete);
			return pickupComplete;
		}, new JsonTransformer());

		get("/event/end", (req, res) -> {
			Event recordingComplete = Event.recordingComplete();
			es.write(recordingComplete);
			return recordingComplete;
		}, new JsonTransformer());

		get("/event/start", (req, res) -> {
			Event recordingStart = Event.recordingStart();
			es.write(recordingStart);
			return recordingStart;
		}, new JsonTransformer());

	}

}

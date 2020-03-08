package goetz.masters.simulation.project2.models;

import java.util.Date;

public class Event {

	private String type;
	private Date time;

	private Event(String type) {
		this.type = type;
		this.time = new Date();
	}

	public static Event newArrival() {
		return new Event("arrival");
	}

	public static Event orderStart() {
		return new Event("order_start");
	}

	public static Event orderComplete() {
		return new Event("order_complete");
	}

	public static Event paymentStart() {
		return new Event("payment_start");
	}

	public static Event paymentComplete() {
		return new Event("payment_complete");
	}

	public static Event pickupStart() {
		return new Event("pickup_start");
	}

	public static Event pickupComplete() {
		return new Event("pickup_complete");
	}

	public static Event recordingStart() {
		return new Event("recording_start");
	}

	public static Event recordingComplete() {
		return new Event("recording_complete");
	}

	public String getType() {
		return type;
	}

	public Date getTime() {
		return time;
	}

}

package goetz.masters.simulation.project2.persistence;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.http.HttpHost;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.xcontent.XContentType;

import com.google.gson.Gson;

import goetz.masters.simulation.project2.models.Event;

public class EsWriter {

	private static EsWriter instance;
	private RestHighLevelClient client;
	private String index;
	private Gson gson;

	private EsWriter() {
		this.client = new RestHighLevelClient(RestClient.builder(new HttpHost("elasticsearch", 9200, "http")));
		SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd_HHmmss");
		this.index = "recording_" + sdf.format(new Date());
		this.gson = new Gson();
	}

	public static EsWriter getInstance() {
		if (instance == null) {
			instance = new EsWriter();
		}
		return instance;
	}

	public void write(Event event) throws IOException {
		IndexRequest request = new IndexRequest(this.index);
		request.source(gson.toJson(event), XContentType.JSON);
		client.index(request, RequestOptions.DEFAULT);
	}
}

package org.fog.test;
import com.azure.messaging.eventhubs.EventHubClientBuilder;
import com.azure.messaging.eventhubs.EventHubConsumerAsyncClient;
import java.util.concurrent.TimeUnit;

public class AzureReceiver {
    private static final String CONNECTION_STRING = 
        "Endpoint=sb://ihsuprodblres065dednamespace.servicebus.windows.net/;" +
        "SharedAccessKeyName=eventhub-listener;" +
        "SharedAccessKey=lsxQzf4ZBO3oWFRbrTx8I6yPR5eu8cJylAIoTCUxzIk=;" +
        "EntityPath=iothub-ehub-personal-t-64729521-a50d8c62e5";

    public static void main(String[] args) throws InterruptedException {
        System.out.println("📡 Connecting to Azure Event Hubs...");

        EventHubConsumerAsyncClient consumer = new EventHubClientBuilder()
            .connectionString(CONNECTION_STRING)
            .consumerGroup("$Default") // Case-sensitive!
            .buildAsyncConsumerClient();

        consumer.receive()
            .subscribe(event -> {
                String data = new String(event.getData().getBody());
                System.out.println("✅ Received Sensor Data: " + data);
            }, error -> {
                System.err.println("❌ Error: " + error.getMessage());
            });

        TimeUnit.MINUTES.sleep(10); // Keep running
    }
}
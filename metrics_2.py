from prometheus_client import start_http_server, Gauge
import time
#g.set(1)
g = Gauge('application_2', 'test_for_application_1')

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8001)
    # Generate some requests.
    while True:
        g.set(0)
        time.sleep(1)

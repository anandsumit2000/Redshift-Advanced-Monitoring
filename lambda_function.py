import os
import sys
import redshift_monitoring

def lambda_handler(event, context):
    # resolve the configuration from the sources required
    config_sources = [event, os.environ]
    redshift_monitoring.monitor_cluster(config_sources)
    return 'Finished'

if __name__ == "__main__":
    lambda_handler(sys.argv[0], None)

# things.py

# Let's get this party started!
import falcon
import bjoern
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('test.log'))
logger.setLevel(logging.INFO)

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.


class ResponseLoggerMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        logger.info('{0} {1} {2}'.format(
            req.method, req.relative_uri, resp.status[:3]))


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('Hello!')


# falcon.API instances are callable WSGI apps
#app = falcon.API(middleware=[ResponseLoggerMiddleware()])
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/api', things)
bjoern.run(app, host='0.0.0.0', port=8080)

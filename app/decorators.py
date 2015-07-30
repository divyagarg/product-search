import time
import functools
import ujson as json
from flask import Response

def logtime(f):
  @functools.wraps(f)
  def wrapped(*args, **kwargs):
    start = time.time()
    rv = f(*args, **kwargs)
    logging.info('Time taken (for args %s) = %s', args, time.time() - start)
    return rv
  return wrapped

def jsonify(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        if not isinstance(rv, dict):
            rv = rv.to_json()
        rv = json.dumps(rv)
        resp = Response(response=rv,
               status=200,
               mimetype="application/json")
        logging.info('Total time taken = %s', time.time() - start)
        return resp
    return wrapped

def logrequest(f):
  @functools.wraps(f)
  def wrapped(*args, **kwargs):
    rv = f(*args, **kwargs)
    # logging.info("Arguments = %s Returned %s" % (kwargs, rv))
    return rv
  return wrapped
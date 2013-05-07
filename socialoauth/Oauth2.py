# -*- coding: utf-8 -*-
'''
Created on 2013-4-27

@author: wwjiang
'''

try:
    import json
except ImportError:
    import simplejson as json

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import gzip, time, urllib, urllib2, logging

class APIError(StandardError):
    '''
    raise APIError if receiving json message indicating failure.
    '''
    def __init__(self, error_code, error, request):
        self.error_code = error_code
        self.error = error
        self.request = request
        StandardError.__init__(self, error)

    def __str__(self):
        return 'APIError: %s: %s, request: %s' % (self.error_code, self.error, self.request)

def _parse_json(s):
    ' parse str into JsonDict '
    def _obj_hook(pairs):
        ' convert json object to python object '
        o = JsonDict()
        for k, v in pairs.iteritems():
            o[str(k)] = v
        return o
    return json.loads(s, object_hook=_obj_hook)

class JsonDict(dict):
    ' general json object that allows attributes to be bound to and also behaves like a dict '
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value

def _encode_params(**kw):
    args = []
    for k, v in kw.iteritems():
        if isinstance(v, basestring):
            qv = v.encode('utf-8') if isinstance(v, unicode) else v #不能是unicode编码
            args.append('%s=%s' % (k, urllib.quote(qv)))
        else:
            qv = str(v)
            args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)


def _read_body(obj):
    using_gzip = obj.headers.get('Content-Encoding', '')=='gzip'
    body = obj.read()
    if using_gzip:
        logging.info('gzip content received.')
        gzipper = gzip.GzipFile(fileobj=StringIO(body))
        fcontent = gzipper.read()
        gzipper.close()
        return fcontent
    return body

def _http_call(the_url, method, authorization, **kw):
    '''
    send an http request and return a json object if no error occurred.
    '''

class APIClient(object):
    '''
    API client using synchronized invocation.
    '''
    def __init__(self, client_id, client_secret, authorize_endpoint,access_endpoint,redirect_uri ):
        self.client_id = str(client_id)
        self.client_secret = str(client_secret)
        self.redirect_uri = redirect_uri
        self.authorize_endpoint = authorize_endpoint
        self.access_endpoint = access_endpoint

    def get_authorize_url(self,**kw):
        '''
        return the authorization url that the user should be redirected to.
        '''
        if not self.redirect_uri:
            raise APIError('21305', 'Parameter absent: redirect_uri', 'OAuth2 request')
        response_type = kw.pop('response_type', 'code')
        authorize_url = '%s?%s' % (self.authorize_endpoint, \
                        _encode_params(client_id = self.client_id, \
                        response_type = response_type, \
                        redirect_uri = self.redirect_uri, **kw))
        return authorize_url   

    def request_access_token(self, code):
        '''
        return access token as a JsonDict: {"access_token":"your-access-token","expires_in":12345678,"uid":1234}, expires_in is represented using standard unix-epoch-time
        '''
        if not self.redirect_uri:
            raise APIError('21305', 'Parameter absent: redirect_uri', 'OAuth2 request')
       
        http_url = self.access_endpoint
        http_body = urllib.quote(client_id = self.client_id, \
                client_secret = self.client_secret, \
                redirect_uri = self.redirect_uri, \
                code = code, grant_type = 'authorization_code')
        req = urllib2.Request(http_url, data=http_body)
    
        try:
            resp = urllib2.urlopen(req)
            body = _read_body(resp)
            r = _parse_json(body)
            if hasattr(r, 'error_code'):
                raise APIError(r.error_code, r.get('error', ''), r.get('request', ''))
            return r
        except urllib2.HTTPError, e:
            try:
                r = _parse_json(_read_body(e))
            except:
                r = None
                if hasattr(r, 'error_code'):
                    raise APIError(r.error_code, r.get('error', ''), r.get('request', ''))
                raise e
        current = int(time.time())
        expires = r.expires_in + current
        
        return JsonDict(access_token=r.access_token, expires=expires, expires_in=expires, uid=r.get('uid', None))

    #fix me
    def refresh_token(self, refresh_token):
        req_str = '%s%s' % (self.auth_url, 'access_token')
        r = _http_call(req_str, \
            client_id = self.client_id, \
            client_secret = self.client_secret, \
            refresh_token = refresh_token, \
            grant_type = 'refresh_token')
        current = int(time.time())
        expires = r.expires_in + current
        
        return JsonDict(access_token=r.access_token, expires=expires, expires_in=expires, uid=r.get('uid', None))

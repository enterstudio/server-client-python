from .endpoint import Endpoint
from .exceptions import ServerResponseError, ServerInfoEndpointNotFoundError
from ...models import ServerInfoItem
import logging

logger = logging.getLogger('tableau.endpoint.server_info')


class ServerInfo(Endpoint):
    @property
    def baseurl(self):
        return "{0}/serverInfo".format(self.parent_srv.baseurl)

    def get(self):
        """ Retrieve the server info for the server.  This is an unauthenticated call """
        try:
            server_response = self.get_unauthenticated_request(self.baseurl)
        except ServerResponseError as e:
            if e.code == "404003":
                raise ServerInfoEndpointNotFoundError

        server_info = ServerInfoItem.from_response(server_response.content)
        return server_info

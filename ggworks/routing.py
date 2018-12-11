# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import ggworks.ggworks_channels.routing

application = ProtocolTypeRouter({
  # (http->django views is added by default)
  'websocket': AuthMiddlewareStack(
    URLRouter(
      ggworks.ggworks_channels.routing.websocket_urlpatterns
    )
  ),
})
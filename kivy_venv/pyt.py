import json
import requests

requests.put("http://pigrinatorstand.local/newPath",data=json.dumps({"path":[{"direction": "forward","value":20},{"direction": "right","value":45}]}))
import json
import urllib.parse

try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    ROBOT = False
except Exception:
    ROBOT = False

# create a sample json
a = {'browserName': 'Chrome',
    'browserVersion': '91.0',
    'LT:Options': {
      'platform': 'Windows 10',
      'build': 'browser-library',
      'name': 'browser-library',
      'user': 'mayankmaurya',
      'accessKey': '4N7wU1Sq7cBGRHCaGf5Y72mTS30xyLV1faGphyvELhuNoTLMRk'
    }
  }

# Convert JSON to String
y = json.dumps(a)
print("Encoded" + urllib.parse.urlencode(a))

@keyword("Capability")
def caps():
    return urllib.parse.urlencode(a)
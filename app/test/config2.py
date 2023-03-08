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



@keyword("Capability")
def caps():
    # create a sample json
  a = {
        "lt:options": {
		      "w3c": True,
		      "platformName": "android",
		      "deviceName": "Vivo V20",
		      "platformVersion": "11",
		     "isRealMobile": True
	      }  
      }

  # Convert JSON to String
  y = json.dumps(a)
  print("Encoded" + urllib.parse.quote(y))  
  return urllib.parse.quote(y)

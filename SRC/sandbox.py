from presenter.xmler import *
from model.globalsvar import *

parser = xmler()
parser.loadXML(START_FILE)
parser.testprintxml()
print(parser.get_formatet_intag(HUB_TELEMETRY_TAG))
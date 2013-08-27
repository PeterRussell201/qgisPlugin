from opengeo.geoserver.support import xml_property, write_bool, ResourceInfo, url,\
    write_string

def workspace_from_index(catalog, node):
    name = node.find("name")
    return Workspace(catalog, name.text)

class Workspace(ResourceInfo): 
    resource_type = "workspace"

    def __init__(self, catalog, wsname):
        super(Workspace, self).__init__()
        self.catalog = catalog
        self.wsname = wsname

    @property
    def href(self):
        return url(self.catalog.service_url, ["workspaces", self.wsname + ".xml"])

    @property
    def coveragestore_url(self):
        return url(self.catalog.service_url, ["workspaces", self.wsname, "coveragestores.xml"])

    @property
    def datastore_url(self):
        return url(self.catalog.service_url, ["workspaces", self.wsname, "datastores.xml"])

    
    name = xml_property("name")
    writers = dict(name = write_string("name"))


    def __repr__(self):
        return "%s @ %s" % (self.name, self.href)

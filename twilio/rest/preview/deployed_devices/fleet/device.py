# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import deserialize
from admin.twilio.base import values
from admin.twilio.base.instance_context import InstanceContext
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page


class DeviceList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, fleet_sid):
        """
        Initialize the DeviceList

        :param Version version: Version that contains the resource
        :param fleet_sid: The unique identifier of the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceList
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceList
        """
        super(DeviceList, self).__init__(version)

        # Path Solution
        self._solution = {'fleet_sid': fleet_sid, }
        self._uri = '/Fleets/{fleet_sid}/Devices'.format(**self._solution)

    def create(self, unique_name=values.unset, friendly_name=values.unset,
               identity=values.unset, deployment_sid=values.unset,
               enabled=values.unset):
        """
        Create a new DeviceInstance

        :param unicode unique_name: A unique, addressable name of this Device.
        :param unicode friendly_name: A human readable description for this Device.
        :param unicode identity: An identifier of the Device user.
        :param unicode deployment_sid: The unique SID of the Deployment group.
        :param bool enabled: The enabled

        :returns: Newly created DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'Identity': identity,
            'DeploymentSid': deployment_sid,
            'Enabled': enabled,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return DeviceInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'], )

    def stream(self, deployment_sid=values.unset, limit=None, page_size=None):
        """
        Streams DeviceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode deployment_sid: Find all Devices grouped under the specified Deployment.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(deployment_sid=deployment_sid, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, deployment_sid=values.unset, limit=None, page_size=None):
        """
        Lists DeviceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode deployment_sid: Find all Devices grouped under the specified Deployment.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance]
        """
        return list(self.stream(deployment_sid=deployment_sid, limit=limit, page_size=page_size, ))

    def page(self, deployment_sid=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DeviceInstance records from the API.
        Request is executed immediately

        :param unicode deployment_sid: Find all Devices grouped under the specified Deployment.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DevicePage
        """
        params = values.of({
            'DeploymentSid': deployment_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return DevicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeviceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DevicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DevicePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a DeviceContext

        :param sid: A string that uniquely identifies the Device.

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        """
        return DeviceContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a DeviceContext

        :param sid: A string that uniquely identifies the Device.

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        """
        return DeviceContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.DeviceList>'


class DevicePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the DevicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param fleet_sid: The unique identifier of the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DevicePage
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DevicePage
        """
        super(DevicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        return DeviceInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.DevicePage>'


class DeviceContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, fleet_sid, sid):
        """
        Initialize the DeviceContext

        :param Version version: Version that contains the resource
        :param fleet_sid: The fleet_sid
        :param sid: A string that uniquely identifies the Device.

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        """
        super(DeviceContext, self).__init__(version)

        # Path Solution
        self._solution = {'fleet_sid': fleet_sid, 'sid': sid, }
        self._uri = '/Fleets/{fleet_sid}/Devices/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a DeviceInstance

        :returns: Fetched DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DeviceInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the DeviceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name=values.unset, identity=values.unset,
               deployment_sid=values.unset, enabled=values.unset):
        """
        Update the DeviceInstance

        :param unicode friendly_name: A human readable description for this Device.
        :param unicode identity: An identifier of the Device user.
        :param unicode deployment_sid: The unique SID of the Deployment group.
        :param bool enabled: The enabled

        :returns: Updated DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Identity': identity,
            'DeploymentSid': deployment_sid,
            'Enabled': enabled,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return DeviceInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.DeviceContext {}>'.format(context)


class DeviceInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, fleet_sid, sid=None):
        """
        Initialize the DeviceInstance

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        super(DeviceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'url': payload['url'],
            'unique_name': payload['unique_name'],
            'friendly_name': payload['friendly_name'],
            'fleet_sid': payload['fleet_sid'],
            'enabled': payload['enabled'],
            'account_sid': payload['account_sid'],
            'identity': payload['identity'],
            'deployment_sid': payload['deployment_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'date_authenticated': deserialize.iso8601_datetime(payload['date_authenticated']),
        }

        # Context
        self._context = None
        self._solution = {'fleet_sid': fleet_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeviceContext for this DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceContext
        """
        if self._context is None:
            self._context = DeviceContext(
                self._version,
                fleet_sid=self._solution['fleet_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Device.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: URL of this Device.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def unique_name(self):
        """
        :returns: A unique, addressable name of this Device.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description for this Device
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def fleet_sid(self):
        """
        :returns: The unique identifier of the Fleet.
        :rtype: unicode
        """
        return self._properties['fleet_sid']

    @property
    def enabled(self):
        """
        :returns: Device enabled flag.
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def account_sid(self):
        """
        :returns: The unique SID that identifies this Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def identity(self):
        """
        :returns: An identifier of the Device user.
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def deployment_sid(self):
        """
        :returns: The unique SID of the Deployment group.
        :rtype: unicode
        """
        return self._properties['deployment_sid']

    @property
    def date_created(self):
        """
        :returns: The date this Device was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Device was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def date_authenticated(self):
        """
        :returns: The date this Device was authenticated.
        :rtype: datetime
        """
        return self._properties['date_authenticated']

    def fetch(self):
        """
        Fetch a DeviceInstance

        :returns: Fetched DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the DeviceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset, identity=values.unset,
               deployment_sid=values.unset, enabled=values.unset):
        """
        Update the DeviceInstance

        :param unicode friendly_name: A human readable description for this Device.
        :param unicode identity: An identifier of the Device user.
        :param unicode deployment_sid: The unique SID of the Deployment group.
        :param bool enabled: The enabled

        :returns: Updated DeviceInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            identity=identity,
            deployment_sid=deployment_sid,
            enabled=enabled,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.DeviceInstance {}>'.format(context)

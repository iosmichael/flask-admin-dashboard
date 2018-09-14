# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import serialize
from admin.twilio.base import values
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page


class StreamMessageList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, stream_sid):
        """
        Initialize the StreamMessageList

        :param Version version: Version that contains the resource
        :param service_sid: Service Instance SID.
        :param stream_sid: Stream SID.

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        """
        super(StreamMessageList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'stream_sid': stream_sid, }
        self._uri = '/Services/{service_sid}/Streams/{stream_sid}/Messages'.format(**self._solution)

    def create(self, data):
        """
        Create a new StreamMessageInstance

        :param dict data: Stream Message body.

        :returns: Newly created StreamMessageInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        """
        data = values.of({'Data': serialize.object(data), })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return StreamMessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            stream_sid=self._solution['stream_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.StreamMessageList>'


class StreamMessagePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the StreamMessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Instance SID.
        :param stream_sid: Stream SID.

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessagePage
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessagePage
        """
        super(StreamMessagePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of StreamMessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        """
        return StreamMessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            stream_sid=self._solution['stream_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.StreamMessagePage>'


class StreamMessageInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, stream_sid):
        """
        Initialize the StreamMessageInstance

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        """
        super(StreamMessageInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'sid': payload['sid'], 'data': payload['data'], }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'stream_sid': stream_sid, }

    @property
    def sid(self):
        """
        :returns: Stream Message SID.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def data(self):
        """
        :returns: Stream Message body.
        :rtype: dict
        """
        return self._properties['data']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.StreamMessageInstance>'

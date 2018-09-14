# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import deserialize
from admin.twilio.base import serialize
from admin.twilio.base import values
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page


class NotificationList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.notify.v1.service.notification.NotificationList
        :rtype: twilio.rest.notify.v1.service.notification.NotificationList
        """
        super(NotificationList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Notifications'.format(**self._solution)

    def create(self, body=values.unset, priority=values.unset, ttl=values.unset,
               title=values.unset, sound=values.unset, action=values.unset,
               data=values.unset, apn=values.unset, gcm=values.unset,
               sms=values.unset, facebook_messenger=values.unset, fcm=values.unset,
               segment=values.unset, alexa=values.unset, to_binding=values.unset,
               identity=values.unset, tag=values.unset):
        """
        Create a new NotificationInstance

        :param unicode body: Indicates the notification body text.
        :param NotificationInstance.Priority priority: Two priorities defined: low and high.
        :param unicode ttl: This parameter specifies how long the notification is valid.
        :param unicode title: Indicates the notification title.
        :param unicode sound: Indicates a sound to be played.
        :param unicode action: Specifies the actions to be displayed for the notification.
        :param dict data: This parameter specifies the custom key-value pairs of the notification's payload.
        :param dict apn: APNS specific payload that overrides corresponding attributes in a generic payload for Bindings with the apn BindingType.
        :param dict gcm: GCM specific payload that overrides corresponding attributes in generic payload for Bindings with gcm BindingType.
        :param dict sms: SMS specific payload that overrides corresponding attributes in generic payload for Bindings with sms BindingType.
        :param dict facebook_messenger: Messenger specific payload that overrides corresponding attributes in generic payload for Bindings with facebook-messenger BindingType.
        :param dict fcm: FCM specific payload that overrides corresponding attributes in generic payload for Bindings with fcm BindingType.
        :param unicode segment: The segment
        :param dict alexa: The alexa
        :param unicode to_binding: The destination address in a JSON object.
        :param unicode identity: Delivery will be attempted only to Bindings with an Identity in this list.
        :param unicode tag: Delivery will be attempted only to Bindings that have all of the Tags in this list.

        :returns: Newly created NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        data = values.of({
            'Identity': serialize.map(identity, lambda e: e),
            'Tag': serialize.map(tag, lambda e: e),
            'Body': body,
            'Priority': priority,
            'Ttl': ttl,
            'Title': title,
            'Sound': sound,
            'Action': action,
            'Data': serialize.object(data),
            'Apn': serialize.object(apn),
            'Gcm': serialize.object(gcm),
            'Sms': serialize.object(sms),
            'FacebookMessenger': serialize.object(facebook_messenger),
            'Fcm': serialize.object(fcm),
            'Segment': serialize.map(segment, lambda e: e),
            'Alexa': serialize.object(alexa),
            'ToBinding': serialize.map(to_binding, lambda e: e),
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationList>'


class NotificationPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.notify.v1.service.notification.NotificationPage
        :rtype: twilio.rest.notify.v1.service.notification.NotificationPage
        """
        super(NotificationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.service.notification.NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationPage>'


class NotificationInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Priority(object):
        HIGH = "high"
        LOW = "low"

    def __init__(self, version, payload, service_sid):
        """
        Initialize the NotificationInstance

        :returns: twilio.rest.notify.v1.service.notification.NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'identities': payload['identities'],
            'tags': payload['tags'],
            'segments': payload['segments'],
            'priority': payload['priority'],
            'ttl': deserialize.integer(payload['ttl']),
            'title': payload['title'],
            'body': payload['body'],
            'sound': payload['sound'],
            'action': payload['action'],
            'data': payload['data'],
            'apn': payload['apn'],
            'gcm': payload['gcm'],
            'fcm': payload['fcm'],
            'sms': payload['sms'],
            'facebook_messenger': payload['facebook_messenger'],
            'alexa': payload['alexa'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, }

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def identities(self):
        """
        :returns: List of Identities.
        :rtype: unicode
        """
        return self._properties['identities']

    @property
    def tags(self):
        """
        :returns: List of Tags
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def segments(self):
        """
        :returns: The segments
        :rtype: unicode
        """
        return self._properties['segments']

    @property
    def priority(self):
        """
        :returns: Two priorities defined: low and high.
        :rtype: NotificationInstance.Priority
        """
        return self._properties['priority']

    @property
    def ttl(self):
        """
        :returns: This parameter specifies how long the notification is valid.
        :rtype: unicode
        """
        return self._properties['ttl']

    @property
    def title(self):
        """
        :returns: Indicates the notification title.
        :rtype: unicode
        """
        return self._properties['title']

    @property
    def body(self):
        """
        :returns: Indicates the notification body text.
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def sound(self):
        """
        :returns: Indicates a sound to be played.
        :rtype: unicode
        """
        return self._properties['sound']

    @property
    def action(self):
        """
        :returns: Specifies the actions to be displayed for the notification.
        :rtype: unicode
        """
        return self._properties['action']

    @property
    def data(self):
        """
        :returns: This parameter specifies the custom key-value pairs of the notification's payload.
        :rtype: dict
        """
        return self._properties['data']

    @property
    def apn(self):
        """
        :returns: APNS specific payload that overrides corresponding attributes in a generic payload for Bindings with the apn BindingType.
        :rtype: dict
        """
        return self._properties['apn']

    @property
    def gcm(self):
        """
        :returns: GCM specific payload that overrides corresponding attributes in generic payload for Bindings with gcm BindingType.
        :rtype: dict
        """
        return self._properties['gcm']

    @property
    def fcm(self):
        """
        :returns: FCM specific payload that overrides corresponding attributes in generic payload for Bindings with fcm BindingType.
        :rtype: dict
        """
        return self._properties['fcm']

    @property
    def sms(self):
        """
        :returns: SMS specific payload that overrides corresponding attributes in generic payload for Bindings with sms BindingType.
        :rtype: dict
        """
        return self._properties['sms']

    @property
    def facebook_messenger(self):
        """
        :returns: Messenger specific payload that overrides corresponding attributes in generic payload for Bindings with facebook-messenger BindingType.
        :rtype: dict
        """
        return self._properties['facebook_messenger']

    @property
    def alexa(self):
        """
        :returns: The alexa
        :rtype: dict
        """
        return self._properties['alexa']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationInstance>'

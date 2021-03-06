# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import deserialize
from admin.twilio.base import values
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page


class VerificationList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the VerificationList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.

        :returns: twilio.rest.preview.acc_security.service.verification.VerificationList
        :rtype: twilio.rest.preview.acc_security.service.verification.VerificationList
        """
        super(VerificationList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Verifications'.format(**self._solution)

    def create(self, to, channel, custom_message=values.unset):
        """
        Create a new VerificationInstance

        :param unicode to: To phonenumber
        :param unicode channel: sms or call
        :param unicode custom_message: A custom message for this verification

        :returns: Newly created VerificationInstance
        :rtype: twilio.rest.preview.acc_security.service.verification.VerificationInstance
        """
        data = values.of({'To': to, 'Channel': channel, 'CustomMessage': custom_message, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return VerificationInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.AccSecurity.VerificationList>'


class VerificationPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the VerificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.

        :returns: twilio.rest.preview.acc_security.service.verification.VerificationPage
        :rtype: twilio.rest.preview.acc_security.service.verification.VerificationPage
        """
        super(VerificationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of VerificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.acc_security.service.verification.VerificationInstance
        :rtype: twilio.rest.preview.acc_security.service.verification.VerificationInstance
        """
        return VerificationInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.AccSecurity.VerificationPage>'


class VerificationInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Channel(object):
        SMS = "sms"
        CALL = "call"

    def __init__(self, version, payload, service_sid):
        """
        Initialize the VerificationInstance

        :returns: twilio.rest.preview.acc_security.service.verification.VerificationInstance
        :rtype: twilio.rest.preview.acc_security.service.verification.VerificationInstance
        """
        super(VerificationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'service_sid': payload['service_sid'],
            'account_sid': payload['account_sid'],
            'to': payload['to'],
            'channel': payload['channel'],
            'status': payload['status'],
            'valid': payload['valid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, }

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Verification.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def to(self):
        """
        :returns: To phonenumber
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def channel(self):
        """
        :returns: sms or call
        :rtype: VerificationInstance.Channel
        """
        return self._properties['channel']

    @property
    def status(self):
        """
        :returns: pending, approved, denied or expired
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def valid(self):
        """
        :returns: successful verification
        :rtype: bool
        """
        return self._properties['valid']

    @property
    def date_created(self):
        """
        :returns: The date this Verification was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Verification was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.AccSecurity.VerificationInstance>'

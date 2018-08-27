# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

import os
import platform
from admin.twilio import __version__
from admin.twilio.base.exceptions import TwilioException
from admin.twilio.base.obsolete import obsolete_client
from admin.twilio.http.http_client import TwilioHttpClient


class Client(object):
    """ A client for accessing the Twilio API. """

    def __init__(self, username=None, password=None, account_sid=None, region=None,
                 http_client=None, environment=None):
        """
        Initializes the Twilio Client

        :param str username: Username to authenticate with
        :param str password: Password to authenticate with
        :param str account_sid: Account Sid, defaults to Username
        :param str region: Twilio Region to make requests to
        :param HttpClient http_client: HttpClient, defaults to TwilioHttpClient
        :param dict environment: Environment to look for auth details, defaults to os.environ

        :returns: Twilio Client
        :rtype: twilio.rest.Client
        """
        environment = environment or os.environ

        self.username = username or environment.get('TWILIO_ACCOUNT_SID')
        """ :type : str """
        self.password = password or environment.get('TWILIO_AUTH_TOKEN')
        """ :type : str """
        self.account_sid = account_sid or self.username
        """ :type : str """
        self.region = region
        """ :type : str """

        if not self.username or not self.password:
            raise TwilioException("Credentials are required to create a TwilioClient")

        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client = http_client or TwilioHttpClient()
        """ :type : HttpClient """

        # Domains
        self._accounts = None
        self._api = None
        self._chat = None
        self._fax = None
        self._ip_messaging = None
        self._lookups = None
        self._monitor = None
        self._notify = None
        self._preview = None
        self._pricing = None
        self._proxy = None
        self._taskrouter = None
        self._trunking = None
        self._video = None
        self._messaging = None
        self._wireless = None
        self._sync = None
        self._studio = None

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
        """
        Makes a request to the Twilio API using the configured http client
        Authentication information is automatically added if none is provided

        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects

        :returns: Response from the Twilio API
        :rtype: twilio.http.response.Response
        """
        auth = auth or self.auth
        headers = headers or {}

        headers['User-Agent'] = 'twilio-python/{} (Python {})'.format(
            __version__,
            platform.python_version(),
        )
        headers['X-Twilio-Client'] = 'python-{}'.format(__version__)
        headers['Accept-Charset'] = 'utf-8'

        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'

        if self.region:
            head, tail = uri.split('.', 1)

            if not tail.startswith(self.region):
                uri = '.'.join([head, self.region, tail])

        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    @property
    def accounts(self):
        """
        Access the Accounts Twilio Domain

        :returns: Accounts Twilio Domain
        :rtype: twilio.rest.accounts.Accounts
        """
        if self._accounts is None:
            from twilio.rest.accounts import Accounts
            self._accounts = Accounts(self)
        return self._accounts

    @property
    def api(self):
        """
        Access the Api Twilio Domain

        :returns: Api Twilio Domain
        :rtype: twilio.rest.api.Api
        """
        if self._api is None:
            from twilio.rest.api import Api
            self._api = Api(self)
        return self._api

    @property
    def chat(self):
        """
        Access the Chat Twilio Domain

        :returns: Chat Twilio Domain
        :rtype: twilio.rest.chat.Chat
        """
        if self._chat is None:
            from twilio.rest.chat import Chat
            self._chat = Chat(self)
        return self._chat

    @property
    def fax(self):
        """
        Access the Fax Twilio Domain

        :returns: Fax Twilio Domain
        :rtype: twilio.rest.fax.Fax
        """
        if self._fax is None:
            from twilio.rest.fax import Fax
            self._fax = Fax(self)
        return self._fax

    @property
    def ip_messaging(self):
        """
        Access the IpMessaging Twilio Domain

        :returns: IpMessaging Twilio Domain
        :rtype: twilio.rest.ip_messaging.IpMessaging
        """
        if self._ip_messaging is None:
            from twilio.rest.ip_messaging import IpMessaging
            self._ip_messaging = IpMessaging(self)
        return self._ip_messaging

    @property
    def lookups(self):
        """
        Access the Lookups Twilio Domain

        :returns: Lookups Twilio Domain
        :rtype: twilio.rest.lookups.Lookups
        """
        if self._lookups is None:
            from twilio.rest.lookups import Lookups
            self._lookups = Lookups(self)
        return self._lookups

    @property
    def monitor(self):
        """
        Access the Monitor Twilio Domain

        :returns: Monitor Twilio Domain
        :rtype: twilio.rest.monitor.Monitor
        """
        if self._monitor is None:
            from twilio.rest.monitor import Monitor
            self._monitor = Monitor(self)
        return self._monitor

    @property
    def notify(self):
        """
        Access the Notify Twilio Domain

        :returns: Notify Twilio Domain
        :rtype: twilio.rest.notify.Notify
        """
        if self._notify is None:
            from twilio.rest.notify import Notify
            self._notify = Notify(self)
        return self._notify

    @property
    def preview(self):
        """
        Access the Preview Twilio Domain

        :returns: Preview Twilio Domain
        :rtype: twilio.rest.preview.Preview
        """
        if self._preview is None:
            from twilio.rest.preview import Preview
            self._preview = Preview(self)
        return self._preview

    @property
    def pricing(self):
        """
        Access the Pricing Twilio Domain

        :returns: Pricing Twilio Domain
        :rtype: twilio.rest.pricing.Pricing
        """
        if self._pricing is None:
            from twilio.rest.pricing import Pricing
            self._pricing = Pricing(self)
        return self._pricing

    @property
    def proxy(self):
        """
        Access the Proxy Twilio Domain

        :returns: Proxy Twilio Domain
        :rtype: twilio.rest.proxy.Proxy
        """
        if self._proxy is None:
            from twilio.rest.proxy import Proxy
            self._proxy = Proxy(self)
        return self._proxy

    @property
    def taskrouter(self):
        """
        Access the Taskrouter Twilio Domain

        :returns: Taskrouter Twilio Domain
        :rtype: twilio.rest.taskrouter.Taskrouter
        """
        if self._taskrouter is None:
            from twilio.rest.taskrouter import Taskrouter
            self._taskrouter = Taskrouter(self)
        return self._taskrouter

    @property
    def trunking(self):
        """
        Access the Trunking Twilio Domain

        :returns: Trunking Twilio Domain
        :rtype: twilio.rest.trunking.Trunking
        """
        if self._trunking is None:
            from twilio.rest.trunking import Trunking
            self._trunking = Trunking(self)
        return self._trunking

    @property
    def video(self):
        """
        Access the Video Twilio Domain

        :returns: Video Twilio Domain
        :rtype: twilio.rest.video.Video
        """
        if self._video is None:
            from twilio.rest.video import Video
            self._video = Video(self)
        return self._video

    @property
    def messaging(self):
        """
        Access the Messaging Twilio Domain

        :returns: Messaging Twilio Domain
        :rtype: twilio.rest.messaging.Messaging
        """
        if self._messaging is None:
            from twilio.rest.messaging import Messaging
            self._messaging = Messaging(self)
        return self._messaging

    @property
    def wireless(self):
        """
        Access the Wireless Twilio Domain

        :returns: Wireless Twilio Domain
        :rtype: twilio.rest.wireless.Wireless
        """
        if self._wireless is None:
            from twilio.rest.wireless import Wireless
            self._wireless = Wireless(self)
        return self._wireless

    @property
    def sync(self):
        """
        Access the Sync Twilio Domain

        :returns: Sync Twilio Domain
        :rtype: twilio.rest.sync.Sync
        """
        if self._sync is None:
            from twilio.rest.sync import Sync
            self._sync = Sync(self)
        return self._sync

    @property
    def studio(self):
        """
        Access the Studio Twilio Domain

        :returns: Studio Twilio Domain
        :rtype: twilio.rest.studio.Studio
        """
        if self._studio is None:
            from twilio.rest.studio import Studio
            self._studio = Studio(self)
        return self._studio

    @property
    def addresses(self):
        """
        :rtype: twilio.rest.api.v2010.account.address.AddressList
        """
        return self.api.account.addresses

    @property
    def applications(self):
        """
        :rtype: twilio.rest.api.v2010.account.application.ApplicationList
        """
        return self.api.account.applications

    @property
    def authorized_connect_apps(self):
        """
        :rtype: twilio.rest.api.v2010.account.authorized_connect_app.AuthorizedConnectAppList
        """
        return self.api.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        """
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryList
        """
        return self.api.account.available_phone_numbers

    @property
    def calls(self):
        """
        :rtype: twilio.rest.api.v2010.account.call.CallList
        """
        return self.api.account.calls

    @property
    def conferences(self):
        """
        :rtype: twilio.rest.api.v2010.account.conference.ConferenceList
        """
        return self.api.account.conferences

    @property
    def connect_apps(self):
        """
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppList
        """
        return self.api.account.connect_apps

    @property
    def incoming_phone_numbers(self):
        """
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList
        """
        return self.api.account.incoming_phone_numbers

    @property
    def keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.key.KeyList
        """
        return self.api.account.keys

    @property
    def messages(self):
        """
        :rtype: twilio.rest.api.v2010.account.message.MessageList
        """
        return self.api.account.messages

    @property
    def new_keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyList
        """
        return self.api.account.new_keys

    @property
    def new_signing_keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.new_signing_key.NewSigningKeyList
        """
        return self.api.account.new_signing_keys

    @property
    def notifications(self):
        """
        :rtype: twilio.rest.api.v2010.account.notification.NotificationList
        """
        return self.api.account.notifications

    @property
    def outgoing_caller_ids(self):
        """
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdList
        """
        return self.api.account.outgoing_caller_ids

    @property
    def queues(self):
        """
        :rtype: twilio.rest.api.v2010.account.queue.QueueList
        """
        return self.api.account.queues

    @property
    def recordings(self):
        """
        :rtype: twilio.rest.api.v2010.account.recording.RecordingList
        """
        return self.api.account.recordings

    @property
    def signing_keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyList
        """
        return self.api.account.signing_keys

    @property
    def sip(self):
        """
        :rtype: twilio.rest.api.v2010.account.sip.SipList
        """
        return self.api.account.sip

    @property
    def short_codes(self):
        """
        :rtype: twilio.rest.api.v2010.account.short_code.ShortCodeList
        """
        return self.api.account.short_codes

    @property
    def tokens(self):
        """
        :rtype: twilio.rest.api.v2010.account.token.TokenList
        """
        return self.api.account.tokens

    @property
    def transcriptions(self):
        """
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionList
        """
        return self.api.account.transcriptions

    @property
    def usage(self):
        """
        :rtype: twilio.rest.api.v2010.account.usage.UsageList
        """
        return self.api.account.usage

    @property
    def validation_requests(self):
        """
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestList
        """
        return self.api.account.validation_requests

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio {}>'.format(self.account_sid)


@obsolete_client
class TwilioClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioRestClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioIpMessagingClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioLookupsClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioMonitorClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioPricingClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioTaskRouterClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioTrunkingClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass

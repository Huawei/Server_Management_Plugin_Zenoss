'''
HMMBladeMap
'''
from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetMap
    )
from DeviceDefine import HMMHEALTH, HMMCPUHEALTH
from DeviceDefine import HMMFRUCONTROL


class HMMBladeMap(SnmpPlugin):
    '''
    HMMBladeMap
    '''

    relname = 'hmmblades'
    modname = 'ZenPacks.community.HuaweiServer.HMMBlade'

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.6.0':  'b1Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.6.0':  'b2Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.6.0':  'b3Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.6.0':  'b4Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.6.0':  'b5Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.6.0':  'b6Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.6.0':  'b7Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.6.0':  'b8Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.6.0':  'b9Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.6.0': 'b10Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.6.0': 'b11Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.6.0': 'b12Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.6.0': 'b13Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.6.0': 'b14Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.6.0': 'b15Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.6.0': 'b16Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.6.0': 'b17Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.6.0': 'b18Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.6.0': 'b19Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.6.0': 'b20Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.6.0': 'b21Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.6.0': 'b22Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.6.0': 'b23Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.6.0': 'b24Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.6.0': 'b25Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.6.0': 'b26Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.6.0': 'b27Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.6.0': 'b28Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.6.0': 'b29Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.6.0': 'b30Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.6.0': 'b31Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.6.0': 'b32Presence',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.8.0':  'b1Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.8.0':  'b2Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.8.0':  'b3Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.8.0':  'b4Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.8.0':  'b5Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.8.0':  'b6Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.8.0':  'b7Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.8.0':  'b8Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.8.0':  'b9Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.8.0': 'b10Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.8.0': 'b11Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.8.0': 'b12Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.8.0': 'b13Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.8.0': 'b14Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.8.0': 'b15Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.8.0': 'b16Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.8.0': 'b17Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.8.0': 'b18Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.8.0': 'b19Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.8.0': 'b20Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.8.0': 'b21Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.8.0': 'b22Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.8.0': 'b23Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.8.0': 'b24Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.8.0': 'b25Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.8.0': 'b26Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.8.0': 'b27Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.8.0': 'b28Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.8.0': 'b29Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.8.0': 'b30Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.8.0': 'b31Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.8.0': 'b32Health',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.20.0':  'b1BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.20.0':  'b2BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.20.0':  'b3BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.20.0':  'b4BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.20.0':  'b5BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.20.0':  'b6BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.20.0':  'b7BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.20.0':  'b8BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.20.0':  'b9BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.20.0': 'b10BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.20.0': 'b11BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.20.0': 'b12BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.20.0': 'b13BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.20.0': 'b14BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.20.0': 'b15BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.20.0': 'b16BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.20.0': 'b17BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.20.0': 'b18BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.20.0': 'b19BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.20.0': 'b20BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.20.0': 'b21BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.20.0': 'b22BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.20.0': 'b23BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.20.0': 'b24BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.20.0': 'b25BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.20.0': 'b26BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.20.0': 'b27BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.20.0': 'b28BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.20.0': 'b29BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.20.0': 'b30BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.20.0': 'b31BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.20.0': 'b32BladeVersion',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.32.0':  'b1BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.32.0':  'b2BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.32.0':  'b3BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.32.0':  'b4BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.32.0':  'b5BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.32.0':  'b6BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.32.0':  'b7BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.32.0':  'b8BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.32.0':  'b9BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.32.0': 'b10BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.32.0': 'b11BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.32.0': 'b12BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.32.0': 'b13BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.32.0': 'b14BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.32.0': 'b15BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.32.0': 'b16BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.32.0': 'b17BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.32.0': 'b18BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.32.0': 'b19BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.32.0': 'b20BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.32.0': 'b21BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.32.0': 'b22BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.32.0': 'b23BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.32.0': 'b24BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.32.0': 'b25BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.32.0': 'b26BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.32.0': 'b27BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.32.0': 'b28BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.32.0': 'b29BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.32.0': 'b30BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.32.0': 'b31BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.32.0': 'b32BiosBootOption',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.57.0':  'b1ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.57.0':  'b2ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.57.0':  'b3ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.57.0':  'b4ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.57.0':  'b5ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.57.0':  'b6ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.57.0':  'b7ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.57.0':  'b8ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.57.0':  'b9ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.57.0': 'b10ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.57.0': 'b11ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.57.0': 'b12ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.57.0': 'b13ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.57.0': 'b14ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.57.0': 'b15ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.57.0': 'b16ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.57.0': 'b17ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.57.0': 'b18ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.57.0': 'b19ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.57.0': 'b20ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.57.0': 'b21ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.57.0': 'b22ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.57.0': 'b23ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.57.0': 'b24ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.57.0': 'b25ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.57.0': 'b26ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.57.0': 'b27ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.57.0': 'b28ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.57.0': 'b29ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.57.0': 'b30ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.57.0': 'b31ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.57.0': 'b32ProductName',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.2006.1.5.1.0':  'b1CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.2006.1.5.1.0':  'b2CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.2006.1.5.1.0':  'b3CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.2006.1.5.1.0':  'b4CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.2006.1.5.1.0':  'b5CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.2006.1.5.1.0':  'b6CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.2006.1.5.1.0':  'b7CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.2006.1.5.1.0':  'b8CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.2006.1.5.1.0':  'b9CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.2006.1.5.1.0': 'b10CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.2006.1.5.1.0': 'b11CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.2006.1.5.1.0': 'b12CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.2006.1.5.1.0': 'b13CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.2006.1.5.1.0': 'b14CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.2006.1.5.1.0': 'b15CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.2006.1.5.1.0': 'b16CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.2006.1.5.1.0': 'b17CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.2006.1.5.1.0': 'b18CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.2006.1.5.1.0': 'b19CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.2006.1.5.1.0': 'b20CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.2006.1.5.1.0': 'b21CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.2006.1.5.1.0': 'b22CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.2006.1.5.1.0': 'b23CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.2006.1.5.1.0': 'b24CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.2006.1.5.1.0': 'b25CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.2006.1.5.1.0': 'b26CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.2006.1.5.1.0': 'b27CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.2006.1.5.1.0': 'b28CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.2006.1.5.1.0': 'b29CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.2006.1.5.1.0': 'b30CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.2006.1.5.1.0': 'b31CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.2006.1.5.1.0': 'b32CPUHealth',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.2002.1.3.0':  'b1FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.2002.1.3.0':  'b2FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.2002.1.3.0':  'b3FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.2002.1.3.0':  'b4FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.2002.1.3.0':  'b5FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.2002.1.3.0':  'b6FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.2002.1.3.0':  'b7FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.2002.1.3.0':  'b8FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.2002.1.3.0':  'b9FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.2002.1.3.0': 'b10FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.2002.1.3.0': 'b11FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.2002.1.3.0': 'b12FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.2002.1.3.0': 'b13FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.2002.1.3.0': 'b14FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.2002.1.3.0': 'b15FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.2002.1.3.0': 'b16FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.2002.1.3.0': 'b17FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.2002.1.3.0': 'b18FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.2002.1.3.0': 'b19FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.2002.1.3.0': 'b20FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.2002.1.3.0': 'b21FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.2002.1.3.0': 'b22FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.2002.1.3.0': 'b23FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.2002.1.3.0': 'b24FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.2002.1.3.0': 'b25FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.2002.1.3.0': 'b26FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.2002.1.3.0': 'b27FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.2002.1.3.0': 'b28FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.2002.1.3.0': 'b29FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.2002.1.3.0': 'b30FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.2002.1.3.0': 'b31FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.2002.1.3.0': 'b32FruHotSwapState',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.1.47.0':  'b1BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.2.47.0':  'b2BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.3.47.0':  'b3BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.4.47.0':  'b4BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.5.47.0':  'b5BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.6.47.0':  'b6BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.7.47.0':  'b7BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.8.47.0':  'b8BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.9.47.0':  'b9BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.10.47.0': 'b10BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.11.47.0': 'b11BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.12.47.0': 'b12BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.13.47.0': 'b13BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.14.47.0': 'b14BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.15.47.0': 'b15BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.16.47.0': 'b16BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.17.47.0': 'b17BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.18.47.0': 'b18BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.19.47.0': 'b19BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.20.47.0': 'b20BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.21.47.0': 'b21BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.22.47.0': 'b22BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.23.47.0': 'b23BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.24.47.0': 'b24BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.25.47.0': 'b25BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.26.47.0': 'b26BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.27.47.0': 'b27BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.28.47.0': 'b28BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.29.47.0': 'b29BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.30.47.0': 'b30BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.31.47.0': 'b31BmcIP',
        '.1.3.6.1.4.1.2011.2.82.1.82.4.32.47.0': 'b32BmcIP',
        })

    def process(self, device, results, log):
        '''
        process oid
        '''

        log = log
        device = device
        getdata = results[0]

        relmap = self.relMap()
        for row in range(1, 33):
            name = 'Blade_' + str(row)
            bnproductname = 'b'+str(row)+'ProductName'
            bnpresence = 'b'+str(row)+'Presence'
            if 1 != int(getdata.get(bnpresence)):
                continue
            bnbladeversion = 'b'+str(row)+'BladeVersion'
            bnhealth = 'b'+str(row)+'Health'
            bncpunealth = 'b'+str(row)+'CPUHealth'
            bnbiosbootoption = 'b'+str(row)+'BiosBootOption'
            bnfrucontrol = 'b'+str(row)+'FruHotSwapState'
            bnbmcip = 'b'+str(row)+'BmcIP'
            ipstrlist = str(getdata.get(bnbmcip)).split(',')
            bnip = ''
            bnipmask = ''
            for idx in ipstrlist:
                if idx.find('IP:') != -1:
                    bnip = idx[idx.find('IP:')+4:]
                if idx.find('Mask: ') != -1:
                    bnipmask = idx[idx.find('Mask:')+6:]
            relmap.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': str(row),
                'hbname': getdata.get(bnproductname),
                'hbversion': getdata.get(bnbladeversion),
                'hbhealth': HMMHEALTH.get(getdata.get(bnhealth), 'unknown'),
                'hbcpuhealth': HMMCPUHEALTH.get(getdata.get(bncpunealth),
                                                'unknown'),
                'hbbiosbootoption': getdata.get(bnbiosbootoption),
                'hbIP': bnip,
                'hbIPMask': bnipmask,
                'hbfrucontrol': HMMFRUCONTROL.get(
                    getdata.get(bnfrucontrol), 'unknown'),
                }))
        return relmap

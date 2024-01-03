# Sample script for bandwidth usage monitoring using SNMP
from pysnmp.hlapi import *

def get_bandwidth(device_ip, community_string):
        oid = '1.3.6.1.2.1.2.2.1.10.1'  # SNMP OID for incoming bytes on the first interface

            error_indication, error_status, error_index, var_binds = next(
                            getCmd(SnmpEngine(),
                                               CommunityData(community_string),
                                                              UdpTransportTarget((device_ip, 161)),
                                                                             ContextData(),
                                                                                            ObjectType(ObjectIdentity(oid)))
                                )

                if error_indication:
                            print(f"Error: {error_indication}")
                                elif error_status:
                                            print(f"Error: {error_status}")
                                                else:
                                                            return var_binds[0][1]

                                                        # Example usage
                                                        device_ip = '192.168.1.1'
                                                        community_string = 'public'

                                                        incoming_bytes = get_bandwidth(device_ip, community_string)
                                                        print(f"Incoming Bytes on {device_ip}: {incoming_bytes}")


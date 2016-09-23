# Ansible grep filter plugin
# 
# Grzegorz Bajson gbajson@gmail.com
# 
# Example usage:
# string: aaabbccc
# list: [ "aaa", "bbb", "aaa" ] 
# filtered: "{{ string | grep("aaa") }} # filtered=[ "aaabbccc" ]
# filtered: "{{ list | grep("aaa") }} # filtereed=[ "aaa", "aaa" ]

import re

# FITXIT: gbajson - doesn't handle dicts
def grep(values, pattern):
    if not isinstance(values, list):
        values = [ values ]
    return [ v for v in values if re.match(pattern, v) ]


class FilterModule(object):
    def filters(self):
        return {
           'grep' : grep
        }


from typing import List


class Solution:
    def __init__(self):
        self.domain_freq_dict = {}

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        for cpdomain in cpdomains:
            freq_str, whole_domain = cpdomain.split(" ")
            self.update_freq_dict(int(freq_str), whole_domain)

        return ["{} {}".format(v, k) for k, v in self.domain_freq_dict.items()]

    def update_freq_dict(self, freq, whole_domain):
        self.domain_freq_dict.setdefault(whole_domain, 0)
        self.domain_freq_dict[whole_domain] += freq
        for i, v in enumerate(whole_domain):
            if v == ".":
                sub_domain = whole_domain[i + 1:]
                self.domain_freq_dict.setdefault(sub_domain, 0)
                self.domain_freq_dict[sub_domain] += freq

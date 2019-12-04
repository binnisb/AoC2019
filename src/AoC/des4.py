from typing import Union, List, Any, Tuple
import attr

@attr.s
class Passwords(object):
    low: int = attr.ib(converter=int)
    high: int = attr.ib(converter=int)

    @staticmethod
    def is_password(pw, allow_part_of_large=True):
        prev = 0
        curr_len = 1
        lengths = set()
        for c in str(pw):
            c_int = int(c)
            if c_int < prev:
                return False
            if c_int == prev:
                curr_len += 1
            else:
                lengths.add(curr_len)
                curr_len = 1
            prev = c_int
        lengths.add(curr_len)
        if not allow_part_of_large:
            return 2 in lengths
        return max(lengths) >= 2
    
    def count_passwords(self, allow_part_of_large=True):
        count = 0
        for pw in range(self.low, self.high+1):
            if self.is_password(pw, allow_part_of_large):
                count += 1
        return count
def solve41(path: str = 'assets/des4.1.txt') -> int:
    pw = Passwords(136760, 595730)
    return pw.count_passwords(allow_part_of_large=True)

def solve42(path: str = 'assets/des4.1.txt') -> int:
    pw = Passwords(136760, 595730)
    return pw.count_passwords(allow_part_of_large=False)


if __name__ == "__main__":
    print(f"solve 4.1: {solve41()}")
    print(f"solve 4.2: {solve42()}")
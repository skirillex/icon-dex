from auto_generate.common.functions import get_coefficients
from auto_generate.common.functions import get_max_exp_array
from auto_generate.common.constants import NUM_OF_COEFFICIENTS
from auto_generate.common.constants import MIN_PRECISION
from auto_generate.common.constants import MAX_PRECISION


coefficients = get_coefficients(NUM_OF_COEFFICIENTS)
maxExpArray = get_max_exp_array(coefficients,MAX_PRECISION+1)
maxExpArrayShl = [((maxExpArray[precision]+1)<<(MAX_PRECISION-precision))-1 for precision in range(len(maxExpArray))]


len1 = len(str(MAX_PRECISION))
len2 = len(hex(maxExpArrayShl[0]))


print('    uint256[{}] private maxExpArray;'.format(len(maxExpArray)))
print('    constructor() public {')
for precision in range(len(maxExpArray)):
    prefix = '  ' if MIN_PRECISION <= precision <= MAX_PRECISION else '//'
    print('    {0:s}  maxExpArray[{1:{2}d}] = {3:#0{4}x};'.format(prefix,precision,len1,maxExpArrayShl[precision],len2))
print('    }')

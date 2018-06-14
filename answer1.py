import json
import requests
from collections import defaultdict
from json import _default_encoder

def main():
    data = requests.get( 'http://mysafeinfo.com/api/data?list=englishmonarchs&format=json').json()
    d = defaultdict( lambda: defaultdict( set ) )
    for k in data:
        d[ k [ 'cty' ] ] [ k[ 'hse' ] ].add( k[ 'nm' ] )

    def serialize( obj ):
        if isinstance( obj, set ):
            return _default_encoder.encode( list( obj ) )
        return _default_encoder.encode(obj )
    print(json.dumps( d, default=serialize ))
    
if __name__ == '__main__':
    main()
